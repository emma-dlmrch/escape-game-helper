from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from .serializers import (
    GameDetailSerializer, GameListSerializer,
    StepListSerializer, StepDetailSerializer,
    ScenarioListSerializer, ScenarioDetailSerializer, 
    ScenarioNodeListSerializer, ScenarioNodeDetailSerializer,
    ClueListSerializer, ClueDetailSerializer, ScenarioNodeTreeSerializer, ScenarioPlaySerializer, StepPlaySerializer, ScenarioNodePlaySerializer
    )
from .models import Game, ScenarioNode, Step, Scenario, Clue
from .permissions import IsGameAuthor, IsScenarioAuthor, IsStepAuthor, IsClueAuthor, IsScenarioNodeAuthor
import logging

class MultipleSerializerMixin:
    # Un mixin est une classe qui ne fonctionne pas de façon autonome
    # Elle permet d'ajouter des fonctionnalités aux classes qui les étendent

    detail_serializer_class = None

    def get_serializer_class(self):
        # Notre mixin détermine quel serializer à utiliser
        # même si elle ne sait pas ce que c'est ni comment l'utiliser
        if (self.action == 'retrieve' or self.action == 'update' ) and self.detail_serializer_class is not None:
            # Si l'action demandée est le détail alors nous retournons le serializer de détail
            return self.detail_serializer_class
        return super().get_serializer_class()
    

class GameViewSet(MultipleSerializerMixin,ModelViewSet):
    """Return games created by request user"""
    #Works only with detailed view, test what happens for modif and deletion
    permission_classes = [IsGameAuthor]

    pagination_class = None #added 

    serializer_class = GameListSerializer

    detail_serializer_class = GameDetailSerializer

    def get_queryset(self):
        
        queryset = Game.objects.filter(author=self.request.user) #commented for testing purposes
        # queryset = Game.objects.all()
        return queryset
    
# Issue with detailed view, try to refactor, does not solve the issue
# class GameListAPIView(APIView):
 
#     def get(self, *args, **kwargs):
#         games = Game.objects.filter(author=self.request.user)
#         serializer = GameListSerializer(games, many=True)
#         return Response(serializer.data)

# class GameDetailsAPIView(APIView):

#     def get_object(self, game_id):
#         try:
#             return Game.objects.get(id = game_id)
#         except Game.DoesNotExist:
#             raise Http404

#     def get(self, request, game_id, format=None):
#         game = self.get_object(game_id)
#         serializer = GameDetailSerializer(game)
#         return Response(serializer.data)
    
class StepViewSet(MultipleSerializerMixin,ModelViewSet):

    permission_classes = [IsStepAuthor]

    serializer_class = StepListSerializer

    detail_serializer_class = StepDetailSerializer

    def get_queryset(self):
        #queryset = Step.objects.all()
        queryset = Step.objects.filter(game__author=self.request.user)
        return queryset
    
class ScenarioViewSet(MultipleSerializerMixin,ModelViewSet):

    permission_classes = [IsScenarioAuthor]

    serializer_class = ScenarioListSerializer

    detail_serializer_class = ScenarioDetailSerializer

    def get_queryset(self):
        #queryset = Scenario.objects.all()
        queryset = Scenario.objects.filter(game__author=self.request.user)
        return queryset
    
class ScenarioNodeViewSet(MultipleSerializerMixin,ModelViewSet):

    permission_classes = [IsScenarioNodeAuthor]

    serializer_class = ScenarioNodeListSerializer

    detail_serializer_class = ScenarioNodeDetailSerializer #We can come back to the details serializer now that treeSerializer is called at Scenario level
    #detail_serializer_class = ScenarioNodeTreeSerializer

    def get_queryset(self):
        
        queryset = ScenarioNode.objects.filter(scenario__game__author=self.request.user)
        # queryset = ScenarioNode.objects.all()
        return queryset

    
class ClueViewSet(MultipleSerializerMixin,ModelViewSet):

    permission_classes = [IsClueAuthor]

    serializer_class = ClueListSerializer

    detail_serializer_class = ClueDetailSerializer

    def get_queryset(self):
        
        queryset = Clue.objects.filter(step__game__author=self.request.user)
        return queryset
    


    
class GamePlayViewSet(ReadOnlyModelViewSet):

    serializer_class = GameListSerializer

    def get_queryset(self):
        
        queryset = Game.objects.all()
        return queryset
    
class ScenarioPlayViewSet(ReadOnlyModelViewSet):

    serializer_class = ScenarioPlaySerializer

    def get_queryset(self):
        
        queryset = Scenario.objects.all()
        return queryset
    
class StepPlayViewSet(ReadOnlyModelViewSet):

    serializer_class = StepPlaySerializer

    def get_queryset(self):
        
        queryset = Step.objects.all()
        return queryset

class ScenarioNodePlayViewSet(ReadOnlyModelViewSet):

    serializer_class = ScenarioNodePlaySerializer

    def get_queryset(self):
        
        queryset = ScenarioNode.objects.all()
        return queryset
    
    @action(detail=False, methods=['post'], url_path="answer/(?P<node_id>\d+)", url_name="answer")
    def check_answer(self, request, node_id):
        queryset = ScenarioNode.objects.filter(id=node_id).get()
        answer = queryset.step.answer.strip().lower()
        proposition = request.data.get("answer").strip().lower()
        if proposition == answer:
            next_nodes_query = ScenarioNode.objects.filter(parent_node=node_id)
            serializer = ScenarioNodePlaySerializer(next_nodes_query, many=True)
            return Response(serializer.data)
        else:
            return Response(data={'message':False})
    
class CluePlayViewSet(ReadOnlyModelViewSet):

    serializer_class = ClueDetailSerializer

    def get_queryset(self):
        
        queryset = Clue.objects.all()
        return queryset