import joblib
from pathlib import Path
from pandas import read_csv
from argparse import ArgumentParser
from sklearn.linear_model import LinearRegression

parser = ArgumentParser()
parser.add_argument('--x-train', type=str)
parser.add_argument('--y-train', type=str)
parser.add_argument('--model', type=str)
args = parser.parse_args()

x_train = read_csv(args.x_train)
y_train = read_csv(args.y_train)

linear_regressor = LinearRegression()
linear_regressor.fit(x_train, y_train)

Path(args.model).parent.mkdir(exist_ok=True, parents=True)

joblib.dump(linear_regressor, args.model)