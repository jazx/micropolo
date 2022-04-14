# micropolo

Version del server Markopolo adaptada a micropython.

### INSTALACION

Instrucciones para instalarlo en NODEMCU/WEMOS/etc. Funciona sin problemas en los chip esp8266. No se ha probado en chips esp32, pero deberia correr sin inconvenientes.

1. En el directorio 'mycropython' se incluye la version del firmware que fue utilizada en este proyecto.
2. Instalar esptool desde pip3 (de otro modo la funcion erase_flash no se completa y luego falla la inicializacion del modulo).
3. Instalar con los comandos (reemplazar puerto por el correspondiente):

        ~ esptool.py --port /dev/ttyUSB0 erase_flash
        ~ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin

4. Ingresar con picocom

		    ~ picocom /dev/ttyUSB0 -b115200

5. Una vez dentro presionar una vez enter para lograr el *>>>* de la consola. Mediante 'import os' se puede acceder a la lectura de directorios y archivos.

6. Active la recepcion de archivos. Deberá configurar un password y definir (e)nable. El **PASWORD_DE_WEBRPL** que defina debera utilizarlo mas tarde. Recuerdelo. La configuracino se realiza con la siguiente orden.

        >>> import webrepl_setup

7. Configurar red wifi con:

        >>> import network
        >>> sta_if = network.WLAN(network.STA_IF)
        >>> sta_if.active(True)
        >>> sta_if.ifconfig(('192.168.1.44', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
        >>> sta_if.connect('NOMBRE_DE_LA_RED', 'CONTRASEÑA')
        >>> sta_if.isconnected()

8. Sin cerrar esa terminal, abra otra. Para subir los archivos dirijase al directorio 'micropolo' y edite el archivo 'server_config.py'. Allí se incluyen los datos de la red, el puerto e IP donde correra el servidor, y el password del servidor. Este es el contenido del archivo:

        #micropolo server config
        port_srv = 9070
        password = 'barcelona'
        
        #network configuration
        essid = 'NOMBRE_DE_LA_RED'
        netpw = 'CONTRASEÑA'
        ip_srv = '192.168.1.44'
        ip_gw = '192.168.1.1'
        ip_mask = '255.255.255.0'
        ip_dns = '8.8.8.8'

9. Desde el mismo directorio utilice el **bucle for** que se indica a continuacion para realizar un upload de todos los archivos (debe utilizar el password que creo en la configuracion de webrpl:

        ~ cd micropolo
        ~ for file in * ; do A=$file ; python3 ../micropython/webrepl/webrepl_cli.py -p PASWORD_DE_WEBRPL $file 192.168.1.44:$file  ; done
        
10. Reinicie el dispositivo. El servidor iniciara con la configuracion definida previamente.
