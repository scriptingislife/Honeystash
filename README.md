# CloudsOfHoney

## Setup
0. cd conf/ssh
0. ssh-keygen -f id_rsa -t rsa -C coh -N ''
0. vim group_vars/all and set:
    1. slack_channel
    1. slack_token

## Rsync

## Flink


## Supported operating systems
* Ubuntu Serve 16.04

## To do:
* Set hostname
* Secure Flink behind NGINX
* Setup UFW firewall
* Setup chroot for malware
* Better way to generate SSH keys and distribute
