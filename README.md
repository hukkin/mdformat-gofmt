[![Build Status](https://github.com/hukkinj1/mdformat-gofmt/workflows/Tests/badge.svg?branch=master)](<https://github.com/hukkinj1/mdformat-gofmt/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)
[![PyPI version](<https://img.shields.io/pypi/v/mdformat-gofmt>)](<https://pypi.org/project/mdformat-gofmt>)

# mdformat-gofmt
> Mdformat plugin to gofmt Go code blocks

## Description
mdformat-gofmt is an [mdformat](https://github.com/executablebooks/mdformat) plugin
that makes mdformat format Go code blocks with [gofmt](https://golang.org/cmd/gofmt).
The plugin invokes gofmt in a subprocess so having Go installed is a requirement.

## Installing
1. [Install Go](https://golang.org/doc/install)
1. Install mdformat-gofmt
   ```bash
   pip install mdformat-gofmt
   ```

## Usage
```bash
mdformat YOUR_MARKDOWN_FILE.md
```
