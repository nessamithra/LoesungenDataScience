""" Enthält Funktionen zur Visualisierung von Datensets 
@author Mascha Schmidt
"""
import numpy as np
import matplotlib.pyplot as plt

from src.ML_Modules.DataAnalysis.Analyse import *


def plot_2dim_set(feature_v:np.ndarray,label_v:np.ndarray= [],ax=None,label:str="",label_names=[],title=""):
    """ Plots a 2d Feature Vektor with the colors of the labels if given
    Return:
        axis, scatter plot handle
    """

    # Konfiguriere den Plot
    newPlot = (ax == None)
    if newPlot:
        fig, ax = plt.subplots(1)


    # Plotte mit oder ohne Farben
    if len(label_v) <= 0:
        sc_plot = __plot_2dim_noColor(feature_v, ax,          label)
    else:
        sc_plot = __plot_2dim_Color  (feature_v, ax, label_v, label)

    if newPlot:
        ax.set(title=f"Visualisierung des Datensatzes {title}",xlabel="Feature 1",ylabel="Feature 2")
        if(len(label_names)!=0):
            fig.legend(handles=sc_plot.legend_elements()[0],labels=label_names)
        else:
            ax.legend()

    return ax, sc_plot


def __plot_2dim_noColor(feature_v:np.ndarray, ax, label:str):
    if label == "":
        label = "Datenpunkte"
    plot = ax.scatter(get_feature(feature_v,0),get_feature(feature_v,1),label=label)
    return plot
    
def __plot_2dim_Color(feature_v:np.ndarray,ax,label_v:np.ndarray,label:str):

    # Kontrolliere, ob die Dimensionen ein Plotten erlauben
    feature_points = feature_v.shape[0]
    label_points   = label_v.shape[0]
    


    plot = ax.scatter(get_feature(feature_v,0),get_feature(feature_v,1),c=label_v,label=label)
    return plot

