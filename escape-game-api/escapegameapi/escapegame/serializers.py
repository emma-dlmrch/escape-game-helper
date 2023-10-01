from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Scenario, Game, ScenarioNode, Clue, Step

#ToDO: Implement unit tests
#Todo: remove scenarios, useless for game list
class GameSerializer(ModelSerializer):

    scenarios = serializers.SerializerMethodField()
    
    class Meta:
        model = Game
        fields = ['id', 'name', 'description', 'date_created', 'date_updated', 'scenarios']
    
    def get_scenarios(self, instance):
        
        queryset = instance.scenarios.all()
        serializer = ScenarioSerializer(queryset, many=True)
        return serializer.data


class GameDetailSerializer(ModelSerializer):

    scenarios = serializers.SerializerMethodField()

    steps = serializers.SerializerMethodField()
    
    class Meta:
        model = Game
        fields = ['id', 'name', 'description', 'date_created', 'date_updated', 'steps', 'scenarios']
    
        
    def get_scenarios(self, instance):
        
        queryset = instance.scenarios.all()
        serializer = ScenarioSerializer(queryset, many=True)
        return serializer.data
    
        
    def get_steps(self, instance):
        
        queryset = instance.steps.all()
        serializer = StepSerializer(queryset, many=True)
        return serializer.data


class StepSerializer(ModelSerializer):
    
    class Meta:
        model = Step
        fields = ['id', 'game', 'title']

class StepDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Step
        fields = ['id', 'game', 'title', 'text', 'answer']


class ScenarioSerializer(ModelSerializer):
    
    class Meta:
        model = Scenario
        fields = ['id', 'name']

class ScenarioDetailSerializer(ModelSerializer):

    scenario_nodes = serializers.SerializerMethodField()
    
    class Meta:
        model = Scenario
        fields = ['id', 'name', 'scenario_nodes']
    
    def get_scenario_nodes(self, instance):
        
        queryset = instance.scenario_nodes.all()
        serializer = ScenarioNodeSerializer(queryset, many=True)
        return serializer.data


class ScenarioNodeSerializer(ModelSerializer):

    step_title = serializers.SerializerMethodField()
    
    class Meta:
        model = ScenarioNode
        fields = ['id','scenario', 'step', 'step_title', 'parent_node']
    
    def get_step_title(self, instance):

        return instance.step.title

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
        serializer = ScenarioNodeSerializer(queryset, many=True)
        return serializer.data

class ClueSerializer(ModelSerializer):

    class Meta:
        model = Clue
        fields = ['id','step', 'title', 'text']

class ClueDetailSerializer(ModelSerializer):

    class Meta:
        model = Clue
        fields = ['id','step', 'title', 'text']