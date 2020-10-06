import simpy
import math


def simulacionpedido(env):
    while True:
        print("Basico{0}".format(str(env.now)))
        d_basico = 10
        yield env.timeout(d_basico)

        print("Medio{0}".format(str(env.now)))
        d_medio = 25
        yield env.timeout(d_medio)

        print("Premium{0}".format(str(env.now)))
        d_premiun = 55
        yield env.timeout(d_premiun)

if __name__== '__main__':
    env = simpy.Environment()
    env.process(simulacionpedido(env))
    env.run(until=38)



