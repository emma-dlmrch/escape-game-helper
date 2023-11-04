<template>
    <div class="modal fade show background-modal" @click="goBack">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Supprimer un noeud</h5>
                    <button type="button" class="btn-close close-btn" aria-label="Close" @click="goBack"></button>
                </div>

                <div class="modal-body">
                    <p>Etes-vous sûr.e de vouloir supprimer ce noeud ? Les noeuds enfants seront supprimés également. Vos
                        étapes existeront toujours.</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary btn-sm close-btn" @click="goBack">Non</button>
                    <button type="submit" class="btn btn-dark btn-sm" @click="deleteNode">Oui</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'DeleteNode',
    props: ["nodeId"],
    emits: ['node-deleted'],
    data() {
        return {

        }
    },
    methods: {

        deleteNode() {
            axios.delete('scenario_node/' + this.nodeId + "/")
                .then(() => {
                    this.$emit('node-deleted');
                },
                    (error) => { console.log("Error", error) });
        },

        goBack(e) {
            if (e.target.className.includes("background-modal") || e.target.className.includes("close-btn")) {
                this.$emit('node-deleted');
            }
        },

    },
}
</script>