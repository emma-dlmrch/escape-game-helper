<template>
    <h1>Etape : {{ step.title }}</h1>
    <form @submit.prevent="modifyStep">
        <div class="form-group">
            <label for="step-name">Nom de l'étape :</label>
            <input id="step-name" type="text" class="form-control" v-model.lazy="step.title"
                @click="disableWasUpdatedMessage" required>
        </div>
        <div class="form-group">
            <label>Texte :</label>
            <!-- <textarea id="step-text" class="form-control" v-model="step.text" rows="5" @click="disableWasUpdatedMessage" required></textarea> -->
            <QuillEditor ref="quill" v-if="quillReady" v-model:content="step.text" contentType="html" theme="snow"
                :modules="modules" :toolbar="toolbarOptions" @click="disableWasUpdatedMessage" />
        </div>
        <div class="form-group">
            <label for="step-answer">Réponse attendue :</label>
            <input id="step-answer" type="text" class="form-control" v-model="step.answer"
                @click="disableWasUpdatedMessage">
            <small id="answer-help" class="form-text text-muted">Laisse le champ vide si l'étape ne requiert pas de
                réponse</small>
        </div>
        <div class="form-group">
            <input id="is_last" type="checkbox" class="form-check-input" v-model="step.is_last"
                @click="disableWasUpdatedMessage">
            <label for="step-is_last">Dernière étape ?</label>
            <!-- <small id="is_last-help" class="form-text text-muted">Permet de stopper le chronomètre</small> -->
        </div>
        <div>
            <button type="submit" class="btn btn-dark btn-sm"><i class="bi bi-pencil"></i> Enregistrer</button>

        </div>
        <small v-if="wasUpdated" class="form-text text-muted"><i class="bi bi-check"></i> Modifications enregistrées
            !</small>
    </form>

    <div v-if="step.is_last">
        <h2>Textes alternatifs</h2>
        <button @click="createDefaultNewEndGameText" class="btn btn-dark btn-sm"><i
                                class="bi bi-plus-lg"></i> Nouveau</button>
        <div v-for="egt in endGameTexts" v-bind:key="egt.id">
            <!-- <div class="form-group">
                <label for="end-text-name">Titre :</label>
                <input id="end-text-name" type="text" class="form-control" v-model.lazy="egt.title" required>
            </div> -->
            <div class="form-group">
                <label for="end-text-text">Texte :</label>
                <QuillEditor v-if="quillReady" v-model:content="egt.text" contentType="html" theme="snow"
                :modules="modules" :toolbar="toolbarOptions" @click="updateEndGameUpdateStatus(egt.id, false)"/>
            </div>
            <div class="form-group">
                <label for="end-text-minTime">Temps min :</label>
                <input id="end-text-minTime" type="number" class="form-control" v-model="egt.min_time" @click="updateEndGameUpdateStatus(egt.id, false)" required>
                <small class="form-text text-muted">  {{ displayHourSeconds(egt.min_time) }}</small>
            </div>
            <div class="form-group">
                <label for="end-text-maxTime">Temps max :</label>
                <input id="end-text-maxTime" type="number" class="form-control" v-model="egt.max_time" @click="updateEndGameUpdateStatus(egt.id, false)" required>
                   <small class="form-text text-muted"> {{ displayHourSeconds(egt.max_time) }}</small>

            </div>
            <div>
                <small v-if="isUpdateEndGamePending(egt.id)"> <i
                                class="bi bi-exclamation-triangle"></i> Données non enregistrées</small>
            </div>
            <button @click="updateEndGameText(egt)" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-pencil"></i> Enregistrer</button>
            <button @click="deleteEndGameText(egt.id)" type="button" class="btn btn-outline-dark btn-sm"><i
                                class="bi bi-trash"></i> Supprimer</button>
        </div>
    </div>
    <h2>Les indices</h2>
    <div class="table-responsive">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Titre</th>
                    <th scope="col">Texte</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="clue in clues" v-bind:key="clue.id">
                    <th scope="row"><i class="bi bi-search"></i> {{ clue.title }}</th>
                    <td><i class="bi bi-journal-text"></i> {{ $inlineHTML(clue.text.substring(0, 20)) }} ...</td>
                    <td><button @click="modifyClue(clue.id)" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-pencil"></i> Modifier</button>&nbsp;
                        <button @click="deleteClue(clue.id)" type="button" class="btn btn-outline-dark btn-sm"><i
                                class="bi bi-trash"></i> Supprimer</button>
                    </td>
                </tr>
                <tr>
                    <th><input type="text" v-model="newClue.title" placeholder="Nouvel indice" maxlength="50"
                            class="form-control small-input" /></th>
                    <td><input type="text" v-model="newClue.text" placeholder="Entre un texte" maxlength="50"
                            class="form-control small-input" /></td>
                    <td><button @click="createNewClue" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-plus-lg"></i> Créer</button></td>
                </tr>
            </tbody>
        </table>
    </div>
    <div>
        <button @click="cancel" type="button" class="btn btn-dark btn-sm"><i class="bi bi-arrow-left"></i>
            Retour</button>
    </div>
</template>

