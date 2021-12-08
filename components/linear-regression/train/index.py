from pathlib import Path
from pandas import read_csv
from argparse import ArgumentParser
from sklearn.linear_model import LinearRegression
from pickle import dump, load

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
with open(args.model, 'wb') as output_file:
    dump(linear_regressor, output_file)