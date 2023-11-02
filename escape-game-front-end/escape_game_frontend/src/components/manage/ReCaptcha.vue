<template>
    <div class="sample-captcha">
      <input class="form-control" id="captcha" type="text" v-model="inputValue" @click="emitValidity" placeholder="Copie les catactères ci-dessous" required/>
  
      <VueClientRecaptcha
        :value="inputValue"
        @isValid="emitValidity"
      />
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import VueClientRecaptcha from "vue-client-recaptcha";

  export default {
    components: {
      VueClientRecaptcha,
    },
    emits : ['value-entered'],
    setup() {
      /* pass value to captcha  */
      const inputValue = ref(null);
      return {
        inputValue,
      };
    },

    methods:{
        emitValidity(value) {
            this.$emit('value-entered', value);
        },
    }
  };
  </script>