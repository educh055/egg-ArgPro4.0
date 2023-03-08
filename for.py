#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 20:25:04 2022

@author: edu
"""

#for, para 
lista = ['a','b','c']
for letra in lista:
    print('esta es la letra:'+letra)
#for, con identacion 
for l in lista:
    num_l= lista.index(l)+1
    print(f'letra {num_l}')
#for, nombres
nombres = ['pablo', 'edu', 'avers', 'soe']
for nom in nombres:
    if nom.startswith('e'):
        print(nombres)

#for, mas if y else
for nom2 in nombres:
    if nom2.startswith('e'):
        print(nombres)
    else: 
        print('nombre nombre que o comienza con e')

numeros2=[1,2,3,4,5,6]
mi_valor=0
for num2 in numeros2:
    mi_valor = mi_valor + num2
    print(mi_valor)
print(mi_valor)
    
#palabra= 'python'
for a,b,c in [[1,2,3],['a','b','c']]:
#    print(l1)
    print(a)
    print(b)
dic={'clave1':'a','clave2':'b','clave3':'c'}    
for a,b in dic.values():
#    print(item)
    print(a)
    print(b)