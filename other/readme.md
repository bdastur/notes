# Misc notes before it can find a proper category.

* [Application container security](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf)
* [Automatically get Docker security vulnerabilities posted to slack channel](http://rprakashg.io/blog/posts/post-docker-security-updates-to-slack/)
* [Kwalify is a parser, schema validator for yaml](http://www.kuwata-lab.com/kwalify/)
* [Useful tmux config and other dot files](https://github.com/alghanmi/dotfiles/blob/master/.tmux.conf)
* [Open Sensus - OpenCensus is a single distribution of libraries that collect metrics and distributed traces from your services ](https://opencensus.io/)
* [A free certificate authority](https://letsencrypt.org/)
* [Everything curl - ebook](https://ec.haxx.se/)
* [Precommit hooks](https://github.com/pre-commit/pre-commit-hooks/tree/master/pre_commit_hooks)
* [Terraform for zdt updates](https://medium.com/@endofcake/using-terraform-for-zero-downtime-updates-of-an-auto-scaling-group-in-aws-60faca582664)
* [Terraform vs CF](https://medium.com/@endofcake/terraform-vs-cloudformation-1d9716122623)
* [Glitch](https://glitch.com/)
* [Bonnie++ filesystem benchmarking](https://www.linux.com/news/using-bonnie-filesystem-performance-benchmarking/)
* [Atlantis - terraform pull request automation](https://www.runatlantis.io/)
* [Terraform compliance](https://terraform-compliance.com/)
* [FedRamp compliance with terraform](https://www.hashicorp.com/resources/automating-fedramp-security-compliance-with-terraform)
* [Jsonnet](https://jsonnet.org/learning/tutorial.html)
* [codepen](https://codepen.io/bdastur/pen/MWYwXjG)
* [High performance browser networking](https://hpbn.co/introduction-to-wireless-networks/)
* [How to write a changelog](https://keepachangelog.com/en/0.3.0)
* [c4 model for visualizing software architecture](https://c4model.com/)
* [Writing Github Profile Readme](https://dev.to/m0nica/how-to-create-a-github-profile-readme-1paj)
* [Elements of a beautiful README](https://github.com/matiassingers/awesome-readme)
* [Markdown Cheetsheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)
* [JSON Crack - Visualize JSON data](https://github.com/AykutSarac/jsoncrack.com)
* [Dan McKinley - Data Driven Done Right. Talk at lean startup conference](https://mcfunley.com/data-driven-products-lean-startup-2014)
* [Dan McKinley - Choose boring tech](https://mcfunley.com/choose-boring-technology)
* [Camille Fournier - Make boring plans](https://skamille.medium.com/make-boring-plans-9438ce5cb053)

* [Nomad home server](https://mrkaran.dev/posts/home-server-nomad/)
* [Caddy reverse proxy](https://caddyserver.com/docs/quick-starts/https)
* [API Testing automation](https://github.com/intuit/karate)
* [Manage runtime versions with CLI](https://asdf-vm.com/#/)
* [Github - Awesome code review](https://github.com/joho/awesome-code-review)
* [Terminal like website](https://hackernoon.com/how-to-make-a-terminal-like-portfolio-website-for-yourself-27d7a7030004)
* [cross-shell prompt. customizable prompt](https://starship.rs/)
* [change data capture tool](https://debezium.io/)
* [How to set default github branch from master to main](https://stevenmortimer.com/5-steps-to-change-github-default-branch-from-master-to-main/)
* [The Twelve Factors](https://12factor.net/)
* [Microservice or Distributed Monolith pitfall](https://www.gremlin.com/blog/is-your-microservice-a-distributed-monolith/)
* [CNCF CLoud Native Lanscape](https://landscape.cncf.io/?grouping=no&sort=stars)
* [ytt: CLI for patching and templating yaml files](https://carvel.dev/ytt/docs/v0.39.0/)
* [Measuring engineering productivity](https://abseil.io/resources/swe-book/html/ch07.html)
* [Google Software Engineering book](https://abseil.io/resources/swe-book/html/toc.html)
* [chatGPT Usecases](https://cookup.ai/chatgpt/usecases/#assistant)
* [CLI Command line tools](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6)
* [Software Architecture Design Patterns](https://www.redhat.com/architect/14-software-architecture-patterns)
* [Tool - gitprecommit/gitcommit - prevents from comitting secrets, passwords etc](https://github.com/awslabs/git-secrets)
* [Tool - create ephemeral preview environments.](https://github.com/livecycle/preevy)
* [Blog - What do metrics tell you? challenge and be skeptical](https://www.scarletink.com/be-skeptical-challenging-beliefs-underlying-everything/)
* [List of vim bundles](https://github.com/sharpicx/dotfiles/tree/main/.vim/plugged)
* [PlantUML - generate diagrams](https://plantuml.biz/en/guide)
* [Large collection of opensource frameworks/tools/libraries](https://free-for.dev/#/)
* [Convert shell script to compiled C code - https://github.com/neurobin/shc](https://neurobin.github.io/shc/)

# Linux tips:

* [Linux n/w troubleshooting](https://www.redhat.com/sysadmin/beginners-guide-network-troubleshooting-linux)
* [Shell script static analysis tool](https://www.shellcheck.net/wiki/Home)
* [Computer Architecture](https://cpu.land/the-basics)


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
* http://flaws.cloud/hint1.html
* https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/
* https://github.com/influxdata/telegraf


### Vulnerability database
* https://www.cvedetails.com/

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


## How to:

### ps:

##### Display environment variables for a process with ps command

```
ps eww $PID | tr ' ' '\n' | grep =

```

##### Repeat informational header on every page of ps output

```
ps -h
```

##### Get additional information with ps keywords

Include the process state in the output:

```
ps -efh  -o state
```

Include the cpu and mem consumption:

```
ps -ef -o mem -o cpu

```


### grep:

##### Search for a string in a file (basic).

```
$ grep multipart aws/readme.md 
  to use multipart upload.
* For objects larger than 100 MB you should use multipart upload.
* For larger objects use multipart Upload
* Always complete or abort a multipart upload - else the individual chunks
(py3env) ALSONEWLYSTRONG:notes behzad.dastur$ 
```

#### search for string with spaces in a file (basic)

```
$ grep "multipart upload" aws/readme.md 
  to use multipart upload.
* For objects larger than 100 MB you should use multipart upload.
* Always complete or abort a multipart upload - else the individual chunks
```

#### Ignore case (case insensitive)

```
$ grep -i "multipart upload" aws/readme.md 
  to use multipart upload.
* For objects larger than 100 MB you should use multipart upload.
### Multipart Upload:
* For larger objects use multipart Upload
* Always complete or abort a multipart upload - else the individual chunks

```

#### Show context for your searches.

```
 -A num, --after-context=num
     Print num lines of trailing context after each match.  See also the -B and -C options.

-B num, --before-context=num
    Print num lines of leading context before each match.  See also the -A and -C options.

-C[num, --context=num]
    Print num lines of leading and trailing context surrounding each match.  The default is 2 and is equivalent to -A 2 -B 2.  Note: no whitespace may be given
    between the option and its argument.
```

Example:
```
$ grep -C 2  "multipart upload" aws/readme.md 
* Durability : 99. 11 9s and Availability: 99.99%
* Largest file size you can use to PUT an object: 5GB. After that you have
  to use multipart upload.
* For objects larger than 100 MB you should use multipart upload.
* Minimum file size: 0 bytes
* Maximum file/object size: 5TB.
--
--
* For larger objects use multipart Upload
* Each chunk should be minimum 5MB size.
* Always complete or abort a multipart upload - else the individual chunks
  upload will not be cleaned up and will cost.

```

#### Invert match (-v)


```
$ grep -v  "multipart upload" aws/readme.md 
 AWS Notes:

## Links:
[AWS Learning Library](https://www.aws.training/LearningLibrary)
[E2connect - a way of authenticating SSh sessions using IAM](https://github.com/glassechidna/ec2connect)
[S3 Benchmark](https://github.com/dvassallo/s3-benchmark)
:
```

##### How to ignore blank lines (-v)

```
$ grep -v  "^$" aws/readme.md |more
 AWS Notes:
## Links:
[AWS Learning Library](https://www.aws.training/LearningLibrary)
[E2connect - a way of authenticating SSh sessions using IAM](https://github.com/glassechidna/ec2connect)
[S3 Benchmark](https://github.com/dvassallo/s3-benchmark)
[Open Guides AWS](https://github.com/open-guides/og-aws)
:

```

#### How to recursively search files within a directory.  (-r)

```
-R, -r, --recursive
    Recursively search subdirectories listed.

-S      If -R is specified, all symbolic links are followed.  The default is not to follow symbolic links.
```

Example:

```
$ grep -r "multipart upload" aws/
aws//s3_multipart.py:A very simple example of using boto3 client APIs for multipart upload.
aws//s3_multipart.py:Some key things to consider when performing the multipart upload.
aws//s3_multipart.py:    Upload a large file using multipart upload.
aws//s3_multipart.py:    1. Initiate a multipart upload. Get the upload id which will be used in
aws//s3_multipart.py:    # Initiate multipart upload.
aws//s3_multipart.py:        print "Exception occured initiating multipart upload: %s" % err
aws//readme.md:  to use multipart upload.
aws//readme.md:* For objects larger than 100 MB you should use multipart upload.
aws//readme.md:* Always complete or abort a multipart upload - else the individual chunks

```

#### Only include specific files while searching for a pattern. (--include)


```
$ grep -r "multipart upload" aws/ --include "*.md"
aws//readme.md:  to use multipart upload.
aws//readme.md:* For objects larger than 100 MB you should use multipart upload.
aws//readme.md:* Always complete or abort a multipart upload - else the individual chunks
(py3env) ALSONEWLYSTRONG:notes behzad.dastur$ 

```





















