from django.shortcuts import render

# Create your views here.
def cm(request):
    return render(request, 'customerManager.html')