from django.db import models


# Create your models here.
gender_choices = (
    ('male', 'male'),
    ('female', 'female'),
)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=gender_choices)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


