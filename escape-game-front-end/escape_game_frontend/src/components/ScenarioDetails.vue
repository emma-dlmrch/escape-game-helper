<template>
    <h1>{{ scenario.name }}</h1>
    <!-- <div>
        <blocks-tree :data="treeData" :horizontal="treeOrientation=='1'" :collapsable="true"></blocks-tree>
    </div> -->
    <div>
        <!-- Does not work now that nodes are sent in tree organisation from backend -->
        <!-- <div v-for="scenarioNode in scenarioNodes" v-bind:key="scenarioNode.id">
        {{ scenarioNode.parent_node_title }} > {{ scenarioNode.step_title }}</div> -->

    </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'ScenarioDetails',
    data (){
        return {
            scenarioId: this.$route.params.scenarioId,
            scenario: {
                name:''
            },
            scenarioNodes: [],
        }

    },

    methods: {
        getScenarioData() {
            axios.get("scenario/" + this.scenarioId + "/")
                .then(response => {
                    this.scenario = response.data
                    this.scenarioNodes = response.data.scenario_nodes
                }, (error) => {
                    console.log(error)
                }
                )
        },
    },

    created() {
        this.getScenarioData()
    }
}


</script>

<!-- <script>
import { defineComponent,ref,reactive } from 'vue';

export default defineComponent({

    setup() {

        let selected = ref([]);
        let treeOrientation = ref("0");
        let treeData = reactive({
            label: 'root',
            expand: true,
            some_id: 1,
            children: [
                { label: 'child 1', some_id: 2, },
                { label: 'child 2', some_id: 3, },
                { 
                    label: 'subparent 1', 
                    some_id: 4, 
                    expand: false, 
                    children: [
                        { label: 'subchild 1', some_id: 5 },
                        {  
                            label: 'subchild 2', 
                            some_id: 6, 
                            expand: false, 
                            children: [
                                { label: 'subchild 11', some_id: 7 },
                                { label: 'subchild 22', some_id: 8 },
                            ]
                        },
                    ]
                },
            ]
        });

        const toggleSelect = (node, isSelected) => {
            isSelected ? selected.value.push(node.some_id) : selected.value.splice(selected.value.indexOf(node.some_id), 1);
            if(node.children && node.children.length) {
                node.children.forEach(ch=>{
                    toggleSelect(ch,isSelected)
                })
            }
        }

        return {
            treeData,
            selected,
            toggleSelect,
            treeOrientation
        }
    }
})

</script> -->