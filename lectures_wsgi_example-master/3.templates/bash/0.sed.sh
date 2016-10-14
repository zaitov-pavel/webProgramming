#! /usr/bin/env bash

SRC_SERVER_PUB_IP=192.168.0.100
SRC_SERVER_LOCAL_IP=127.0.0.1
FQDN=example.com

sed -e "s/{{ SRC_SERVER_PUB_IP }}/${SRC_SERVER_PUB_IP}/"\
  -e "s/{{ SRC_SERVER_LOCAL_IP }}/${SRC_SERVER_LOCAL_IP}/"\
  -e "s/{{ FQDN }}/${FQDN}/g" < 0.nginx_proxy_conf.tpl > proxy.nginx.conf
