from pandas import read_csv
from pathlib import Path
from argparse import ArgumentParser

dataset = read_csv('data/train.csv')
sample = read_csv('data/test.csv')

parser = ArgumentParser()
parser.add_argument('--dataset', type=str)
parser.add_argument('--sample', type=str)
parser.add_argument('--output-data-uri', type=str)
parser.add_argument('--output-sample-uri', type=str)

args = parser.parse_args()

# Make paths to store datasets
Path(args.output_data_uri).parent.mkdir(parents=True, exist_ok=True)
Path(args.output_sample_uri).parent.mkdir(parents=True, exist_ok=True)


# Make paths to store dataset path and write to a file
Path(args.dataset).parent.mkdir(parents=True, exist_ok=True)
Path(args.dataset).write_text(args.output_data_uri)

Path(args.sample).parent.mkdir(parents=True, exist_ok=True)
Path(args.sample).write_text(args.output_sample_uri)

dataset.to_csv(args.dataset, index=False)
sample.to_csv(args.sample, index=False)