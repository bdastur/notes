#!/usr/bin/env python

import os
import subprocess
import json


class Command(object):
    def __init__(self, kubeconfig=None):
        if kubeconfig is None:
            print("Require a kubeconfig file")
            return
        self.kubeconfig=kubeconfig

    def execute_cmd(self, cmd):
        cmd = cmd.split()
        myenv = os.environ.copy()
        myenv["KUBECONFIG"] = self.kubeconfig

        proc = subprocess.Popen(cmd, env=myenv, stdout=subprocess.PIPE)
        outs, errs = proc.communicate()
        print("outs:", outs)
        jdata = {}
        try:
            jdata = json.loads(outs)
            print "jdata: ", jdata
        except ValueError:
            print("No json data")

        return jdata


class KubeParser(object):
    @staticmethod
    def pods_summary(json_data):
        for item in json_data['items']:
            print item['metadata']['name']


def main():
    print("Main")
    kc = Command("/Users/behzad.dastur/clusters/ilmtest/kubeconfig")
    jdata = kc.execute_cmd("kubectl get pods -o json")

    kp = KubeParser()
    kp.pods_summary(jdata)


if __name__ == "__main__":
    main()
