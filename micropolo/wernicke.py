import dicc

def procesar(incom):
    #ponemos todo en minusculas
    incom = incom.lower()
    #analiza sintaxis y crea tags    
    tags = dicc.tagcreator(incom)
    #print("Recived: %s" % ingreso)
    #print("User: %s" % user)
    print("Tags: %s" % tags)
    return tags
