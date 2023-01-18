from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField("Title", max_length=150)
    description = models.CharField("Description", max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add= True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    File = models.FileField("File", upload_to='Todo', blank=True, null=True)
    complete = models.BooleanField("Complete", default=False)

    def __str__(self):
        return self.name


    