from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response 
# View have API which are self proclaimed

# Create your views here.
from .models import Items

class ItemsView(APIView):
	# Under this we can create all method
	def get(self, request):
		if 'name' in request.GET:
			data = Items.objects.filter(name=request.GET['name']).values('name', 'price').first()#if we need a single object then we use GET insted of Filter. 1) If we will get data then there will be no data in json. 
		else:
			data = Items.objects.all().values('name', 'price')

			# it will bring all the values from item field which has every data about name and price
		return Response({"test":"pass"},status=200)
		# \admin is known as endpoint
		# Here we have made an service for wich we have to create endpoints. To invoke the view.

		def post(self, request):
			data = request.data
			print(data)
			item_obj = Items.objects.create(name=data['name'], price=data['price'])
			return Response({"message":"created"}, status=202)

			# here GET is a function where values are declared