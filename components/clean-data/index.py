import numpy as np
import pandas as pd
from pickle import dump
from pathlib import Path
from argparse import ArgumentParser
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
parser = ArgumentParser()
parser.add_argument('--dataset', type=str)
parser.add_argument('--data', type=str)
parser.add_argument('--column-transformer', type=str)
args = parser.parse_args()
Path(args.data).parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(args.dataset)

# Split the data into independent and dependent variables and remove unnecessary columns
x = df.iloc[:, 2:-2].values
y = df.iloc[:, -1].values

#Encode Gender column
le = LabelEncoder()
x[:, 0] = le.fit_transform(x[:, 0])

# Fill NaN values in Product_Category_2 column 
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
x[:, 7] = imputer.fit_transform(x[:, 7].reshape(-1, 1)).reshape(1, -1)[0]

# Onehot encode the Age, City_Category, Stay_In_Current_City_Years columns
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1, 3, 4])], remainder='passthrough')
x = ct.fit_transform(x)

# Merge the dataset to pass it to the next component
x = pd.DataFrame(x)
y = pd.DataFrame(y)
data = pd.concat([x,y], axis=1)

# Write the data to a csv file
data.to_csv(path_or_buf=args.data, index=False)

# Write the column transformer object into a file
Path(args.column_transformer).parent.mkdir(parents=True, exist_ok=True)
with open(args.column_transformer, 'wb') as output_file:
    dump(ct, output_file)