import yaml

from .namespace import R
from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import  XSD 



class GraphWrapper:

    def __init__(self,graph : Graph):
        self.graph = graph

    def add_instance(self,type : str,id : str) -> URIRef:
        rdf_ref  = URIRef(R.URL+"#"+id)
        self.graph.add((rdf_ref, RDF.type, URIRef(R.URL+"#"+type)))
        return rdf_ref
    
    def add_reference(self,type : str,source : URIRef,target_id) -> None:
        self.graph.add((source, URIRef(R.URL+"#"+type), URIRef(R.URL+"#"+target_id)))

    def add_str_property(self,type : str,source : URIRef,value : str) -> None:
        self.graph.add((source, URIRef(R.URL+"#"+type), Literal(value, datatype=XSD.string)))



def create_rdf_from_yaml(graph,filename):
    with open(filename, "r", encoding='UTF-8') as stream:
        try:
            relations =  yaml.safe_load(stream)
            
            wrapper = GraphWrapper(graph)
            # Step one , create MessageId, Service, Interface  Ids
            #TODO Validate
            for id in relations:
                t = id.split('/', 1)[0]
                obj = relations[id]
                rdf = wrapper.add_instance(t,id)
                for property_name in obj:
                    property = obj[property_name]
                    l = property # List
                    if isinstance(property, str):
                        l = [property]
                   
                    for value in l:
                        if property_name.startswith('$'):
                            wrapper.add_reference(property_name[1:],rdf,value)
                        else:
                            wrapper.add_str_property(property_name,rdf,value)

        except yaml.YAMLError as exc:
            print(exc)

def append_yaml(data,filename):
    with open(filename, 'a') as f:
        f.write("\n")
        yaml.dump(data, f)
        f.write("\n")
