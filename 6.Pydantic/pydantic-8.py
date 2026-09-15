import os 
from pydantic import BaseModel,Field

class Product(BaseModel):
    name:str=Field(description='Name of the product')
    category:str =Field(description='Category of the product')
    price:float=Field(description='Price of the product')
    in_stock:bool=Field(default=False,description='whether product is available')

p = Product(name='Apple iphone 18',category='Smart Phone',price=165000,in_stock=True)
print(type(p))
print(p)
print(type(p.model_dump()))  # dict
print(p.model_dump()) # to get dict object
print(type(p.model_dump_json()))# json
print(p.model_dump_json())#to get json object