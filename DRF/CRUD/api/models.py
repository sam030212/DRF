from django.db import models

# Create your models here.

# creating company model


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    about = models.TextField(max_length=100)
    type = models.CharField(max_length=100, choices=
                            (('IT', 'IT'),
                            ('NON IT', 'NON IT'),
                            ('MOBILE PHONES', 'MOBILE PHONES')
                            ))
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
