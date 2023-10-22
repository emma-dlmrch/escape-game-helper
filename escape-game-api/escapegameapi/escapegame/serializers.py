from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers
from authentication.models import User

from .models import Scenario, Game, ScenarioNode, Clue, Step
import logging

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

    def validate(self, data):
        user = self.context['request'].user
        if data['author'].id !=  user.id:
            raise ValidationError('Creation not allowed: User Id not consistent with requester')
        return data


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

    def validate(self, data):
        user = self.context['request'].user
        if data['game'].author.id !=  user.id:
            raise ValidationError('Creation not allowed: game not owned by requester')
        return data

class StepDetailSerializer(ModelSerializer):
    
    clues = serializers.SerializerMethodField()

    class Meta:
        model = Step
        fields = ['id', 'game', 'title', 'text', 'answer', 'clues']

    def get_clues(self, instance):
        queryset = instance.clues.all()
        serializer = ClueListSerializer(queryset, many=True)
        return serializer.data


class ScenarioListSerializer(ModelSerializer):
    
    class Meta:
        model = Scenario
        fields = ['id', 'name', 'game']
    
    def validate(self, data):

        user = self.context['request'].user
        if data['game'].author.id !=  user.id:
            raise ValidationError('Creation not allowed: game not owned by requester')
        return data
    


class ScenarioDetailSerializer(ModelSerializer):

    scenario_nodes = serializers.SerializerMethodField()
    scenario_nodes_flat = serializers.SerializerMethodField()
    
    class Meta:
        model = Scenario
        fields = ['id', 'name', 'game', 'scenario_nodes', 'scenario_nodes_flat'] #I gave up trying to flatten the data at frond end level
    
    def get_scenario_nodes(self, instance):
        queryset = instance.scenario_nodes.exclude(parent_node__isnull=False)
        serializer = ScenarioNodeTreeSerializer(queryset, many=True)
        return serializer.data

    def get_scenario_nodes_flat(self, instance):
        queryset = instance.scenario_nodes.all()
        serializer = ScenarioNodeListSerializer(queryset, many=True)
        return serializer.data
    


class ScenarioNodeListSerializer(ModelSerializer):

    label = serializers.SerializerMethodField()
    # label = serializers.CharField()
    parent_node_title = serializers.SerializerMethodField()
    
    class Meta:
        model = ScenarioNode
        fields = ['id','scenario', 'step', 'label', 'parent_node', 'parent_node_title']
    
    def get_label(self, instance):
        label = "(parent: {}) {}".format(self.get_parent_node_title(instance),instance.step.title)
        return label
    
    def get_parent_node_title(self, instance):  
        if instance.parent_node is not None:
            parent_node = ScenarioNode.objects.get(id=instance.parent_node.id)
            return parent_node.step.title
        return 'root'
    
    def validate(self, data):

        user = self.context['request'].user
        if data['step'].game.author.id !=  user.id:
            raise ValidationError('Creation not allowed: game not owned by requester')
        # now check that there is no first node already
        if data['parent_node'] == None:
            if ScenarioNode.objects.filter(scenario = data['scenario']).filter(parent_node = None).count() > 0:
                raise ValidationError('There is already a root node for this scenario')
        return data

#test a serializer that calls itself    
class ScenarioNodeTreeSerializer(ModelSerializer):
    #step_title = serializers.SerializerMethodField()
    #child_nodes = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    
    class Meta:
        model = ScenarioNode
        fields = ['id','scenario', 'step', 'label', 'parent_node', 'children',] #ajout label pour voir au lieu de step_title
    
    def get_label(self, instance):

        return instance.step.title
    
    def get_children(self, instance):
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

    def validate(self, data):

        user = self.context['request'].user
        if data['step'].game.author.id !=  user.id:
            raise ValidationError('Creation not allowed: game not owned by requester')
        return data

class ClueDetailSerializer(ModelSerializer):

    class Meta:
        model = Clue
        fields = ['id','step', 'title', 'text']


class ScenarioPlaySerializer(ModelSerializer):

    first_node = serializers.SerializerMethodField()
    
    class Meta:
        model = Scenario
        fields = ['id', 'name', 'game','first_node']

    def get_first_node(self, instance):
        queryset = instance.scenario_nodes.filter(parent_node = None)
        if len(queryset) == 0:
            raise ValidationError('no first node was defined')
        serializer = ScenarioNodeListSerializer(queryset[0], many=False)
        return serializer.data
    
class StepPlaySerializer(ModelSerializer):
    
    class Meta:
        model = Step
        fields = ['id', 'game', 'title', 'text', 'clues']

    def get_clues(self, instance):
        queryset = instance.clues.all()
        serializer = ClueListSerializer(queryset, many=True)
        return serializer.data
    
class ScenarioNodePlaySerializer(ModelSerializer):

    label = serializers.SerializerMethodField()

    class Meta:
        model = ScenarioNode
        fields = ['id','scenario', 'step', 'label']

    def get_label(self, instance):
        return instance.step.title
    