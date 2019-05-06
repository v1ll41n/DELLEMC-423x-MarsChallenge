#this Script for setting up the docker-compose settings {localip , check connections)

import requests
import yaml
import netifaces as ni
import re
import os
import time


#getting localHost IP
ni.ifaddresses('eth0')
ip = 'http://'+ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
#print ip

#updating ip in docker-compose.yml file
#1-matching local IP
# with open('docker-compose.yml','r') as f:
  # x=yaml.load(f);#print x
  # endpoint=''.join(x['services']['Dashboard']['environment']);print endpoint
  # g=''.join(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', endpoint))
  # d=endpoint.replace(g,'192.168.1.107');print d
  # x['services']['Dashboard']['environment']=list(d)
  # with open("my_file.yaml", "w") as w :
     # yaml.dump(x, w,default_flow_style=False)
	 
def begin_compose():
  print "[+]Starting Docker Compose"
  os.system('docker-compose up -d --build')
  
def check_connections(ip):
   #checking Flare:
   print "[+]Checking FLare..."
   r = requests.get(ip+':9000')
   try: print "[+] Flare ON"
   except : print "[-]Exiting... Flare is not running";exit(0)

   print "[+]Checking Temperature sensor"
   try: r = requests.get(ip+':9001');print "[+] Temperature sensor ON"
   except : print "[-]Exiting... Temperature sensor is not running";exit(0)

   print "[+]Checking Radiation sensor"
   try : r = requests.get(ip+':9002');print "[+] Radiation sensor ON"
   except : print "[-]Exiting... Radiation sensor is not running";exit(0)

   print "[+]Checking The Publisher"
   try : r = requests.get(ip+':9003');print "[+] The Publisher is ON"
   except : print "[-]Exiting... The Publisher is not running";exit(0)

   print "[+]Checking the Aggregator"
   try: r = requests.get(ip+':9004');print "[+] Flare ON"
   except : print "[-]Exiting... the Aggregator is not running";exit(0)

   print "[+]Checking the GameController"
   try : r = requests.get(ip+':8000');print "[+] GameController ON"
   except : print "[-]Exiting... GameController is not running";exit(0)

   print "[+]Checking the Dashboard"
   try : r = requests.get(ip+':8001');print "[+] Dashboard ON"
   except : print "[-]Exiting... Dashboard is not running";exit(0)

try:
   begin_compose()
   time.sleep(10)
   check_connections(ip)
except KeyboardInterrupt:
   print "[-]Keyboard Interrupt is Received... Exiting";
   os.system('docker stop $(docker ps -q)')
   exit(0)
