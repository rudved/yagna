from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app.models import SavingsAccount


def show(request):
    d1 = SavingsAccount.objects.all()
    return render(request,'index.html',{"data":d1})


def savedata(request):
    acno = request.POST.get('acno')
    name = request.POST.get('name')
    type = request.POST.get('type')
    age = request.POST.get('age')
    gen = request.POST.get('gen')
    blc = request.POST.get('blc')
    SavingsAccount(acno=acno,name=name,type=type,age=age,gender=gen,blc=blc).save()
    return render(request,'index.html')


def showone(request):
    acno = request.GET.get('acno')
    try:
        res = SavingsAccount.objects.get(acno=acno)
        return JsonResponse({'response':True,'data':{'racno':res.acno,'rname':res.name,'rtype':res.type,'rage':res.age,'rgender':res.gender,'rblc':res.blc}})
    except:
       return JsonResponse({'response':False})