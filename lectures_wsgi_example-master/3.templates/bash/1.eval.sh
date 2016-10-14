#! /usr/bin/env bash

# render a template configuration file
# expand variables + preserve formatting
render_template() {
  eval "echo \"$(cat $1)\""
}

SRC_SERVER_PUB_IP=192.168.0.100
SRC_SERVER_LOCAL_IP=127.0.0.1
FQDN=example.com

render_template 1.nginx_proxy_conf.tpl > proxy.nginx.conf
