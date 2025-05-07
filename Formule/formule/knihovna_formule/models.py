from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    image = models.ImageField(upload_to='teams/', null=True, blank=True)

    def __str__(self):
        return self.name
class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    number = models.IntegerField()
    nationality = models.CharField(max_length=100)
    image = models.ImageField(upload_to='drivers/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Track(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    length_km = models.FloatField()
    image = models.ImageField(upload_to='tracks/', null=True, blank=True)

    def __str__(self):
        return self.name
class GrandPrix(models.Model):
    name = models.CharField(max_length=100)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} – {self.date}"
