#!/usr/bin/env python                                                               
# -*- coding: utf-8 -*- 


import os
import sys
import subprocess
from loguru import logger


class Command(object):
    '''
    Command Handlerself
    '''
    def __init__(self):
        pass

    def execute(self, cmd, cwd=None, env=None, popen=False):
        """
        :param cmd Command String
        :param cwd Current working dir (Default: None)
        :param env Environment Variables (Default: None)
        :param popen Flag - Use subprocess Popen or check_output (Default: False)

        Use popen flag if you want to see output of a long running task while
        it is executing.

        :return (return code, output)
        """
        if popen:
            cmdoutput = ""
            sproc = subprocess.Popen(cmd,
                                     env=env,
                                     cwd=cwd,
                                     shell=True,
                                     stdout=subprocess.PIPE)
            while True:
                nextline = sproc.stdout.readline()
                nextline = nextline.decode("utf-8")
                cmdoutput += nextline
                if nextline == '' and sproc.poll() is not None:
                    break

                sys.stdout.write(nextline)
                sys.stdout.flush()

            return sproc.returncode, cmdoutput

        try:
            cmd = cmd.split(" ")
            cmdoutput = subprocess.check_output(cmd,
                                                cwd=cwd,
                                                stderr=subprocess.STDOUT,
                                                shell=False,
                                                timeout=20,
                                                env=env)

        except subprocess.CalledProcessError as err:
            logger.error("Failed to execute{}. Err {}", cmd, err)
            return err.returncode, ""

        except FileNotFoundError as err:
            logger.error("File Not Found {}", err)
            return 127, ""

        cmdoutput = cmdoutput.decode("utf-8")

        return 0, cmdoutput


def main():
    pyenvRoot = "/tmp/pyenvs"
    pyenvName = "testenv"

    cmdObj = Command()

    pyenvPath = os.path.join(pyenvRoot, pyenvName)
    pyenvBin = os.path.join(pyenvPath, "bin")
    pyenvPython = os.path.join(pyenvBin, "python")
    pyenvPip = os.path.join(pyenvBin, "pip")

    # Create a new virtual env.

    cmd = "python -m venv %s" % pyenvPath
    ret, output = cmdObj.execute(cmd, popen=True)
    print("Ret: ", ret)
    print("output: ", output)

    # Install package click.
    cmd = "%s install click" % pyenvPip
    ret, output = cmdObj.execute(cmd)
    print("%s %s" % (ret, output))

    # Install package flask.
    cmd = "%s install flask" % pyenvPip
    ret, output = cmdObj.execute(cmd, popen=True)
    print("%s %s" % (ret, output)) 



if __name__ == '__main__':
    main()


