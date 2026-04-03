texto = "   Andres.Lopez99@GMAIL.com   "

limpio = texto.lower().strip() #Damos el codigo limpio en minusculas y sin espacios al principio y al final

verificacion_de_arroba = limpio.find("@") #Verificamos si el email contiene "@"

#Si el email contiene "@" entonces separamos por usuario y dominio
if verificacion_de_arroba > 0:
    separacion = limpio.split("@")
    print(separacion)
else:
    print("El email brindado no contiene (@)")
    
username = separacion[0] #Tomamos solo el usuario para trabajar

username = username.replace(".", "_") #remplazamos "." por "_"

print(username)

username = username.replace("_", "") #Eliminamos los espacios de por medio

print(username)

user = username.isalnum() #Verificamos si es alfanumerico

#verficamos si el dominio contiene "gmail"
dominio = separacion[1] 

dominio = dominio.find("gmail")

#Verificamos si ambas condiciones se cumplen
if user == True and dominio == True:
    print("Ambas condiciones se cumplen") 
else: 
    print("Una o ambas condiciones no se cumplen")

print(limpio.count("a")) #cuantas veces aparece "a" en el email limpio

print(limpio.find("@")) #posicion de "@" en el email limpio

#verificaciones de como empieza y termina el email
print(limpio.startswith("a"))

print(limpio.endswith("com"))