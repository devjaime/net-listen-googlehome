import sys
import subprocess, time
import os 
from decouple import config

IP_NETWORK = config('IP_CONFIG')
IP_DEVICE = config('IP_DEVICE') + ":"

proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
while True:
  
  line = proc.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  connected_ip = line.decode('utf-8').split()[3]
  if connected_ip != IP_DEVICE:
    print("El invitado no a llegado - " + IP_NETWORK +  " -  " + IP_DEVICE)
  if connected_ip == IP_DEVICE:
      print("El invitado acaba de llegar")
      time.sleep(15)
      subprocess.Popen(["say", "ok google, turn on room"])
      print("Encender Luces")
      time.sleep(15)
      subprocess.Popen(["say", "ok google, turn on air"])
      print("Enceder aire acondicionado")
      time.sleep(15)
      subprocess.Popen(["say", "ok google, play yoga music on spotify"])
      print("Musica relajante")
      time.sleep(15)
      subprocess.Popen(["say", "ok google, script"])
      print("Saludar al invitado")
      time.sleep(15)
      break