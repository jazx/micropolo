def first_corrections(ingreso):
    #vocales minusculas con tilde
    ingreso = ingreso.replace('%C3%A1','a')
    ingreso = ingreso.replace('%C3%A9','e')
    ingreso = ingreso.replace('%C3%AD','i')
    ingreso = ingreso.replace('%C3%B3','o')
    ingreso = ingreso.replace('%C3%BA','u')
    ingreso = ingreso.replace('á','a')
    ingreso = ingreso.replace('é','e')
    ingreso = ingreso.replace('í','i')
    ingreso = ingreso.replace('ó','o')
    ingreso = ingreso.replace('ú','u')
    ingreso = ingreso.replace('\\xc3\\xa1','a')
    ingreso = ingreso.replace('\\xc3\\xa9','e')
    ingreso = ingreso.replace('\\xc3\\xad','i')
    ingreso = ingreso.replace('\\xc3\\xb3','o')
    ingreso = ingreso.replace('\\xc3\\xba','u')
    #Eñes
    ingreso = ingreso.replace('%C3%91','N')
    ingreso = ingreso.replace('%C3%B1','n')
    ingreso = ingreso.replace('\\xc3\\xb1','n')
    ingreso = ingreso.replace('\\xc3\\x91','N')
    #vocales mayusculas con tilde
    ingreso = ingreso.replace('%C3%81','A')
    ingreso = ingreso.replace('%C3%89','E')
    ingreso = ingreso.replace('%C3%8D','I')
    ingreso = ingreso.replace('%C3%93','O')
    ingreso = ingreso.replace('%C3%9A','U')
    ingreso = ingreso.replace('\\xc3\\x81','A')
    ingreso = ingreso.replace('\\xc3\\x89','E')
    ingreso = ingreso.replace('\\xc3\\x8d','I')
    ingreso = ingreso.replace('\\xc3\\x93','O')
    ingreso = ingreso.replace('\\xc3\\x9a','U')
    #espacios
    ingreso = ingreso.replace('%20','+')
    ingreso = ingreso.replace(' ','+')
    #dieresis
    ingreso = ingreso.replace('\\xc3\\xbc','u')
    return ingreso





def limpiar(entrada):
    #aisla la cadena de entrada'
    import re
    separador = re.compile(' HTTP/1.1')
    recibido = separador.split(entrada)
    entrada = recibido[0]
    separador2 = re.compile('GET /')
    recibido = separador2.split(entrada)
    entrada = recibido[1]
    
    #quita acentos y otras
    entrada=first_corrections(entrada)
    
    #pone en minusculas
       
    return entrada





def getpasswd(entrada):
    #entrada = 'aqui esta el texto procesado'
    import re    
    inpassword = re.sub('.*PSW_', '', entrada)
    inpassword = re.sub('_PSW.*$', '', inpassword)
    return inpassword

def getuser(entrada):
    #entrada = 'aqui esta el texto procesado'
    import re    
    inpassword = re.sub('.*USR_', '', entrada)
    inpassword = re.sub('_USR.*$', '', inpassword)
    return inpassword


def getcom(entrada):
    #entrada = 'aqui esta el texto procesado'
    import re    
    inpassword = re.sub('.*COM_', '', entrada)
    inpassword = re.sub('_COM.*$', '', inpassword)
    return inpassword
