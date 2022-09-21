from django.http import HttpResponse
from django.shortcuts import render,redirect
from model.models import Modelo
from study.models import Study
from client.models import *
from model.models import Modelo, Wallet_Model
import requests, os, urllib.request
from bs4 import BeautifulSoup
from .models import Configuration

dolar = 0

def online_values():
    response_one_dollar= requests.get('http://www.xe.com/es/currencyconverter/convert/?Amount=1&From=USD&To=COP')
    soup_one_dollar = BeautifulSoup(response_one_dollar.content, 'html.parser')
    container_dollar = soup_one_dollar.find('p', 'iGrAod')
    one_dollar = container_dollar.contents[0]
    return float(one_dollar.replace(',','.'))

def dollar_to_cop(request):
	global dolar
	if request.is_ajax():
		dollar_amount = request.GET.get('dollar')
		dolar = dollar_amount
		dolar = float(dolar)
		result = online_values() * dolar
		return HttpResponse(result)

def Home(request):
	_models = Modelo.objects.filter(online= True)
	config = Configuration.objects.last().value_token_transaction

	return render(request,'index.html',{'model':_models,'token_transaction':config})


def Register(request):
	mssg = ""
	if request.method == 'POST':
		if request.POST.get('term') is not None:
			try:
				Study(
					name_study = request.POST.get('username'),
					pswd = request.POST.get('pswd'),
					email = request.POST.get('email'),
					birthday = request.POST.get('birthday')
				).save()
				return redirect('Home')
			except Exception as e:
				mssg = "Ese nombre ya esta registrado"
	return render(request,'authentication/register.html',{'mssg':mssg})

def Login(request):
	if request.method == 'POST':
		try:
			study = Study.objects.get(email = request.POST.get('email'), pswd= request.POST.get('pswd'))
			return redirect('Home')
		except Study.DoesNotExist as e:
			print("Error")
	return render(request,'authentication/login.html')


def Shopping_Tokens(request):
	global dolar
	if request.is_ajax():
		c = Client.objects.get(email = request.session['email_client'])
		wallet = Wallet_Client.objects.get(client=c)
		wallet.amount = int(wallet.amount) + int(dolar)
		wallet.save()
		config = Configuration.objects.last()
		config.value_token_transaction = int(config.value_token_transaction) + 1
		config.save()
		return HttpResponse(dolar)



def Dar_Tips(request):
	global dolar
	if request.is_ajax():
		c = Client.objects.get(email = request.session['email_client'])
		wallet = Wallet_Client.objects.get(client=c)
		if wallet.convert_dollar_to_tokens() > 0:
			w = Wallet_Model.objects.last()
			w.amount = int(w.amount) + int(dolar)
			w.save()
		return HttpResponse()



