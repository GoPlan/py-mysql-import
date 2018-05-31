import subprocess

HOST = 'localhost'
PORT = 3306
RUN = 'mysqlimport'


class MySqlImportWrapper:

    def __call__(self, config):
        importer = MySqlImportWrapper(config)
        status = importer.run()
        return status

    def __init__(self, cnf):
        self._cmd = cnf['cmd'] or RUN
        self._host = cnf['host'] or HOST
        self._port = cnf['port'] or PORT
        self._user = cnf['user']
        self._pass = cnf['password']
        self._columns = cnf['columns']

    def run(self):

        cmd = [
            self._cmd,
            '--local'
        ]

        return subprocess.run(cmd)

    @staticmethod
    def validate_config(config):
        print('validating config ...')
