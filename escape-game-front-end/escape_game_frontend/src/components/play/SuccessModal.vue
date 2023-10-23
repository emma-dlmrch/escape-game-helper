<template>
    <div class="modal fade show background-modal" @click="goBack">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Bonne réponse !</h5>
                    <button type="button" class="btn-close close-btn" aria-label="Close" @click="goBack"></button>
                </div>
                <div class="modal-body">
                    <p>C'est la bonne réponse ! </p>
                    <div v-if="unlockedNodes.length">
                    <p >Vous avez débloqué les étapes suivantes : </p>
                    <p v-for="node in unlockedNodes" v-bind:key="node.id"> {{ node.label }}</p>
                </div>
                <div class="modal-footer">
                        <button type="button" class="btn btn-secondary btn-sm close-btn" @click="goBack">Fermer</button>
                </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'SuccessModal',
    props: ["unlocked-nodes"],
    emits: ['message-read'],
    components: {

    },
    data() {
        return {
            clue: {
                title: '',
                text: ''
            },

        }
    },
    methods: {

        goBack(e) {
            if (e.target.className.includes("background-modal") || e.target.className.includes("close-btn")) {
                this.$emit('message-read');
            }
        },
    },


    created() {
    }
}


</script>