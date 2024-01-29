from django.db import models

# Create your models here.
class List(models.Model):
    list_context = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(null=True,blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.list_context
