

class Command():
    def run(self, file):
        pass

class MySqlImportCommand(Command):
    def run(self, file):
        print(file.fullpath)