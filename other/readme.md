# Misc notes before it can find a proper category.

[Application container security](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf)
[Automatically get Docker security vulnerabilities posted to slack channel](http://rprakashg.io/blog/posts/post-docker-security-updates-to-slack/)
[Kwalify is a parser, schema validator for yaml](http://www.kuwata-lab.com/kwalify/)
[Useful tmux config and other dot files](https://github.com/alghanmi/dotfiles/blob/master/.tmux.conf)
[Open Sensus - OpenCensus is a single distribution of libraries that collect metrics and distributed traces from your services ](https://opencensus.io/)
[A free certificate authority](https://letsencrypt.org/)


# Linux tips:

## How to terminate a unresponsive ssh connection.
Say you are working on a remote host, execute a command and it hangs, or the 
ssh connection hangs.
```
Hit <Enter>
Type ~.
```

From the official ssh manpage:
```
-e escape_char
Sets the escape character for sessions with a pty (default: '~'). The escape 
character is only recognized at the beginning of a line. 
The escape character followed by a dot ('.') closes the connection; 
followed by control-Z suspends the connection; 
and followed by itself sends the escape character once. 
Setting the character to ''none'' disables any escapes and makes the session fully transparent.
```

OOM Killer:
https://www.oracle.com/technetwork/articles/servers-storage-dev/oom-killer-1911807.html

OOM refers to a computing state where all available memory, including swap space, has been
allocated. Normally this will cause the system to panic and stop functioning as expected. There
is a switch that controls OOM behavior in /proc/sys/vm/panic_on_oom. When set to 1, the kernel
will panic on OOM. A setting of 0 instructs the kerneel to call a function named oom_killer on an
OOM. Usually OOM Killer will kill rogue processes to let the system survive.

