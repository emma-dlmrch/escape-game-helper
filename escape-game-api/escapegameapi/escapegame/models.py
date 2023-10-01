from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

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
    #image = models.ImageField(verbose_name='Game step picture')
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

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='scenarios')

    # if steps were linear
    # def list_ordered_steps(self):
    #     """Return list of ordered steps for a specific game branch"""
    #     return self.game_branch_entrys.order_by('rank')

       
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
        
#if steps were linear
# class GameBranchEntry(models.Model):

#     game_branch = models.ForeignKey(GameBranch, on_delete=models.CASCADE)
#     step = models.ForeignKey(Step, on_delete=models.CASCADE)
#     rank = models.IntegerField()

#     class Meta:
#         unique_together = ('game_branch', 'rank',)

#     def __str__(self):
#         return (self.game_branch.name + " - " + self.step.title + " - " + str(self.rank))

