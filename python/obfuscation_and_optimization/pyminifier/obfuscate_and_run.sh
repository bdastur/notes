#!/bin/bash

# Obfuscate.
# Note using --obfuscate option obfuscates function name, which I want to avoid.
#
pyminifier --obfuscate-variables --obfuscate-builtins --replacement-length=10 \
    -o primeLib_Obfuscated.py primeLib.py

./app.py


