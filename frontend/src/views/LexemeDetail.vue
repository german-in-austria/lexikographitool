<template>
  <v-container v-if="lexeme">

    <v-row no-gutters>
      <v-col cols="12" lg="">
        <span class="text-h3">{{ lexeme.dialectWord }}</span>
        <report-dialog :button="true" kind="lexeme" :item="lexeme"></report-dialog>
        <lexeme-edit-dialog
            v-if="lexeme.can_edit"
            style="display: inline-block; float: right" :lexeme='lexeme'></lexeme-edit-dialog>

        <card-dialect
            class="elevation-3"
            style="max-width: 25rem; margin: auto"
            :card="lexeme"
        >
          <template slot="button">

          </template>

        </card-dialect>


      </v-col>
      <v-col cols="12" lg="2" class="ml-3" v-if="similarLexemes.length!= 0">
        <span class="text-caption">ähnliche Wörter</span>
        <v-row>
          <v-col v-for="(item, index) in similarLexemes" :key="index" cols="12">

            <v-card :color="color(item)" :to="'/lexeme/' + item.id">
              <v-card-text>{{ item.dialectWord }}</v-card-text>
            </v-card
            >
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row></v-row>
    <p class="text-h4">Kommentare</p>
    <v-list>
      <template>
        <div v-for="(post, index) in posts" :key="index">
          <v-list-item dense>
            <v-list-item-content>
              <v-list-item-content>{{ post.text }}</v-list-item-content>
              <v-list-item-subtitle>{{
                  post.author.username
                }}
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
            solo
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
import LexemeEditDialog from "@/components/LexemeEditDialog";
import axios from "axios";
import ReportDialog from "@/components/ReportDialog";

export default {
  components: {ReportDialog, CardDialect, LexemeEditDialog},
  data: () => ({
    lexeme: null,
    postText: "",
    posts: [],
    similarLexemes: [],
  }),
  created() {
    RequestHandler.getLexeme(this.$route.params.id).then((response) => {
      this.lexeme = response.data;
    });
    RequestHandler.getPostsByLexemeId(this.$route.params.id).then(
        (response) => (this.posts = response.data)
    );
    axios
        .get("lexemes/similar/" + this.$route.params.id + "/")
        .then((response) => (this.similarLexemes = response.data));
  },
  methods: {
    createPost() {
      if (this.$refs.postText.validate()) {
        RequestHandler.createPost(
            this.postText,
            null,
            this.lexeme.id
        ).then((response) => {
          this.postText = "";
          this.posts.push(response.data);
        });
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
        "#f1d8c5",
        "#f9f0c2",
        "#b1d4ec",
        "#b3b8df",
        " #ece9dd",
        "#ffb3ba",
        "#ffffba",
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