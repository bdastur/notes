# Git tips

## Useful Links
* [https://github.com/awslabs/git-secrets](Git secrets) 

## Securely releasing code on opensource.

### Git Secrets:
Useful tool, that prevents you from commiting passpowrds and sensitive info. It will
scan for passwords, secrets and other sensitive data.

Usage:

```
# install:
> brew install git-secrets

# settin git up for your git repo.
> cd <your git repo>
>  git secrets --install
>  git secrets --register-aws
>  git secrets --scan


```






