import joblib
from json import dump
from pickle import load
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--label-encoder', type=str)
parser.add_argument('--column-transformer', type=str)
parser.add_argument('--standard-scaler', type=str)
parser.add_argument('--linear-regressor', type=str)

args = parser.parse_args()

with open(args.label_encoder, 'rb') as out:
    le = load(out)


with open(args.column_transformer, 'rb') as out:
    ct = load(out)


with open(args.standard_scaler, 'rb') as out:
    sc = load(out)


linear_regressor = joblib.load(args.model)

# with open(args.linear_regressor, 'rb') as out:
#     linear_regressor = load(out)

input_data = [[1, '36-45', 1, 'B', '1', 1, 4, 14.0]]

predicted_price = linear_regressor.predict(sc.transform(ct.transform(input_data)))

print(predicted_price)