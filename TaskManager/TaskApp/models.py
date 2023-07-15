from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)
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
    due_date = models.DateTimeField()
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