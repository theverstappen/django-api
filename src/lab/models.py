from django.db import models

# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    link = models.URLField(null=True)
    file = models.FileField(blank=False, null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.description, self.file.name)