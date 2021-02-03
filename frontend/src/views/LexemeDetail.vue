<template>
  <perfect-scrollbar>

    <v-container fluid v-if="lexeme">
      <v-row no-gutters>
        <v-col cols="9">
          <p class="text-h3">{{ lexeme.dialectWord }}</p>
          <p class="text-h4">{{ lexeme.word }}</p>
          <v-col class="pa-0">
            <v-row no-gutters v-if="!!lexeme.description">
              <v-col cols="2"> Beschreibung:</v-col>
              <v-col>
                {{ lexeme.description }}
              </v-col>
            </v-row>
            <v-row no-gutters v-if="!!lexeme.examples && lexeme.examples.length != 0">
              <v-col cols="2"> Beispiele:</v-col>
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
              <v-col cols="2"> Kategorien:</v-col>
              <v-col>
        <span v-for="(category, index) in lexeme.categories" :key="category.id">
          <span>{{ category.category }}</span>
          <span v-if="index + 1 < lexeme.categories.length">, </span>
        </span>
              </v-col>
            </v-row>

            <v-row no-gutters v-if="!!lexeme.origin">
              <v-col cols="2"> Bundesland:</v-col>
              <v-col>
                {{ lexeme.origin }}
              </v-col>
            </v-row>
            <v-row no-gutters v-if="!!lexeme.dialect">
              <v-col cols="2"> Dialekt:</v-col>
              <v-col>
                {{ lexeme.dialect }}
              </v-col>
            </v-row>

            <v-row
                no-gutters
                v-if="!!lexeme.pronunciations && lexeme.pronunciations.length != 0"
            >
              <v-col cols="2"> Aussprache:</v-col>
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
              <v-col cols="2"> Etymology:</v-col>
              <v-col>
        <span v-for="(etymology, index) in lexeme.etymologies" :key="etymology.id">
          <span>{{ etymology.etymology }}</span>
          <span v-if="index + 1 < lexeme.etymologies.length">, </span>
        </span>
              </v-col>

            </v-row>
          </v-col>
        </v-col>
      </v-row>
      <v-divider class="mt-5 mb-5"></v-divider>
      <v-row no-gutters>
        <v-col cols="6">
          <p class="text-h4">Kommentare</p>

          <v-list>
            <v-list-item>
              <v-textarea
                  label="Kommentar verfassen "
                  v-model="postText"
                  outlined
                  rows="1"
                  no-resize
                  append-icon="mdi-send"
                  @click:append="createPost"
                  class="ma-0 pa-0"
                  ref="postText"
                  required
                  :rules="[(v) => !!v || 'Bitte gib einen Text ein']"
              ></v-textarea>
            </v-list-item>

            <template v-for="(post, index) in posts">
              <v-list-item :key="index">

                <v-list-item-content>
                  <v-list-item-text>{{ post.text }}</v-list-item-text>
                  <v-list-item-subtitle>{{ post.author.username }}</v-list-item-subtitle>
                  <card-post :post="post" class="mt-1 mr-5"></card-post>
                </v-list-item-content>

              </v-list-item>
              <v-divider :key="index"></v-divider>

            </template>
          </v-list>
        </v-col>
      </v-row>

    </v-container>
  </perfect-scrollbar>

</template>

<script>
import RequestHandler from "../utils/RequestHandler.js";

export default {
  data: () => ({
    lexeme: null,
    postText: '',
    posts: [],
  }),
  created() {
    RequestHandler.getLexeme(this.$route.params.id).then((response) => {
      this.lexeme = response.data;
    });
    RequestHandler.getPostsByLexemeId(this.$route.params.id).then((response) => (this.posts = response.data));
  },
  methods: {
    createPost() {
      if (this.$refs.postText.validate()) {
        RequestHandler.createPost(this.postText, null, this.$route.params.id).then((response) => {
          this.postText = "";
          this.posts.push(response.data);
        });
      }
    }
  },
};
</script>

<style>
.ps {
  height: 85vh;
}
</style>