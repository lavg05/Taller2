
import simpy 
import string
import random 


def  aleatorio ():
        myrg = random.SystemRandom()
        length = 6
        letters_and_digits = string.ascii_letters + string.digits 
        aleatorios = str().join((myrg.choice(letters_and_digits) for _ in range(length)))
        print(aleatorios)
        return aleatorios
        
   
def circulacion(env):
      
    while i <=1000000 is True:
        aleatorios = aleatorio()   
        for i in range (len(aleatorios)):
            if aleatorios[5] == "0" or aleatorios[5] == "3" or aleatorios[5] == "6" or aleatorios[5] == "9":
                print("NumerosDedicados{0}".format(str(env.now)))
                d_numeros = 0
                print("Puede salis los domingo")
                yield env.timeout(d_numeros)

            elif aleatorios[5] == "2" or aleatorios[5] == "4" or aleatorios[5] == "8":
                print("Numeros impares{0}".format(str(env.now)))
                d_impares = 1
                print("Puede salir los martes, jueves y sabados")
                yield env.timeout(d_impares)
       
            elif aleatorios[5] == "1" or aleatorios[5] == "5" or aleatorios[5] == "7" or aleatorios[5] == "9":
                print("Numeros pares {0}".format(str(env.now)))
                d_pares = 2
                print("Puede conducir los Lunes, miercoles y viernes")
                yield env.timeout(d_pares)
            
        else:
            print("No puedes salir")

        print(aleatorios)          
aleatorio() 
                                     
if __name__== '__main__':
    env = simpy.Environment()
    env.process(circulacion(env))
    env.run(until=1000000)

 