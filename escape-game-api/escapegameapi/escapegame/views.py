from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import (
    GameSerializer, GameDetailSerializer, 
    StepSerializer, StepDetailSerializer,
    ScenarioSerializer, ScenarioDetailSerializer, 
    ScenarioNodeSerializer, ScenarioNodeDetailSerializer,
    ClueSerializer, ClueDetailSerializer
    )
from .models import Game, ScenarioNode, Step, Scenario, Clue
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

    serializer_class = GameSerializer

    detail_serializer_class = GameDetailSerializer

    #TO DO there should be a filter for user
    def get_queryset(self):
        
        queryset = Game.objects.all()
        return queryset
    
class StepViewSet(MultipleSerializerMixin,ModelViewSet):

    serializer_class = StepSerializer

    detail_serializer_class = StepDetailSerializer

    #TO DO there should be a filter for user
    def get_queryset(self):
        
        queryset = Step.objects.all()
        return queryset
    
class ScenarioViewSet(MultipleSerializerMixin,ModelViewSet):

    serializer_class = ScenarioSerializer

    detail_serializer_class = ScenarioDetailSerializer

    #TO DO there should be a filter for user
    def get_queryset(self):
        
        queryset = Scenario.objects.all()
        return queryset
    
class ScenarioNodeViewSet(MultipleSerializerMixin,ModelViewSet):

    serializer_class = ScenarioNodeSerializer

    detail_serializer_class = ScenarioNodeDetailSerializer

    #TO DO there should be a filter for user
    def get_queryset(self):
        
        queryset = ScenarioNode.objects.all()
        return queryset
    
class ClueViewSet(MultipleSerializerMixin,ModelViewSet):

    serializer_class = ClueSerializer

    detail_serializer_class = ClueDetailSerializer

    #TO DO there should be a filter for user
    def get_queryset(self):
        
        queryset = Clue.objects.all()
        return queryset