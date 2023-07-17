#!/usr/bin/env python
# -*- coding: utf-8 -*-


from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=True, outformat="png"):
    ELB("lb") >> EC2("web") >> RDS("userdb")
