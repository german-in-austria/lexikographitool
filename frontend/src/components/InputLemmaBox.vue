<template>
<div>
  <v-combobox
      solo

      flat
      :value="value"
              :label="label"
              :search-input.sync="text"
              :item-text="itemText"
              :items="items"
              append-icon=""
              :required="true"
              :rules="[(v) => !!v || 'Lemma muss angegeben werde']"

  ><template v-slot:append><slot name="append"></slot></template>
  </v-combobox>
  </div>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import Axios from 'axios';

export default {
  name: "InputLemmaBox",
  props: ['value','label','type','required'],
  data: () => ({
    text:null,
    items:['asd'],
  }),
  methods: {
  },
  watch:{
    text(){
      if(this.type==='lexeme')
        RequestHandler.searchLexemesByWord(this.text).then(response=> this.items= response.data)
      else if (this.type === 'variety' )
        Axios.get('varieties/' + this.text + '/').then(response=> this.items= response.data)
      this.$emit('input', this.text)
    }
  },
  computed: {
    // a computed getter
    itemText: function () {
      switch(this.type) {
        case 'lexeme':
            return 'word'
        case 'dialect':
            return 'dialect'
        default:
          return 'word'
      }
    }
  }


}
</script>

<style scoped>

</style>