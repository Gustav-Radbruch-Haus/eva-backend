from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
#import request as req
from . import forms
from . import models

# Create your views here.


def index(request):
    req_pending = models.Rental.objects.filter(
        state=models.Rental.PENDING).order_by('begin')
    req_upcoming = models.Rental.objects.filter(
        state=models.Rental.ACCEPTED).order_by('begin')
    req_running = models.Rental.objects.filter(
        state=models.Rental.IN_PROGRESS).order_by('begin')
    req_finished = models.Rental.objects.filter(
        state=models.Rental.FINISHED).order_by('begin')[:10]
    return TemplateResponse(request, 'rentals/dashboard.html', {'req_upcoming_count': req_upcoming.count(), 'req_pending_count': req_pending.count(), 'req_running_count': 2, 'req_finished_count': 25, 'req_pending': req_pending, 'req_upcoming': req_upcoming, 'req_running': req_running, 'req_finished': req_finished})

def showDetails(request, requestSlug):
        instance = get_object_or_404(models.Rental, slug=requestSlug)
        return TemplateResponse(request, 'registration/profile.html', {'reqID':requestSlug, 'req':instance})

def makeRequest(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.RentalrequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            instance = form.save()

            #data = {
            #'username': 'root',
            #'password': 'SVgrh123456!'
            #}
            #response = req.post('http://localhost:3000/users/login', data=data)

            # redirect to a new URL:
            return TemplateResponse(request, 'request/receivedrequest.html', {'req': instance})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.RentalrequestForm()

    return render(request, 'request/makerequest.html', {'form': form})

    #curl http://localhost:3000/users/login -d "username=root&password=SVgrh123456!"

    #curl -H "Authorization: Bearer veMnGcGDrUAG0d3Sl9j92_X5-V0exCvtq3j6sioH8dQ" -H "Content-type:application/json" -X POST http://localhost:3000/api/boards/LZFFTtWzFAxnfvy8J/cards  -d '{ "title": "Card title text", "description": "Card description text", "authorId": "The appropriate existing userId", "swimlaneId": "The destination swimlaneId" }'
