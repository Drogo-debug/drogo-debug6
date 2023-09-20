import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.shortcuts import render

from webscrapperapp.models import links


# Create your views here.
def home(request):
    if request.method=='POST':
        newlink=request.POST.get('page','')
        url=requests.get(newlink)
        btsp=BeautifulSoup(url.text,'html.parser')
        for link in btsp.find_all('a'):
            li_adress=link.get('href')
            li_name=link.string
            links.objects.create(address=li_adress,stringname=li_name)
        return HttpResponseRedirect('/')
    else:
        datavalues=links.objects.all()



    return render(request,'home.html',{'datavalues':datavalues})