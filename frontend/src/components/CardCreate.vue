<template>
  <v-container fluid>
    <p class="text-h3">Wort hinzufügen</p>
    <v-tabs
        v-model="tab"
        align-with-title
    >
      <v-tabs-slider color="yellow"></v-tabs-slider>

      <v-tab>Anfänger*in</v-tab>
      <v-tab>Sammler*in</v-tab>
      <v-tab>Lexikograph*in</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <card-create-form :easy="true" :lexeme="lex"></card-create-form>

      </v-tab-item>
      <v-tab-item>
        <card-create-form :medium="true" :lexeme="lex"></card-create-form>

      </v-tab-item>
      <v-tab-item>
        <card-create-form :lexeme="lex"></card-create-form>

      </v-tab-item>
    </v-tabs-items>
    <v-btn @click="createNewLexeme">erstellen</v-btn>
    <v-snackbar
        v-model="snackbarSuccessful"
        :timeout="2000"
        color="success"
        centered
        height="500"
    >
      Wort hinzugefügt!
    </v-snackbar>
    <v-snackbar
        v-model="snackbarFailure"
        :timeout="2000"
        color="error"
        top
    >
      Hoppla! Ein fehler ist aufgetreten.
    </v-snackbar>
  </v-container>
</template>

<script>


import requestHandler from "@/utils/RequestHandler";
import Lexeme from "@/objects/Lexeme";
import RequestHandler from "@/utils/RequestHandler";
import CardCreateForm from "@/components/CardCreateForm";

export default {
  name: "CardCreate",
  components: {
    CardCreateForm
  },
  data: () => ({
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
      source:'',
    },
    snackbarSuccessful: false,
    snackbarFailure: false,
    valid: false,
    tab: null,

  }),
  methods: {
    async createNewLexeme() {
      // var categories = [];
      // this.categories.forEach((item) => categories.push(new Category(item)));
      let lexeme = new Lexeme(
          this.lex.word,
          this.lex.description,
          this.lex.dialectWord,
          this.lex.kind,
          this.lex.location.id,
          this.lex.sensitive,
          this.lex.variety,
          this.lex.source,
      );

      lexeme = await requestHandler.postLexeme(lexeme);
      console.log('1')
      console.log(this.lex.etymologies)
      console.log('1')

      console.log(this.lex.examples)
      console.log('1')

      console.log(this.lex.pronunciations)
      console.log('1')

      console.log(this.lex.categories)
      console.log('1')

      requestHandler.postEtymologies(this.lex.etymologies.filter(value => {
        return !!value.value
      }), lexeme.data.id)
      requestHandler.postExamples(this.lex.examples.filter(value => {
        return !!value.value
      }), lexeme.data.id)
      requestHandler.postPronunciations(this.lex.pronunciations.filter(value => {
        return !!value.value
      }), lexeme.data.id)
      requestHandler.addCategoriesWithLexeme(this.lex.categories, lexeme.data.id)
      this.snackbarSuccessful = true;
      this.resetForm();
    },
    submit() {
      if (this.$refs.form_normal.validate()) {
        this.createNewLexeme();
      }
    },
    submit_simple() {
      if (this.$refs.form_simple.validate()) {
        this.createNewLexeme();
      }
    },
    resetForm() {
      this.lex.dialectWord = ''
      this.lex.variety = ''
      this.lex.lexeme = ''
      this.lex.description = ''
      this.lex.examples = []
      this.lex.pronunciations = []
      this.lex.etymologies = []
      this.lex.kind = 'N'
      this.lex.categories = []
      this.lex.sensitive = false
    },
  },
  mounted() {
    RequestHandler.searchCategories('').then(response => this.category_list = response.data)

  }
};
</script>

<style scoped>
.v-text-field.v-text-field--solo .v-input__control {
  min-height: 56px;
}
</style>