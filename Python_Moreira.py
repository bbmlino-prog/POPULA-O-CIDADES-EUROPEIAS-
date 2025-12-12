# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 11:09:05 2025

@author: USER
"""

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np


with st.sidebar:
    ESCOLHA = option_menu(
        "NAVEGAÇÃO", ["Iniciar", "Editar", "Guardar", "Enviar"],
        menu_icon="cast",
        icons=["house", "bar-chart","search", "graph-up-arrow"],
        default_index=0
        )



if ESCOLHA == "Iniciar":
    st.title("iniciando")
    df = pd.DataFrame({"X": [1, 2], "Y": [2, 3]})
    st.write(df.describe()) 
    
if ESCOLHA == "Editar":
    st.title("Editando")
    x = np.linspace(-5, 2, 100)
    y1 = x**3 + 5*x**2 + 10
    y2 = 3*x**2 + 10*x
    y3 = 6*x + 10
    fig, ax = plt.subplots()
    ax.plot(x, y1, color="blue", label="y(x)")
    ax.plot(x, y2, color="red", label="y'(x)")
    ax.plot(x, y3, color="green", label="y''(x)")
    ax.set_xlabel("tempo")
    ax.set_ylabel("espaço")
    ax.legend()
    st.pyplot(fig)
    
 ##População de algumas Cidades da Europa   
if ESCOLHA=="Guardar":
    st.title("Guardando")
    s=pd.Series([909976, 8615246, 2872086, 2273305], name="População", index=["Estocolmo", "Londres", "Roma", "Paris"])
    s
    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    s.plot(ax=axes[0], kind='line', title='linha')
    s.plot(ax=axes[1], kind='bar', title='barra')
    s.plot(ax=axes[2], kind='box', title='box')
    s.plot(ax=axes[3], kind='pie', title='circular')
    st.pyplot(fig)
   
if ESCOLHA == "Enviar":
    st.title("Enviando")


    
    



    


