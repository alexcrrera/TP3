import numpy as np
from matplotlib import pyplot as plt
from utils import display_graph_from_dict
from graph import*

graph = {"A" : ["B"], "B" : [], "C": ["A","B"],"D":["C"],"E":["C","D"]}

ajouter_noeud(graph,"X")

ajouter_arete(graph,"X","A")
display_graph_from_dict(graph)


