<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" max-width="40rem" scrollable>
      <template v-slot:activator="{ on, attrs }">
        <v-btn v-bind="attrs" v-on.native.stop="on" text
        >Wort melden
        </v-btn>
      </template>
      <v-card>
        <v-card-title>Wort melden</v-card-title>
        <v-card-text>
          <v-textarea  v-model="reportMessage" required label="Bitte gib hier eine Begründung an, warum du das wort melden möchtest" ></v-textarea>
        </v-card-text>
        <v-card-actions>
        <v-btn @click="report">Wort melden</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import Axios from "axios";

export default {
name: "ReportDialog",
  props:['lexeme'],
  data: ()=>({
    dialog:false,
    reportMessage:'',
  }),
  methods:{
  report(){
    Axios.post('report/' + this.lexeme.id + '/',{message:this.reportMessage}).then(()=>{
      this.dialog = false;
      this.reportMessage = '';
    })
  }
  }
}
</script>

<style scoped>

</style>