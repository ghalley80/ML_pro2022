from django.shortcuts import render
import pandas as pd
from joblib import load
import numpy as np

model=load('./savedModel/model.joblib')

def index(request):
    if request.method=="POST":
        date=float(request.POST['date'])
        month=float(request.POST['month'])
        year=float(request.POST['year'])
        
        inputs=pd.DataFrame(data=({"day":[date],"month":[month],"year":[year]}),index=[0])
        
        y_pred=model.predict(inputs)
        final="USD Rate: " + str(np.round(y_pred[0],3))
        
        return (render(request,"index.html",{"result":final}))
    return render(request,"index.html")
