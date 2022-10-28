from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


# Create your views here.
def demo(request):
    obj=place.objects.all()
    new=team.objects.all()

    return render(request,'index.html',{'result':obj,'display':new})
# def result(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     sub=x-y
#     mult=x*y
#     div=x/y
#     return render(request,'result.html',{'result':res,'substraction':sub,"multiply":mult,'divide':div})
