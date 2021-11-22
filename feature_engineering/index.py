import argparse
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import train_test_split

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str)
parser.add_argument()
args = parser.parse_args()

data = pd.read_csv(args.data)

#Split the data into test and train set
#550068 is the index from which the testing dataset starts(values in Y column are null from this index in the final output dataframe)
x = data.iloc[0:550068, :-1]
y = data.iloc[0:550068, -1]
sample_data = data.iloc[550068:-1, :-1]

#Split the data into training and test set

