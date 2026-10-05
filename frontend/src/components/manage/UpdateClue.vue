<template>
<h1>Indice : {{ clue.title }}</h1>
    <form @submit.prevent="updateClue">
        <div class="form-group">
            <label for="title">Titre :</label>
            <input id="title" type="text" class="form-control" v-model.lazy="clue.title" @click="disableWasUpdatedMessage">
        </div>
        <div class="form-group">
            <label>Texte :</label>
            <!-- <textarea  id="text" class="form-control" v-model="clue.text" rows="5" @click="disableWasUpdatedMessage"></textarea> -->
            <QuillEditor ref="quill" v-model:content="clue.text" contentType="html" theme="snow" :modules="modules"
                :toolbar="toolbarOptions"
                @click="disableWasUpdatedMessage" />
        </div>
        <div class="button-general-div">
            <button type="submit" class="btn btn-dark btn-sm"><i class="bi bi-pencil"></i> Enregistrer</button>
        </div>
        <small v-if ="wasUpdated" class="form-text text-muted"><i class="bi bi-check"></i> Modifications enregistrées !</small>
    </form>
    <p></p>
    <button type="button" class="btn btn-dark btn-sm" @click="cancel"><i class="bi bi-arrow-left"></i> Retour</button>
</template>

<script>
import axios from 'axios';
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import BlotFormatter from '@enzedonline/quill-blot-formatter2'
import { registerAudioBlot, audioHandler } from '@/quill/audio';
import { imageHandler } from '@/quill/image';


export default {
    name:'UpdateClue',
    components: {
        QuillEditor
    },
    data () {
        return {
            clueId: this.$route.params.clueId,
            stepId: this.$route.params.stepId,
            gameId: this.$route.params.gameId,
            clue: {
                step:'',
                title:'',
                text:'',
            },
            wasUpdated : false,
            modules: [
            {
                name: 'blotFormatter',  
                module: BlotFormatter, 
                // options: {/* options */}
            },
            ],
            toolbarOptions: { 
                container : [
                    {'header': [1, 2, 3, false] }, 
                    'bold', 
                    'italic', 
                    'underline', 
                    { 'list': 'ordered' }, 
                    { 'list': 'bullet' }, 
                    'link', 
                    'image', 
                    'video',
                    'audio' 
                ],                 
                handlers : {
                    image: this.imageUploadHandler,
                    audio : audioHandler
                }
            },
        }
    },
    methods: {
        getClueData() {
            axios.get("clue/" + this.clueId + "/")
                .then(response => {
                    this.clue = response.data;
                }, (error) => {
                    console.log(error)
                }
                )

        },

        updateClue(){
            axios.put('clue/' + this.clueId + "/", this.clue)
                .then(response => {
                    if (response.status == 200) {
                        this.wasUpdated = true
                    }
                },
                    (error) => { console.log("Error", error) });

        },
        cancel(){
            this.$router.push({ name: 'StepDetails', params: { gameId: this.gameId, stepId: this.stepId } })
        },
        disableWasUpdatedMessage(){
            this.wasUpdated = false
        },
        
        async imageUploadHandler() {
            await imageHandler(this.$refs.quill.getQuill(), this.gameId);
        },
    },
    async created(){
        this.getClueData();
        await registerAudioBlot();
    }
}
</script>