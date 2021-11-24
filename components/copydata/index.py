from pandas import read_csv
from pathlib import Path
from argparse import ArgumentParser

dataset = read_csv('data/train.csv')
sample = read_csv('data/test.csv')

parser = ArgumentParser()
parser.add_argument('--data-set', type=str)
parser.add_argument('--sample', type=str)

args = parser.parse_args()

Path(args.data_set).parent.mkdir(parents=True, exist_ok=True)
Path(args.sample).parent.mkdir(parents=True, exist_ok=True)

dataset.to_csv(args.data_set, index=False)
sample.to_csv(args.sample, index=False)