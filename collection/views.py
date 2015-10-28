from django.shortcuts import render

# Create your views here.
def index(request) :
	price = 6 #simulating money
	data = "Apples"

	return render(request, 'index.html', {
		'price': price,
		'data': data,

		})