#uvicorn main:app --reload

from fastapi import FastAPI,Depends
from database import SessionLocal,engine
import database_models
from sqlalchemy.orm import Session
from models import Product
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")

def greet():
    return "Welcome to Telusko Trac"

products=[
    Product(id=1,name="phone",description="18 Pro",price=4800,quantity=3),
    Product(id=2,name="laptop",description="18 Pro ultra",price=3800,quantity= 10),
    Product(id=3,name="android",description="15 Pro ultra",price=3800,quantity= 10),
    Product(id=4,name="tablet",description="18 Pro ultra",price=3800,quantity= 10),
    Product(id=6,name="watch table",description="16 Pro ultra",price=3800,quantity= 10)
    
]

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()    
        
def init_db():
    db = SessionLocal()
    existing_count = db.query(database_models.Product).count()
    if existing_count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

init_db()

@app.get("/products/")
def get_all_products(db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product
    return "product not found" 

@app.post("/products/")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "Product Updated"
    else:
     return "No Product Found"  

@app.delete("/products/{id}")
def delete_product(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:           
        return "No product found"    
      
    
