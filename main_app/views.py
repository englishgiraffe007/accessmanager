from django.shortcuts import render
# Create your views here.
def index(request):
    firstProgram = "OfficeManager"
    secondProgram = "CustomerManager"
    context = {'firstProgram': firstProgram,
        'secondProgram': secondProgram}
    return render(request, 'index.html', context)
def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')
def officemanager(request):
    return render(request, 'officemanager.html')
def customermanager(request):
    return render(request, 'customermanager.html')
def helppage(request):
    return render(request, 'help.html')
def contact(request):
    return render(request, 'contact.html')