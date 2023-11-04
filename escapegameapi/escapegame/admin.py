from django.contrib import admin

from .models import Game, Clue, Step, Scenario, ScenarioNode

#to be removed when deployed
admin.site.register(Game)
admin.site.register(ScenarioNode)
admin.site.register(Scenario)
admin.site.register(Clue)
admin.site.register(Step)

