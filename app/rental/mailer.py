from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from rental.models import Rental, RentalActivity

def notify_rm_new_request(rental: Rental):
    receiver = rental.email
    member = rental.responsibleMember
    plaintext = get_template('mail/notify_new_request.txt')
    #htmly     = get_template('email.html')

    d = { 'name': rental.firstname + " " + rental.surname, 'facility': rental.facility, 'datefrom': rental.begin,'dateto': rental.end, 'reason': rental.reason}

    subject, from_email, to = 'A new request is made', 'noreply@grh-hamburg.de', 'rentalmanagers@grh-hamburg.de'
    text_content = plaintext.render(d)
    #html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #msg.attach_alternative(html_content, "text/html")
    msg.send()

def notify_tn_request_approved(rental: Rental):
    receiver = rental.email
    member = rental.responsibleMember
    plaintext = get_template('mail/confirm_received.txt')
    #htmly     = get_template('email.html')

    d = { 'name': rental.firstname + " " + rental.surname, 'facility': rental.facility, 'datefrom': rental.begin,'dateto': rental.end, 'rental_member': rental.responsibleMember.get_full_name }

    subject, from_email, to = 'Confirmation of your rental', 'noreply@grh-hamburg.de', receiver
    text_content = plaintext.render(d)
    #html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #msg.attach_alternative(html_content, "text/html")
    msg.send()
    log = RentalActivity(rental=rental, status="success", comment="Mail sent: Request Accepted.")
    log.save()

def notiy_tn_request_rejected(rental: Rental):
    receiver = rental.email
    member = rental.responsibleMember
    plaintext = get_template('mail/deny_request_rejected.txt')
    #htmly     = get_template('email.html')

    d = { 'name': rental.firstname + " " + rental.surname, 'facility': rental.facility, 'datefrom': rental.begin,'dateto': rental.end, 'rental_member': rental.responsibleMember }

    subject, from_email, to = 'Rejection of your rental request', 'noreply@grh-hamburg.de', receiver
    text_content = plaintext.render(d)
    #html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #msg.attach_alternative(html_content, "text/html")
    msg.send()
    log = RentalActivity(rental=rental, status="error", comment="Mail sent: Request Rejected.")
    log.save()