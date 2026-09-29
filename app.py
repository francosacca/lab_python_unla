from fastapi import FastAPI, status, HTTPException
from database import db_session, Products
from schema import ProductCreate,ProductResponse

app = FastAPI()

@app.get("/products",status_code=status.HTTP_200_OK)
async def getProducts():
    try:
        products = Products.query.all()
        response = {"products": products}
        return response
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred while trying to retrieve products: {e}")

@app.get("/products/{product_id}",status_code=status.HTTP_200_OK)
async def getProductId(product_id: int):
    try:
        product = Products.query.get(product_id)

        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        response = {"product:": product}
        return response

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred while trying to get product with id {product_id}: {e}")    



@app.post("/products",status_code=status.HTTP_201_CREATED,response_model=ProductResponse)
async def newProduct(product_data: ProductCreate):
    try:
        product = Products.query.filter_by(name=product_data.name).first()

        if product:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product already exists")
        
        product = Products(
            name=product_data.name,
            price=product_data.price
        )

        db_session.add(product)
        db_session.commit()
        db_session.refresh(product)
        
        return product
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred while trying to create product: {e}")

@app.put("/products{product_id}",status_code=status.HTTP_200_OK,response_model=ProductResponse)
async def productMod(product_id: int, product_data: ProductCreate):
    try:
        product = Products.query.get(product_id)
        
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        product.name = product_data.name
        product.price = product_data.price

        db_session.commit()
        db_session.refresh(product)

        return product

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred while trying to create product: {e}")

