<template>
    <!-- <div ref="myDiv" > -->
    <QuillEditor v-bind:content="modelValue" @input="updateText"  contentType="html" theme="snow"
        :modules="modules" :toolbar="toolbarOptions" />

    <!-- </div> -->



</template>

<script>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import ImageUploader from 'quill-image-uploader';
import BlotFormatter from 'quill-blot-formatter'
import store from '@/store';
import axios from 'axios';


export function imageHandler(file, gameId) {
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
            .then((res) => {
                resolve("/" + res.data.image_relative_path);
            })
            .catch(err => {
                reject("Upload failed");
                console.error("Error:", err)
            })

    }
    )
    // }
}


export default {
    name: 'TextEditor',
    components: {
        QuillEditor
    },
    props: {
        modelValue: {
            type: String,
            default: "",
        },
        gameId: {
            type: String,
            default: ""
        },
    },
    computed: {

    },
    data() {
        return {
            isMounted: false,
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
                { 'header': [1, 2, 3, false] },
                'bold',
                'italic',
                'underline',
                { 'list': 'ordered' },
                { 'list': 'bullet' },
                'link',
                'image',
                'video'
            ],
        }
    },
    methods: {
        updateText(event){
            console.log("Update triggered")
            // $emit('update:modelValue', $event.target.innerHTML)
            if (event && event.target.innerHTML) {
                this.$emit('update:modelValue', event.target.innerHTML) 
            }
        }
    },
    // watch: {
    //     QuillEditor() {
    //         console.log("OUIVG")
    //     }   
    // },
    // mounted (){
    //     this.isMounted = true;

    // }

}
</script>