from django.shortcuts import render
# Create your views here.
def prabhas(request):
    d={'name':'prabhas','star':'rebel'}
    return render(request,'prabhas.html',context=d)
