from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import (
    GameDetailSerializer, GameListSerializer,
    StepListSerializer, StepDetailSerializer,
    ScenarioListSerializer, ScenarioDetailSerializer, 
    ScenarioNodeListSerializer, ScenarioNodeDetailSerializer,
    ClueListSerializer, ClueDetailSerializer
    )
from .models import Game, ScenarioNode, Step, Scenario, Clue
from .permissions import IsGameAuthor
# Create your views here.

class MultipleSerializerMixin:
    # Un mixin est une classe qui ne fonctionne pas de façon autonome
    # Elle permet d'ajouter des fonctionnalités aux classes qui les étendent

    detail_serializer_class = None

    def get_serializer_class(self):
        # Notre mixin détermine quel serializer à utiliser
        # même si elle ne sait pas ce que c'est ni comment l'utiliser
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            # Si l'action demandée est le détail alors nous retournons le serializer de détail
            return self.detail_serializer_class
        return super().get_serializer_class()
    

class GameViewSet(MultipleSerializerMixin,ModelViewSet):
    """Return games created by request user"""
    #Works only with detailed view, now that there is a filter, useless or not ? To be tester for all objects
    permission_classes = [IsGameAuthor]

    serializer_class = GameListSerializer

    detail_serializer_class = GameDetailSerializer

    def get_queryset(self):
        
        queryset = Game.objects.filter(author=self.request.user)
        return queryset
    
class StepViewSet(MultipleSerializerMixin,ModelViewSet):

    serializer_class = StepListSerializer

    detail_serializer_class = StepDetailSerializer

    def get_queryset(self):
        
        queryset = Step.objects.filter(game__author=self.request.user)
        return queryset
    
class ScenarioViewSet(MultipleSerializerMixin,ModelViewSet):

    serializer_class = ScenarioListSerializer

    detail_serializer_class = ScenarioDetailSerializer

    def get_queryset(self):
        
        queryset = Scenario.objects.filter(game__author=self.request.user)
        return queryset
    
class ScenarioNodeViewSet(MultipleSerializerMixin,ModelViewSet):

    serializer_class = ScenarioNodeListSerializer

    detail_serializer_class = ScenarioNodeDetailSerializer

    def get_queryset(self):
        
        queryset = ScenarioNode.objects.filter(scenario__game__author=self.request.user)
        return queryset
    
class ClueViewSet(MultipleSerializerMixin,ModelViewSet):

    serializer_class = ClueListSerializer

    detail_serializer_class = ClueDetailSerializer

    def get_queryset(self):
        
        queryset = Clue.objects.filter(step__game__author=self.request.user)
        return queryset