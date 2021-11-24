import numpy as np
import pandas as pd
from pathlib import Path
from argparse import ArgumentParser
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


parser = ArgumentParser()
parser.add_argument('--sample', type=str)
parser.add_argument('--predictioninput', type=str)

args = parser.parse_args()
Path(args.predictoninput).parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(args.sample)

df.dropna(inplace=True)

x_sample = df.iloc[:, 2:-2].values

le = LabelEncoder()
x_sample[:, 0] = le.fit_transform(x_sample[:, 0])

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1, 3, 4])], remainder='passthrough')
x_sample = ct.fit_transform(x_sample)

df = pd.DataFrame(x_sample)

df.to_csv(args.predictioninput, index=False)
