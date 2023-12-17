from django.db import models

# Create your models here.
class Pattern(models.Model):
    work_time = models.IntegerField(default=25)
    rest_time = models.IntegerField(default=5)

    def __str__(self):
        return f"work: {self.work_time} & rest: {self.rest_time} schedule"
