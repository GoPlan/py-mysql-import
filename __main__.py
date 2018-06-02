import argparse
import configparser

from .run import MySqlBatchImport


arg_parser = argparse.ArgumentParser(description='A MySQL csv import tool')
arg_parser.add_argument('-c', '--config',
                        default=MySqlBatchImport.DEFAULT_CONFIG_FILE,
                        help='Configuration file')

arg = arg_parser.parse_args()
arg = vars(arg)

cnf_file = arg['config']

MySqlBatchImport.run(cnf_file)