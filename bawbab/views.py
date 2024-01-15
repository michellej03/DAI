from django.shortcuts import render

def verify(request):
    return render(request, 'verify.html', {'page': 'verify'})

def setup(request):
    return render(request, 'setup.html', {'page': 'setup'})
