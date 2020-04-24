from django.db import models

PRIORITY = (("danger", "high"), ("info", "normal"), ("success", "low"))

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()  # CharFieldより長い文章を使う場合
    priority = models.CharField(max_length = 50, choices = PRIORITY)
    duedate = models.DateField()

    def __str__(self):
        return self.title

