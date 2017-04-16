#Autores: Mathias Muller, Paula Segura, Mauricio Araica
#Fisica 1
#16 de abdril del 2017
#Asignacion pracitca 4 - Movimiento Proyectiles

from visual import *
from math import *
import cmath
from fractions import Fraction
import sys

#Variables pre definidas
#########################################
#Angulo de disparo
angulo_de_disparo = 65
#Velocidad inicial
velocidad_inicial = 9
#########################################

#Variables Globales
###############
gravedad = 9.8
dt = 0.01
altura_inicial = -2
tiempo_total_vuelo = (2 * velocidad_inicial * math.sin(math.radians(angulo_de_disparo))) / gravedad
distancia_proyectil = velocidad_inicial * math.cos(math.radians(angulo_de_disparo)) * tiempo_total_vuelo
###############

#Entrypoint de la aplicacion
def iniciar_programa():
    iniciar_mundo()
#Inicia la parte grafica de la aplicacion
def iniciar_mundo():

    ventana = display(title='Movimiento Proyectiles.',
     x=0, y=0, width=900, height=600,
     center=(5,0,0), background=(0,1,1))

    arbol = cylinder(pos=(2.3,0.1,3), axis=(0,1,0), radius=0.1, material=materials.wood)
    hojas_arbol = sphere(pos=(2.3,1,3), axis=(0.5,0.5,3), radius=0.4)
    hojas_arbol.color=(0,1,0)

    arbol2 = cylinder(pos=(3,0.1,3), axis=(0,1,0), radius=0.1,  material=materials.wood)
    hojas_arbol2 = sphere(pos=(3,1,3), axis=(0.5,0.5,3), radius=0.4)
    hojas_arbol2.color=(0,1,0)

    arbol3 = cylinder(pos=(5,-2,3), axis=(0,1,0), radius=0.1, material=materials.wood)
    hojas_arbol3 = sphere(pos=(5,-1,3), axis=(0.5,0.5,3), radius=0.4)
    hojas_arbol3.color=(0,1,0)

    sol = sphere(pos=(8,2.5,1), axis=(0.5,0.5,3), radius=0.3)
    sol.color=(1,1,0)

    base = box(pos=(0,altura_inicial,1), height=0.1, width=0.5, material=materials.wood)
    base.color=(1,0.9,0.3)

    cannon = cylinder(pos=(0,altura_inicial,1), radius=0.1)

    bola_cannon = sphere(pos=(0,altura_inicial,1),radius=0.1,
    make_trail = true, material=materials.chrome, opacity=0.5)

    caja = box(pos=(distancia_proyectil,altura_inicial,0), length=0.3, height=0.3, width=0.1, material=materials.wood)
    caja2 = box(pos=(distancia_proyectil + 0.1,altura_inicial + 0.3,0), length=0.3, height=0.3, width=0.1, material=materials.marble)
    caja3 = box(pos=(distancia_proyectil + 0.3,altura_inicial,0), length=0.3, height=0.3, width=0.1, material=materials.wood)

    #El sistema inicia en 'click' del sistema
    ventana.waitfor('click')
    temp_angulo = 0
    #Este While inicializa el cannon con el angulo de disparo apropiado
    while temp_angulo <= angulo_de_disparo:
    	cannon.axis[0] = cos(math.radians(temp_angulo))
    	cannon.axis[1] = sin(math.radians(temp_angulo))
    	temp_angulo += 0.1
    	rate(300)

############################
#Logica y movimiento
############################

    t=0
    bola_en_aire = True
    flag = False
    while bola_en_aire:
        rate(50)
        bola_cannon.pos = (velocidad_inicial*cos(math.radians(angulo_de_disparo))*t,
                            altura_inicial + velocidad_inicial*t*sin(math.radians(angulo_de_disparo)) -0.5 * gravedad *t**2)

        if bola_cannon.y < -2: #El proyectil llega al suelo
            print "bola_cannon.pos = ",bola_cannon.pos,"t = ",t
            bola_en_aire = False
            flag = True
        t += dt

    tiempo = 0
    while tiempo < 0.6:
        rate(400)
        caja.pos = (distancia_proyectil + tiempo + 1.6, + altura_inicial + t - 0.4 * gravedad*tiempo**2 , -3)
        caja2.pos = (distancia_proyectil + tiempo + 0.2, +  altura_inicial + t - 0.3 * gravedad*tiempo**2, 1)
        caja3.pos = (distancia_proyectil + tiempo + 0.3, + altura_inicial + t - 0.4 * gravedad*tiempo**2, 2)
        tiempo += 0.001
#inizializamos el script
iniciar_programa()
