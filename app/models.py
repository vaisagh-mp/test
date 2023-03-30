from django.db import models


class Categories(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class customers(models.Model):
    c_name=models.CharField(max_length=50)

    def __str__(self):
        return self.c_name
    
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(null=True,blank=True)
    prodapp=models.TextField(null=True,blank=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to='product')
    customers=models.ManyToManyField(customers)

    def __str__(self):
        return self.title
    


    