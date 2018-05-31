import argparse

parser = argparse.ArgumentParser(description='A MySQL csv import tool')

parser.add_argument('-c', '--command',
                    default='mysqlimport',
                    help='mysqlimport command')

parser.add_argument('-d', '--data',
                    default='data',
                    help='Directory containing CSV data files')

parser.add_argument('-f', '--finished',
                    default='data/finished',
                    help='Directory for finished CSV files')

args = parser.parse_args()
print(vars(args))
