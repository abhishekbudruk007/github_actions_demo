from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.
def Home(request):
    # sql_query = "select * from products"
    return render(request,"app_demo/home.html")
