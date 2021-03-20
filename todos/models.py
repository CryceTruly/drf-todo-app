from django.db import models
from helpers.models import BaseModel
from authentication.models import User

class Todo(BaseModel):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)



