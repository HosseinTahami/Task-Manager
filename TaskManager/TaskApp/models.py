from django.db import models
import datetime
from django.conf import settings
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)
    img = models.ImageField(
        upload_to = 'images/',
        default='/images/cat_default.png'
        )
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=225)
    def __str__(self):
        return self.name

class Task(models.Model):
    TASK_FINISHED = 'F'
    TASK_ONGOING = 'O'
    TASK_STATUS_CHOICES =[
        ('F', TASK_FINISHED),
        ('O', TASK_ONGOING)
    ]
    title = models.CharField(max_length=225)
    description = models.TextField()
    default_date = datetime.datetime.today() + datetime.timedelta(days=1)
    due_date = models.DateTimeField(default=default_date)
    status = models.CharField(
        max_length=1,
        choices=TASK_STATUS_CHOICES,
        default=TASK_ONGOING
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
        )
    tags = models.ManyToManyField(Tag)
    # file = models.FileField(
    #     upload_to='images/',
    #     default='task_default.png'
    #     )
    file = models.FileField(upload_to='images/', blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.file:
    #         self.file = 'images/task_default.png'
    #     super().save(*args, **kwargs)
