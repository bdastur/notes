# Linux Networking.

## Useful links
[Linux networking tools](https://wizardzines.com/networking-tools-poster.pdf)


## Network Routing

### ip route commands

```
ip route show                                       Display the routing table
ip route add 10.0.2.0/24 via 10.0.2.10 dev eth1      Add a route
ip route del 10.0.2.0/24 via 10.0.2.10 dev eth1      Delete  a route
ip route add default via 10.0.2.10                   Add a default gateway
ip route add prohibit 10.0.2.0/24                    Block destination route
ip route add blackhole 100.0.2.0/25                  Block destination route, silently discard.

```

Syntax of `ip route add`

```
ip route add <network to connect to> via <ip used to reach the network> dev <interface name>
```


#### Adding a default gateway with route
```
ip route add default via 10.0.0.1 dev eth0 
```

#### Adding a default gateway with ip
```
ip route add default via 10.0.2.20
```

#### Prohibiting access

```
[cloud_user@ip-10-0-3-10 ~]$ sudo ip route delete 10.0.1.0/24 via 10.0.3.20 dev eth0
[cloud_user@ip-10-0-3-10 ~]$ sudo ip route add prohibit 10.0.1.0/24
[cloud_user@ip-10-0-3-10 ~]$ ping 10.0.1.10
Do you want to ping broadcast? Then -b. If not, check your local firewall rules.
[cloud_user@ip-10-0-3-10 ~]$ ping 10.0.1.10 -b
WARNING: pinging broadcast address
connect: Permission denied
```

### Displaying statistics on network sockets.

#### SS: A utility to investigate network sockets.

```
-l, --listening           display listening server sockets
-a, --all                 Display all sockkets(default: connected)
-i, --iinterfaces         display interface table
-s, --summary             Show socket usage summary
-e, --extended            Show detailed socket information
-n, --numeric             Don't resolve names
-p, --programs            Display PID/Proram name for sockets
-t, --tcp                 Display only TCP sockets
-u, --udp                 Display only UDP sockets


```

### Network configuration files.

#### ifcfg-eth<n>
On RHEL based systems the interface configuration files are named after the
interface that they reference. eg: ifcfg-eth0. Located in /etc/sysconfig/network-scripts
directory.
[RHEL Documentation - network interfaces](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/s1-networkscripts-interfaces)
```
TYPE=Ethernet           Type of network interface device
BOOTPROTO=none          Specify boot protocol none|dhcp|bootp
DEFROUTE=yes            Specify default route for IPV4 yes|no
USERCTL=yes             Allow non-root users to control this device  yes|no
IPV4_DEFROUTE=yes       
IPV4_FAILURE_FATAL=no   Disable the device if the configuration fails yes|no
IPV6_FAILURE_FATAL=no   Disable the device if the configuration fails yes|no
IPV6INIT=yes            Enable or disable IPV6 on the interface
NAME=eth0               Specify the name for the interface
UUID=..                 Unique identifier for the device 
ONBOOT=yes              Activate interface on boot yes|no
HWADDR=e0:5b:42:fc:43   Specify the MAC address for the interface
IPADDR=10.0.1.12        IPV4 address
PREFIX=24               Network prefix
NETMASK=255.255.255.0   Specify netmask
GATEWAY=10.0.1.1        Gateway address
DNS1=192.168.3.23       DNS Server
DNS2=10.213.33.3        Another DNS server
PEERDNS=yes             Modify the /etc/resolv.conf file yes|no
```


#### /etc/hosts
Associate hostnames with IP addresses

#### /etc/resolv.conf
Specifies DNS servers and searches domains for the host.

#### /etc/sysconfig/network
Used to specify global network settings

#### /etc/nsswitch.conf
Used to determine which source to obtain name-service information and in what
order. 








