from django.forms import ModelForm, ValidationError
from datetime import timedelta
import holidays
from . import models

class RentalCommentForm(ModelForm):
    class Meta:
        model = models.RentalComment
        fields = ['comment']

class RentalrequestForm(ModelForm):
    class Meta:
        model = models.Rental
        fields = ['begin', 'end', 'facility', 'firstname', 'surname', 'apartement',
                  'email', 'phone', 'estimated_number_of_people', 'reason', 'comment']

    def __init__(self, *args, **kwargs):
        super(RentalrequestForm, self).__init__(*args, **kwargs)
        self.fields['begin'].widget.attrs['placeholder'] = 'DD.MM.YYYY HH:MM:SS'
        self.fields['end'].widget.attrs['placeholder'] = 'DD.MM.YYYY HH:MM:SS'

    def clean(self):
        cleaned_data = super().clean()
        begin = cleaned_data.get("begin")
        end = cleaned_data.get("end")
        facility = cleaned_data.get("facility")
        rentalsForTheFacility = models.Rental.objects.filter(facility=facility)
        deHolidays = us_holidays = holidays.CountryHoliday('DE', prov='HH')

        ### VALIDATION OF RENTAL REQUESTS ###
        # Valid options for Bar-Rental
        if facility == models.Rental.BAR:
            if begin.isoweekday() == 5 or begin.isoweekday() == 7:
                raise ValidationError(
                    "The BAR cannot be rented on fridays or sundays!")
            if begin.hour < 18:
                raise ValidationError(
                    "The BAR cannot be rented before 18:00:00 (6:00:00 PM)!")
            if (end - begin) > timedelta(hours=24):
                raise ValidationError(
                    "The BAR cannot be rented more than one day in a row!")
            if end.hour > 15:
                raise ValidationError(
                    "The BAR has to be returned before 15:00:00 (3:00:00 PM) the next day!")

        # Validate DateTime
        if begin > end:
            raise ValidationError(
                {'begin': ["The begin of the rental has to be before the end of it.", ]})

        # Special validations for Bar and Tea Room
        if facility.code == models.Rental.BAR or facility.code == models.Rental.TEA_ROOM:
            if begin.date() in deHolidays or end.date() in deHolidays:
                raise ValidationError(
                    "The cannot be a rental during hoolidays!")

            for rental in rentalsForTheFacility:
                if rental.begin <= begin and begin <= (rental.end + timedelta(minutes=59)):
                    raise ValidationError(
                        {'begin': ["The facility is already rented on that date and time!", ]})
                if (rental.begin - timedelta(minutes=59)) <= end and end <= (rental.end + timedelta(minutes=59)):
                    raise ValidationError(
                        {'end': ["The facility is already rented on that date and time!", ]})
                if begin <= rental.begin and rental.end <= end:
                    raise ValidationError(
                        "The facility is already rented on that date and time!")
