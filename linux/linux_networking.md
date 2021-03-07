# Linux Networking.



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













