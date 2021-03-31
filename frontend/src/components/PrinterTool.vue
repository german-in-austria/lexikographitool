<template>
  <div>
   <div v-if="showInPrint" id="printMe">
     <v-row no-gutters v-for="card in cards" :key="card.id">
       <v-col>{{card.dialectWord}}</v-col>
       <v-col>{{card.word}}</v-col>
       <v-col>{{card.description}}</v-col>
     </v-row>
      
   </div>
    <v-btn @click="print">Drucken</v-btn>
  </div>
</template>

<script>
export default {
  props:['cards'],
  data() {
    return {
      output: null,
      dialog: false,
      showInPrint: false,
      
    };
  },
  methods: {
    print() {
      this.showInPrint = true; // show the <p> tag

      // Use nextTick to trigger the print on next update
      this.$nextTick(() => {
        this.$htmlToPaper("printMe", null, () => {
          console.warn("done");
          this.showInPrint = false; // hide the <p> tag when printing is done
        });
      });
    },
  },
};
</script>
