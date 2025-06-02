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

from machine import Pin, SoftI2C
import ssd1306

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.show()

# configura a rede para acessar o roteador 
rede = network.WLAN(network.STA_IF)
# ativa a rede 
rede.active(True)
# imprime todas as redes localizadas
print(rede.scan())
# se conecta a rede do Wokwi-GUEST
rede.connect("PUC-ACD","")
# espera a ter a conexão estar ok 
cnt = 25
while not rede.isconnected():
    print(".",end="")
    cnt -= 1
    if cnt < 0: break
    sleep(0.5)
    
rede.active(False)
sleep(0.5)
rede.active(True)
rede.connect("Wokwi-GUEST","")
#rede.connect("casa","veneza03")
# espera a ter a conexão estar ok 
while not rede.isconnected():
    print(".",end="")
    sleep(1)

# imprime os dados da rede
print(rede.ifconfig())

ip_alocado = rede.ifconfig()

# 
print(ip_alocado[0])
ip = ip_alocado[0]
oled.text('Endereco IP', 0, 0,3)
oled.text(str(ip), 0, 10)
oled.text('Hello, World 2!', 0, 20)      
oled.show()


from machine import SoftSPI, Pin
from micropython import const
from max7219 import Matrix8x8

max_clk = const(26) #18) #26)
max_cs = const(25)  #05)  #25)
max_din = const(33)  #23) #33)

spi = SoftSPI(sck=max_clk, mosi=max_din, miso=14)

display = Matrix8x8(spi, Pin(max_cs), 8)
display.scroll('TECTI')

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
print("wait for connections...")
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  nome = request.find('/?nome=')
  http = request.find('HTTP/')
  texto = request[nome:http]
  texto = texto[texto.find('=')+1:] 
  print(request[nome:http])
  print(texto)
  display.scroll(texto)

  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()



