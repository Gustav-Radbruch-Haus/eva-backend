from django.db import models

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
        return '%s:%s %s >> %s' % (self.get_facility_display(), self.firstname, self.surname, self.begin)
