def adivinar(intentos):
    contador = 0
    import random
    numero = random.randint(0, 100)
    print(numero)
    while intentos > contador:
        contador += 1
        print('Intento', contador, 'de', intentos, '. Elige un número entre 0 y 100: ')
        valor = int(input())
        if valor == numero:
            return 'Acertó'
            #return ('Acertó en el intento', contador)
    else:
        return 'Se agotaron los intentos'
        #return 'Se agotaron los intentos. El valor correcto era: ', numero

intentos = int(input('Seleccione la cantidad de intentos: '))
print(adivinar(intentos))