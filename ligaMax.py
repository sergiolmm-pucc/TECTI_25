'''
    Projeto para aula de Wokwi
    Ligando o display max7219  ( 8 modulos)
'''
from machine import SoftSPI, Pin
from micropython import const
from max7219 import Matrix8x8

max_clk = const(26)
max_cs = const(25)
max_din = const(33)

spi = SoftSPI(sck=max_clk, mosi=max_din, miso=14)

display = Matrix8x8(spi, Pin(max_cs), 8)
display.scroll('TECTI')



