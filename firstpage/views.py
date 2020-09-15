from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

	#return HttpResponse('<h1>This is Index Page</h1>')

from pickle import load
model = load(open('./models/model.pkl', 'rb'))
scaler = load(open('./models/scaler.pkl', 'rb'))

def predictMileage(request):
	if request.method == 'POST':
		print(request.POST.dict()) # get all the value available in the form in dictonary
		val = {
		'cylinders' : request.POST.get('cylinderVal'),
      	'displacement' : request.POST.get('dispVal'),
      	'horsepower' : request.POST.get('hrsPwrVal'),
      	'acceleration' : request.POST.get('accVal'),
      	'weight' : request.POST.get('weightVal'),
      	'origin' : request.POST.get('originVal'),
      	'model year' : request.POST.get('modelVal')
       }
	data = pd.DataFrame(val, columns = ['cylinders',	'displacement',	'horsepower',	'acceleration', 'weight',	'origin',	'model year'],index=[0])
	data_scaled = scaler.transform(data)
	predictedVal = model.predict(data_scaled)[0]
	if predictedVal > 0:
		msg = 'Mileage of Your Car is appox ' + str(round(predictedVal,2)) +' mpg.'
	else :
		msg = "Error , Check Values Again else Something Wrong with Your Car"
	context = {
		'val' : msg,
		'data' : val,
		'year' : val['model year'],
	}
	return render(request, 'index.html', context)