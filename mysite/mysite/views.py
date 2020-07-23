from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello Manish")
    return render(request, 'index.html')


def about(request):
    print(request.GET.get('text', 'default'))
    return HttpResponse("about manish")
