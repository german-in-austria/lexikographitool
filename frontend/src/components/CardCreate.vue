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
        <v-form v-model="form_simple" ref="form_simple">
          <v-container>
            <v-row no-gutters>
              <v-col cols=12>
              <v-text-field
                    v-model="dialectWord"
                    label="Lemma"
                    :rules="[(v) => !!v || 'Lemma muss angegeben werde']"
                    required
                >
                <template v-slot:prepend><input-tool-tip tip='Das Stichwort / spannende Wort, das du angeben möchtest.'></input-tool-tip></template>
    </v-text-field>
                </v-col>
                <v-col cols="12">
                <input-lemma-box label="standarddeutsche Entsprechung (wenn vorhanden)" v-model="lexeme" type="lexeme">
               <template v-slot:prepend><input-tool-tip tip='Wenn möglich, schreibe hier ein standarddeutsches (="hochdeutsches") Wort ein, dass deinem Wort entspricht, du kannst auch mehrere Wörter einfügen.'></input-tool-tip></template>
                </input-lemma-box>
              </v-col>
              <v-col cols="12">
                <v-text-field
                    v-model="description"
                    label="Bedeutungserklärung"
                    required
                >
                <template v-slot:prepend><input-tool-tip tip='Hier kannst du eine oder mehrere Bedeutungen des Wortes angeben, versuche dabei so genau wie möglich zu sein. Die erste Beudeutung sollte die Hauptbedeutung sein.'></input-tool-tip></template>
                
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <input-multiple label="Beispiele" v-model="examples">
                <template v-slot:prepend><input-tool-tip tip='Hier kannst du Beispiele angeben, wie das Wort verwendet wird, am besten in einem Satz.'></input-tool-tip></template>
                </input-multiple>
              </v-col>
              
              <v-col cols="12">
                <input-button-group v-model="kind" :items="kindItems"></input-button-group>
              </v-col>
              
              <v-col cols="12">
                <v-combobox label="Kategorie" v-model="categories" :return-object="false" append-icon="" item-text="category" :items="category_list" multiple></v-combobox>
              </v-col>
              <v-col cols="12">
                <input-lemma-box label="Sprechweise / Varietät" v-model="variety" type="variety" :required="true">
                <template v-slot:prepend><input-tool-tip tip='Unter "Varietät" verstehen wir verschiedene Formen ein und derselben Sprache, z.B. kann das ein bestimmert Dialekt (z.B.: Vorarlbergerisch) oder eine Jugensprache ( Wiener Jugendsprache) oder eine Fachsprache (Handwerk, Landwirtschaft, Biologie) sein. Ihr wisst selbst am besten, welcher Sprechweise ihr welches WOrt zuprdnen würdet! '></input-tool-tip></template>
                
                </input-lemma-box>
              </v-col>
              <v-col cols="12">
                
                <input-location :loadHome='true' v-model="location">
                <template v-slot:prepend><input-tool-tip tip='Ort an dem das Wort verwendet wird, du kannst einzelne Orte angeben oder ganze Regionen.'></input-tool-tip></template>
                
                </input-location>
              </v-col>
              <v-col>
                <v-checkbox
                    v-model="sensitive"
                    label="ACHTUNG: Dieses Wort hat einen ulgären Inhalt oder kann als beleidigend empfunden werden!"
                ></v-checkbox>
              </v-col>
    <v-btn @click="resetForm">Zurücksetzen</v-btn>

              <v-btn color="primary" @click="submit_simple">Wort hinzufügen</v-btn>
            </v-row>
          </v-container>
        </v-form>
      </v-tab-item>
      <v-tab-item>
        <v-form v-model="form_normal" ref="form_normal">
          <v-container>
            <v-row no-gutters>
              <v-col cols=12>
              <v-text-field
                    v-model="dialectWord"
                    label="Lemma"
                    :rules="[(v) => !!v || 'Lemma muss angegeben werde']"
                    required
                >
                <template v-slot:prepend><input-tool-tip tip='Das Stichwort / spannende Wort, das du angeben möchtest.'></input-tool-tip></template>
    </v-text-field>
                </v-col>
                <v-col cols="12">
                <input-lemma-box label="standarddeutsche Entsprechung (wenn vorhanden)" v-model="lexeme" type="lexeme">
               <template v-slot:prepend><input-tool-tip tip='Wenn möglich, schreibe hier ein standarddeutsches (="hochdeutsches") Wort ein, dass deinem Wort entspricht, du kannst auch mehrere Wörter einfügen.'></input-tool-tip></template>
                </input-lemma-box>
              </v-col>
              <v-col cols="12">
                <v-text-field
                    v-model="description"
                    label="Bedeutungserklärung"
                    required
                >
                <template v-slot:prepend><input-tool-tip tip='Hier kannst du eine ider mehrere Bedeutungen des Wortes angeben, versuche dabei so genau wie möglich zu sein. Die erste Beudeutung sollte die Hauptbedeutung sein.'></input-tool-tip></template>
                
                </v-text-field>
              </v-col>
              
              
              <v-col cols="12">
                <input-multiple label="Beispiele" v-model="examples">
                <template v-slot:prepend><input-tool-tip tip='Hier kannst du Beispiele angeben, wie das Wort verwendet wird, am besten in einem Satz.'></input-tool-tip></template>
                </input-multiple>
              </v-col>

              <v-col cols="12">
                <input-multiple label="Aussprache (IPA)" v-model="pronunciations">
                <template v-slot:prepend><input-tool-tip tip='Aussprache verschriftlicht nach Internationalem Phonetischem Alphabet (IPA)'></input-tool-tip></template>
                
                </input-multiple>
              </v-col>
              
              <v-col cols="12">
                <input-button-group v-model="kind" :items="kindItems"></input-button-group>
              </v-col>
              
              <v-col cols="12">
                <v-combobox label="Kategorie" v-model="categories" :return-object="false" append-icon="" item-text="category" :items="category_list" multiple></v-combobox>
              </v-col>
              <v-col cols="12">
                <input-lemma-box label="Sprechweise / Varietät" v-model="variety" type="variety">
                <template v-slot:prepend><input-tool-tip tip='Unter "Varietät" verstehen wir verschiedene Formen ein und derselben Sprache, z.B. kann das ein bestimmert Dialekt (z.B.: Vorarlbergerisch) oder eine Jugensprache ( Wiener Jugendsprache) oder eine Fachsprache (Handwerk, Landwirtschaft, Biologie) sein. Ihr wisst selbst am besten, welcher Sprechweise ihr welches WOrt zuprdnen würdet! '></input-tool-tip></template>
                
                </input-lemma-box>
              </v-col>
              <v-col cols="12">
                
                <input-location :loadHome='true' v-model="location">
                <template v-slot:prepend><input-tool-tip tip='Ort an dem das Wort verwendet wird, du kannst einzelne Orte angeben oder ganze Regionen.'></input-tool-tip></template>
                
                </input-location>
              </v-col>
              <v-col>
                <v-checkbox
                    v-model="sensitive"
                    label="ACHTUNG: Dieses Wort hat einen vulgären Inhalt oder kann als beleidigend empfunden werden!"
                ></v-checkbox>
              </v-col>
    <v-btn @click="resetForm">Zurücksetzen</v-btn>

              <v-btn color="success" @click="submit_simple">Wort hinzufügen</v-btn>
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
        <v-form v-model="form_difficult" ref="form_difficult">
          <v-container>
            <v-row no-gutters>
              <v-col cols=12>
              <v-text-field
                    v-model="dialectWord"
                    label="Lemma"
                    :rules="[(v) => !!v || 'Lemma muss angegeben werde']"
                    required
                >
                <template v-slot:prepend><input-tool-tip tip='Das Stichwort / spannende Wort, das du angeben möchtest.'></input-tool-tip></template>
    </v-text-field>
                </v-col>
                <v-col cols="12">
                <input-lemma-box label="standarddeutsche Entsprechung (wenn vorhanden)" v-model="lexeme" type="lexeme">
               <template v-slot:prepend><input-tool-tip tip='Wenn möglich, schreibe hier ein standarddeutsches (="hochdeutsches") Wort ein, dass deinem Wort entspricht, du kannst auch mehrere Wörter einfügen.'></input-tool-tip></template>
                </input-lemma-box>
              </v-col>
              <v-col cols="12">
                <v-text-field
                    v-model="description"
                    label="Bedeutungserklärung"
                    required
                >
                <template v-slot:prepend><input-tool-tip tip='Hier kannst du eine ider mehrere Bedeutungen des Wortes angeben, versuche dabei so genau wie möglich zu sein. Die erste Beudeutung sollte die Hauptbedeutung sein.'></input-tool-tip></template>
                
                </v-text-field>
              </v-col>
              
              
              <v-col cols="12">
                <input-multiple label="Beispiele" v-model="examples">
                <template v-slot:prepend><input-tool-tip tip='Hier kannst du Beispiele angeben, wie das Wort verwendet wird, am besten in einem Satz.'></input-tool-tip></template>
                </input-multiple>
              </v-col>

              <v-col cols="12">
                <input-multiple label="Aussprache (IPA)" v-model="pronunciations">
                <template v-slot:prepend><input-tool-tip tip='Aussprache verschriftlicht nach Internationalem Phonetischem Alphabet (IPA)'></input-tool-tip></template>
                
                </input-multiple>
              </v-col>

              <v-col cols="12">
                <input-multiple label="Etymologie" v-model="etymologies">
                <template v-slot:prepend><input-tool-tip tip='Hier kannst du die Herkunft des Wortes beschreiben, wenn du sie weißt.'></input-tool-tip></template>
                
                </input-multiple>
              </v-col>
              <v-col cols="12">
                <input-button-group v-model="kind" :items="kindItems"></input-button-group>
              </v-col>
              
              <v-col cols="12">
                <v-combobox label="Kategorie" v-model="categories" :return-object="false" append-icon="" item-text="category" :items="category_list" multiple></v-combobox>
              </v-col>
              <v-col cols="12">
                <input-lemma-box label="Sprechweise / Varietät" v-model="variety" type="variety">
                <template v-slot:prepend><input-tool-tip tip='Unter "Varietät" verstehen wir verschiedene Formen ein und derselben Sprache, z.B. kann das ein bestimmert Dialekt (z.B.: Vorarlbergerisch) oder eine Jugensprache ( Wiener Jugendsprache) oder eine Fachsprache (Handwerk, Landwirtschaft, Biologie) sein. Ihr wisst selbst am besten, welcher Sprechweise ihr welches WOrt zuprdnen würdet! '></input-tool-tip></template>
                
                </input-lemma-box>
              </v-col>
              <v-col cols="12">
                
                <input-location :loadHome='true' v-model="location">
                <template v-slot:prepend><input-tool-tip tip='Ort an dem das Wort verwendet wird, du kannst einzelne Orte angeben oder ganze Regionen.'></input-tool-tip></template>
                
                </input-location>
              </v-col>
              <v-col>
                <v-checkbox
                    v-model="sensitive"
                    label="ACHTUNG: Dieses Wort hat einen vulgären Inhalt oder kann als beleidigend empfunden werden!"
                ></v-checkbox>
              </v-col>
    <v-btn @click="resetForm">Zurücksetzen</v-btn>

              <v-btn color="success" @click="submit_simple">Wort hinzufügen</v-btn>
            </v-row>
          </v-container>
     
        </v-form>


      </v-tab-item>
    </v-tabs-items>
    {{lexeme}}
    <v-snackbar
        v-model="snackbarSuccessful"
        :timeout="2000"
        color="success"
        top    
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
import InputLocation from "@/components/InputLocation";


