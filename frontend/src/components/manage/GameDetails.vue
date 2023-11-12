<template>
    <h1>Jeu : {{ game.name }}</h1>
    <form @submit="modifyGame">
        <div class="form-group">
            <label for="name">Nom :</label>
            <input type="text" id="name" class="form-control" v-model.lazy="game.name" @click="disableWasUpdatedMessage"
                required>
        </div>
        <div class="form-group">
            <label for="description">Text descriptif :</label>
            <!-- <textarea class="form-control" v-model="game.description" id="description" rows="3" @click="disableWasUpdatedMessage" required></textarea> -->
            <QuillEditor v-model:content="game.description" contentType="html" theme="snow" :modules="modules"
                :toolbar="toolbarOptions"
                @click="disableWasUpdatedMessage" />

            <p>OTHER TEST</p>
            <!-- <TextEditor v-model="game.description" :gameId="gameId"/> -->
            <text-editor v-model="game.description" :gameId="gameId" @click="disableWasUpdatedMessage"></text-editor>
        </div>
        <div class="button-general-div">
            <button type="submit" class="btn btn-dark btn-sm"><i class="bi bi-pencil"></i> Enregistrer</button>
        </div>
        <small v-if="wasUpdated" class="form-text text-muted"><i class="bi bi-check"></i> Modifications enregistrées
            !</small>
    </form>

    <h2>Liste d'étapes</h2>
    <div class="table-responsive">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Etapes</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="step in this.steps" v-bind:key="step.id">
                    <th scope="row"><i class="bi bi-journal-text"></i> {{ step.title }}</th>
                    <td><button @click="modifyStep(step.id)" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-pencil"></i> Gérer</button>&nbsp;
                        <button @click="deleteStep(step.id)" type="button" class="btn btn-outline-dark btn-sm"><i
                                class="bi bi-trash"></i> Supprimer</button>
                    </td>
                </tr>
                <tr>
                    <th><input class="form-control small-input" type="text" v-model="newStep.title"
                            placeholder="Nouvelle étape" maxlength="50"></th>
                    <td><button @click="createNewStep" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-plus-lg"></i> Créer</button></td>
                </tr>
            </tbody>
        </table>
    </div>
    <h2>Organiser mes étapes</h2>
    <div class="table-responsive">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col" colspan="2">Scénarios</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="scenario in this.scenarios" v-bind:key="scenario.id">
                    <th scope="row"><i class="bi bi-share"></i> {{ scenario.name }}</th>
                    <th scope="row"><i class="bi bi-link-45deg"></i> {{ scenario.slug }}</th>
                    <td><button @click="modifyScenario(scenario.id)" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-pencil"></i> Gérer</button>&nbsp;<button @click="deleteScenario(scenario.id)"
                            type="button" class="btn btn-outline-dark btn-sm"><i class="bi bi-trash"></i> Supprimer</button>
                    </td>
                </tr>
                <tr>
                    <th><input class="form-control small-input" type="text" v-model="newScenario.name"
                            placeholder="Nouveau scénario" maxlength="50"></th>
                    <th>
                        <input class="form-control small-input" type="text" @change="updateSlug" :value="newScenario.slug"
                            placeholder="la-cle-unique-du-scenario" maxlength="50" title="Ne peut contenir que les caractères suivants : a-z, 0-9 et -.">
                    </th>
                    <td><button @click="createNewScenario" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-plus-lg"></i> Créer</button></td>
                </tr>
            </tbody>
        </table>
    </div>

    <button @click="cancel" class="btn btn-dark btn-sm"><i class="bi bi-arrow-left"></i> Retour</button>
</template>

<script>
import axios from 'axios'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import ImageUploader from 'quill-image-uploader';
import BlotFormatter from 'quill-blot-formatter'
import store from '@/store';
import TextEditor from './TextEditor.vue';

export function imageHandler (file, gameId) {
    // if (file.size > 100000) {
    //         // alert("volume de l'image trop important, veuillez la réduire")
    //         // return 
    // } else {
    return new Promise((resolve, reject) => {
        const formData = new FormData();
        formData.append("game", gameId);
        formData.append("image", file);
        formData.append("author", store.state.userId)

        axios.post('/upload-image/', formData)
            .then(res => {
                console.log("PARENT")
                console.log("/" + res.data.image_relative_path)
                resolve("/"+res.data.image_relative_path);
            })
            .catch(err => {
                reject("Upload failed");
                console.error("Error:", err)
            })

        }
    )
    // }
}

