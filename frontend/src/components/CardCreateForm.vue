<template>
  <v-container>
    <v-row no-gutters>
      <v-col cols="12">
        <v-text-field
          v-model="lexeme.dialectWord"
          label="Lemma"
          :rules="[(v) => !!v || 'Lemma muss angegeben werde']"
          required
        >
          <template v-slot:prepend
            ><input-tool-tip
              tip="Das Stichwort / spannende Wort, das du angeben möchtest."
            ></input-tool-tip
          ></template>
        </v-text-field>
      </v-col>
      <v-col cols="12">
        <input-lemma-box
          label="standarddeutsche Entsprechung (wenn vorhanden)"
          v-model="lexeme.word"
          type="lexeme"
        >
          <template v-slot:prepend
            ><input-tool-tip
              tip='Wenn möglich, schreibe hier ein standarddeutsches (="hochdeutsches") Wort ein, dass deinem Wort entspricht, du kannst auch mehrere Wörter einfügen.'
            ></input-tool-tip
          ></template>
        </input-lemma-box>
      </v-col>
      <v-col cols="12">
        <v-text-field
          v-model="lexeme.description"
          label="Bedeutungserklärung"
          required
        >
          <template v-slot:prepend
            ><input-tool-tip
              tip="Hier kannst du eine ider mehrere Bedeutungen des Wortes angeben, versuche dabei so genau wie möglich zu sein. Die erste Beudeutung sollte die Hauptbedeutung sein."
            ></input-tool-tip
          ></template>
        </v-text-field>
      </v-col>

      <v-col cols="12">
        <input-multiple label="Beispiele" v-model="lexeme.examples">
          <template v-slot:prepend
            ><input-tool-tip
              tip="Hier kannst du Beispiele angeben, wie das Wort verwendet wird, am besten in einem Satz."
            ></input-tool-tip
          ></template>
        </input-multiple>
      </v-col>

      <v-col cols="12">
        <input-multiple
          label="Aussprache (IPA)"
          v-model="lexeme.pronunciations"
        >
          <template v-slot:prepend
            ><input-tool-tip
              tip="Aussprache verschriftlicht nach Internationalem Phonetischem Alphabet (IPA)"
            ></input-tool-tip
          ></template>
        </input-multiple>
      </v-col>

      <v-col cols="12">
        <input-multiple label="Etymologie" v-model="lexeme.etymologies">
          <template v-slot:prepend
            ><input-tool-tip
              tip="Hier kannst du die Herkunft des Wortes beschreiben, wenn du sie weißt."
            ></input-tool-tip
          ></template>
        </input-multiple>
      </v-col>
      <v-col cols="12">
        <input-button-group
          v-model="lexeme.kind"
          :items="kindItems"
        ></input-button-group>
      </v-col>

      <v-col cols="12">
        <v-combobox
          label="Kategorie"
          v-model="lexeme.categories"
          :return-object="false"
          append-icon=""
          item-text="category"
          :items="category_list"
          multiple
        ></v-combobox>
      </v-col>
      <v-col cols="12">
        <input-lemma-box
          label="Sprechweise / Varietät"
          v-model="lexeme.dialect"
          type="dialect"
        >
          <template v-slot:prepend
            ><input-tool-tip
              tip='Unter "Varietät" verstehen wir verschiedene Formen ein und derselben Sprache, z.B. kann das ein bestimmert Dialekt (z.B.: Vorarlbergerisch) oder eine Jugensprache ( Wiener Jugendsprache) oder eine Fachsprache (Handwerk, Landwirtschaft, Biologie) sein. Ihr wisst selbst am besten, welcher Sprechweise ihr welches WOrt zuprdnen würdet! '
            ></input-tool-tip
          ></template>
        </input-lemma-box>
      </v-col>
      <v-col cols="12">
        <input-location :loadHome="true" v-model="lexeme.location">
          <template v-slot:prepend
            ><input-tool-tip
              tip="Ort an dem das Wort verwendet wird, du kannst einzelne Orte angeben oder ganze Regionen."
            ></input-tool-tip
          ></template>
        </input-location>
      </v-col>
      <v-col>
        <v-checkbox
          v-model="lexeme.sensitive"
          label="ACHTUNG: Dieses Wort hat einen vulgären Inhalt oder kann als beleidigend empfunden werden!"
        ></v-checkbox>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import InputLemmaBox from "@/components/InputLemmaBox";
import InputMultiple from "@/components/InputMultiple";
import InputButtonGroup from "@/components/InputButtonGroup";
import InputLocation from "@/components/InputLocation";
import InputToolTip from "./InputToolTip.vue";
import Axios from "axios";

export default {
  props: ["lexeme"],
  components: {
    InputButtonGroup,
    InputMultiple,
    InputLemmaBox,
    InputLocation,
    InputToolTip,
  },
  data: () => ({
    category_list: [],
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
  mounted() {
    Axios.get("categories/").then(
      (response) => (this.category_list = response.data)
    );
  },
 
};
</script>