def actuar(incom):
    
    salida = ['go','--------','Tags detectadas, pero sin accion definida. Configure una accion para '+incom]

    #procesando reflejos
    f = open("actions.conf", "r")
        
    for linea in f:
        
        accion = linea.split('=')
        codigo = accion[0]
        
        if(incom == codigo):

            print('Motor Cortex ACTIVE')
            comando = accion[1]
            respuesta = accion[2]
            
            print('Recived: ',codigo)
            print('Exec:',comando)
            print('>>>:',respuesta)
            print('')
            
            salida = ['stop',comando,respuesta]
    
    f.close()
    
    return salida
