# Albert AWS console opener plugin "awscaller"

<p align="center">
  <!-- <img src="https://i.imgur.com/gPCNyGQ.png" alt="Cover image"/> -->
  <img src="https://i.imgur.com/2Uf93Rp.png" alt="Cover image"/>
</p>

This is a Python extension for [albert](https://github.com/albertlauncher/albert) that aims to help us developers/devops by opening and AWS console page using the provided service name.

## Installation

> Note: This plugin depends on [Albert Launcher v0.17.*](https://albertlauncher.github.io/installing/)

Clone the branch/tag you want (i.e. main, v0.3.0, etc):

```sh
git clone https://github.com/davegallant/awscaller -b main \
  ~/.local/share/albert/org.albert.extension.python/modules/awscaller
```

Then you just need to go to the Extension settings and enable the "awscaller" Python extension:

<p align="center">
  <img src="https://i.imgur.com/XlOlSNc.png" alt="Enabling Python Extension"/>
</p>

## Usage

To trigger the extension you should type `aws <service name>` to open the given service page on your aws console, or type only `aws` to open the console home.

Examples:

```
aws lambda
aws s3
aws rds
aws apigateway
aws ec2
aws ecs
```

---

We also support query string parameters that can be used for pretty much anything AWS console supports doing via query strings.

How to use:

```
aws <service> <key>:<value>...
```

Example:

```
aws ec2 region:us-east-1
```

## Backlog

- Allow specific querying for specific aws services, such as EC2 filters
