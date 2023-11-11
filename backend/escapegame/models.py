import os
from uuid import uuid4
from django.db import models
from django.conf import settings
from authentication.models import User
from django.core.files.storage import FileSystemStorage
from rest_framework.serializers import ModelSerializer, ValidationError

# Create your models here.

class Game(models.Model):

    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Step(models.Model):
    """Game step, either a riddle or only text if no answer is expected"""
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='steps')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=5000)
    answer = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.title 


class Clue(models.Model):

    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='clues')
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.title 

class Scenario(models.Model):
    """A scenario is the order of steps/riddles. Scenario can be ramificated"""

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=128)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='scenarios')
       
    def __str__(self):
        return self.name 
    
class ScenarioNode(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='scenario_nodes')
    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='steps')
    parent_node = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.parent_node:
            return self.scenario.name + " : " + self.parent_node.step.title + " -> " + self.step.title
        return self.scenario.name + ", start : "  + self.step.title
        

def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1].lower()
    filename = '{}-{}.{}'.format(instance.game.id, uuid4().hex[0:10], ext)
    return os.path.join(upload_to, filename)

class Image(models.Model):    
    upload_storage = FileSystemStorage(location=settings.STORAGE_DIR, base_url='/uploads')
    # author is redundant now that game is an attribute
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=path_and_rename, storage=upload_storage) 
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='images')
