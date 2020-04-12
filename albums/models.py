from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Album(models.Model):
    title = models.CharField(max_length=50)
    description =  models.TextField(blank=True)
    url = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    categories = models.ManyToManyField(Category, blank=True)
    private = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def start_date_pretty(self):
        return self.start_date.strftime('%b %e %Y')

    def end_date_pretty(self):
        return self.end_date.strftime('%b %e %Y')
