from django.shortcuts import render,redirect
from .models import Client, Wallet_Client

def Register(request):
	if request.method == 'POST':
		Client(
			name = request.POST.get('name'),
			phone = request.POST.get('phone'),
			email = request.POST.get('email'),
			user = request.POST.get('username'),
			password = request.POST.get('pswd')
		).save()
		Wallet_Client(
			amount = 0,
			client = Client.objects.get(email = request.POST.get('email'))
		).save()
		request.session['email_client'] = request.POST.get('email') 
		request.session['img_client'] = Client.objects.get(email = request.POST.get('email')).img.url
		return redirect('Home')

	return render(request,'authentication/register_client.html')


def LogOut_Client(request):
	print(request.session['email_client'])
	del request.session['email_client']

	return redirect('Home')

def Login_Client(request):
	if request.method == 'POST':
		try:
			c = Client.objects.get(email = request.POST.get('email'), password = request.POST.get('pswd'))
			request.session['email_client'] = request.POST.get('email')
			request.session['img_client'] = c.img.url
			wallet = Wallet_Client.objects.get(email = request.POST.get('email'))
			request.session['amount_wallet_client'] = wallet.amount
			return redirect('Home')
		except Client.DoesNotExist as e:
			print(e)
	return render(request,'authentication/login_client.html')




def Profile(request):
	return render(request,'user/profile_client.html')







