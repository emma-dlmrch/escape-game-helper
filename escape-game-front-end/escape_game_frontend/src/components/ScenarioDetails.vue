<template>
    <h1>{{ scenario.name }}</h1>
    <div>
        <blocks-tree :data="scenarioNodes" :horizontal="treeOrientation == '1'" :collapsable="true"></blocks-tree>
    </div>
    <div>
        <!-- Does not work now that nodes are sent in tree organisation from backend -->
        <div v-for="scenarioNode in scenarioNodes" v-bind:key="scenarioNode.id">
            {{ scenarioNode.parent_node }} > {{ scenarioNode.label }}</div>

    </div>
</template>

<script>
import axios from 'axios'
import { ref, reactive } from 'vue'

export default {
    name: 'ScenarioDetails',
    data() {
        return {
            scenarioId: this.$route.params.scenarioId,
            scenario: {
                name: ''
            },
            scenarioNodes: {},
            test: {
                label: 'trololo',
                // expand: true,
                id: 1,
                children: [
                    { label: 'child 1', id: 2, },
                    { label: 'child 2', id: 3, },
                    {
                        label: 'subparent 1',
                        id: 4,
                        // expand: false,
                        children: [
                            { label: 'subchild 1', id: 5 },
                            {
                                label: 'subchild 2',
                                id: 6,
                                // expand: false,
                                children: [
                                    { label: 'subchild 11', id: 7 },
                                    { label: 'subchild 22', id: 8 },
                                ]
                            },
                        ]
                    },
                ]
            }
        }

    },

    methods: {
        getScenarioData() {
            axios.get("scenario/" + this.scenarioId + "/")
                .then(response => {
                    this.scenario = response.data
                    this.scenarioNodes = response.data.scenario_nodes
                    console.log(this.scenarioNodes)
                }, (error) => {
                    console.log(error)
                }
                )
        },
    },

    created() {
        this.getScenarioData()
        console.log('le test qui marche')
        console.log(this.test)
        console.log('mon arbre qui marche pas :')
        console.log(this.scenarioNodes)
    },
    setup() {

        let selected = ref([]);
        let treeOrientation = ref("0");
        let treeData = reactive({
            label: 'root',
            expand: true,
            id: 1,
            children: [
                // { label: 'child 1', id: 2, },
                // { label: 'child 2', id: 3, },
                // {
                //     label: 'subparent 1',
                //     id: 4,
                //     expand: false,
                //     children: [
                //         { label: 'subchild 1', id: 5 },
                //         {
                //             label: 'subchild 2',
                //             id: 6,
                //             expand: false,
                //             children: [
                //                 { label: 'subchild 11', id: 7 },
                //                 { label: 'subchild 22', id: 8 },
                //             ]
                //         },
                //     ]
                // },
            ]
        });

        const toggleSelect = (node, isSelected) => {
            isSelected ? selected.value.push(node.some_id) : selected.value.splice(selected.value.indexOf(node.some_id), 1);
            if (node.children && node.children.length) {
                node.children.forEach(ch => {
                    toggleSelect(ch, isSelected)
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
}


</script>