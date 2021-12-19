# AWS Route53.


## DNS Concepts:

**TLDs** (Top Level Domains)
* The last word in a domain name represents the "top level domain".
* The second word represents "second level domain name" (it's optional)
* Most general part of the domain (eg: .com, .edu, .org)
* Top of the hierarchy in terms of domain names.
* TLDs are controlled by IANA - Internet Assigned Numbers Authority in a root zone
  database - a DB of all available top level domains.
* ICANN - Internet Corporation for Assigned Names and Numbers.

IPV4: 32 bit field - over 4 billion addresses.
IPV6: 128 bit field - over 340 undecillion addresses.

* Domain names: Human friendly name used to associate to an internet source.
* A proper FQDN ends with a '.', indicating the root of the DNS hierarchy.
* Sometimes software that calls for an FQDN does not require an ending '.'. But it
  is required to conform to ICANN standards.

* In the URI: api.aws.amazon.com.
api            --> host
aws.amazon.com --> subdomain
amazon         --> Second level domain
com            --> top level domain
.              --> root

* DNS uses port 53 to serve requests.
* Primary protocol used is UDP, to serve requests.
* When the response data exceeds 512 bytes TCP protocol is used.

**Name Servers:**
* A computer designated to translate domain names to IP addresses.
* A name server can be authoritative, meaning that they give answers to queries
  about domains under their control. Or they may point to other servers to serve
  cached copies of other name servers data.

**Zone files:**
* A simple text file that contains mapping between domain names and IP addresses.
* This is how a DNS server finally identifies which IP maps to a certain domain name.
* Zone files reside in name servers and define the resources available under a
  specific domain, or the place where one can go to get that info.

**Top Level Domain (TLD) Name Registrars:**
* Domain names must be unique.
* Domain registrar is an org or commercial entity that manages reservation of
  internet domain names.
* A domain name registrar must be accredited by a generic TLD registry and/or
  a country code TLD.


**Steps involved in DNS resolution:**
* When you type a domain name in your browser, the computer first checks it's host
  file to see if the domain name is stored locally.
* If not it will check it's DNS cache to see if the site was visited before.
* If it still does not have a record of that domain name, it will contact a DNS
  server to resolve the domain name.
* DNS is a hierarchical system. At the top of the system are root servers.
* There is approximately 13 root servers in operation.
* When a request comes in for a domain that a lower level name server cannot resolve,
  a query is made to the root server for domain.
* The root servers are mirrored and replicated. When requests are made to a certain
  root server, the request will be routed to the nearest mirror of the root server.
* The root servers won't actually know where the domain is hosted. They will
  however be able to direct the requester to the name server that handles the
  specifically requested TLD.
* For eg: If request for www.wikipedia.org is made to the root server, it will check
  it's zone files for a listing that matches the domain name buit will not find it.
  It will instead find a record for .org TLD and give the requester address of the
  name server responsible for .org addresses.

**Top level domain servers:**
* After the root server returns the address of the appropriate server responsible
  for the TLD, the requester sends a new request to that address.
* Once again when the name server searches it's zone files it will not find one in
  it's records. However it will find a listing of the IP address of the same server
  responsible for wikipedia.org.

**Domain-level name servers:**
* At this point the requester has the IP address of the name server that is
  responsible for knowing the actual IP address of the resource.
* It sends a request to the name server to resolve www.wikipedia.org.
* The name server checks it's zone files and finds a zone file associated with
  wikipedia.org. Inside the file is a record that contains the IP address of the
  .www host.
* The name server returns the final address to the requester.

**Resolving name servers:**
* A resolving name server is configured to ask other servers questions.
* It's primary function is to act as an intermediary for a user, caching previous
  query results for improving speed and providing the address of appropriate root
  servers to resolve new requests.
* A user will have a few name servers cofnigured on their computer system.
* Name servers are typically provided by an ISP or other organizations.
* There are public DNS servers that you can query.

**Zone files:**
* Zone files are the way the name servers store info about domains they know.
* The more zone files a name server has, the more requests it will be able to
  answer authoritatively.
* If the server is configured to handle recursive queries, like a resolving name
  server, it will find the answer and return it. Otherwise it will tell the
  requesting entity where to look next.
* Zone files describe a DNS zone, which is a subset of the entire DNS.
* Generally used to configure a single domain.
* Zone file's $ORIGIN directive is a parameter queal to the zone's highest level
  of authority by default.
* If a zone file is used to configure example.com domain, the $ORIGIN would be
  set to example.com
* TTL - Time to Live value. Defines the length of time the previously queried results
  are available to the caching name server before they expire.

### Record Types
A record is a single mapping between a resource and a name.

**Start of Authority Record (SOA):**
* Mandatory for all zone files.
* Identifies the base DNS information about the domain.
* Each zone contains a single SOA record.
* Stores information about:
  - Name of the DNS server for that zone.
  - The administrator of the zone.
  - The current version of the data file.
  - Number of seconds a secondary name server should wait before checking for
    updates.
  - Number of seconds a secondary name server should wait before retrying failed
    zone transfer.
  - Max number of seconds a secondary name can use data before it must be refreshed
    or expire.
  - Default TTL value for resource records in the zone.

**A and AAAA Records:**
* Both types of address records map a host to an IP address.
* A: maps a host to IPV4 address
* AAAA: maps a host to an IPV6 address
* A stands for Address

**Canonical Name (CNAME):**
* Defines an alias for the CNAME for your server (the domain name defined in
  A or AAAA record).
* Resolves one domain to another.

**Mail Exchange (MX):**
* Define the mail serers used for a domain and ensures emails are routed correctly.
* MX record should point to a host defined by A or AAAA record and not defined
  by CNAME.

**Name Server (NS):**
* Used by TLD servers to direct traffic to the DNS server that contains the
  authoritative DNS record.

**Pointer (PTR):**
* PTR record is essential the reverse of an A record.
* PTR records map an IP address to a DNS name.
* Mainly used to check if the server name is associated with an IP address from
  where the connection was initiatd.

**Sender Policy Framework (SPF):**
* SPF records are used by mail servers to combat spam.
* It tells a mail server what IP addresses are authorized to send emails from
  your domain name.
* Prevents people from spoofing emails from your domain name.

**Text (TXT):**
* Used to hold text information.
* Provides the ability to associate some arbitary and unformatted text with
  a host or other name, such as human readable information about a server,
  network, data center.

**Service (SRV):**
* It is a specification of data in the DNS defining the location of the servers for
  specified services.


## Route53 three main functions:

### Domain registration:
* Amazon route53 lets you register domain names, such as example.com.
* You also have an option to transfer an already registered domain name with
  another registrar to route53.
* Supports domain registration for a wide variety of generic TLDs and geographic
  TLDs.
* There is a limit of 20 domain names for new customers as of March 2021.
* If you have an existing account and your default limit is 50 now, it will remain 
  at 50. Reference: Amazon Route 53 Quotas.


### DNS Service:
* Route53 is an authoritative DNS service.
* When someone enters your domain name in a browser or sends you an email, a DNS
  request is forwarded to the nearest Route53 DNS server in a global network of 
  authoritative DNS servers. Route53 responds with the IP address that you specified.
* If you registered your domain with another domain registrar, that registrar is
  probably providing DNS service for your domain. You can transfer DNS service to
  Route53 without having to transfer the registration for the domain.


### Hosted Zones:
* A hosted zone is a collection of resource record sets hosted by route53.
* A hosted zone represents resource record sets that are managed together under a
  single domain name.
* Each hosted zone has it's own metadata and configuration information.
* There are two types of hosted zones:
  - Private hosted zone: Holds information about how you want to route traffic
    for a domain and it's subdomains within one or more VPCs.
  - Public hosted zone: How you want to route traffic on the internet for
    a domain and it's subdomains.
* Resource record sets contained in a hosted zone must share the same suffix.


## Supported Record Types:
* A
* AAAA
* CNAME
* MX
* NS
* PTR
* SOA
* SPF
* SRV
* TXT

* **Alias Records** have special function that is not present in other DNS servers.
* Their main function is to provide special functionality and integration into
  AWS services.
* Unlike CNAME records, they can also be used at the Zone Apex, where CNAME cannot.
* Alias records can also point to AWS resources that are hosted in other accounts
  by manually entering the ARN.

## Routing Policies:

**Simple**
* This is the default routing policy when you create a new resource.
* If you choose a simple routing policy you can only have one record with multiple
  IP addresses. If you specify multiple values in a record, Route53 returns all values
  to the user in a random order.

**Weighted**
* Allows you to split traffic based on different weights assigned.
* EG: you can set 10% of traffic to go to us-east-1 and 90% to go to eu-west-1.
* Healthchecks:
  - Can set health checks on indivisual record sets.
  - If a record set fails a health check, it will be removed from Route53 until it
    passes the health check.
  - You can set SNS notifications to alert you if a health check fails.

**Latency based routing policy**
* Allows routing based on lowest network latency.
* To use latency-based routing, you create a latency resource record set for the
  Amazon EC2 (or ELB) resource in each region that hosts your site.
* When route53 receives a query, it selects the latency resource record set for
  the region that gives the user the lowest latency.

**Failover routing policy**
* Use when you want to create an active/passive setup.
* Route53 will monitor the health of your primary site using healt check.
* A health check monitors the health of your endpoints.

**Geolocation Routing policy**
* Let's you choose where your traffic will be sent based on geographic location
  of your users (i.e location from which DNS queries originate).
 
**Geoproximity Routing (Traffic Flow only mode)**
* Route traffic based on geographic location of your users and your resources.
* You can optionally choose to route more traffic or less to a given resource by
  specifying a value, known as a bias. A bias expands or shrinks the size of the
  geographic region from which traffic is routed to a resource.

NOTE: To use geoproximity routing, you must use Route53 traffic flow.

**Multivalue Answer policy**
* Similar to simple routing, however it allows you to check the health of each
  resource, so Route53 only returns values for healthy resources.
* Can respond to DNS queries with up to 8 IP addresses of 'healthy' targets.

































