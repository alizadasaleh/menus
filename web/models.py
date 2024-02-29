from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True) 
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_name = models.CharField(max_length=100)  

    def get_absolute_url(self):
        if self.name:
            return reverse(self.name)
        return self.url

    def __str__(self):
        return self.title
