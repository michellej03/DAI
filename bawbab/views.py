# views.py
from django.shortcuts import render, redirect
from .forms import VerificationForm

def verify(request):
    if request.method == 'POST':
        verification_form = VerificationForm(request.POST)
        if verification_form.is_valid():
            # Process the form data and move to the next step
            return redirect('setup.html')
    else:
        verification_form = VerificationForm()

    return render(request, 'verify.html', {'verification_form': verification_form})
def setup(request):
    # Your view logic here
    return render(request, 'setup.html')