from .command import MySqlImportCommand
from .file import FileBench

import configparser
import os
import inspect
import pathlib
import shutil


class App():

    DEFAULT_CONFIG_FILE = "import.cnf"
    DEFAULT_DATA_DIR = "data"
    DEFAULT_CACHED_DIR = "cached"
    DEFAULT_FINISHED_DIR = "finished"

    SCRIPT_CMD = "cmd"
    SCRIPT_DB_TABLE = "db_table"
    SCRIPT_DB_DBNAME = "db_dbname"
    SCRIPT_DATA_DIR = 'data_dir'
    SCRIPT_CACHE_DIR = 'cache_dir'
    SCRIPT_FINISHED_DIR = 'finished_dir'

    CNF_SCRIPT = "SCRIPT"
    CNF_MYSQLIMPORT = "MYSQLIMPORT"

    @staticmethod
    def run(cnf_file=DEFAULT_CONFIG_FILE):

        cnf_parser = configparser.ConfigParser()
        cnf_parser.read(cnf_file)

        cnf_script = cnf_parser[App.CNF_SCRIPT]
        cnf_mysqlimport = cnf_parser[App.CNF_MYSQLIMPORT]

        command = MySqlImportCommand(
            cnf_script[App.SCRIPT_CMD],
            cnf_script[App.SCRIPT_CACHE_DIR],
            cnf_script[App.SCRIPT_DB_DBNAME],
            cnf_script[App.SCRIPT_DB_TABLE],
            cnf_mysqlimport)

        filebench = FileBench(
            cnf_script[App.SCRIPT_DATA_DIR],
            cnf_script[App.SCRIPT_FINISHED_DIR])

        iterator = iter(filebench.get_unprocessed_files())

        for file in iterator:
            file.process(command)

    @staticmethod
    def prepare():
        os.mkdir(App.DEFAULT_DATA_DIR)
        os.mkdir(App.DEFAULT_CACHED_DIR)
        os.mkdir(App.DEFAULT_FINISHED_DIR)

        module = inspect.getfile(App)
        module_path = os.path.dirname(module)

        import_cnf = pathlib.PurePath(module_path,
                                      App.DEFAULT_CONFIG_FILE)

        shutil.copy(import_cnf, App.DEFAULT_CONFIG_FILE)
