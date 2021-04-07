<template>
  <v-container v-if="lexeme">
    <v-row>
      <v-col cols="12" lg="">
        <card-dialect
            :all-information="true"
          style="max-width: 25rem; margin: auto"
          :card="lexeme"
        >
          <template slot="button"> </template>
        </card-dialect>
      </v-col>
    </v-row>
    <v-row no-gutters v-if="similarDialectWords.length != 0">
      <v-col cols="12"
        ><p class="text-h6">
          andere Begriffe für {{ lexeme.dialectWord }}
        </p></v-col
      >
      <v-col v-for="(item, index) in similarDialectWords" :key="index">
        <v-card
          elevation="0"
          :color="color(item) + ' lighten-4'"
          :to="'/lexeme/' + item.id"
        >
          <v-card-text
            ><span v-if="!!item.word">{{ item.word }}</span
            ><span v-else>{{ item.description }}</span></v-card-text
          >
        </v-card>
      </v-col>
    </v-row>
    <v-row no-gutters v-if="similarWords.length != 0">
      <v-col
        ><p class="text-h6">andere Begriffe für {{ lexeme.word }}</p></v-col
      >
      <v-col v-for="(item, index) in similarWords" :key="index" cols="12">
        <v-card
          elevation="0"
          :color="color(item) + ' lighten-4'"
          :to="'/lexeme/' + item.id"
        >
          <v-card-text>{{ item.dialectWord }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <p class="text-h4">Kommentare</p>
    <v-list>
      <template>
        <div v-for="(post, index) in posts" :key="index">
          <v-list-item dense>
            <v-list-item-content>
              <v-list-item-content>{{ post.text }}</v-list-item-content>
              <v-list-item-subtitle
                >{{ post.author.username }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
        </div>
      </template>

      <v-list-item>
        <v-textarea
          label="Kommentar verfassen "
          v-model="postText"
          flat
          hide-details
          dense
          rows="1"
          no-resize
          outlined
          append-icon="mdi-send"
          @click:append="createPost"
          ref="postText"
          required
          :rules="[(v) => !!v || 'Bitte gib einen Text ein']"
        ></v-textarea>
      </v-list-item>
    </v-list>
  </v-container>
</template>

<script>
import RequestHandler from "../utils/RequestHandler.js";
import CardDialect from "@/components/CardDialect";
import axios from "axios";

export default {
  components: { CardDialect },
  data: () => ({
    lexeme: null,
    postText: "",
    posts: [],
    similarDialectWords: [],
    similarWords: [],
  }),
  created() {
    RequestHandler.getLexeme(this.$route.params.id).then((response) => {
      this.lexeme = response.data;
    });
    RequestHandler.getPostsByLexemeId(this.$route.params.id).then(
      (response) => (this.posts = response.data)
    );
    axios
      .get("lexemes/similar/" + this.$route.params.id + "/?dialectword")
      .then((response) => (this.similarDialectWords = response.data));
    axios
      .get("lexemes/similar/" + this.$route.params.id + "/")
      .then((response) => (this.similarWords = response.data));
  },
  methods: {
    createPost() {
      if (this.$refs.postText.validate()) {
        RequestHandler.createPost(this.postText, null, this.lexeme.id).then(
          (response) => {
            this.postText = "";
            this.posts.push(response.data);
          }
        );
      }
    },
    addToFavorites() {
      RequestHandler.addLexemeToFavorite(this.lexeme.id).then(
        () => (this.lexeme.in_favorites = true)
      );
    },
    removeFromFavorites() {
      RequestHandler.removeLexemeFromFavorite(this.lexeme.id).then(
        () => (this.lexeme.in_favorites = false)
      );
    },
    color(lexeme) {
      const crypto = require("crypto");
      const hash = crypto
        .createHash("sha1")
        .update(lexeme.dialectWord + lexeme.word + lexeme.description)
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
  computed: {},
};
</script>

<style>
.ps {
  height: 85vh;
}
</style>