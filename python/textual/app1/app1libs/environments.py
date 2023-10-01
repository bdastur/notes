#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import pprint

class Environments():
    def __init__(self, envFile="./configs/environments.json"):
        self.validated = False
        if not os.path.exists(envFile):
            print("File %s does not exist!" % envFile)
            return
        self.envFile = envFile

        # Parse environments
        with open(self.envFile, 'r') as inFile:
            self.envData = json.load(inFile)

        ret, msg = self.validateEnvironmentConfig()
        if not ret: 
            print("Environment config [%s] is not valid [%s]" % \
                  (self.envFile, msg))
            return

        self.validated = True
    
    def validateEnvironmentConfig(self) -> (bool, str):
        validClouds = ["cloud-aws", "cloud-azure", "cloud-gcp"]

        for cloud in self.envData.keys():    
            if cloud not in validClouds:
                return False, "Invalid cloud %s specified. Supported %s" % (cloud, validClouds)
        
        return True, "Environment config parsed successfully"

    def getAwsEnvironments(self):
        return self.envData["cloud-aws"]
    
    def getAwsEnvironmentRegion(self, id):
        if self.envData["cloud-aws"].get(id, None) is None:
            return None, "Id %s not found" % id
        if self.envData["cloud-aws"][id].get("region", None) is None:
            return None, "'region' not found in env config [%s]" % id

        return self.envData["cloud-aws"][id]["region"]

    def getAwsEnvironemntDescription(self, id):
        if self.envData["cloud-aws"].get(id, None) is None:
            return None, "Id %s not found" % id
        if self.envData["cloud-aws"][id].get("description", None) is None:
            return None, "'description' not found in env config [%s]" % id
        
        return self.envData["cloud-aws"][id]["description"]
    
    def getAwsEnvironmentProfile(self, id):
        if self.envData["cloud-aws"].get(id, None) is None:
            return None, "Id %s not found" % id
        if self.envData["cloud-aws"][id].get("profile", None) is None:
            return None, "'profile' not found in env config [%s]" % id
        
        return self.envData["cloud-aws"][id]["profile"]

    def dumpEnvironmentConfig(self):
        pp = pprint.PrettyPrinter()
        pp.pprint(self.envData)


        

