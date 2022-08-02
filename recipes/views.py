from django.shortcuts import render

def home(request):
    return render(request,'recipes/pages/home.html',{'name':'André Luiz'})

def recipes(request,id):
    return render(request,'recipes/pages/recipe-view.html')





