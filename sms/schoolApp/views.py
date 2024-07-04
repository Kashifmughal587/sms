from django.shortcuts import render
from django.http import HttpResponse

def sayHello (request):
    # return HttpResponse ('Hello World')
    return render(request, 'hello.html', {"name": "Kashif Shehzad"})

# Create your views here.
