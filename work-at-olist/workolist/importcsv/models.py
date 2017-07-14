from django.db import models

class Channel(models.Model):
    """
    Class responsible for creating the data model of objects reallocated to the Channels
    """
    #Fields models/object
    name = models.CharField('Name Channel:', max_length=20, unique=True, blank=False)
    description = models.CharField('Description:',max_length=50, null=True, blank=True)
    category_channel = models.ManyToManyField(
        'Category',
    )
    #return a string reference to name the object
    def __str__(self):
        return self.name
    #Metadata the model
    class Meta:
        ordering = ['name']
        get_latest_by = ['id']

class Category(models.Model):
    """
    Class responsible for creating the data model of the objects that are reallocated to Categories
    """
    #Fields models/object
    name = models.CharField('Name:', max_length=20, blank=False)
    description = models.CharField('Description:', max_length=50, null=True, blank=True)
    sub_category = models.ManyToManyField(
        'SubCategory',
    )
    #return a string reference to name the object
    def __str__(self):
        return self.name
    #Metadata the model
    class Meta:
        ordering = ['name']
        get_latest_by = ['id']

class SubCategory(models.Model):
    """
    Class responsible for creating the data model of objects that are reallocated to Sub-categories
    """
    #Fields models/object
    name = models.CharField('Name SubCategory:', max_length=20, default=" ", blank=False)
    description = models.CharField('Description:',max_length=50, null=True, blank=True)

    #return a string reference to name the object
    def __str__(self):
        return self.name
    #Metadata the model
    class Meta:
        ordering = ['name']
        get_latest_by = ['id']
