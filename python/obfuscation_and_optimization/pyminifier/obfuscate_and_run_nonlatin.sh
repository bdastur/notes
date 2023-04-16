#!/bin/bash

# Obfuscate.
# Note using --obfuscate option obfuscates function name, which I want to avoid.
#
pyminifier --obfuscate-variables --obfuscate-builtins --replacement-length=10 \
    --nonlatin\
    -o primeLib_Obfuscated_nonlatin.py primeLib.py

./app_nonlatin.py


