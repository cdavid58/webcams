from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Register/$',Register,name="Register_Client"),
	url(r'^LogOut_Client/$',LogOut_Client,name="LogOut_Client"),
	url(r'^Login_Client/$',Login_Client,name="Login_Client"),
	url(r'^Profile/$',Profile,name="Profile_Client"),
]