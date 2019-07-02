from django.shortcuts import render
from django.template.response import TemplateResponse
from . import forms

# Create your views here.

def index(request):
    return TemplateResponse(request, 'registration/profile.html', {})


def makeRequest(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.RentalrequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            instance = form.save()
            # redirect to a new URL:
            return TemplateResponse(request, 'request/receivedrequest.html', {'req':instance})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.RentalrequestForm()

    return render(request, 'request/makerequest.html', {'form': form})