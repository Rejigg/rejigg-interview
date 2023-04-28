from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    """
    Describes a Business within a Search.
    """

    business = models.ForeignKey(
        "Business", on_delete=models.CASCADE, related_name="leads"
    )
    is_favorite = models.BooleanField(default=False)

class Business(models.Model):
    """
    A Company listed on the Rejigg platform.
    """

    name = models.CharField(max_length=256, default=None, null=True, blank=True)
    description = models.TextField(default=None, null=True, blank=True)

    @property
    def safe_industry(self):
        if self.industries:
            return self.industries.first()
        else:
            return Industry.objects.first()
        
    @property
    def owner(self):
        if self.affiliations.filter(is_owner=True).exists():
            return self.affiliations.filter(is_owner=True).first().person
        elif self.person_set.exists():
            return self.person_set.first()
        else:
            return Person.objects.first()

class Industry(models.Model):
    """
    Businesses may belong to multiple Industries.
    """

    name = models.CharField(max_length=128, blank=True, null=True)
    businesses = models.ManyToManyField("Business", related_name="industries")

class Person(models.Model):
    """
    A real-world Person. Not necessarily a User.
    """
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="person",
    )
    businesses = models.ManyToManyField(Business, through="Affiliation")
    full_name = models.CharField(max_length=128, blank=True, null=True)
    about_me = models.TextField()
    profile_img_url = models.TextField(default=None, null=True, blank=True)


class Affiliation(models.Model):
    """
    Describes a Person's relationship with a Business.
    """

    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="affiliations"
    )
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="affiliations"
    )
    is_owner = models.BooleanField(default=False)

