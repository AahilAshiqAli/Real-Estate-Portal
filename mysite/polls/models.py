from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length = 122) 
    password = models.CharField(max_length = 12)
    phone = models.CharField(max_length = 12)
    address = models.CharField(max_length = 222)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zipcode = models.CharField(max_length = 5)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date = models.DateField()
     
    def __str__(self):
        return self.email.split('@')[0]
    
class EliteEstateRoyce(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    baths = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elite_estate_royce'