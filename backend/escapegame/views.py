import logging
import re

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from .serializers import (
    GameDetailSerializer, GameListSerializer, ImageSerializer,
    StepListSerializer, StepDetailSerializer,
    ScenarioListSerializer, ScenarioDetailSerializer, 
    ScenarioNodeListSerializer, ScenarioNodeDetailSerializer,
    ClueListSerializer, ClueDetailSerializer, ScenarioPlaySerializer, StepPlaySerializer, ScenarioNodePlaySerializer
    )
from .models import Game, ScenarioNode, Step, Scenario, Clue
from .permissions import IsGameAuthor, IsScenarioAuthor, IsStepAuthor, IsClueAuthor, IsScenarioNodeAuthor


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if (self.action == 'retrieve' or self.action == 'update' ) and self.detail_serializer_class is not None:
            return self.detail_serializer_class

        return super().get_serializer_class()
    

class GameViewSet(MultipleSerializerMixin,ModelViewSet):
    """Return games created by request user"""

    permission_classes = [IsGameAuthor]
    pagination_class = None 
    serializer_class = GameListSerializer
    detail_serializer_class = GameDetailSerializer

    def get_queryset(self):
        queryset = Game.objects.filter(author=self.request.user)
        return queryset

    
class StepViewSet(MultipleSerializerMixin,ModelViewSet):
    permission_classes = [IsStepAuthor]
    serializer_class = StepListSerializer
    detail_serializer_class = StepDetailSerializer

    def get_queryset(self):
        queryset = Step.objects.filter(game__author=self.request.user)
        return queryset

    
class ScenarioViewSet(MultipleSerializerMixin,ModelViewSet):
    permission_classes = [IsScenarioAuthor]
    serializer_class = ScenarioListSerializer
    detail_serializer_class = ScenarioDetailSerializer

    def get_queryset(self):
        queryset = Scenario.objects.filter(game__author=self.request.user)
        return queryset
    

class ScenarioNodeViewSet(MultipleSerializerMixin,ModelViewSet):
    permission_classes = [IsScenarioNodeAuthor]
    serializer_class = ScenarioNodeListSerializer
    detail_serializer_class = ScenarioNodeDetailSerializer

    def get_queryset(self):
        queryset = ScenarioNode.objects.filter(scenario__game__author=self.request.user)
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
    lookup_field = 'slug'

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
    

    @staticmethod
    def _subst_char(substr):
        subst_chars = {
            "à": "a", "â": "a", "ä": "a",
            "é": "e", "ê": "e", "è": "e",
            "î": "i", "ï": "i",
            "ô": "o", "ö": "o", 
            "û": "u", "ù": "u", "ü": "u",
            "ç": "c",
        }
        match = substr.group(0)
        if match in subst_chars:
            return subst_chars[match]

        return ""


    @staticmethod
    def _normalize(text):
        return re.sub(r'[\Wàâäéèêîïôöûüùç]', ScenarioNodePlayViewSet._subst_char, text.lower())


    @action(detail=False, methods=['post'], url_path="answer/(?P<node_id>\d+)", url_name="answer")
    def check_answer(self, request, node_id):
        queryset = ScenarioNode.objects.filter(id=node_id).get()
        answer = ScenarioNodePlayViewSet._normalize(queryset.step.answer)
        proposition = ScenarioNodePlayViewSet._normalize(request.data.get("answer"))
        if proposition == answer:
            next_nodes_query = ScenarioNode.objects.filter(parent_node=node_id)
            serializer = ScenarioNodePlaySerializer(next_nodes_query, many=True)
            return Response(serializer.data)

        return Response(data={'message':False})
    

class CluePlayViewSet(ReadOnlyModelViewSet):
    serializer_class = ClueDetailSerializer

    def get_queryset(self):
        queryset = Clue.objects.all()
        return queryset


class ImageView(APIView):
    def post(self, request, format=None):
        context = {'request': request}
        serializer = ImageSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

