from fastapi import FastAPI
from database import Session, Productos 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/productos")
def obtener_productos():
    
    sesion = Session()
    
    
    productos_db = sesion.query(Productos).all()
    
    
    sesion.close()
    
  
    lista_resultado = []
    for producto in productos_db:
        lista_resultado.append({
            "id": producto.id,
            "nombre": producto.nombre,
            "precio": producto.precio
        })
        
   
    return lista_resultado