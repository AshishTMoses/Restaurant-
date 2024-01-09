from django.db import models

# Create your models here.


class RestaurantDb(models.Model):
    Rest_name = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Star_rating = models.IntegerField(null=True, blank=True)
    Rate = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Contact_No = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="Restaurant images", null=True, blank=True)


class ListRestDb(models.Model):
    Rest_list = models.CharField(max_length=100, null=True, blank=True)
    Rest_type = models.CharField(max_length=100, null=True, blank=True)
    Branches = models.CharField(max_length=100, null=True, blank=True)
    Cost = models.IntegerField(null=True, blank=True)
    Review = models.CharField(max_length=100, null=True, blank=True)
    Res_img = models.ImageField(upload_to="Image",null=True, blank=True)

