from django.urls import path
from . import views

# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
	path('',views.indexview,name='index'),
	path("Soham",views.homeview,name="homepage"),
	path("blog_list",views.blog_list,name="blog_list"),
	path("customers",views.customersview,name="customers"),
	path("query",views.queryview,name="query"),
	path("query",views.gtaview,name="gta"),

   
       ]


