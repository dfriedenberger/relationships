from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from src.rdf_util import create_rdf_from_yaml, append_yaml
from src.model import get_model, get_nodes
from rdflib import Graph

#import uvicorn


app = FastAPI()


@app.get("/api/model")
def model():
    graph = Graph()
    create_rdf_from_yaml(graph,"data/relations.yaml")
    return get_model(graph)
    
@app.get("/api/nodes/{types}")
def nodes(types):

    graph = Graph()
    create_rdf_from_yaml(graph,"data/relations.yaml")

    nodes = []
    for type in types.split('+'):
        print(type)
        nodes.extend(get_nodes(graph,type))
    return nodes


@app.post("/api/create")
async def create(request: Request):
    json = await request.json()
    print(json)
    append_yaml(json,"data/relations.yaml")
    return "ok";


@app.get("/health")
def health():
    return {"Status": "UP"}

app.mount("/", StaticFiles(directory="htdocs",html = True))


#if __name__ == '__main__':
#    uvicorn.run(app, host="0.0.0.0", port=9999)
