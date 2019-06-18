#!/bin/bash
###########################################################
# Create a staging folder from where we will run the app.
# This way we version control any thirdpart js/css only once.
###########################################################
if [[ -z $1 ]]; then
    echo "Usage $0 <app to run>"
    echo " Example: $0 bsapp.py"
    echo "Apps: [`ls *.py`]"

fi

# Create staging.
APPNAME=$1
STAGING_ROOT="/tmp/flask_kata"
STAGING_STATIC="${STAGING_ROOT}/static"
STAGING_TEMPLATES="${STAGING_ROOT}/templates"
STAGING_THIRDPARTY="${STAGING_STATIC}/thirdparty"
STAGING_JS="${STAGING_STATIC}/js"
STAGING_CSS="${STAGING_STATIC}/css"

THIRDPARTY_FOLDER="../../../frontend/thirdparty/"

mkdir -p ${STAGING_STATIC}
mkdir -p ${STAGING_TEMPLATES}
mkdir -p ${STAGING_JS}
mkdir -p ${STAGING_CSS}


cp *.py ${STAGING_ROOT}/.
cp static/js/* ${STAGING_JS}/.
cp static/css/* ${STAGING_CSS}/.
cp templates/* ${STAGING_TEMPLATES}/.

if [[ ! -e ${STAGING_THIRDPARTY} ]]; then
    echo "No staging thirdparty"
    cp -R ${THIRDPARTY_FOLDER} ${STAGING_THIRDPARTY}
fi

# Run the app.

${STAGING_ROOT}/${APPNAME}
