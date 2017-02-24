from django.shortcuts import render

# Create your views here.
def om(request):
    return render(request, 'officeManager.html')