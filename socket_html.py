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

def web_page():
    html = """<html><head></head><body><H1>Aula TEC TI </H1></body></html>  """
    return html

# inicia a conexão com socket
# socket TCP/IP 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# escutando na porta 80
s.bind(('', 80))
# escutando até 5 conexões simultaneas
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()


