#! /usr/bin/en bash

sudo mn -c
rm -f mn*
sudo ps  aux | egrep "python"
green='\033[0;32m'
echo "\n ${green} PIDs with spaces"
read var1 var2 var3 var4
sudo kill -9 $var1 $var2 $var3 $var4
