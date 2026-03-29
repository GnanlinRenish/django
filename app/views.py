from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Container
from django.contrib import auth

def app(request):
    if request.method=='POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        Container.objects.create(name=name,date=date)
        return redirect('app')
    else:
        data=Container.objects.all()
        return render (request,'app.html',{'data': data})



def edit(request, id):
    item = get_object_or_404(Container, id=id)

    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.date = request.POST.get('date')
        item.save()   

        return redirect('app')

    return render(request, 'edit.html', {'item': item})

def delete(request,id):
    item=get_object_or_404(Container,id=id)
    if request.method=='POST':
        item.delete()
        return redirect('app')
    return redirect ('app')