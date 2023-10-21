from rest_framework.permissions import BasePermission
import logging

class IsGameAuthor(BasePermission):
    """
    Custom permission to only allow owners to edit resource.
    """
    def has_object_permission(self, request, view, game):
        
        return game.author.id == request.user.id
    
class IsScenarioAuthor(BasePermission):
    """
    Custom permission to only allow owners to edit resource.
    """

    def has_object_permission(self, request, view, scenario):
        
        return scenario.game.author.id == request.user.id
    
class IsStepAuthor(BasePermission):
    """
    Custom permission to only allow owners to edit resource.
    """
    def has_object_permission(self, request, view, step):
        
        return step.game.author.id == request.user.id
    
class IsClueAuthor(BasePermission):
    """
    Custom permission to only allow owners to edit resource.
    """
    def has_object_permission(self, request, view, clue):
        
        return clue.step.game.author.id == request.user.id
    
class IsScenarioNodeAuthor(BasePermission):
    """
    Custom permission to only allow owners to edit resource.
    """
    def has_object_permission(self, request, view, node):

        return node.scenario.game.author.id == request.user.id