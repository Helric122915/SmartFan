from subprocess import *
from datetime import datetime

cmdEth0 = "ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"
cmdWlan0 = "ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
  p = Popen(cmd, shell=True, stdout=PIPE)
  output = p.communicate()[0]
  return output

def getIP():
  if run_cmd(cmdWlan0) != "":
    return run_cmd(cmdWlan0)
  elif run_cmd(cmdEth0) != "":
    return run_cmd(cmdEth0)
  else:
    return "No IP Address Found."

def getNow():
  return datetime.now().strftime('%b %d %H:%M:%S')
