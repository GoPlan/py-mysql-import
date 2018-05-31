import os
import pathlib
import filecmp
import shutil


class FileHandler:

    def __call__(self, file):
        self.run(file)

    def __init__(self, table_name, cnf):
        self._table_name = table_name
        self._data_dir = cnf['data_dir']
        self._normalized_dir = cnf['normalized_dir']
        self._finished_dir = cnf['finished_dir']

    @property
    def data_dir(self):
        return self._data_dir

    def run(self, file):

        file_data_path = self._get_data_path(file)
        file_normalized_path = self._get_normalized_path(file)
        file_finished_path = self._get_finished_path(file)

        if os.path.isdir(file_data_path):
            return

        if os.path.exists(file_normalized_path) and filecmp.cmp(file_data_path, file_normalized_path, True):
            return

        if os.path.exists(file_finished_path) and filecmp.cmp(file_data_path, file_finished_path, True):
            return

        shutil.copy(file_data_path, file_normalized_path)

        return file_normalized_path

    def _get_data_path(self, file):
        return pathlib.PurePath(os.getcwd(), self._data_dir, file)

    def _get_normalized_path(self, file):
        return pathlib.PurePath(os.getcwd(), self._normalized_dir, self._get_normalized_name(file))

    def _get_finished_path(self, file):
        return pathlib.PurePath(os.getcwd(), self._finished_dir, self._get_normalized_name(file))

    def _get_normalized_name(self, file):
        return '%s.%s' % (self._table_name, file)