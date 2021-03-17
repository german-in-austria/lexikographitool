<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" max-width="40rem" scrollable>
      <template v-slot:activator="{ on, attrs }">
        <v-btn v-bind="attrs" v-on.native.stop="on" text small
        >
          <v-icon>mdi-pencil-outline</v-icon>
          Wort bearbeiten
        </v-btn>
      </template>
      <v-card :color="color + ' lighten-4'">
        <v-card-title class="headline">
          Wort bearbeiten
          <v-spacer></v-spacer>
        </v-card-title>

        <v-divider></v-divider>
        <v-card-text>

          <card-create-form :lexeme="lex"></card-create-form>
        </v-card-text>

        <v-divider></v-divider>
        <v-card-actions>
          <v-btn text @click="createNewLexeme">Speichern</v-btn>
        </v-card-actions>
      </v-card>

    </v-dialog>
    <v-snackbar
        v-model="snackbarSuccessful"
        :timeout="2000"
        color="success"
        centered
        height="500"
    >
      Wort bearbeitet!
    </v-snackbar>
  </v-row>
</template>

<script>
import CardCreateForm from "@/components/CardCreateForm";
import requestHandler from "@/utils/RequestHandler"
import Lexeme from "@/objects/Lexeme"
import Axios from 'axios';

export default {
  components: {CardCreateForm},
  props: ["lexeme"],
  data: () => ({
    dialog: false,
    snackbarSuccessful: false,
    lex: {
      dialectWord: "",
      variety: "",
      lexeme: "",
      description: "",
      examples: [{value: ""}],
      pronunciations: [{value: ""}],
      etymologies: [{value: ""}],
      kind: "N",
      location: {id: -1, zipcode: null, place: null},
      categories: [],
      sensitive: false,
      source: '',
    },
  }),
  watch: {
    dialog() {
      this.lex.dialectWord = this.lexeme.dialectWord;
      this.lex.word = this.lexeme.word;
      this.lex.description = this.lexeme.description;
      this.lex.variety = this.lexeme.veriety;
      this.lex.kind = this.lexeme.kind;
      this.lex.source = this.lexeme.source;
      this.lex.examples = this.lexeme.examples.map((item) => {
        return {value: item.example};
      });
      this.lex.pronunciations = this.lexeme.pronunciations.map((item) => {
        return {value: item.pronunciation};
      });
      this.lex.etymologies = this.lexeme.etymologies.map((item) => {
        return {value: item.etymology};
      });
      this.lex.categories = this.lexeme.categories.map((item) => {
        return item.category;
      });
      this.lex.sensitive = this.lexeme.sensitive;
    },
  },
  computed: {
    color() {
      const crypto = require("crypto");
      const hash = crypto
          .createHash("sha1")
          .update(
              this.lexeme.dialectWord + this.lexeme.word + this.lexeme.description
          )
          .digest("hex");

      const colors = [
        "card1",
        "card2",
        "card3",
        "card4",
        "card5",
        "card6",
        "card7",
      ];
      return colors[Math.floor(parseInt(hash, 16) % colors.length)];
    },
  },
  methods: {
    async createNewLexeme() {
      // var categories = [];
      // this.categories.forEach((item) => categories.push(new Category(item)));
      var lexemeId;
      var lexeme = new Lexeme(
          this.lex.word,
          this.lex.description,
          this.lex.dialectWord,
          this.lex.kind,
          this.lex.location.id,
          this.lex.sensitive,
          this.lex.variety,
          this.lex.source,
      );
      Axios.put('lexeme/' + this.lexeme.id + '/', lexeme)
          .then((response) => {
            lexemeId = response.data.id;
            requestHandler.postEtymologies(this.lex.etymologies, lexemeId);
            requestHandler.postExamples(this.lex.examples, lexemeId);
            requestHandler.postPronunciations(this.lex.pronunciations, lexemeId);
            requestHandler.addCategoriesWithLexeme(this.lex.categories, lexemeId);

            this.snackbarSuccessful = true;
            this.updateParent()
            this.dialog = false
          });
    },
    updateParent() {
      this.lexeme.dialectWord = this.lex.dialectWord;
      this.lexeme.word = this.lex.word;
      this.lex.description = this.lexeme.description;
      this.lexeme.veriety = this.lex.variety;
      this.lexeme.kind = this.lex.kind;
      this.lexeme.source = this.lex.source;
      this.lexeme.examples = this.lex.examples.map((item) => {
        return {example: item.value};
      });
      this.lexeme.pronunciations = this.lex.pronunciations.map((item) => {
        return {pronunciation: item.value};
      });
      this.lexeme.etymologies = this.lex.etymologies.map((item) => {
        return {etymology: item.value};
      });
      this.lexeme.categories = this.lex.categories.map((item) => {
        return {category: item};
      });
      this.lexeme.sensitive = this.lex.sensitive;
    }
  },
};
</script>