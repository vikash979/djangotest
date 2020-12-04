from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView , View
from .models import Employee
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from django.template.loader import get_template
from django.contrib.auth import authenticate,login,logout
from . import serializers


class LoginViews(TemplateView):
	template_name = "test_project/login.html"
	def get(self,request):
		context_data = {}
		if request.user.is_authenticated:
			return HttpResponseRedirect("/testlogin/home/")
		else:
			return render(request, self.template_name, context_data)

	def post(self,request):
		context_data ={}
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:

			if user.is_active:
				login(request, user)
				request.session['fav_color'] = 'blue'

				return HttpResponseRedirect("/testlogin/home/")
			else:
				context_data['error'] = {"errors" : "Username or Password is not correct"}
				return render(request, self.template_name, context_data)
			return render(request, self.template_name, context_data)




class homeViews(TemplateView):
	template_name = "test_project/home.html"
	def get(self, request, id=None):
		context_data = {}
		context_data['error'] = ''

		return render(request, self.template_name, context_data)

	def post(self,request):
		context_data = {}
		if request.POST.get('submit') == 'submit':
			name = request.POST.get('name')
			email = request.POST.get('email')
			address = request.POST.get('address')
			Employee.objects.create(employee_name=name, employee_email=email, employee_address=address)
			return HttpResponseRedirect("/testlogin/home/")


		return render(request, self.template_name, context_data)



class EmployeeView(APIView):

	def get(self,request, format=None):

		employee_obj =  Employee.objects.all()
		serializer = serializers.EmployeeSerializer(employee_obj,many=True)
		return Response(serializer.data)



def deleteList(request):
	print(request.GET.get('id'))
	employee_obj =  Employee.objects.filter(id=request.GET.get('id')).delete()
	return HttpResponseRedirect("/testlogin/home/")

class updateHome(TemplateView):
	template_name = "test_project/update.html"

	def get(self,request):
		context_data={}
		employee_obj =  Employee.objects.filter(id=request.GET.get('id'))
		
		context_data['emp'] = employee_obj

		return render(request, self.template_name, context_data)

	def post(self,request):
		context_data = {}
		if request.POST.get('submit') == 'submit':
			name = request.POST.get('name')
			email = request.POST.get('email')
			address = request.POST.get('address')
			Employee.objects.filter(id=request.POST.get('mainid')).update(employee_name=name, employee_email=email, employee_address=address)
			return HttpResponseRedirect("/testlogin/home/")


		return render(request, self.template_name, context_data)










