from .sparql_queries import SparQLWrapper
from .namespace import R
from rdflib import URIRef

def get_model(graph):
    
    model = {
        "nodes" : [],
        "edges" : []
    }

    wrapper = SparQLWrapper(graph)

    for instance in wrapper.get_instances():
        k = instance.split('#')[-1]
        t = wrapper.get_type(instance).split('#')[-1]
        n = wrapper.get_single_object_property(instance,"https://frittenburger.de/2022/05/Relations#name")
        model["nodes"].append( { "key": k , "type": t , "name" : n })
    for from_ref, to_ref in wrapper.get_references():
        model["edges"].append( { "from": from_ref.split('#')[-1] , "to": to_ref.split('#')[-1]} )


    return model

def get_nodes(graph,type):

    nodes = []

    wrapper = SparQLWrapper(graph)
    for instance in wrapper.get_instances_of_type(URIRef(R.URL+"#"+type)):
        k = instance.split('#')[-1]
        n = wrapper.get_single_object_property(instance,URIRef(R.URL+"#name"))
        nodes.append({"key" : n , "value" : k})

    return nodes