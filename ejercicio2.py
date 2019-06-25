#historia de usuario
#la historia de usuario es como un pequeño resumen de una actividad que se quiere realizar 
#historia: demora al comprar un producto en una tienda
#como: implementar una página web, para poder comprar en línea
#quiero_lograr: un fácil acceso a las personas, para poder comprar

n = input("ingrese su nombre: ")

def menu():
    print("=-="*30)
    print ("Seleccione una opción: ")
    print ("\t1 - usted eligio comprar una blusa  ")
    print ("\t2 - usted eligio comprar una pantalon ")
    print ("\t3 - usted eligio comprar una zapatos ")
    print ("\t4 - salir ")

while True:
    menu()
    menu_opciones = input("Ingrese un número: ")
    if menu_opciones == "1":
        print("")
        print("usted eligio comprar una blusa")
        
    elif menu_opciones == "2":
        print("")
        print("usted eligio comprar una pantalon")
    
    elif menu_opciones == "3":
        print("")
        print("usted eligio comprar una zapatos")

    elif menu_opciones == "4":
        print("")
        print("Haz pulsado la opción salir ")
        
