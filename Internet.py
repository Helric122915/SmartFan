from subprocess import *
from datetime import datetime

cmd = "ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
  p = Popen(cmd, shell=True, stdout=PIPE)
  output = p.communicate()[0]
  return output

def getIP():
  return run_cmd(cmd)

def getNow():
  return datetime.now().strftime('%b %d %H:%M:%S')
