from django.db import models
from django.urls import reverse
from datetime import date

RATINGS = (
    ('5', '5 stars'),
    ('4', '4 stars'),
    ('3', '3 stars'),
    ('2', '2 stars'),
    ('1', '1 star'),
)

class Experience(models.Model):
  method = models.CharField(max_length=50)
  equipment = models.CharField(max_length=50)

  def __str__(self):
    return self.method

  def get_absolute_url(self):
    return reverse('experiences_detail', kwargs={'pk': self.id})

class Sunset(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    experiences = models.ManyToManyField(Experience)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sunset_id': self.id})
    
    def viewed_for_today(self):
        return self.viewing_set.filter(date=date.today()).count() >= 1

class Viewing(models.Model):
    date = models.DateField()
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0]
        )
    
    sunset = models.ForeignKey(Sunset, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"

    class Meta:
        ordering = ['-date']