<script>
import axios from 'axios'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import BlotFormatter from '@enzedonline/quill-blot-formatter2'
import { imageHandler } from '@/quill/image';
import { registerAudioBlot, audioHandler } from '@/quill/audio';


export default {
    name: 'GameDetails',
    components: {
        QuillEditor
    },
    data() {
        return {
            quillReady: false,

            gameId: this.$route.params.gameId,
            stepId: this.$route.params.stepId,
            step: {
                title: '',
                text: '',
                answer: '',
                is_last: ''
            },
            clues: [],
            newClue: {
                title: '',
                text: '',
                step: ''
            },
            endGameTexts: [],
            newEndGameText: {
                title: '',
                text: '',
                step: '',
                minTime: '',
                maxTime: ''
            },
            wasUpdated: false,
            endGameTextUpdatePending: [],
            modules: [
            {
                name: 'blotFormatter',
                module: BlotFormatter,
                // options: {/* options */}
            },
            ],
            toolbarOptions: {
                container: [
                    { 'header': [1, 2, 3, false] },
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
                handlers: {
                    audio: audioHandler,
                    image: this.imageUploadHandler
                }
            }

        }
    },

    methods: {
        getStepData() {
            axios.get("step/" + this.stepId + "/")
                .then(response => {
                    this.step = response.data;
                    this.clues = response.data.clues
                    this.endGameTexts = response.data.end_game_texts
                }, (error) => {
                    console.log(error)
                }
                )

        },

        modifyStep() {
            axios.put('step/' + this.stepId + "/", this.step).then((response) => {
                if (response.status == 200) {
                    this.wasUpdated = true
                }
            }).catch((e) => {
                console.log("Couldn't edit step", e);
            });
        },

        cancel() {
            this.$router.push({ name: 'GameDetails', params: { id: this.gameId } })
        },

        //INDICES
        createNewClue() {

            if (this.newClue.title.length < 1) { this.newClue.title = 'Indice sans nom' }
            if (this.newClue.text.length < 1) { this.newClue.text = 'Pas de description' }
            this.newClue.step = this.stepId
            axios.post('clue/', this.newClue).then(() => {
                this.newClue.title = ''
                this.newClue.text = ''
                this.getStepData()
            }).catch((error) => {
                console.error("Error during form submission:", error);
            });

        },

        deleteClue(clueId) {
            if (confirm("Etes vous sûr.e de vouloir supprimer cet indice ?")) {
                axios.delete('clue/' + clueId + "/")
                    .then(() => {
                        this.getStepData();
                    },
                        (error) => { console.log("Error", error) });
            }
        },
        modifyClue(clueId) {
            this.$router.push({ name: 'UpdateClue', params: { gameId: this.gameId, stepId: this.stepId, clueId: clueId } })
        },

        //TETE DE FIN ALTERNATIF
        createDefaultNewEndGameText() {
            this.newEndGameText.title = "Title"
            this.newEndGameText.text = "Texte"
            this.newEndGameText.min_time = 0
            this.newEndGameText.max_time = 3600
            this.createNewEndGameText();
        },
        createNewEndGameText() {

            this.newEndGameText.step = this.stepId
            axios.post('end_game_text/', this.newEndGameText).then(() => {
                this.newEndGameText.title = ''
                this.newEndGameText.text = ''
                this.newEndGameText.minTime = ''
                this.newEndGameText.maxTime = ''
                this.getStepData()
            }).catch((error) => {
                console.error("Error during form submission:", error);
            });

        },

        deleteEndGameText(endgameTextId) {
            if (confirm("Etes vous sûr.e de vouloir supprimer ce texte ?")) {
                axios.delete('end_game_text/' + endgameTextId + "/")
                    .then(() => {
                        this.getStepData();
                    },
                        (error) => { console.log("Error", error) });
            }
        },
        updateEndGameText(egt) {
            axios.put('end_game_text/' + egt.id + "/", egt)
                .then(response => {
                    if (response.status == 200) {
                        this.updateEndGameUpdateStatus(egt.id, true)
                    }
                },
                    (error) => { console.log("Error", error) });

        },
        
        updateEndGameUpdateStatus(id, bool) {
            if (bool) {
                this.removeUpdateEndGamePending(id)
            } else if (!this.isUpdateEndGamePending(id)) {
                this.endGameTextUpdatePending.push(id)
            }
        },

        isUpdateEndGamePending(id) {
            return this.endGameTextUpdatePending.includes(id)
        },

        removeUpdateEndGamePending(id) {
            this.endGameTextUpdatePending =
                this.endGameTextUpdatePending.filter(item => item !== id)
        },

        disableWasUpdatedMessage() {
            this.wasUpdated = false
        },

        displayHourSeconds(s) {
            var nbH = Math.floor(s/3600);
            var nbM=  Math.floor((s-nbH*3600)  / 60);
            var nbS=  s-nbH*3600 -nbM*60;
            return nbH + ' h ' + nbM + ' min ' + nbS + ' s'
        },

        async imageUploadHandler() {
            await imageHandler(this.$refs.quill.getQuill(), this.gameId);
        },

    },
    async created() {
        this.getStepData();
        await registerAudioBlot()
        this.quillReady = true
    }
}
</script>