import argparse
import configparser

from .mysqlimport_wrapper import MySqlImportWrapper
from .file_handler import FileHandler

CNF_SCRIPT = "SCRIPT"
CNF_MYSQLIMPORT = "MYSQLIMPORT"

DEFAULT_CONFIG_FILE = "%s/import.cnf" % __package__

arg_parser = argparse.ArgumentParser(description='A MySQL csv import tool')
arg_parser.add_argument('-c', '--config',
                        default= DEFAULT_CONFIG_FILE,
                        help='Configuration file')

arg = arg_parser.parse_args()
arg = vars(arg)

cnf_parser = configparser.ConfigParser()
cnf_parser.read(arg['config'])
cnf_mysqlimport = cnf_parser[CNF_MYSQLIMPORT]
cnf_script = cnf_parser[CNF_SCRIPT]

FileHandler(cnf_script)

MySqlImportWrapper.validate_config(cnf_mysqlimport)
MySqlImportWrapper(cnf_mysqlimport)