from django.db import models
from SignLog.models import CustomUser
# Create your models here.


# Create your models here.
class Worlds(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    progress_point = models.IntegerField(default=0)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    extra_note = models.TextField(blank=True)
    is_pathbreaking = models.BooleanField(default=False)
    task_point = models.IntegerField(default=0)
    

    def safe_description(self):
        from django.utils.safestring import mark_safe
        return mark_safe(self.description)

class World_Tasks(models.Model):
    world = models.ForeignKey(Worlds, on_delete=models.CASCADE)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)