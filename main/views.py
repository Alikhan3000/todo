from django.shortcuts import render, HttpResponse

 #Create your views here
def homepage(request):
    return HttpResponse("this is my first page")

def test(request):
    return render(request, "test.html")

