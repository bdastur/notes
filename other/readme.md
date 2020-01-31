# Misc notes before it can find a proper category.

[Application container security](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf)
[Automatically get Docker security vulnerabilities posted to slack channel](http://rprakashg.io/blog/posts/post-docker-security-updates-to-slack/)
[Kwalify is a parser, schema validator for yaml](http://www.kuwata-lab.com/kwalify/)
[Useful tmux config and other dot files](https://github.com/alghanmi/dotfiles/blob/master/.tmux.conf)
[Open Sensus - OpenCensus is a single distribution of libraries that collect metrics and distributed traces from your services ](https://opencensus.io/)
[A free certificate authority](https://letsencrypt.org/)
[Everything curl - ebook](https://ec.haxx.se/)
[Precommit hooks](https://github.com/pre-commit/pre-commit-hooks/tree/master/pre_commit_hooks)
[Terraform for zdt updates](https://medium.com/@endofcake/using-terraform-for-zero-downtime-updates-of-an-auto-scaling-group-in-aws-60faca582664)
[Terraform vs CF](https://medium.com/@endofcake/terraform-vs-cloudformation-1d9716122623)
[Glitch](https://glitch.com/)
[Bonnie++ filesystem benchmarking](https://www.linux.com/news/using-bonnie-filesystem-performance-benchmarking/)
[Atlantis - terraform pull request automation](https://www.runatlantis.io/)
[Teerraform compliance](https://terraform-compliance.com/)
[Jsonnet](https://jsonnet.org/learning/tutorial.html)
[codepen](https://codepen.io/bdastur/pen/MWYwXjG)
[High performance browser networking](https://hpbn.co/introduction-to-wireless-networks/)

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

## Followups:
http://flaws.cloud/hint1.html
https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

Vulnerability database
https://www.cvedetails.com/

## Setting up AWS blog feeds in slack

```
Title: AWS Blog
URL: http://feeds.feedburner.com/AmazonWebServicesBlog
Title: What's New
URL: http://aws.amazon.com/rss/whats-new.rss?nc1=f_so_rs
Title: AWS Security Blog
URL: http://blogs.aws.amazon.com/security/blog/feed/recentPosts.rss
Title: AWS Compute Blog
URL: http://feeds.feedburner.com/AwsComputeBlog
Title: AWS Big Data Blog
URL: http://blogs.aws.amazon.com/bigdata/blog/feed/recentPosts.rss

/feed subscribe <ur>
/feed list
```

