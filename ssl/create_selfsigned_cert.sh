#!/bin/bash

echo "Generate self signed cert"
COUNTRY="US"
STATE="CA"
LOCALITY=MOUNTAINVIEW
ORG="Acme Corp"
ORG_UNIT="Eng"
COMMON_NAME="acme.com"

VALIDITY_DAYS="30"
CERT_PATH="/tmp/tls/cert.pem"
KEY_PATH="/tmp/tls/key.pem"

openssl req -x509 \
  -nodes  \
  -subj "/C=${COUNTRY}/ST=${STATE}/L=${LOCALITY}/O=${ORG}/OU=${ORG_UNIT}/CN=${COMMON_NAME}" \
  -newkey rsa:4096 \
  -keyout ${KEY_PATH} -out ${CERT_PATH} \
  -days ${VALIDITY_DAYS} 

