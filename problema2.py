import simpy
import math



def usuarios(env):
    while True:
        print("Primera fase {0} usuarios".format(str(env.now)))
        d_primera = 3
        yield env.timeout(d_primera)

        print("Segunda fase {0} usuarios".format(str(env.now)))
        d_segunda = 8
        yield env.timeout(d_segunda)

        print("Tercera fase {0} usuarios".format(str(env.now)))
        d_tercera = 14
        yield env.timeout(d_tercera)

if __name__== '__main__':
    env = simpy.Environment()
    env.process(usuarios(env))
    env.run(until=900) #Transformacion de minutos a segundos 900

