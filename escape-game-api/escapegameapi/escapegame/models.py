from django.db import models

# Create your models here.

class Game(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Step(models.Model):
    """Game step, either a riddle or only text if no answer is expected"""
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=5000)
    #image = models.ImageField(verbose_name='Game step picture')
    answer = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.title 


class Clue(models.Model):

    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.title 

class GameBranch(models.Model):

    name = models.CharField(max_length=255)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    #to add in TU
    def list_ordered_steps(self):
        """Return list of ordered steps for a specific game branch"""
        return self.game_branch_entrys.order_by('rank')
       
    def __str__(self):
        return self.name 

class GameBranchEntry(models.Model):

    game_branch = models.ForeignKey(GameBranch, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    rank = models.IntegerField()

    class Meta:
        unique_together = ('game_branch', 'rank',)

    def __str__(self):
        return (self.game_branch.name + " - " + self.step.title + " - " + str(self.rank))

