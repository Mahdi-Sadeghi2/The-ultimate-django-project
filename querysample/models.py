from django.db import models

# Create your models here.


class Country(models.Model):
    COUNTRIES = [
        ("IND", "India"),
        ("USA", "United States of America"),
        ("UK", "United Kingdom"),
        ("AUS", "Australia"),
        ("UA", "Austria"),
        ("SP", "Spain"),
        ("CAN", "Canada"),
        ("GER", "Germany"),
        ("FRA", "France"),
        ("ITA", "Italy"),
        ("BRA", "Brazil"),
        ("MEX", "Mexico"),
        ("JPN", "Japan"),
        ("CHN", "China"),
        ("RUS", "Russia"),
        ("CHL", "Chile"),
        ("SWE", "Sweden"),
        ("NOR", "Norway"),
        ("FIN", "Finland"),
        ("DEN", "Denmark"),
        ("BEL", "Belgium"),
        ("CHE", "Switzerland"),
        ("NZ", "New Zealand"),
        ("SGP", "Singapore"),
        ("KOR", "South Korea"),
        ("SA", "South Africa"),
        ("ARG", "Argentina"),
        ("COL", "Colombia"),
        ("PHL", "Philippines"),
        ("THA", "Thailand"),
        ("NET", "Netherland"),
        ("IRL", "Ireland"),
        ("AUT", "Austria"),
        ("HUN", "Hungary"),
        ("CZE", "Czech Republic"),
        ("POL", "Poland"),
        ("POR", "Portugal"),
        ("GRC", "Greece"),
        ("TUR", "Turkey"),
        ("UAE", "United Arab Emirates"),
        ("EGY", "Egypt"),
        ("KEN", "Kenya"),
        ("NGA", "Nigeria"),
        ("VNM", "Vietnam"),
        ("MYS", "Malaysia"),
        ("IDN", "Indonesia"),
        ("PK", "Pakistan"),
        ("BD", "Bangladesh"),
        ("BGR", "Bulgaria"),
        ("ROU", "Romania"),
        ("LVA", "Latvia"),
        ("LTU", "Lithuania"),
        ("EST", "Estonia"),
        ("SVK", "Slovakia"),
        ("SVN", "Slovenia"),
        ("CYP", "Cyprus"),
        ("LUX", "Luxembourg"),
        ("MLT", "Malta"),
        ("AND", "Andorra"),
        ("MON", "Monaco"),
        ("SMR", "San Marino"),
        ("VAT", "Vatican City"),
        ("ISL", "Iceland"),
        ("KAZ", "Kazakhstan"),
        ("AZE", "Azerbaijan"),
        ("GEO", "Georgia"),
        ("ARM", "Armenia"),
        ("KIR", "Kiribati"),
        ("TUV", "Tuvalu"),
        ("WSM", "Samoa"),
        ("FJI", "Fiji"),
        ("PNG", "Papua New Guinea"),
        ("TLS", "Timor-Leste"),
    ]

    country = models.CharField(max_length=35, choices=COUNTRIES, default=None)

    def __str__(self):
        return self.country


class Sate(models.Model):
    name = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, null=True)
    state = models.ForeignKey(Sate, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
