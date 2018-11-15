from django.shortcuts import render
from.forms import bioform
from django.http import HttpResponse

def bioview(request):
    if request.method=='POST':
        form=bioform(request.POST)
        if form.is_valid():
            return HttpResponse('Data is Inserted')
        else:
            return HttpResponse('Data is not Inserted')
        pass
    else:
        form=bioform()
        return render(request,'biodatafile.html',{'form':form})





