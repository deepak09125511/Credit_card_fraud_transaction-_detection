from django.shortcuts import render
import numpy as np
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

model_data = joblib.load('predictor/fraud_model.pkl')
w = model_data['weights']
b = model_data['bias']

def home_view(request):
    return render(request, 'predictor/home.html')

def sigmoid(z):
    return 1/(1+np.exp(-z))

def predict_new(x,w,b):
    z = np.dot(x,w)+b
    return sigmoid(z)>=0.9

@csrf_exempt
def predict_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            features = data.get('features', [])
            
            if len(features) != 31:
                return JsonResponse({'error': 'Expected 31 features for prediction.'})
            
            x = np.array(features)
            prediction = predict_new(x, w, b)
            return JsonResponse({'prediction': int(prediction)})
        
        except Exception as e:
            return JsonResponse({'error': str(e)})
    
    return JsonResponse({'message': 'Send a POST request with 31 features.'})



