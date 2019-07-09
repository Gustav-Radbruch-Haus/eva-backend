from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#import request as req
from . import forms
from . import models

# Create your views here.

@login_required
def index(request):
    req_pending = models.Rental.objects.filter(
        state=models.Rental.PENDING).order_by('begin','received_on')
    req_upcoming = models.Rental.objects.filter(
        state=models.Rental.ACCEPTED).order_by('begin')
    req_running = models.Rental.objects.filter(
        state=models.Rental.IN_PROGRESS).order_by('begin')
    req_finished = models.Rental.objects.filter(
        state=models.Rental.FINISHED).order_by('begin')[:10]
    req_clarify = models.Rental.objects.filter(
        state=models.Rental.CLARIFICATION).order_by('begin')
    req_rejected = models.Rental.objects.filter(
        state=models.Rental.REJECTED).order_by('begin')[:10]
    return TemplateResponse(request, 'rentals/dashboard.html', {'req_upcoming_count': req_upcoming.count(), 'req_pending_count': req_pending.count(), 'req_running_count': req_running.count() , 'req_finished_count': req_finished.count(), 'req_rejected_count': req_rejected.count(), 'req_clarify_count': req_clarify.count(), 'req_pending': req_pending, 'req_upcoming': req_upcoming, 'req_running': req_running, 'req_finished': req_finished, 'req_rejected': req_rejected, 'req_clarify': req_clarify})

@login_required
def showDetails(request, requestSlug):
    instance = get_object_or_404(models.Rental, slug=requestSlug)
    instance_comments = models.RentalComment.objects.filter(rental=instance.id).order_by('-created_at')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.RentalCommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            sF = form.save(commit=False)
            sF.creator = request.user
            sF.rental = instance
            sF.save()
            return TemplateResponse(request, 'rentals/details.html', {'reqID':requestSlug, 'req':instance, 'comments':instance_comments, 'form': forms.RentalCommentForm()})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.RentalCommentForm()

    return TemplateResponse(request, 'rentals/details.html', {'reqID':requestSlug, 'req':instance, 'comments':instance_comments, 'form': form})

@login_required
def commentOnRequest(request, requestSlug):
    rental = get_object_or_404(models.Rental, slug=requestSlug)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.RentalCommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.rental = rental.id
            return HttpResponseRedirect(reverse('requestDetail', args=[requestSlug]))
    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponseRedirect(reverse('requestDetail', args=[requestSlug]))


@login_required
def acceptRequest(request, requestSlug):
        instance = get_object_or_404(models.Rental, slug=requestSlug)
        instance.state = models.Rental.ACCEPTED
        # TODO Ignore instance that are not pending
        instance.save()
        return HttpResponseRedirect(reverse('rentalDashboard'))

@login_required
def rejectRequest(request, requestSlug):
        instance = get_object_or_404(models.Rental, slug=requestSlug)
        instance.state = models.Rental.REJECTED
        # TODO Ignore instance that are not pending
        instance.save()
        return HttpResponseRedirect(reverse('rentalDashboard'))

@login_required
def startRequest(request, requestSlug):
        instance = get_object_or_404(models.Rental, slug=requestSlug)
        instance.state = models.Rental.IN_PROGRESS
        # TODO Ignore instance that are not pending
        instance.save()
        return HttpResponseRedirect(reverse('rentalDashboard'))

@login_required
def finishRequest(request, requestSlug):
        instance = get_object_or_404(models.Rental, slug=requestSlug)
        instance.state = models.Rental.FINISHED
        # TODO Ignore instance that are not pending
        instance.save()
        return HttpResponseRedirect(reverse('rentalDashboard'))


@login_required
def clarifyRequest(request, requestSlug):
        instance = get_object_or_404(models.Rental, slug=requestSlug)
        instance.state = models.Rental.CLARIFICATION
        # TODO Ignore instance that are not pending
        instance.save()
        return HttpResponseRedirect(reverse('rentalDashboard'))

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
