<template>
  <v-dialog
      v-model="dialog"
      width="500"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-hover v-slot="{ hover }">
        <v-card :elevation="hover ? 5 : 0" outlined
                class=" transition-swing"
                :color="color + ' lighten-4'"


        >
          <v-card-subtitle
          >
            <v-icon> mdi-account</v-icon>
            <span>{{ post.author.username }}</span></v-card-subtitle
          >
          <v-card-text>{{ post.text }}</v-card-text>
          <v-card-actions>
            <v-btn icon>
              <v-icon>mdi-thumb-up-outline</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-icon
                v-bind="attrs"
                v-on="on">mdi-comment
            </v-icon>
          </v-card-actions>
        </v-card>
      </v-hover>
    </template>
    <v-card
        :color="color + ' lighten-4'">

      <v-card-title class="elevation-5">
        Kommentieren
      </v-card-title>

      <v-card-text>
          <div v-for="(answer,index) in children" :key="index">
                <v-list-item-subtitle class="font-weight-bold">{{ answer.author.username }}</v-list-item-subtitle>

                <v-list-item-title>{{ answer.text }}</v-list-item-title>
          </div>

      </v-card-text>
      <v-spacer></v-spacer>
      <v-card-actions  class="overflow-x-hidden elevation-5">
        <v-textarea class="post-textarea" v-model="answerText" rows="1" auto-grow placeholder="Kommentieren ..." dense
                    outlined
        @keyup.enter="sendAnswer"></v-textarea>
        <v-scroll-x-reverse-transition>
          <v-btn @click="sendAnswer" v-if="!!answerText" icon>
            <v-icon>mdi-send</v-icon>
          </v-btn>
        </v-scroll-x-reverse-transition>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<script>
import RequestHandler from "../utils/RequestHandler";
import Axios from "axios";

export default {
  name: 'card-post',
  props: ["post",],
  data: () => ({
    answer: false,
    answerText: "",
    dialog: false,
    children: null,

  }),
  methods: {
    sendAnswer() {
        RequestHandler.createPost(this.answerText, this.post.id).then(
            (response) => {
              this.answer = false;
              this.answerText = "";
              this.children.push(response.data)
            }
        );

    },
  },
  watch: {
    dialog() {
      Axios.get('post/' + this.post.id + '/').then(response => this.children = response.data.children)

    }
  },
  computed: {
    color() {
      const crypto = require("crypto");
      const hash = crypto
          .createHash("sha1")
          .update(this.post.text)
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
};
</script>

<style>

.post-textarea {
  max-height: 150px;
  overflow: auto;
}
</style>