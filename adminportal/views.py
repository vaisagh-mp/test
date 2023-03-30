from django.shortcuts import render, redirect
from app.models import *
from accounts.models import *
from django.contrib.auth import authenticate, login, logout
# from adminportal.forms import productform


def pdisplay(request):
     results=Product.objects.all()
     return render(request,"admin.html",{"Product":results})


def pinsert(request):
    if request.method=="POST":
        savep=Product()
        savep.title=request.POST.get('Title')
        savep.selling_price=request.POST.get('Selling')
        savep.discounted_price=request.POST.get('Discounted')
        savep.description=request.POST.get('Description')
        savep.composition=request.POST.get('Composition')
        savep.prodapp=request.POST.get('prodapp')
        savep.category=Categories.objects.get(id=request.POST['Category'])
        savep.product_image=request.FILES.get('image')
        savep.save()
        return redirect('pdisplay')
    else:
        categories = Categories.objects.all()
        context = {
            'categories' : categories,
        }
        return render(request,'productcreate.html',context)


def pedit(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'POST':
        product.title=request.POST['Title']
        product.selling_price=request.POST['Selling']
        product.discounted_price=request.POST['Discounted']
        product.description=request.POST['Description']
        product.composition=request.POST['Composition']
        product.prodapp=request.POST['Prodapp']
        product.category=Categories.objects.get(id=request.POST['Category'])
        product.product_image=request.FILES['image']
        product.save()
        return redirect('pdisplay')
    else:
        categories = Categories.objects.all()
        context = {
            'Product':product,
            'categories' : categories,
        }
        return render(request,'productedit.html',context)
    
     
def pdelete(request,id):
     delproduct=Product.objects.get(id=id)
     delproduct.delete()
     results=Product.objects.all()
     return render(request,"admin.html",{"Product":results})



def Logout(request):
    logout(request)
    return redirect('Login')