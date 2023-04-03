from django.db import models

class Faq(models.Model):
    name = models.TextField()
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField()
    date = models.DateField()
    author = models.ForeignKey("Author", on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Social(models.Model):
    url = models.URLField()
    icon = models.FileField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30)
    value = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    
