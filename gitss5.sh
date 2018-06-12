#!/bin/bash
case $1 in

on)
git config --global http.proxy 'socks5://foo:1080' 
git config --global https.proxy 'socks5://foo:1080'
;;

off)
git config --global --unset http.proxy
git config --global --unset https.proxy
;;

status)
git config --get http.proxy
git config --get https.proxy
;;
esac
exit 0


#how to use
# replace foo to ss5 server
# name it to gitss5
# chmod +x gitss5
# gitss5 on
# gitss5 off
# gitss5 status
