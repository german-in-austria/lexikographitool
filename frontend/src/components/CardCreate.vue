<template>
  <v-container fluid>
    <v-tabs
        v-model="tab"
        align-with-title
    >
      <v-tabs-slider color="yellow"></v-tabs-slider>

      <v-tab>Einfach</v-tab>
      <v-tab>Schwierig</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-form v-model="form_simple" ref="form_simple">
          <v-container>
            <v-row no-gutters>

              <v-col cols="12">
                <v-text-field
                    v-model="dialectWord"
                    label="Dialektwort"
                    :rules="[(v) => !!v || 'Dialektwort muss angegeben werde']"
                    required
                ></v-text-field>
              </v-col>

              <v-col cols="6">
                <input-lemma-box label="Lemma" v-model="lexeme" type="lexeme"></input-lemma-box>
              </v-col>
              <v-col cols="6">
                <v-text-field
                    v-model="description"
                    label="Beschreibung"
                    required
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <input-multiple label="Beispiele" v-model="examples"></input-multiple>
              </v-col>
              <v-col cols="4">
                <input-multiple label="Aussprache" v-model="pronunciations"></input-multiple>
              </v-col>
              <v-col cols="4">
                <input-multiple label="Etymology" v-model="etymologies"></input-multiple>
              </v-col>
              <v-col cols="12">
                <input-button-group v-model="kind" :items="kindItems"></input-button-group>
              </v-col>
              <v-col cols="12">
                <v-combobox label="Kategorie" v-model="categories" :return-object="false" append-icon="" item-text="category" :items="category_list" multiple></v-combobox>
              </v-col>
              <v-col cols="12">
                <input-lemma-box label="Dialekt" v-model="dialect" type="dialect"></input-lemma-box>
              </v-col>
              <v-col cols="12">
                <card-create-location v-model="location"></card-create-location>
              </v-col>
              <v-col>
                <v-checkbox
                    v-model="vulgar"
                    label="Bei diesem Wort handelt es sich um einenen vulgären Ausruck"
                ></v-checkbox>
              </v-col>
              <v-btn color="success" @click="submit">Wort hinzufügen</v-btn>
            </v-row>

          </v-container>
        </v-form>
<!--        {{ dialectWord }},-->
<!--        {{ dialect }}-->
<!--        {{ lexeme }},-->
<!--        {{ description }},-->
<!--        {{ categories }},-->
<!--        {{ examples }},-->
<!--        {{ pronunciations }},-->
<!--        {{ kind }},-->
<!--        {{ location }}-->

      </v-tab-item>
      <v-tab-item>
<!--        hallo-->
      </v-tab-item>
    </v-tabs-items>
    <v-snackbar
        v-model="snackbarSuccessful"
        :timeout="2000"
        color="success"
    >
      Wort hinzugefügt!
    </v-snackbar>
    <v-snackbar
        v-model="snackbarFailure"
        :timeout="2000"
        color="error"
    >
      Hoppla! Ein fehler ist aufgetreten.
    </v-snackbar>
  </v-container>
</template>

<script>
import CardCreateLocation from "@/components/CardCreateLocation";


import Dialect from "@/objects/Dialect";
import requestHandler from "@/utils/RequestHandler";
import Lexeme from "@/objects/Lexeme";
import InputLemmaBox from "@/components/InputLemmaBox";
import InputMultiple from "@/components/InputMultiple";
import InputButtonGroup from "@/components/InputButtonGroup";
import RequestHandler from "@/utils/RequestHandler";

export default {
  name: "CardCreate",
  components: {
    InputButtonGroup,
    InputMultiple,
    InputLemmaBox,
    CardCreateLocation,
  },
  data: () => ({
    dialectWord: '',
    dialect: '',
    lexeme: '',
    description: '',
    examples: [],
    pronunciations: [],
    etymologies: [],
    kind: 'N',
    location: {id:-1,zipcode: null, place: null},
    categories: [],
    vulgar: false,
    form_simple: null,
    tab: null,

    snackbarSuccessful: false,
    snackbarFailure: false,
    valid: false,

    category_list:[],
    kindItems: [
      {
        id: 1,
        name: "Substantiv/Nomen",
        value: "N",
      },
      {
        id: 2,
        name: "Verb",
        value: "V",
      },
      {
        id: 3,
        name: "Adjectiv",
        value: "Aj",
      },
      {
        id: 4,
        name: "Adverb",
        value: "Av",
      },
      {
        id: 5,
        name: "Phrase",
        value: "P",
      },
    ],
  }),
  methods: {
    async createNewLexeme() {
      // var categories = [];
      // this.categories.forEach((item) => categories.push(new Category(item)));
      var lexemeId;
      var lexeme = new Lexeme(
          this.lexeme,
          this.description,
          this.dialectWord,
          this.kind,
          this.dialect,
          this.location.id
      );
      requestHandler
          .createDialect(new Dialect(this.dialect))
          .then(() => requestHandler.postLexeme(lexeme))
          .then((response) => {
            lexemeId = response.data.id;
            requestHandler.postEtymologies(this.etymologies, lexemeId);
            requestHandler.postExamples(this.examples, lexemeId);
            requestHandler.postPronunciations(this.pronunciations, lexemeId);
            requestHandler.addCategoriesWithLexeme(this.categories, lexemeId);

            this.snackbarSuccessful = true;
            this.resetForm();
          });
    },
    submit() {
      if (this.$refs.form_simple.validate()) {
        this.createNewLexeme();
      }
    },
    resetForm() {
      this.dialectWord = ''
      this.dialect = ''
      this.lexeme = ''
      this.description = ''
      this.examples = []
      this.pronunciations = []
      this.etymologies = []
      this.kind = 'N'
      this.categories = []
      this.vulgar = false
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