#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import app1libs.environments as environments

class UT(unittest.TestCase):
    def test_environment_basic(self):
        env = environments.Environments()
        self.assertEqual(env.validated, False, msg="Expecting false")

        env = environments.Environments(envFile="../configs/environments.json")
        self.assertEqual(env.validated, True, msg="Expecting True")

        env = environments.Environments(envFile="testdata/testenvironments.json")
        self.assertEqual(env.validated, True, msg="Expected validated True")

        # Get AWS environments.
        awsEnvs = env.getAwsEnvironments()
        self.assertEqual(len(awsEnvs), 2, msg="Expecting 2 environment definitions")
        env.dumpEnvironmentConfig()

        # Get AWS environemnt info.
        region = env.getAwsEnvironmentRegion("dev")
        self.assertEqual(region, "us-east-1", 
                         msg="Expecting region 'us-east-1', Got %s" % region)
        profile = env.getAwsEnvironmentProfile("dev")
        self.assertEqual(profile, "dev0", 
                         msg="Expecting profile 'dev0', got %s" % profile)

    def test_environment_invalid(self):
        env = environments.Environments(envFile="./testdata/invalid01.json")
        self.assertEqual(env.validated, False, msg="Expecting not validated")


