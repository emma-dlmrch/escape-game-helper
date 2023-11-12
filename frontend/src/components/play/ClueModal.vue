<template>
    <div class="modal fade show background-modal" @click="goBack">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{clue.title}}</h5>
                    <button type="button" class="btn-close close-btn" aria-label="Close" @click="goBack"></button>
                </div>
                <div class="modal-body">
                    <p v-html="$sanitize(clue.text)"></p>

                <div class="modal-footer">
                        <button type="button" class="btn btn-secondary btn-sm close-btn" @click="goBack">Fermer</button>
                </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'ClueModal',
    props: ["clueId"],
    emits: ['clue-read'],
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
        getClueData() {
            axios.get("play/clue/" + this.clueId + "/")
                .then(response => {
                    this.clue = response.data
                }, (error) => {
                    console.log(error)
                }
                )
        },

        goBack(e) {
            if (e.target.className.includes("background-modal") || e.target.className.includes("close-btn")) {
                this.$emit('clue-read');
            }
        },
    },


    created() {
        this.getClueData()
    }
}


</script>