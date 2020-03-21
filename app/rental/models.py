from django.db import models
from django.conf import settings

from django.utils.safestring import mark_safe

import uuid
# Create your models here.



class Facility(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])













class RentalQuerySets(models.QuerySet):
    def pending(self):
        return self.filter(state=Rental.PENDING).order_by('begin','received_on')

    def accepted(self):
        return self.filter(state=Rental.ACCEPTED).order_by('begin')

    def in_progress(self):
        return self.filter(state=Rental.IN_PROGRESS).order_by('begin')

    def finished(self):
        return self.filter(state=Rental.FINISHED).order_by('begin')[:10]

    def in_clarification(self):
        return self.filter(state=Rental.CLARIFICATION).order_by('begin')

    def rejected(self):
        return self.filter(state=Rental.REJECTED).order_by('begin')[:10]


class RentalManager(models.Manager):
    def get_queryset(self):
        return RentalQuerySets(self.model, using=self._db)  # Important!

    def pending(self):
        return self.get_queryset().pending()
        
    def accepted(self):
        return self.get_queryset().accepted()

    def in_progress(self):
        return self.get_queryset().in_progress()

    def finished(self):
        return self.get_queryset().finished()

    def in_clarification(self):
        return self.get_queryset().in_clarification()

    def rejected(self):
        return self.get_queryset().rejected()





class Rental(models.Model):
    PENDING = 'PD'
    ACCEPTED = 'AC'
    IN_PROGRESS = 'IP'
    CLARIFICATION = 'CL'
    FINISHED = 'FI'
    REJECTED = 'XX'

    TEA_ROOM = 'TR'
    BAR = 'BA'
    BOAT = 'BO'
    SPORTSHALL = 'GY'
    GAMES = 'GA'
    WS_TOOLS = 'WS'
    
    STATE_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (IN_PROGRESS, 'In Progress'),
        (CLARIFICATION, 'In Clarification'),
        (FINISHED, 'Finished'),
        (REJECTED, 'Rejected'),
    ]

    objects = RentalManager()
    slug = models.SlugField()
    received_on = models.DateField(auto_now_add=True)
    begin = models.DateTimeField()
    end = models.DateTimeField()
    facility = models.ForeignKey(Facility, on_delete=models.DO_NOTHING)
    responsibleMember = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default=PENDING,
    )
    firstname = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    apartement = models.CharField(max_length=12)
    estimated_number_of_people = models.IntegerField()
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    reason = models.CharField(max_length=255)
    comment = models.TextField(blank=True)

    def __str__(self):
        return '%s:%s %s >> %s: %s to %s' % (self.facility, self.firstname, self.surname, self.begin.date(), self.begin.time(), self.end.time())

    def get_state_tag(self):
        if self.state == self.PENDING:
            return mark_safe("""<span class="label label-warning">Pending</span>""")
        elif self.state == self.ACCEPTED:
            return mark_safe("""<span class="label label-success">Accepted</span>""")
        elif self.state == self.IN_PROGRESS:
            return mark_safe("""<span class="label label-primary">Running</span>""")
        elif self.state == self.REJECTED:
            return mark_safe("""<span class="label label-danger">Rejected</span>""")
        elif self.state == self.FINISHED:
            return mark_safe("""<span class="label label-plain">Finished</span>""")
        elif self.state == self.CLARIFICATION:
            return mark_safe("""<span class="label label-information">Clarification</span>""")


    def _get_unique_slug(self):
        slug = uuid.uuid4()
        unique_slug = slug
        num = 1
        while Rental.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class RentalComment(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

class RentalActivity(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    status = models.CharField(max_length=12)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

