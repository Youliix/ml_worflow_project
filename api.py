from typing import Union
from fastapi import FastAPI
import pandas as pd
import pickle
import numpy as np

app = FastAPI()

@app.get("/")
# async def root(petal_width: Union[float, None] = 0, petal_length: Union[float, None] = 0, sepal_width: Union[float, None] = 0): 
async def root(brand: Union[str,None] = '', year: Union[int, None] = 0, fuel_type: Union[str, None] = '' ,door: Union[int, None] = 0, gear: Union[str, None] = '', km: Union[float, None] = 0): 
   
  user_data = pd.DataFrame({"brand" : [str(brand)], "year": [int(year)], "fuel_type": [str(fuel_type)], "door": [int(door)], "gear": [str(gear)], "km": [float(km)]})  
  pickle_model = pickle.load(open('car_estimation_pipeline_v1.pkl', 'rb'))  
  pickle_predict = pickle_model.predict(user_data)
  
  return {'predict': f"{pickle_predict[0]}"}