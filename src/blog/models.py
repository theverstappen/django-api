from django.db import models
from django.utils import timezone
class Posts(models.Model):
    title   = models.CharField(max_length=250, null=False)
    description   = models.CharField(max_length=250, null=True)
    date = models.DateField(default=timezone.now())
    content = models.TextField(null=False)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.title, self.date, self.description, self.content)