import requestHandler from "@/utils/RequestHandler";
import Lexeme from "@/objects/Lexeme";
import InputLemmaBox from "@/components/InputLemmaBox";
import InputMultiple from "@/components/InputMultiple";
import InputButtonGroup from "@/components/InputButtonGroup";
import RequestHandler from "@/utils/RequestHandler";
import InputToolTip from './InputToolTip.vue';

export default {
  name: "CardCreate",
  components: {
    InputButtonGroup,
    InputMultiple,
    InputLemmaBox,
    InputLocation,
    InputToolTip,
  },
  data: () => ({
    dialectWord: '',
    variety: '',
    lexeme: '',
    description: '',
    examples: [{value:''}],
    pronunciations: [{value:''}],
    etymologies: [{value:''}],
    kind: 'N',
    location: {id:-1,zipcode: null, place: null},
    categories: [],
    sensitive: false,
    form_simple: null,
    form_normal: null,
    form_difficult: null,
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
          this.location.id,
          this.sensitive,
          this.variety
      );
      requestHandler.postLexeme(lexeme)
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
      this.dialectWord = ''
      this.variety = ''
      this.lexeme = ''
      this.description = ''
      this.examples = []
      this.pronunciations = []
      this.etymologies = []
      this.kind = 'N'
      this.categories = []
      this.sensitive = false
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