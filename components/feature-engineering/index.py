from pathlib import Path
from argparse import ArgumentParser
from pandas import DataFrame, read_csv
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

parser = ArgumentParser()
parser.add_argument('--x-train', type=str)
parser.add_argument('--x-test', type=str)
parser.add_argument('--y-train', type=str)
parser.add_argument('--y-test', type=str)
parser.add_argument('--data', type=str)

args = parser.parse_args()
Path(args.x_train).parent.mkdir(parents=True, exist_ok=True)
Path(args.y_train).parent.mkdir(parents=True, exist_ok=True)
Path(args.x_test).parent.mkdir(parents=True, exist_ok=True)
Path(args.y_test).parent.mkdir(parents=True, exist_ok=True)

df = read_csv(args.data)

x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

DataFrame(x_train).to_csv(args.x_train)
DataFrame(y_train).to_csv(args.y_train)
DataFrame(x_test).to_csv(args.x_test)
DataFrame(y_test).to_csv(args.y_test)

