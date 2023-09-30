from django.contrib import admin

from .models import GameBranch, Game, GameBranchEntry, Clue, Step

#to be removed when deployed
admin.site.register(Game)
admin.site.register(GameBranchEntry)
admin.site.register(GameBranch)
admin.site.register(Clue)
admin.site.register(Step)

