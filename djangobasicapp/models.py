from django.db import models
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField


class Department(models.Model):
    department_name = models.CharField(max_length=30)
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.department_name


class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name


class Employee(models.Model):
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
    phone_number = PhoneNumberField()
    department = models.ForeignKey(
        Department, default=0, on_delete=models.CASCADE)
    destination_country = models.ForeignKey(
        Country, default="", on_delete=models.CASCADE)

    def __str__(self):
        return "name" + " " + self.fisrt_name + " "+"|" + "country" + " " + self.get_country_display()


class UserRegistration(models.Model):
    GENDER = [
        ("FE", "Female"),
        ("MA", "Male"),
    ]

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

    username = models.CharField(max_length=30, validators=[
                                MinLengthValidator(5)], verbose_name='User Name')
    password = models.CharField(max_length=15, validators=[
                                MinLengthValidator(5)], verbose_name='Password')
    confirm_password = models.CharField(
        max_length=15, validators=[MinLengthValidator(5)], verbose_name='Confirm Password')
    gender = models.CharField(
        max_length=10, choices=GENDER, default=None, verbose_name='Gender')
    country = models.CharField(
        max_length=35, choices=COUNTRIES, default=None, verbose_name='Country')
    brith_date = models.DateField(default=None, verbose_name='Date of Birth')
    email = models.EmailField(default="", max_length=50, verbose_name='Email')
