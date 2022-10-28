import argparse
from rdflib import Graph


from pathlib import Path
from src.rdf_util import create_rdf_from_yaml
from src.model import get_model

# main
parser = argparse.ArgumentParser(description='Create Network from rdf model.')
parser.add_argument('--relations',required=True,help="path to relations yaml")
args = parser.parse_args()

filename = args.relations
model_key = Path(filename).stem

print(model_key)

# Create Rdf-Model
graph = Graph()
create_rdf_from_yaml(graph,filename)
graph.serialize(destination=f"{model_key}.ttl",format='turtle')
model = get_model(graph)

print(model)
  
  