export const slugify = text =>
  text
    .toString()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '-')
    .replace(/[^\w-]+/g, '')
    .replace(/--+/g, '-')
    .replace(/^-+|-+$/g, '')

export default {
    name: 'GameDetails',
    components: {
        QuillEditor,
        TextEditor
    },
    data() {
        return {
            game: {
                name: '',
                description: '',
            },
            gameId: this.$route.params.id,
            steps: [],
            newStep: {
                title: '',
                game: '',
            },
            scenarios: [],
            newScenario: {
                name: '',
                slug: '',
                game: ''
            },
            wasUpdated: false,
            modules: [{
                name: 'imageUploader',
                module: ImageUploader,
                options: {
                    upload: (f) => imageHandler(f, this.gameId)
                }
            },
            {
                name: 'blotFormatter',  
                module: BlotFormatter, 
                // options: {/* options */}
            },
            ],
            toolbarOptions: [
                {'header': [1, 2, 3] }, 
                'bold', 
                'italic', 
                'underline', 
                { 'list': 'ordered' }, 
                { 'list': 'bullet' }, 
                'link', 
                'image', 
                'video'
            ]
        }

    },

    methods: {
        getGameData() {
            axios.get("game/" + this.gameId + "/")
                .then(response => {
                    this.game = response.data
                    this.steps = response.data.steps
                    this.scenarios = response.data.scenarios
                    document.title = "Gérer le jeu : " + this.game.name;

                }, (error) => {
                    console.log(error)
                }
                )
        },

        createNewStep() {
            if (this.newStep.title.length < 1) { this.newStep.title = 'Etape sans nom' }
            this.newStep.game = this.gameId
            axios.post('step/', this.newStep).then(() => {
                this.newStep.title = "";
                this.getGameData()
            }).catch((error) => {
                console.error("Error during form submission:", error);
            });
        },

        createNewScenario() {
            if (this.newScenario.name.length < 1) { this.newScenario.name = 'Scenario sans nom' }
            if (this.newScenario.slug.length < 1) { this.newScenario.slug = slugify(this.newScenario.name) }
            this.newScenario.game = this.gameId
            // just to make sure we have a real slug
            this.newScenario.slug = slugify(this.newScenario.slug)
            axios.post('scenario/', this.newScenario).then(() => {
                this.newScenario.name = "";
                this.newScenario.slug = "";
                this.getGameData()
            }).catch((error) => {
                console.error("Error during form submission:", error);
            });
        },

        updateSlug(e) {
            this.newScenario.slug = slugify(e.target.value)
        },

        deleteScenario(scenarioId) {
            if (confirm("Etes-vous sûr.e de vouloir supprimer ce scénario ?")) {
                axios.delete('scenario/' + scenarioId + "/")
                    .then(() => {
                        this.getGameData();
                    },
                        (error) => { console.log("Error", error) });
            }

        },

        deleteStep(stepId) {
            if (confirm("Etes-vous sûr.e de vouloir supprimer cette étape de jeu ?")) {
                axios.delete('step/' + stepId + "/")
                    .then(() => {
                        this.getGameData();
                    },
                        (error) => { console.log("Error", error) });
            }
        },

        modifyStep(stepId) {
            this.$router.push({ name: 'StepDetails', params: { stepId: stepId, gameId: this.gameId } })
        },

        modifyScenario(scenarioId) {
            this.$router.push({ name: 'ScenarioDetails', params: { gameId: this.gameId, scenarioId: scenarioId } })
        },
        modifyGame(e) {
            e.preventDefault();
            axios.put('game/' + this.gameId + "/", this.game).then((response) => {
                if (response.status == 200) {
                    this.wasUpdated = true
                }
                this.getGameData();
            }, (error) => {
                console.log(error)
            }
            );
        },

        disableWasUpdatedMessage() {
            this.wasUpdated = false
        },

        cancel() {
            this.$router.push({ name: 'GameList' })
        },
    },

    created() {
        this.getGameData();
    },
}
</script>