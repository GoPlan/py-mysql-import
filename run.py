from .command import MySqlImportCommand
from .file import FileBench

import configparser

class MySqlBatchImport():
    
    DEFAULT_CONFIG_FILE = "import.cnf"

    SCRIPT_CMD = "cmd"
    SCRIPT_DB_TABLE = "db_table"
    SCRIPT_DB_DBNAME = "db_dbname"
    SCRIPT_DATA_DIR = 'data_dir'
    SCRIPT_CACHE_DIR = 'cache_dir'
    SCRIPT_FINISHED_DIR = 'finished_dir'

    CNF_SCRIPT = "SCRIPT"
    CNF_MYSQLIMPORT = "MYSQLIMPORT"

    @staticmethod
    def run(cnf_file = DEFAULT_CONFIG_FILE):

        cnf_parser = configparser.ConfigParser()
        cnf_parser.read(cnf_file)

        cnf_script = cnf_parser[MySqlBatchImport.CNF_SCRIPT]
        cnf_mysqlimport = cnf_parser[MySqlBatchImport.CNF_MYSQLIMPORT]

        command = MySqlImportCommand(
            cnf_script[MySqlBatchImport.SCRIPT_CMD],
            cnf_script[MySqlBatchImport.SCRIPT_CACHE_DIR],
            cnf_script[MySqlBatchImport.SCRIPT_DB_DBNAME],
            cnf_script[MySqlBatchImport.SCRIPT_DB_TABLE],
            cnf_mysqlimport)

        filebench = FileBench(
            cnf_script[MySqlBatchImport.SCRIPT_DATA_DIR],
            cnf_script[MySqlBatchImport.SCRIPT_FINISHED_DIR])

        iterator = iter(filebench.get_unprocessed_files())

        for file in iterator:
            file.process(command)