# -*- coding: UTF-8 -*-

import os
import subprocess

class zl_operate_result:
    def __init__(self):
        #标准输出
        self.stderr = None
        self.stdout = None
        self.returncode = 0

        self.stderrPrint = None
        self.stdoutPrint = None
        #操作结果
        self.resultlist = []

    def success(self):
        return self.returncode == 0

s_operate_success_reult = zl_operate_result()

def shell_exec(cmdstr, result = None):
    if result == None:
        result = zl_operate_result()
    else:
        result.stderr = None
        result.stdout = None
        result.returncode = 0
        result.resultlist = []

    proc = subprocess.Popen(cmdstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    if result.stdoutPrint != None :
        while proc.poll() is None:
            for line in iter(proc.stdout.readline, b''):
                s = str(line)
                result.stdoutPrint(s)
                if result.stdout == None:
                    result.stdout = [s]
                else:
                    result.stdout.append(s)

    proc.wait()
    if result.stdoutPrint != None :
        if result.stdout != None:
            result.stdout = "\n".join(result.stdout)
    else:
        result.stdout = proc.stdout.read()
    result.stderr = proc.stderr.read()
    result.returncode = proc.returncode
    return result
