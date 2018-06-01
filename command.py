import os
import shutil
import pathlib
import subprocess


class MySqlImportCommand():

    def __init__(self, command, cache_dir, database, table, config):
        self._cmd = command
        self._cache_dir = cache_dir
        self._database = database
        self._table = table
        self._config = config

    def run(self, file):

        tmp_filename = '%s.%s' % (self._table, file.filename)
        tmp_filepath = str(pathlib.PurePath(os.getcwd(), self._cache_dir, tmp_filename))
        shutil.copy(file.filepath, tmp_filepath)

        cmd = [
            self._cmd,
           '--local',
           '--replace'
        ]

        for item in self._config:
            cmd.append('--%s=%s' % (item, self._config[item]))

        cmd.append(self._database)
        cmd.append(tmp_filepath)

        p = subprocess.run(cmd)

        return p