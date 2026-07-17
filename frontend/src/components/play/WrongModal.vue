<template>
    <div class="modal fade show background-modal" @click="goBack">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Erreur</h5>
                    <button type="button" class="close-btn close-croix" aria-label="Close" @click="goBack">✕</button>
                </div>
                <div class="modal-body">
                    <p>Ce n'est pas la bonne réponse, essaie encore.</p>
</div>
                <div class="modal-footer">
                        <button type="button" class="btn btn-secondary btn-sm close-btn close-button" @click="goBack">Fermer</button>
                </div>

                
            </div>
        </div>
    </div>
</template>
<!-- TODO factoriser les compos de modales en une seul paramétrée -->

<script>
export default {
    name: 'WrongModal',
    emits: ['wrong-read'],
    components: {

    },

    methods: {

        goBack(e) {
            if (e.target.className.includes("background-modal") || e.target.className.includes("close-btn")) {
                this.$emit('wrong-read');
            }
        },
    },
}


</script>