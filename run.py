import argparse
import configparser
import os

from mysqlimport import mysqlimport
from filehandler import FileHandler

CNF_SCRIPT = "SCRIPT"
CNF_FILEHANDLER = "FILEHANDLER"
CNF_MYSQLIMPORT = "MYSQLIMPORT"

DEFAULT_CONFIG_FILE = "%s/import.cnf" % __package__

def files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def run():

    arg_parser = argparse.ArgumentParser(description='A MySQL csv import tool')
    arg_parser.add_argument('-c', '--config',
                            default=DEFAULT_CONFIG_FILE,
                            help='Configuration file')

    arg = arg_parser.parse_args()
    arg = vars(arg)

    cnf_parser = configparser.ConfigParser()
    cnf_parser.read(arg['config'])

    cnf_script = cnf_parser[CNF_SCRIPT]
    cnf_filehandler = cnf_parser[CNF_FILEHANDLER]
    cnf_mysqlimport = cnf_parser[CNF_MYSQLIMPORT]

    mysqlimport_cmd = cnf_script['mysqlimport_cmd']
    mysqlimport_table = cnf_script['mysqlimport_table']
    mysqlimport_database = cnf_script['mysqlimport_database']

    file_handler = FileHandler(mysqlimport_table, cnf_filehandler)

    for file in files(file_handler.data_dir):
        normalized_file = file_handler.run(file)
        code = mysqlimport(mysqlimport_cmd, mysqlimport_database, normalized_file, cnf_mysqlimport)
        print(code)

if __name__ == "__main__":
    run()