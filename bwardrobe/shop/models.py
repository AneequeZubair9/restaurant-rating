from django.db import models

# Create your models here.

class Products(models.Model):

        product_id = models.AutoField
        rest_name = models.CharField(max_length=50)
        category=models.CharField(max_length=50, default="")
        address = models.CharField(max_length=50, default="")
        price = models.IntegerField(default=0)
        desc = models.CharField(max_length=300)
        pub_date = models.DateField()
        image = models.ImageField(upload_to='shop/images', default="")
        Rating=models.IntegerField(default=0,max_length=1)

        def __str__(self):
                return self.rest_name


