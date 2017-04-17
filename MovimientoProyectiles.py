#Autores: Mathias Muller, Paula Segura, Mauricio Araica
#Fisica 1
#16 de abdril del 2017
#Asignacion pracitca 4 - Movimiento Proyectiles

# -*- coding: utf-8 -*-
from visual import *
from math import *
import cmath
from fractions import Fraction
import sys

#Velocidad inicial
velocidad_inicial = 9
#Angulo de disparo
angulo_de_disparo = 45

#Se renderiza la ventana
ventana = display(title='Movimiento Proyectiles.',
      width=1024, height=768,
     center=(5,0,0), background=(color.black),autocenter=true)

#Variables Globales
gravedad = 9.8
dt = 0.005
altura_inicial = 0
tiempo_total_vuelo = (2 * velocidad_inicial * math.sin(math.radians(angulo_de_disparo))) / gravedad
distancia_proyectil = velocidad_inicial * math.cos(math.radians(angulo_de_disparo)) * tiempo_total_vuelo

#Entrypoint de la aplicacion
def iniciar_programa():
    iniciar_mundo()
#Inicia la parte grafica de la aplicacion
def iniciar_mundo():

    star1 = sphere(pos=(7,2.5,1), radius=0.01)
    star1.color=(color.yellow)

    star2 = sphere(pos=(7.3,2.9,1), radius=0.01)
    star2.color=(color.yellow)

    star3 = sphere(pos=(8,2,1), radius=0.01)
    star3.color=(color.yellow)

    star4 = sphere(pos=(4,2.5,1), radius=0.01)
    star4.color=(color.yellow)

    star5 = sphere(pos=(4.3,2.9,1), radius=0.01)
    star5.color=(color.yellow)

    star6 = sphere(pos=(5,2,1), radius=0.01)
    star6.color=(color.yellow)

    star10 = sphere(pos=(2,2.5,1), radius=0.01)
    star10.color=(color.yellow)

    star11 = sphere(pos=(2.3,2.9,1), radius=0.01)
    star11.color=(color.yellow)

    star12 = sphere(pos=(3,2,1), radius=0.01)
    star12.color=(color.yellow)

    star7 = sphere(pos=(1,2.5,1), radius=0.01)
    star7.color=(color.yellow)

    star8 = sphere(pos=(1.3,2.9,1), radius=0.01)
    star8.color=(color.yellow)

    star9 = sphere(pos=(2,2,1), radius=0.01)
    star9.color=(color.yellow)

    #Creacion de arbol
    arbol = cylinder(pos=(3,0.1,3), axis=(0,1,0),make_trail = true, radius=0.1, material=materials.wood)
    hojas_arbol = sphere(pos=(3,1,3),make_trail = true, axis=(0.5,0.5,3), radius=0.4)
    hojas_arbol.color=(0,1,0)

    #Creacion de arbol 2
    arbol2 = cylinder(pos=(6,0.1,3), axis=(0,1,0), radius=0.1,  material=materials.wood)
    hojas_arbol2 = sphere(pos=(6,1,3), axis=(0.5,0.5,3), radius=0.4)
    hojas_arbol2.color=(0,1,0)

    #Creacion de la esfera luna
    luna = sphere(pos=(8,2.5,1), axis=(0.5,0.5,3), radius=0.3)
    luna.color=(1,1,1)

    #Creacion de la esfera luna negra
    menguante = sphere(pos=(8.1,2.5,1), axis=(0.5,0.5,3), radius=0.3)
    menguante.color=(0,0,0)

    #Etiqueta de la velocidad inicial
    etiquetaVelocidadInicial = label(pos=(0.4, 2.3 , 0), text='Velocidad inicial: ' + str(velocidad_inicial)  + ' m/s', color=color.white, border= 10, radius=8)

    #Etiqueta del angulo inicial
    etiquetaAnguloInicial = label(pos=(0.2, 1.5 , 0), text='Angulo inicial: ' + str(angulo_de_disparo)+u'\u00b0', color=color.white, border= 10, radius=8)

    #Base del cannon
    base = box(pos=(0.4,-0.1,0.5), height=0.1, width=0.8, material=materials.wood)
    base.color=(1,0.9,0.3)

    #Cannon del cilindro
    cannon = cylinder(pos=(0,altura_inicial,0), radius=0.1)

    #Bola del cannon
    bola_cannon = sphere(pos=(0,altura_inicial,0),radius=0.1,
    make_trail = true, material=materials.chrome, opacity=0.5)

    #Calculo de tiempo en el eje Y
    tiempoY = (velocidad_inicial * math.sin(math.radians(angulo_de_disparo))) / gravedad

    #Calculo de la posicion maxima Y
    posicionY = (velocidad_inicial * math.sin(math.radians(angulo_de_disparo))) * tiempoY - 0.5 * gravedad * math.pow(tiempoY, 2)

    #Calculo de la posicion maxima X para el eje Y
    posicionX = velocidad_inicial * math.cos(math.radians(angulo_de_disparo)) * tiempoY

    #Calculo del alcance de la pelota
    rango =  velocidad_inicial * math.cos(math.radians(angulo_de_disparo)) * tiempo_total_vuelo

    #Etiqueta de la altura maxima
    etiquetaAltura = label(pos=(posicionX, posicionY + 1 , 0), text='Altura maxima: ' + str('%.2f' % posicionX) + ' m', color=color.white, border= 10, radius=10)
    #Flecha de la altura maxima
    flechaAltura = arrow(pos=(posicionX,posicionY + 0.5, 0), axis=(0,-2,0), length=0.5, shaftwidth=0.2, color=color.yellow)

    #Etiqueta del rango de la pelota
    etiquetaRango = label(pos=(rango, -1 , 0), text='Alcance: ' + str('%.2f' % rango) + ' m', color=color.white, border= 10, radius=10)
    #Flecha del rango de la pelota
    flechaRango =  arrow(pos=(rango,-0.6, 0), axis=(0,2,0), length=0.5, shaftwidth=0.2, color=color.yellow)

    #Caja 1
    caja = box(pos=(distancia_proyectil,altura_inicial,0), length=0.3, height=0.3, width=0.1, material=materials.wood)
    #Caja 2
    caja2 = box(pos=(distancia_proyectil + 0.1,altura_inicial + 0.3,0), length=0.3, height=0.3, width=0.1, material=materials.marble)
    #Caja 3
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

