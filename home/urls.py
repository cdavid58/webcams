from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Home,name="Home"),
	url(r'^Register/$',Register,name="Register"),
	url(r'^Login/$',Login,name="Login"),
	url(r'^Shopping_Tokens/$',Shopping_Tokens,name="Shopping_Tokens"),
	url(r'^Dar_Tips/$',Dar_Tips,name="Dar_Tips"),
	url(r'^dollar_to_cop/$',dollar_to_cop,name="dollar_to_cop"),
]