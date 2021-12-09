import joblib
from pathlib import Path
from pandas import read_csv
from argparse import ArgumentParser
from sklearn.metrics import mean_squared_error, mean_absolute_error

parser = ArgumentParser()
parser.add_argument('--model', type=str)
parser.add_argument('--accuracy', type=str)
parser.add_argument('--x-test', type=str)
parser.add_argument('--y-test', type=str)

args = parser.parse_args()

linear_regressor = joblib.load(args.model)

# with open(args.model, 'rb') as model_file:
#     linear_regressor = load(model_file)

x_test = read_csv(args.x_test)
y_test = read_csv(args.y_test)

y_pred = linear_regressor.predict(x_test)

mae = mean_absolute_error(y_pred, y_test)
mse = mean_squared_error(y_pred, y_test)
output_accuracy = f"\nLinear Regression\nMean Absolute Error: {mae}\nMean Squared Error: {mse}\n"

Path(args.accuracy).parent.mkdir(parents=True, exist_ok=True)

with open(args.accuracy, 'w') as output:
    output.write(output_accuracy)