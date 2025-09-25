


def ajouter_noeud(graph,noeud):

    if(graph.get(noeud) == None):
        graph[noeud] = []
        return
    else:
        return



def ajouter_arete(graph,noeud,arete):

    if(graph.get(noeud) == None):
        raise ValueError("Noeud manquant")
    
    else:
        graph[noeud].append(arete)
        
        


    
    