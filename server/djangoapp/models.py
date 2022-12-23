import datetime
from django.db import models
from django.utils.timezone import now

# Create your models here.

# Create a Car Make model 'class CarMake(models.Model)':
class CarMake(models.Model):
    # - Name
    name = models.CharField(null=False, max_length=50)
    # - Description
    description = models.CharField(null=True, max_length=500)
    # - Any other fields you would like to include in car make model
    # - __str__ method to print a car make object
    def __str__(self):
        return self.name

# Create a Car Model model 'class CarModel(models.Model):':
class CarModel(models.Model):
    # - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    # - Name
    name = models.CharField(null=False, max_length=50)
    # - Dealer id, used to refer a dealer created in cloudant database
    dealer_id = models.IntegerField(null=True)
    # - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    SPORT = "Sport"
    COUPE = "Coupe"
    OTHER = "Other"
    CAR_CHOICES = [(SEDAN, "Sedan"), (SUV, "SUV"), (WAGON, "Station wagon"), (SPORT, "Sports Car"),
                   (COUPE, "Coupe"), (OTHER, 'Other')]
    model_type = models.CharField(
        null=False, max_length=15, choices=CAR_CHOICES, default=SEDAN)
    # - Year (DateField)
    YEAR_CHOICES = []
    for r in range(1969, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    year = models.IntegerField(
        ('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    # - Any other fields you would like to include in car model
    # - __str__ method to print a car make object
    def __str__(self):
        return self.name + ", " + str(self.year) + ", " + self.model_type


# Create a plain Python class 'CarDealer' to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, state, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer full state name
        self.state = state
        # Dealer zip
        self.zip = zip
        self.idx = 0

    def __str__(self):
        return self.full_name + ", " + self.state


# Create a plain Python class 'DealerReview' to hold review data
class DealerReview:
    def __init__(self, dealership, id, name, purchase, review, car_make=None, car_model=None, car_year=None, purchase_date=None, sentiment="neutral"):
        # Required attributes
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        # Optional attributes
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id
        
    def __str__(self):
        return "Reviewer: " + self.name + " Review: " + self.review
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)

# Create a plain Python class 'ReviewPost' to post review data
class ReviewPost:

    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)
