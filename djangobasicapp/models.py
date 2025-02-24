from django.db import models


class Employee(models.Model):
    COUNTRIES = [
        ("IND", "India"),                
        ("USA", "United States of America"),
        ("UK", "United Kingdom"),
        ("AUS", "Australia"),
        ("UA", "Austria"),
        ("SP", "Spain"),

    ]
    fisrt_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tilte_name = models.CharField(max_length=30)
    has_passport = models.BooleanField(default=True)
    salary = models.IntegerField(default=None)
    brith_date = models.DateField(default=None)
    hire_date = models.DateField(default=None)
    notes = models.CharField(max_length=200)
    country = models.CharField(max_length=35, choices=COUNTRIES, default=None)
    email = models.EmailField(default="", max_length=50)
    
    def __str__(self):
        return  "name" + " " +self.fisrt_name +" "+"|" + "country" + " " + self.get_country_display()

