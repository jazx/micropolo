# Complete project details at https://RandomNerdTutorials.com

import cortex
import wernicke
import motor_cortex
from server_config import *

from machine import Pin

pinD1 = Pin(5, Pin.OUT)
pinD2 = Pin(4, Pin.OUT)
pinD3 = Pin(0, Pin.OUT)
pinD4 = Pin(2, Pin.OUT)
pinD5 = Pin(14, Pin.OUT)
pinD6 = Pin(12, Pin.OUT)
pinD7 = Pin(13, Pin.OUT)
pinD8 = Pin(15, Pin.OUT)

def goactions(pin,estado):
    if estado == 'a':
        pin.value(0)
    if estado == 'p':
        pin.value(1)
    if estado == 't':
        status = pin.value()
        if status == 0:
            pin.value(1)
        else:
            pin.value(0)
    



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip_srv, port_srv))
s.listen(5)

puerto=str(port_srv)

print('Micropolo Iniciado en puerto '+puerto)

while True:
  conn, addr = s.accept()
  #print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('........................................')
  #print('Content = %s' % request)
  txtin = cortex.limpiar(request)
  print('Recived: '+txtin)
  
  inpassword = cortex.getpasswd(txtin)
  inuser = cortex.getuser(txtin)
  incom = cortex.getcom(txtin)
  
  #comprueba el password
  if (inpassword == password):
      #print('el password es correcto')
      respuestaalcliente = '...'
      procesamiento=motor_cortex.actuar(incom)
      #define provisoriamente el output como la salida de spinal_reflex
      
      #si spinal_reflex no generó acción se continua con el procesamiento desde wernicke
      if(procesamiento[0] != 'stop'):
          print('Wernicke Area ACTIVE')
          incom = wernicke.procesar(incom)
          procesamiento=motor_cortex.actuar(incom)
          
      respuestaalcliente = procesamiento[2]
      accionarealizar = procesamiento[1]
      
      #ejecutar acciones      
      goactions(pinD1,accionarealizar[0])
      goactions(pinD2,accionarealizar[1])
      goactions(pinD3,accionarealizar[2])
      goactions(pinD4,accionarealizar[3])
      goactions(pinD5,accionarealizar[4])
      goactions(pinD6,accionarealizar[5])
      goactions(pinD7,accionarealizar[6])
      goactions(pinD8,accionarealizar[7])
          
  else:
      respuestaalcliente = 'Conexion rechazada. Password incorrecto.'
      print(respuestaalcliente)
      print('')
      
      

  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(respuestaalcliente)
  conn.close()
