<template>
  <div>
    <v-form v-model="valid" ref="createForm" @submit.prevent="submit">
      <v-container>
        <v-row>
          <v-col>
            <v-text-field
              v-model="dialectWord"
              label="Dialektwort"
              :rules="[(v) => !!v || 'Dialektwort muss angegeben werde']"
              required
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <CardCreateLexem
              @loadLexeme="loadLexeme"
              @inputData="newLexeme"
              :rules="[
                (v) =>
                  !!v ||
                  !!description ||
                  'Hauptlexeme oder Beschreibung muss angegeben werden',
              ]"
            ></CardCreateLexem>
          </v-col>
          <v-col>
            <CardCreateDescription
              @inputData="newDescription"
              :rules="[
                (v) =>
                  !!v ||
                  !!lexeme ||
                  'Hauptlexeme oder Beschreibung muss angegeben werden',
              ]"
            ></CardCreateDescription>
            <!--            <v-text-field label="Beschreibung" v-model="description"></v-text-field>-->
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <card-create-button-group
              :selected="kind"
              @inputData="newKind"
              :items="kinds"
            ></card-create-button-group>
            <card-create-category
              :selected="categories"
              @inputData="newCategory"
              >></card-create-category
            >
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <card-create-button-group
              :selected="type"
              @inputData="newType"
              :items="kindItems"
            ></card-create-button-group>
          </v-col>
          <v-col>
            <CardCreateDialect
              :disabled="type == 'youth-language'"
              @inputData="newDialect"
            ></CardCreateDialect>

            <!--            <v-text-field label="Welcher Dialekt ist das?" v-model="dialect" :disabled="type =='youth-language'"></v-text-field>-->
          </v-col>
        </v-row>
        <card-create-multiple-dropdown
          label="Etymologie (Wortherkunft)"
          @inputData="newEtymology"
        ></card-create-multiple-dropdown>
        <card-create-multiple-dropdown
          label="Aussprache"
          @inputData="newPronunciation"
        ></card-create-multiple-dropdown>
        <card-create-multiple-dropdown
          label="Beispiel"
          @inputData="newExample"
        ></card-create-multiple-dropdown>
        <card-create-location @inputData="newOrigin"></card-create-location>
      </v-container>

      <v-btn class="mr-4" type="submit"> zum Wörterbuch hinzufügen </v-btn>
    </v-form>
  </div>
</template>

<script>
import CardCreateLocation from "@/components/CardCreateLocation";
import CardCreateLexem from "@/components/CardCreateLexem";
import CardCreateButtonGroup from "@/components/CardCreateButtonGroup";
import CardCreateMultipleDropdown from "@/components/CardCreateMultipleDropDown";
// import Lexeme from "@/objects/Lexeme"
import CardCreateCategory from "@/components/CardCreateCategory";
import Category from "@/objects/Category";
// import DialectWord from "@/objects/DialectWord";
import Dialect from "@/objects/Dialect";
import requestHandler from "@/utils/RequestHandler";
import Lexeme from "@/objects/Lexeme";
import CardCreateDescription from "@/components/CardCreateDescription";
import CardCreateDialect from "@/components/CardCreateDialect";

export default {
  name: "CardCreate",
  components: {
    CardCreateDialect,
    CardCreateDescription,
    CardCreateCategory,
    CardCreateMultipleDropdown,
    CardCreateButtonGroup,
    CardCreateLexem,
    CardCreateLocation,
  },
  data: () => ({
    valid: false,
    lexeme: "",
    dialectWord: "",
    dialect: "",
    description: "",
    examples: [],
    etymologies: [],
    pronunciations: [],
    kind_to_update: "N",
    kind: "N",
    origin: "",
    type: "",
    categories: [],
    kindItems: [
      {
        id: 1,
        name: "Dialekt",
        value: "dialect",
      },
      {
        id: 2,
        name: "Jugendsprache",
        value: "youth-language",
      },
    ],
    kinds: [
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
      if (this.type == "youth-language") this.dialect = "Jugendsprache";
      var categories = [];
      this.categories.forEach((item) => categories.push(new Category(item)));
      var lexemeId;
      var lexeme = new Lexeme(
        this.lexeme,
        this.description,
        this.dialectWord,
        this.kind,
        this.dialect,
        this.origin.id
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
        });
    },
    submit() {
      console.log("Lexem:" + this.lexeme);
      console.log("Kategorie:" + this.categories);
      console.log("Dialekt:" + this.dialect);
      console.log("Beschreibung:" + this.description);
      console.log("Beispiel:" + this.examples);
      console.log("Etymologie:" + this.etymologies);
      console.log("Pronunciations:" + this.pronunciations);
      console.log("Art:" + this.kind);
      console.log("Typ:" + this.type);
      console.log(this.origin);

      if (this.$refs.createForm.validate()) {
        this.createNewLexeme();
      }
    },
    newLexeme(value) {
      this.lexeme = value;
    },
    newKind(value) {
      this.kind = value;
    },
    newDescription(value) {
      this.description = value;
    },
    newExample(value) {
      this.examples = value;
    },
    newType(value) {
      this.type = value;
    },
    newOrigin(value) {
      this.origin = value;
    },
    newCategory(value) {
      this.categories = value;
    },
    newDialect(value) {
      this.dialect = value;
    },
    newEtymology(value) {
      this.etymologies = value;
    },
    newPronunciation(value) {
      this.pronunciations = value;
    },
    async loadLexeme() {
      console.log(this.lexeme);
      requestHandler.getFirsLexemeByName(this.lexeme).then((response) => {
        this.categories = [];
        response.data.categories.forEach((c) => {
          this.categories.indexOf(c.category) === -1
            ? this.categories.push(c.category)
            : console.log("This item already exists");
        });
        this.kind = response.data.kind;
      });
    },
  },
};
</script>

<style scoped>
.v-text-field.v-text-field--solo .v-input__control {
  min-height: 56px;
}
</style>