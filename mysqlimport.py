import subprocess
import shutil


def mysqlimport(mysqlimport_cmd, mysqlimport_database, file, cnf_grp):

    cmd = [
        mysqlimport_cmd,
        '--local',
        '--replace'
    ]

    for cnf in cnf_grp:
        cmd.append('--%s' % cnf)

    cmd.append(mysqlimport_database)
    cmd.append(file)

    code = subprocess.run(cmd)

    return code
