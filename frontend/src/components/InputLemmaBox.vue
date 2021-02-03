<template>
  <v-combobox :v-bind="value"
              :label="label"
              :search-input.sync="text"
              :item-text="itemText"
              :items="items"
              append-icon=""
  ></v-combobox>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";

export default {
  name: "InputLemmaBox",
  props: ['value','label','type'],
  data: () => ({
    text:null,
    items:[],
  }),
  methods: {
  },
  watch:{
    text(){
      if(this.type==='lexeme')
        RequestHandler.searchLexemesByWord(this.text).then(response=> this.items= response.data)
      else if (this.type === 'dialect' )
        RequestHandler.searchDialects(this.text).then(response=> this.items= response.data)
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