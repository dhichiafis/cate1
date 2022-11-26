from django.shortcuts import render
def hello(request):
    return render(request,'hello/hello.html')

def again(request):
    return render(request,'hello/again.html')
# Create your views here.
