from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Triumph(models.Model):
    term = models.CharField('Search query', max_length=100)
    result = models.CharField('Result', max_length=255)

    def __str__(self):
        return "{0} - {1}".format(self.term)


class Part(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Search(models.Model):
    brand = models.CharField('Brand', max_length=7)
    term = models.CharField('Search query', max_length=100)
    results = models.ManyToManyField('Part', blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.brand, self.term)


class UserSearchHistory(models.Model):
    search = models.ForeignKey(Search, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.term


class UserFeedback(models.Model):
    search = models.ForeignKey(Search, on_delete=models.CASCADE)
    date = models.DateTimeField()
    comment = models.CharField(max_length=2000)

    def __str__(self):
        return "<Feedback:ID={0}>".format(self.id)


class Sighting(models.Model):
    make = models.CharField('Make', max_length=256)
    model = models.CharField('Model', max_length=256)
    year = models.IntegerField('Year', null=True, blank=True,
                               validators=[MinValueValidator(1800)])
    frame_number = models.CharField('Frame Number', max_length=64, null=True,
                                    blank=True)
    engine_number = models.CharField('Engine Number', max_length=64, null=True,
                                     blank=True)
    notes = models.TextField('Notes', null=True, blank=True)
    country = models.CharField('Country', max_length=256, null=True,
                               blank=True)
    state = models.CharField('State', max_length=256, null=True, blank=True)
    city = models.CharField('City', max_length=256, null=True, blank=True)
    contact = models.TextField('Contact', null=True, blank=True)
    user = models.ForeignKey(User, related_name='sighting', null=True,
                             on_delete=models.SET_NULL)
