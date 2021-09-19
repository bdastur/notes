# Pre-commit

A framework for managing and maintaining multi-language pre-commit hooks.

## Useful Links:
[pre-commit Framework Docs](https://pre-commit.com/)


## Installing on MAC:
```
brew install pre-commit
```

## Usage:

### Create a basic configuration:

* Create .pre-commit-config.yaml file in your git repo.
* You can generate a sample config using `pre-commit sample-config` command as shown
  below:

```
> pre-commit sample-config > .pre-commit-config.yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

```

### Running precommit manually:

```
pre-commit run --all-files
```

### Install git hooks

```
> pre-commit install
pre-commit installed at .git/hooks/pre-commit

```

### Adding badge to yoru repository.

The badge shows that you use pre-commit.

```
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

```

## Terraform precommit

* [Collection of git hooks for Terraform](https://github.com/antonbabenko/pre-commit-terraform)

### Installing hooks
```
brew install terraform-docs
```

### Adding the pre-comming-config config:

```
> cat .pre-commit-config.yaml 
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
-   repo: git://github.com/antonbabenko/pre-commit-terraform
    rev: v1.31.0
    hooks:
    -   id: terraform_docs

```



