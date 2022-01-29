# SSL Operations

## Useful links:
- [How ssl works](https://www.tutorialsteacher.com/https/how-ssl-works)
- [Mozilla Security](https://developer.mozilla.org/en-US/docs/Mozilla/Security/x509_Certificates#Self-signed_certificates)
- [Make locally-trusted development certificates](https://github.com/FiloSottile/mkcert)



## Creating a CSR.

### Simple method:
```
$ openssl req -newkey rsa:2048 -out mynewservice.csr  -nodes -keyout mynewservice_private.key
Generating a 2048 bit RSA private key
..............................+++
......+++
writing new private key to 'mynewservice_private.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) []:US
State or Province Name (full name) []:CA
Locality Name (eg, city) []:Pleasanton
Organization Name (eg, company) []:acme.corp
Organizational Unit Name (eg, section) []:Eng
Common Name (eg, fully qualified host name) []:www.acme.svc.com
Email Address []:acme@acme.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:

$ ls
mynewservice.csr		mynewservice_private.key	myserver.cnf			san.cnf
```

### How to create a CSR with Subject alternative names.

```
$ openssl req -new -config myserver.cnf -out myserver_1.csr -keyout myserver_1_private.key
Generating a 2048 bit RSA private key
............................................+++
......................+++
writing new private key to 'myserver_1_private.key'
-----
ALSONEWLYSTRONG:tls behzad.dastur$

```

## How to create a self signed cert in one command:
```
openssl req -x509 \
  -nodes  \
  -subj "/C=US/ST=California/L=Mountainview/O=AcmeCorp/OU=ENG/CN=acme.svc.com" \
  -newkey rsa:4096 \
  -keyout /tmp/key.pem   -out /tmp/cert.pem   -days 365

```


## How to get common name from a csr

```
$ openssl req -noout -subject -in myservice.csr
subject=/C=US/ST=CA/L=Pleasanton/O=acme.corp/OU=Eng/CN=www.acme.svc.com/emailAddress=acme@acme.com

```

## How to get common name for cert

```
$ openssl x509 -noout -subject -in <cert.pem>
```


## How to get/verify SAN from a csr

```
$ openssl req -noout -text -in myserver_1.csr
```

## Check expiration date of a local certificate

```
$ openssl x509 -noout -dates -in cert.pem
notBefore=Nov 20 23:22:26 2020 GMT
notAfter=Nov 20 23:22:26 2021 GMT

```

## How to get the certificate from a server

```
openssl s_client -state -connect google.com:443
```

## How to checkk the expiration date of cert on server:

```
$ echo | openssl s_client -showcerts -connect google.com:443 | openssl x509 -noout -dates
depth=2 OU = GlobalSign Root CA - R2, O = GlobalSign, CN = GlobalSign
verify return:1
depth=1 C = US, O = Google Trust Services, CN = GTS CA 1O1
verify return:1
depth=0 C = US, ST = California, L = Mountain View, O = Google LLC, CN = *.google.com
verify return:1
DONE
notBefore=Nov  3 07:22:00 2020 GMT
notAfter=Jan 26 07:22:00 2021 GMT

```



## Convert certificate formats:

### Convert DER to PEM format:

```
$ openssl x509 -inform der -in certificate.der -out certificate.pem

```


### Convert PEM to DER format:

```
$ openssl x509 -outform der -in cert.pem -out certificate.der

```






