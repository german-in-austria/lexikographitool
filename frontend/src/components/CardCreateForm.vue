<template>
  <div>
      <v-row no-gutters class="ma-3 create-section">
      <v-col cols="12">
        <v-subheader>{{$t('createWord.lemma')}}<input-tool-tip
            :tip="$t('createWord.lemmaToolTip')"
        ></input-tool-tip></v-subheader>
        <v-text-field
            solo
            flat

            v-model="lexeme.dialectWord"
            :label="$t('createWord.lemma')"
            :rules="[(v) => !!v || 'Lemma muss angegeben werde']"
            required
        >
          <template v-slot:append
          >
            <input-tool-tip
                :tip="$t('createWord.lemmaToolTip')"
            ></input-tool-tip
            >
          </template>
        </v-text-field>
      </v-col>
      <v-col cols="12" v-if="!easy">
        <v-subheader>{{$t('createWord.pronunciation')}}<input-tool-tip
            :tip="$t('createWord.pronunciationToolTip')"
        ></input-tool-tip></v-subheader>
        <input-multiple
            :label="$t('createWord.pronunciation')"
            v-model="lexeme.pronunciations"
        >
          <template v-slot:prepend
          >
            <input-tool-tip
                :tip="$t('createWord.pronunciationToolTip')"
            ></input-tool-tip
            >
          </template>
        </input-multiple>
      </v-col>

      <v-col cols="12" v-if="!easy">

        <input-button-group
            v-model="lexeme.kind"
            :items="kindItems"
        ></input-button-group>
      </v-col>
      <v-expand-transition>
      <v-col cols="12" v-if="lexeme.kind=='N'">

        <input-button-group
            v-model="lexeme.genus"
            :items="genusItems"
        ></input-button-group>
      </v-col>
      </v-expand-transition>
      </v-row>

      <v-row no-gutters class="ma-3 create-section">
      <v-col cols="12">

        <v-subheader>
          {{$t('createWord.lexeme')}}<input-tool-tip
            :tip="$t('createWord.lexemeToolTip')"
        ></input-tool-tip></v-subheader>
        <input-lemma-box
            :label="$t('createWord.lexeme')"
            v-model="lexeme.word"
            type="lexeme"
        >
          <template v-slot:append
          >
            <input-tool-tip
                :tip="$t('createWord.lexemeToolTip')"
            ></input-tool-tip
            >
          </template>
        </input-lemma-box>
      </v-col>
      <v-col cols="12">
        <v-subheader>
          {{$t('createWord.description')}}<input-tool-tip
            :tip="$t('createWord.descriptionToolTip')"
        ></input-tool-tip></v-subheader>
        <v-text-field
            solo

            flat
            v-model="lexeme.description"
            :label="$t('createWord.description')"
            required
        >
          <template v-slot:append
          >
            <input-tool-tip
                :tip="$t('createWord.descriptionToolTip')"
            ></input-tool-tip
            >
          </template>
        </v-text-field>
      </v-col>

      <v-col cols="12" v-if="!easy">
        <v-subheader>
          {{$t('createWord.example')}}<input-tool-tip
            :tip="$t('createWord.exampleToolTip')"
        ></input-tool-tip></v-subheader>
        <input-multiple :label="$t('createWord.example')" v-model="lexeme.examples">
          <template v-slot:append
          >
            <input-tool-tip
                :tip="$t('createWord.exampleToolTip')"
            ></input-tool-tip
            >
          </template>
        </input-multiple>
      </v-col>


      <v-col cols="12" v-if="!easy & !medium">
        <v-subheader>
          {{$t('createWord.etymology')}}<input-tool-tip
            :tip="$t('createWord.etymologyToolTip')"
        ></input-tool-tip></v-subheader>
        <input-multiple :label="$t('createWord.etymology')" v-model="lexeme.etymologies">
          <template v-slot:append
          >
            <input-tool-tip
                :tip="$t('createWord.etymologyToolTip')"
            ></input-tool-tip
            >
          </template>
        </input-multiple>
      </v-col>

      </v-row>
    <v-row no-gutters class="ma-3 create-section">
      <v-col cols="12" v-if="!easy">
        <v-subheader>
          {{$t('createWord.category')}}<input-tool-tip
            :tip="$t('createWord.categoryToolTip')"
        ></input-tool-tip></v-subheader>
        <card-create-add-category :model="lexeme.categories"></card-create-add-category>

      </v-col>

      <v-col cols="12">
        <v-subheader>
          {{$t('createWord.variety')}}<input-tool-tip
            :tip="$t('createWord.varietyToolTip')"
        ></input-tool-tip></v-subheader>
        <input-lemma-box
            :label="$t('createWord.variety')"
            v-model="lexeme.dialect"
            type="variety"
        >
          <template v-slot:append
          >
            <input-tool-tip
                :tip="$t('createWord.varietyToolTip')"
            ></input-tool-tip
            >
          </template>
        </input-lemma-box>
      </v-col>
    </v-row>
    <v-row no-gutters class="ma-3 create-section">
      <v-col cols="12">
        <input-location :loadHome="true" v-model="lexeme.location">
          <template v-slot:append
          >
            <input-tool-tip
                :tip="$t('createWord.locationToolTip')"
            ></input-tool-tip
            >
          </template>
        </input-location>
      </v-col>
      <v-col cols="12" v-if="!easy">
        <v-textarea
            solo

            flat
            v-model="lexeme.source"
            :label="$t('createWord.source')"
            single-line
        >
          <template v-slot:append
          >
            <input-tool-tip
                :tip="$t('createWord.sourceToolTip')"
            ></input-tool-tip
            >
          </template>
        </v-textarea>
      </v-col>
      <v-col>
        <v-checkbox
            v-model="lexeme.sensitive"
            :label="$t('createWord.sensitive')"

        ></v-checkbox>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import InputLemmaBox from "@/components/InputLemmaBox";
