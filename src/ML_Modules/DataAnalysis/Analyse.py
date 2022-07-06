""" Enthält Funktionen zur Analyse und Betrachtung von Datensätzen, 
im besondere von Featurevektoren, Labelvektoren und Weightvektoren 
@author Mascha Schmidt
"""

import numpy as np
def describe_feature_v(feature_v:np.ndarray, show=True):
    """ Gibt informationen zu einem Featurevektor aus 
    - Anzahl Datenpunkte, Anzahl Features
    Parameter:
        - show: Print description , default = true
    Returns:
        Anzahl Datenpunkte, Anzahl Features
    """
    data_point_num = feature_v.shape[0]
    feature_num    = feature_v.shape[1]
    if (show):
        print(f"Anzahl Datenpunkte/Messungen :{data_point_num}")
        print(f"Anzahl Features: {feature_num}")
    
    return data_point_num, feature_num

def describe_label(label_v:np.ndarray, show=True):
    """ Gibt die Beschreibung des Labelvektors aus 
    - Anzahl der Datenpunkt
    - Arten der Labels
    Param
        show : print, default = True
    Return:
       data_point_num, list of unique lables
    """
    vec            = np.array(label_v)
    data_point_num = label_v.shape[0]
    unique         = set(vec)

    if (show):
        print(f"Anzahl Datenpunkte {data_point_num}\nLabels:\n{unique}")

    return data_point_num, unique

def get_feature(feature_v:np.ndarray, feature_num:int, show=False):
    """ Gibt den Vektor mit allen Messwerten zu einem Feature zurück
    Param:
        show : Print , defaul False
    Return:
        feature vektor des gewählten Features
    """
    feature = feature_v[:,feature_num]
    if (show):
        print(f"Feature [{feature_num}],\n {feature}")
    return feature

def get_datapoint(feature_v:np.ndarray, data_num:int, show=False):
    """ Gibt den Vektor den Werten aller Features eines Datenpunktes zurück 
    Param:
        show : Print , defaul False
    Return:
        point:
    """
    point = feature_v[data_num,:] 
    if (show):
        print(f"Punkt [{data_num}],\n {point}")  
    return point