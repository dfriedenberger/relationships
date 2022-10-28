from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from src.rdf_util import create_rdf_from_yaml
from src.model import get_model
from rdflib import Graph

import uvicorn


app = FastAPI()


@app.get("/api/model")
def projects():
    # Todo convert to design in frontend
    graph = Graph()
    create_rdf_from_yaml(graph,"data/relations.yaml")
    return get_model(graph)
    
  
               
    
@app.get("/health")
def health():
    return {"Status": "UP"}

app.mount("/", StaticFiles(directory="htdocs",html = True))


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9999)
