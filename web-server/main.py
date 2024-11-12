import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Profesor(BaseModel):
    nombre : str
    edad: int
    email: str
    direccion : Optional[str]

@app.get('/')
def get_list():
    return [1,2,3,4,5]

@app.get('/profe/{item_id}')
def mostrar_profe(item_id : int):
    return {'profe' : item_id}

@app.post('/profes')
def insertar_profe(profe : Profesor):
    return {'message': f'El profesor {profe.nombre} ha sido añadido a la base de datos'}



#@app.get('/contact', response_class=HTMLResponse)
#def get_list():
#    return """
#        <h1> Hola soy Sebastian Pérez </h1>
#        <p>Soy un programador</p>
#    """



#def run():
#    store.get_categories()

#if __name__ == '__main__':
#    run()