import InputMultiple from "@/components/InputMultiple";
import InputButtonGroup from "@/components/InputButtonGroup";
import InputLocation from "@/components/InputLocation";
import InputToolTip from "./InputToolTip.vue";
import Axios from "axios";
import CardCreateAddCategory from "@/components/CardCreateAddCategory";

export default {
  props: ["lexeme", 'medium', 'easy'],
  components: {
    CardCreateAddCategory,
    InputButtonGroup,
    InputMultiple,
    InputLemmaBox,
    InputLocation,
    InputToolTip,
  },
  data: function () {
    return {
      kindItems: [
        {
          id: 1,
          name: this.$t("createWord.noun"),
          value: "N",
          tooltip:  this.$t("createWord.noun"),
        },
        {
          id: 2,
          name:  this.$t("createWord.verb"),
          value: "V",
          tooltip:  this.$t("createWord.verbTooltip"),

        },
        {
          id: 3,
          name: this.$t("createWord.adjective"),
          value: "Aj",
          tooltip:  this.$t("createWord.adjectiveTooltip"),

        },
        {
          id: 4,
          name:  this.$t("createWord.adverb"),
          value: "Av",
          tooltip:  this.$t("createWord.adverbTooltip"),

        },
        {
          id: 5,
          name: this.$t("createWord.interjection"),
          value: 'I',
          tooltip:  this.$t("createWord.interjectionTooltip"),

        },
        {
          id: 6,
          name:  this.$t("createWord.phrase"),
          value: "P",
          tooltip:  this.$t("createWord.phraseTooltip"),
        },
      ],
      genusItems: [
        {
          id: 1,
          name: this.$t("createWord.female"),
          value: "F",
          tooltip: this.$t("createWord.femaleToolTip"),
        },
        {
          id: 2,
          name:this.$t("createWord.male"),
          value: "M",
          tooltip: this.$t("createWord.maleToolTip"),

        },
        {
          id: 3,
          name: this.$t("createWord.neuter"),
          value: "N",
          tooltip: this.$t("createWord.neuterToolTip"),

        }]
    }
  },
  mounted() {
    Axios.get("categories/").then(
        (response) => (this.category_list = response.data)
    );
  },

};
</script>
<style>
.create-section{
  padding:20px;
  border-radius: 20px;
  border-color: lightgray;
  margin-top: 10px;
  background-color: rgb(0,0,0,0.05);
}

</style>