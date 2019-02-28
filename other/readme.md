# Misc notes before it can find a proper category.

[Application container security](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf)
[Automatically get Docker security vulnerabilities posted to slack channel](http://rprakashg.io/blog/posts/post-docker-security-updates-to-slack/)
[Kwalify is a parser, schema validator for yaml](http://www.kuwata-lab.com/kwalify/)
[Useful tmux config and other dot files](https://github.com/alghanmi/dotfiles/blob/master/.tmux.conf)


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

