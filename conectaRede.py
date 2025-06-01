'''
    Projeto para aula de Wokwi
'''
try:
  import usocket as socket
except:
  import socket

from time import sleep
from machine import Pin
import ubinascii
import machine
import network
import json
import esp
esp.osdebug(None)

# coletor de lixo 
import gc
gc.collect()


# configura a rede para acessar o roteador 
rede = network.WLAN(network.STA_IF)
# ativa a rede 
rede.active(True)
# imprime todas as redes localizadas
print(rede.scan())
# se conecta a rede do Wokwi-GUEST
rede.connect("Wokwi-GUEST","")
# espera a ter a conexão estar ok 
while not rede.isconnected():
    print(".",end="")
    sleep(1)
# imprime os dados da rede
print(rede.ifconfig())

