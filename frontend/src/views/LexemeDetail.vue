<template>
  <v-card>
    <p class="text-subtitle">{{ lexeme.dialect }}</p>
    <p class="text-h3">{{ lexeme.dialectWord }}</p>
    <p class="text-h4">{{ lexeme.word }}</p>
    <v-row no-gutters v-if="!!lexeme.description">
      <v-col> Beschreibung: </v-col>
      <v-col>
        {{ lexeme.description }}
      </v-col>
    </v-row>
    <v-row no-gutters v-if="!!lexeme.examples && lexeme.examples.length != 0">
      <v-col> Beispiele: </v-col>
      <v-col>
        <div v-for="example in lexeme.examples" :key="example.id">
          {{ example.example }}
        </div>
      </v-col>
    </v-row>
    <v-row
      no-gutters
      v-if="!!lexeme.categories && lexeme.categories.length != 0"
    >
      <v-col> Kategorien: </v-col>
      <v-col>
        <span v-for="(category, index) in lexeme.categories" :key="category.id">
          <span>{{ category.category }}</span>
          <span v-if="index + 1 < lexeme.categories.length">, </span>
        </span>
      </v-col>
    </v-row>

    <v-row no-gutters v-if="!!lexeme.origin">
      <v-col> Bundesland: </v-col>
      <v-col>
        {{ lexeme.origin }}
      </v-col>
    </v-row>

  <v-row
      no-gutters
      v-if="!!lexeme.pronunciations && lexeme.pronunciations.length != 0"
    >
      <v-col> Aussprache: </v-col>
      <v-col>
        <span v-for="(pronunciation, index) in lexeme.pronunciations" :key="pronunciation.id">
          <span>{{ pronunciation.pronunciation }}</span>
          <span v-if="index + 1 < lexeme.pronunciations.length">, </span>
        </span>
      </v-col>
    </v-row>

    <v-row
      no-gutters
      v-if="!!lexeme.etymologies && lexeme.etymologies.length != 0"
    >
      <v-col> Etymology: </v-col>
      <v-col>
        <span v-for="(etymology, index) in lexeme.etymologies" :key="etymology.id">
          <span>{{ etymology.etymology }}</span>
          <span v-if="index + 1 < lexeme.etymologies.length">, </span>
        </span>
      </v-col>
    </v-row>
  </v-card>

</template>

<script>
import RequestHandler from "../utils/RequestHandler.js";
export default {
  data: () => ({
    lexeme: null,
  }),
  mounted() {
    RequestHandler.getLexeme(this.$route.params.id).then((response) => {
      this.lexeme = response.data;
    });
  },
};
</script>