from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authentication.models import User

from .models import Scenario, Game, ScenarioNode, Clue, Step

#ToDO: Implement unit tests
#Todo: remove scenarios, useless for game list
class GameListSerializer(ModelSerializer):

    scenarios = serializers.SerializerMethodField()
    
    class Meta:
        model = Game
        fields = ['id', 'author', 'name', 'description', 'date_created', 'date_updated', 'scenarios']
    
    def get_scenarios(self, instance):
        
        queryset = instance.scenarios.all()
        serializer = ScenarioListSerializer(queryset, many=True)
        return serializer.data


class GameDetailSerializer(ModelSerializer):

    scenarios = serializers.SerializerMethodField()

    steps = serializers.SerializerMethodField()
    
    class Meta:
        model = Game
        fields = ['id', 'author', 'name', 'description', 'date_created', 'date_updated', 'steps', 'scenarios']
    
        
    def get_scenarios(self, instance):
        
        queryset = instance.scenarios.all()
        serializer = ScenarioListSerializer(queryset, many=True)
        return serializer.data
    
        
    def get_steps(self, instance):
        
        queryset = instance.steps.all()
        serializer = StepListSerializer(queryset, many=True)
        return serializer.data


class StepListSerializer(ModelSerializer):
    
    class Meta:
        model = Step
        fields = ['id', 'game', 'title']

class StepDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Step
        fields = ['id', 'game', 'title', 'text', 'answer']


class ScenarioListSerializer(ModelSerializer):
    
    class Meta:
        model = Scenario
        fields = ['id', 'name', 'game']
    


class ScenarioDetailSerializer(ModelSerializer):

    scenario_nodes = serializers.SerializerMethodField()
    
    class Meta:
        model = Scenario
        fields = ['id', 'name', 'game', 'scenario_nodes']
    
    def get_scenario_nodes(self, instance):
        # that's ok for a list, now we want a tree view from first parent node
        # queryset = instance.scenario_nodes.all()
        # serializer = ScenarioNodeListSerializer(queryset, many=True)
        # return serializer.data
        queryset = instance.scenario_nodes.exclude(parent_node__isnull=False)
        serializer = ScenarioNodeTreeSerializer(queryset, many=True)
        return serializer.data


class ScenarioNodeListSerializer(ModelSerializer):

    step_title = serializers.SerializerMethodField()
    parent_node_title = serializers.SerializerMethodField()
    
    class Meta:
        model = ScenarioNode
        fields = ['id','scenario', 'step', 'step_title', 'parent_node', 'parent_node_title']
    
    def get_step_title(self, instance):

        return instance.step.title
    
    def get_parent_node_title(self, instance):  
        if instance.parent_node is not None:
            parent_node = ScenarioNode.objects.get(id=instance.parent_node.id)
            return parent_node.step.title
        return 'root'

#test a serializer that calls itself -> OK, now how to send this with first node ?    
class ScenarioNodeTreeSerializer(ModelSerializer):
    step_title = serializers.SerializerMethodField()
    child_nodes = serializers.SerializerMethodField()
    
    class Meta:
        model = ScenarioNode
        fields = ['id','scenario', 'step', 'step_title', 'parent_node', 'child_nodes']
    
    def get_step_title(self, instance):

        return instance.step.title
    
    def get_child_nodes(self, instance):
        queryset = ScenarioNode.objects.filter(parent_node= instance)
        serializer = ScenarioNodeTreeSerializer(queryset, many=True)
        return serializer.data


class ScenarioNodeDetailSerializer(ModelSerializer):

    step_title = serializers.SerializerMethodField()
    child_nodes = serializers.SerializerMethodField()
    
    class Meta:
        model = ScenarioNode
        fields = ['id','scenario', 'step', 'step_title', 'parent_node', 'child_nodes']
    
    def get_step_title(self, instance):

        return instance.step.title
    
    def get_child_nodes(self, instance):
        queryset = ScenarioNode.objects.filter(parent_node= instance)
        serializer = ScenarioNodeListSerializer(queryset, many=True)
        return serializer.data

class ClueListSerializer(ModelSerializer):

    class Meta:
        model = Clue
        fields = ['id','step', 'title', 'text']

class ClueDetailSerializer(ModelSerializer):

    class Meta:
        model = Clue
        fields = ['id','step', 'title', 'text']
