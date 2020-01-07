from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import requests as req
import json
from . import forms
from .models import Rental, Facility, RentalComment
from rental.mailer import notify_rm_new_request, notify_tn_request_approved, notiy_tn_request_rejected

# Create your views here.

@login_required
def index(request):
    req_pending = Rental.objects.pending()
    req_accepted = Rental.objects.accepted()
    req_running = Rental.objects.in_progress()
    req_finished = Rental.objects.finished()
    req_clarify = Rental.objects.in_clarification()
    req_rejected = Rental.objects.rejected()

    return TemplateResponse(request, 'rentals/dashboard.html', {'req_accepted_count': req_accepted.count(), 'req_pending_count': req_pending.count(), 'req_running_count': req_running.count() , 'req_finished_count': req_finished.count(), 'req_rejected_count': req_rejected.count(), 'req_clarify_count': req_clarify.count(), 'req_pending': req_pending, 'req_accepted': req_accepted, 'req_running': req_running, 'req_finished': req_finished, 'req_rejected': req_rejected, 'req_clarify': req_clarify})

@login_required
def showDetails(request, requestSlug):
    instance = get_object_or_404(Rental, slug=requestSlug)
    instance_comments = RentalComment.objects.filter(rental=instance.id).order_by('-created_at')
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
    rental = get_object_or_404(Rental, slug=requestSlug)
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
        instance = get_object_or_404(Rental, slug=requestSlug)
        instance.responsibleMember = request.user
        instance.state = Rental.ACCEPTED
        # TODO Ignore instance that are not pending
        instance.save()
        notify_tn_request_approved(instance)
        return HttpResponseRedirect(reverse('rentalDashboard'))

@login_required
def rejectRequest(request, requestSlug):
        instance = get_object_or_404(Rental, slug=requestSlug)
        instance.state = Rental.REJECTED
        # TODO Ignore instance that are not pending
        instance.save()
        notiy_tn_request_rejected(instance)
        return HttpResponseRedirect(reverse('rentalDashboard'))

@login_required
def startRequest(request, requestSlug):
        instance = get_object_or_404(Rental, slug=requestSlug)
        instance.state = Rental.IN_PROGRESS
        instance.responsibleMember = request.user
        # TODO Ignore instance that are not pending
        instance.save()
        return HttpResponseRedirect(reverse('rentalDashboard'))

@login_required
def finishRequest(request, requestSlug):
        instance = get_object_or_404(Rental, slug=requestSlug)
        instance.state = Rental.FINISHED
        instance.responsibleMember = request.user
        # TODO Ignore instance that are not pending
        instance.save()
        return HttpResponseRedirect(reverse('rentalDashboard'))


@login_required
def clarifyRequest(request, requestSlug):
        instance = get_object_or_404(Rental, slug=requestSlug)
        instance.state = Rental.CLARIFICATION
        instance.responsibleMember = request.user
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

            notify_rm_new_request(instance)
            return TemplateResponse(request, 'request/receivedrequest.html', {'req': instance})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.RentalrequestForm()

    return render(request, 'request/makerequest.html', {'form': form})