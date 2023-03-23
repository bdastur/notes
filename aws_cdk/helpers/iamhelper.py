#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

def main():
    filePath = sys.argv[1]

    print(filePath)
    with open(filePath, "r") as inFile:
        jdata = json.load(inFile)

    print(jdata)
    actions  = jdata["Action"]
    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint(sorted(actions))

if __name__ == '__main__':
    main()
