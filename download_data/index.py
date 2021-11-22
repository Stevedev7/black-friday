import argparse
from pathlib import Path
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str)
parser.add_argument('--dataset', type=str)
parser.add_argument('--sample', type=str)

args = parser.parse_args()
Path(args.dataset).parent.mkdir(parents=True, exist_ok=True)
Path(args.sample).parent.mkdir(parents=True, exist_ok=True)

dataset = pd.read_csv('data/train.csv')
sample = pd.read_csv('data/test.csv')

dataset.to_csv(path_or_buf=args.dataset, index=False)
sample.to_csv(path_or_buf=args.sample, index=False)