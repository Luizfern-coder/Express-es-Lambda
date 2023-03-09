# -*- coding: utf-8 -*-
"""Expressoes Lambda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FGPb_9ClXfaKiCKBmgv1Z9JyX2QfYKb0

## Expressões Lambda - Simplificado

- Funções Anonimas = nome ruim para uma função que não precisa definir e depois usar, você define já usando direto.
"""

preco = 100

def calcular_imposto(preco):
    return preco * 0.5

print(calcular_imposto(preco))



calcular_imposto2 = lambda x: x *0.3

print(calcular_imposto2(preco))

precos = [100, 200, 10, 25, 90, 50, 40]

impostos = list(map(lambda x: x*0.3, precos))

print(impostos)