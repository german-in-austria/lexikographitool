<template>
  <v-container fluid>
    <v-row no-gutters>
      <v-col cols="12" lg='8'>
        <p class="text-h3">Willkommen</p>
        <v-row no-gutters class="pa-5">
          <p class="text-body-1">
            Hilf anderen ihre sprachliche Speisekammer aufzufüllen! Befülle die Dialektkarte oder gehe zu 
            <router-link to="card-create">Wort hinzufügen</router-link> um über noch mehr Einstellmöglichkeiten zu verfügen.
          </p>
          <v-col cols="12" sm="6">
            <card-dialect-prototype ></card-dialect-prototype>
          </v-col>
          <v-col cols="12" sm="6" class="pa-5">
            Klicke direkt auf den Text in der Karte um ihn zu ändern und
            schreibe dein spannendes Stichwort, das du angeben möchtest, in das
            große Textfeld. Gib dazu eine Beschreibung dieses Stichwortes an.
            Und wenn du magst auch noch die Varietät (zum Beispiel
            'tirolerisch', 'wiener Jugendsprache' oder auch 'Fachsprache' ).
          </v-col>
        </v-row>

        <v-row no no-gutters class="mt-10">
          <v-col cols="12">
            <p class="text-h5">Fragen?</p>
            <p class="text-body-1">
              Hat dich etwas schon immer brennend interressiert? Dann stell der
              Community deine Frage!
            </p>
          </v-col>
          <v-col>
            <v-textarea
              label="neue Frage"
              placeholder="Stelle deine Frage hier!"
              v-model="postText"
              outlined
              rows="3"
              row-height="25"
              no-resize
              append-icon="mdi-send"
              @click:append="createPost"
              class="mt-1 mr-5"
              ref="postText"
              required
              :rules="[(v) => !!v || 'Bitte gib einen Text ein']"
            ></v-textarea>
          </v-col>
        </v-row>
      </v-col>
      <v-divider vertical></v-divider>
      <v-col cols="12" lg="3" >
        <p class="text-h5">Entdecke neue Wörter</p>

        <v-col cols="12">
          <p class="text-body-1">Lieblingswort</p>
          <card-dialect class="mx-5" :card="popular"></card-dialect>
        </v-col>
        <v-col cols="12">
          <p class="text-body-1">Heiß Diskutiert</p>
          <card-dialect class="mx-5" :card="discussed"></card-dialect>
        </v-col>
        <v-col> </v-col>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import RequestHandler from "@/utils/RequestHandler";
import CardDialect from "../components/CardDialect.vue";
import CardDialectPrototype from "../components/CardDialectPrototype.vue";
import axios from 'axios'
export default {
  components: { CardDialect, CardDialectPrototype },
  data: () => ({
    cards: [],
    cardActive:false,
    popular: { examples: [] },
    discussed: { examples: [] },
    random: { examples: [] },
    postText: "",
  }),
  mounted() {
    RequestHandler.getLexemesRandom().then((response) => {
      this.cards = response.data;
    });
    axios.get('lexemes/popular/').then(response=>this.popular=response.data)
    axios.get('lexemes/discussed/').then(response=>this.discussed=response.data)
  },
  methods: {
    createPost() {
      if (this.$refs.postText.validate()) {
        RequestHandler.createPost(this.postText, null).then(() => {
          this.postText = "";
          this.$router.push('/postings');
        });
      }
    },
  },
};
</script>