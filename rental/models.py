from django.db import models
from django.conf import settings
import uuid
# Create your models here.


class Rental(models.Model):
    PENDING = 'PD'
    ACCEPTED = 'AC'
    IN_PROGRESS = 'IP'
    CLARIFICATION = 'CL'
    FINISHED = 'FI'
    REJECTED = 'XX'

    STATE_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (IN_PROGRESS, 'In Progress'),
        (CLARIFICATION, 'In Clarification'),
        (FINISHED, 'Finished'),
        (REJECTED, 'Rejected'),
    ]

    TEA_ROOM = 'TR'
    BAR = 'BA'
    BOAT = 'BO'
    SPORTSHALL = 'GY'
    GAMES = 'GA'
    WS_TOOLS = 'WS'

    RENTAL_CHOICES = [
        (TEA_ROOM, 'Tea Room'),
        (BAR, 'Bar'),
        (BOAT, 'Boat'),
        (SPORTSHALL, 'Sportshall'),
        (GAMES, 'Games'),
        (WS_TOOLS, 'Workshop Tools'),
    ]

    objects = models.Manager()
    slug = models.SlugField()
    received_on = models.DateField(auto_now_add=True)
    begin = models.DateTimeField()
    end = models.DateTimeField()
    facility = models.CharField(
        max_length=2,
        choices=RENTAL_CHOICES,
        default=TEA_ROOM,
    )

    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default=PENDING,
    )
    firstname = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    appartement = models.CharField(max_length=12)
    estinated_number_of_people = models.IntegerField()
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    reason = models.CharField(max_length=255)
    comment = models.TextField(blank=True)

    def __str__(self):
        return '%s:%s %s >> %s: %s to %s' % (self.get_facility_display(), self.firstname, self.surname, self.begin.date(), self.begin.time(), self.end.time())

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