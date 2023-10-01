from rest_framework.permissions import BasePermission

class IsGameAuthor(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, game):
        
        # Write permissions are only allowed to the owner of the snippet.
        return game.author == request.user