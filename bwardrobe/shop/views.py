from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil

# Create your views here.

def index(request):
    # products=Products.objects.all()
    # n=len(products)
    # # print(n)
    # nSlides=n//4+ceil((n/4)-(n//4))
    # allProds = [[products,range(1, len(products)), nSlides],
    #             [products,range(1, len(products)), nSlides],
    #
    #             [products,range(1,len(products)), nSlides]]

    allprods=[]
    # it just fetch the category and id of all products in database
    catprod=Products.objects.values('category','id')

    # print(catprod)
    # it just fetch the category and id of all products in database
    cats={item['category'] for item in catprod}
    # it just fetch the category and id of all products in database
    print('yeh ha cats me item')
    print(cats)

    for cat in cats:
        # it fetch the the whole data of category
        prod=Products.objects.filter(category=cat)
        print(prod)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nSlides),nSlides])




    params = { 'product': allprods}
    return render(request,"shop/shop1.html",params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return render(request,"shop/contact.html")
def search(request,id):
    sproducts = Products.objects.filter(id=id)
    return render(request,'shop/search.html', {'sproducts': sproducts[0]})
def prodView(request,id):
    products = Products.objects.filter(id=id)

    return render(request, 'shop/prodView.html', {'products': products[0]})

