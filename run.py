import argparse
import configparser

from mysqlimport_wrapper import MySqlImportWrapper

ARG_DATA = "data"
ARG_FINISHED = "data/finished"
ARG_CONFIG = "import.cnf"

CNF_MYSQLIMPORT = "MYSQLIMPORT"

arg_parser = argparse.ArgumentParser(description='A MySQL csv import tool')

arg_parser.add_argument('-c', '--config',
                        default=ARG_CONFIG,
                        help='Configuration file')

arg_parser.add_argument('-d', '--data',
                        default=ARG_DATA,
                        help='Directory containing CSV data files')

arg_parser.add_argument('-f', '--finished',
                        default=ARG_FINISHED,
                        help='Directory for finished CSV files')

arg = arg_parser.parse_args()
arg = vars(arg)

cnf_parser = configparser.ConfigParser()
cnf_parser.read(arg['config'])
cnf_mysqlimport = cnf_parser[CNF_MYSQLIMPORT]

MySqlImportWrapper.validate_config(cnf_mysqlimport)
MySqlImportWrapper(cnf_mysqlimport)
