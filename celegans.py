#! usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#read files

connect = pd.read_csv("~/Desktop/EDO/EDO_python/CElegansTP/data/Connectome.csv")
neuro = pd.read_csv("~/Desktop/EDO/EDO_python/CElegansTP/data/Neurons_to_Muscles.csv")
senso = pd.read_csv("~/Desktop/EDO/EDO_python/CElegansTP/data/Sensory.csv")

connect = connect.drop(connect.columns[[0]], axis=1)
neuro = neuro.drop(neuro.columns[[0]], axis=1)
senso = senso.drop(senso.columns[[0]], axis=1)


print connect
print neuro
print senso

ConnectomeDictionnary = {}
TypeDictionnary = {}

for name in connect.Neuron.unique():
  ConnectomeDictionnary[name] = {}

  if senso.loc[senso["Neuron"]==name].empty :
    typ = "Unknown"
  else :
    typ = str(((senso.loc[senso["Neuron"]==name].as_matrix())[0])[0]).split('|')


  print typ
  TypeDictionnary[name] = typ

  a = connect.loc[connect["Neuron"] == name]
  z = a.count()[0]
  
  for i in range(0,z):

    cons = a.iloc[[i]].as_matrix()[0]
    target = cons[1]

    ConnectomeDictionnary[name][target] = cons[2] if cons[3] is "exc" else -1.0*cons[2]

print ConnectomeDictionnary
print TypeDictionnary



