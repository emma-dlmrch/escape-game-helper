from rest_framework.permissions import BasePermission

class IsGameAuthor(BasePermission):
    """
    Custom permission to only allow owners to edit resource.
    """
    def has_object_permission(self, request, view, game):
        
        return game.author == request.user