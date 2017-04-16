#Autor: Mathias Muller
#Fisica 1
#16 de abdril del 2017
#Asignacion pracitca 4- Disparo Canon

from visual import *
from math import *
import cmath
from fractions import Fraction
import sys

#Variables pre definidas
#########################################
#Angulo de disparo
angulo_de_disparo = 4
#Velocidad inicial
velocidad_inicial = 10
#########################################

#Variables Globales
###############
gravedad = -9.8
###############

#Entrypoint de la aplicacion
def iniciar_programa():
    iniciar_mundo()

#Inicia la parte grafica de la aplicacion
def iniciar_mundo():

    scene2 = display(title='Movimiento Proyectiles.',
     x=0, y=0, width=900, height=600,
     center=(5,0,0), background=(0,1,1))

    arbol = cylinder(pos=(2.3,0.1,3), axis=(0,1,0), radius=0.1)
    hojas_arbol = sphere(pos=(2.3,1,3), axis=(0.5,0.5,3), radius=0.4)
    hojas_arbol.color=(0,1,0)

    arbol2 = cylinder(pos=(3,0.1,3), axis=(0,1,0), radius=0.1)
    hojas_arbol2 = sphere(pos=(3,1,3), axis=(0.5,0.5,3), radius=0.4)
    hojas_arbol2.color=(0,1,0)

    arbol3 = cylinder(pos=(5,-2,3), axis=(0,1,0), radius=0.1)
    hojas_arbol3 = sphere(pos=(5,-1,3), axis=(0.5,0.5,3), radius=0.4)
    hojas_arbol3.color=(0,1,0)

    cannon = cylinder(pos=(1.1,-2,1), axis=(1,1,0), radius=0.1)

    sol = sphere(pos=(8,2.5,1), axis=(0.5,0.5,3), radius=0.3)
    sol.color=(1,1,0)

    base = box(pos=(1.3,-2,1), height=0.1, width=0.5)
    base.color=(1,0.9,0.3)
#inizializamos el script
iniciar_programa()