#Logica y movimiento

    t=0
    bola_en_aire = True
    flag = False
    #Ciclo del vuelo de la pelota
    while t <= tiempo_total_vuelo:
        rate(100)
        #Animacion de la pelota
        bola_cannon.pos = (velocidad_inicial*cos(math.radians(angulo_de_disparo))*t,
                            altura_inicial + velocidad_inicial*t*sin(math.radians(angulo_de_disparo)) -0.5 * gravedad *t**2)
        #El proyectil llega al suelo
        if bola_cannon.y < -2:
            print "bola_cannon.pos = ",bola_cannon.pos,"t = ",t
            bola_en_aire = False
            flag = True
        t += dt

    tiempo = 0
    #Ciclo para la animacion de las cajas
    while tiempo < 0.6:
        rate(400)
        caja.pos = (distancia_proyectil + tiempo + 1.6, + altura_inicial + t - 0.4 * gravedad*tiempo**2 , -3)
        caja2.pos = (distancia_proyectil + tiempo + 0.2, +  altura_inicial + t - 0.3 * gravedad*tiempo**2, 1)
        caja3.pos = (distancia_proyectil + tiempo + 0.3, + altura_inicial + t - 0.4 * gravedad*tiempo**2, 2)
        tiempo += 0.001

#Validacion del angulo
if angulo_de_disparo > 180 or angulo_de_disparo <= 0 :
	errorAngulo = label(pos=(8, -4 , 0), text='El angulo tiene que ser mayor a 0 y menor a 180', color=color.white, border= 10, radius=8)
else:
    iniciar_programa()
