# SSL Operations


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


## How to get common name from a csr 

```
$openssl req -noout -subject -in myservice.csr
subject=/C=US/ST=CA/L=Pleasanton/O=acme.corp/OU=Eng/CN=www.acme.svc.com/emailAddress=acme@acme.com


```


## How to get/verify SAN from a csr
```
$ openssl req -noout -text -in myserver_1.csr 
```



