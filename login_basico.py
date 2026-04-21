intentos = 3
while intentos > 0:
    usuario = input("introducir usuario: ").lower()
    clave = input("introducir contrasena: ")
    if usuario == "nose" and clave == "1234":
         print("acceso permitido")
         break
    elif usuario != "nose" and clave=="1234":
        intentos -=1
        print(f"usuario incorrecto, te quedan {intentos} intentos")
    elif usuario=="nose" and clave !="1234":
        intentos -=1
        print(f"contrasena incorrecta, te quedan {intentos} intentos")
    else:
        intentos -= 1
        print(f"usuario y contrasena incorrectos, te quedan {intentos} intentos")
    if intentos ==0:
        print("cuenta bloqueada")
