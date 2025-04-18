from django.db import models

class Bien(models.Model):
    TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
        ('office', 'Office'),
    ]

    STATUS_CHOICES = [
        ('for_sale', 'For Sale'),
        ('for_rent', 'For Rent'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
    ]

    title = models.CharField(max_length=255)
    address = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.DecimalField(max_digits=6, decimal_places=2)
    bedroom = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='biens_photos/', blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)  # This will automatically update the field on each save
    city = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
class Photo(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='biens_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image of {self.bien.title}"
