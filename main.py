import argparse
import configparser

from file import File, FileBench
from command import MySqlImportCommand

DEFAULT_CONFIG_FILE = "import.cnf"

CNF_SCRIPT = "SCRIPT"
CNF_MYSQLIMPORT = "MYSQLIMPORT"

SCRIPT_DATA_DIR = 'data_dir'
SCRIPT_FINISHED_DIR = 'finished_dir'


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
    cnf_mysqlimport = cnf_parser[CNF_MYSQLIMPORT]

    command = MySqlImportCommand()
    filebench = FileBench(cnf_script[SCRIPT_DATA_DIR], cnf_script[SCRIPT_FINISHED_DIR])
    iterator = iter(filebench.get_unprocessed_files())

    for file in iterator:
        file.process(command)


if __name__ == "__main__":
    run()