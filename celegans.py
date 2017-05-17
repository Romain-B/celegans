#! usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint

#read files

connect = pd.read_csv("./CElegansTP/data/Connectome.csv", ) #commentaire
neuro = pd.read_csv("./CElegansTP/data/Neurons_to_Muscles.csv")
senso = pd.read_csv("./CElegansTP/data/Sensory.csv")

connect = connect.drop(connect.columns[[0]], axis=1)
neuro = neuro.drop(neuro.columns[[0]], axis=1)
senso = senso.drop(senso.columns[[0]], axis=1)


# print connect
# print neuro
# print senso

ConnectomeDictionnary = {}
TypeDictionnary = {}

names = connect.Neuron.unique()
sens = senso["Neuron"].tolist()
musc = neuro["Origin"].tolist()


for name in names:
  ConnectomeDictionnary[name] = {}
  typ = ""
  b = True
  print name
  if name in sens:
    typ += "sensor"
    b = False
  if name in musc:
    typ += "motor"
    b = False
  if b is True:
    typ += "interneuron"

  TypeDictionnary[name] = typ

  a = connect.loc[connect["Neuron"] == name]
  z = a.count()[0]
  
  for i in range(0,z):

    cons = a.iloc[[i]].as_matrix()[0]
    target = cons[1]

    ConnectomeDictionnary[name][target] = cons[2] if cons[3] == "exc" else -1.0*cons[2]

print ConnectomeDictionnary
print TypeDictionnary


ti = 0
tmax = 35
h = 0.1

xseq = np.arange(ti,tmax,h)

for elem in range(len(xseq)):
	I.append(randint(0,1))

def derivve(V,step):
	deriv = (urest - V + rm*I[step]) / (rm*cm)
	return deriv


