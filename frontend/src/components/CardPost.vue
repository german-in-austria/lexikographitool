<template>
  <v-hover v-slot="{ hover }">
    <v-card :elevation="hover ? 2 : 0" outlined :to="'posting/' + post.id">
      <v-card-subtitle
        ><v-icon> mdi-account</v-icon>
        <span>{{ post.author.username }}</span></v-card-subtitle
      >
      <v-card-title>{{ post.text }}</v-card-title>
      <v-card-actions v-if="!answer">
        <v-btn icon>
          <v-icon>mdi-thumb-up-outline</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-thumb-down-outline</v-icon>
        </v-btn>
        <v-spacer> </v-spacer>
        <v-icon @click.prevent="setAnswer">mdi-comment</v-icon>
      </v-card-actions>

      <v-card-actions v-else>
        <v-text-field
          v-model="answerText"
          ref="answerInput"
          outlined
          @keydown.esc="answer = false"
          append-icon="mdi-send"
          @click:append="sendAnswer"
          prepend-inner-icon="mdi-close"
          @click:prepend-inner="answer = false"
          required
          :rules="[(v) => !!v || 'Bitte gib eine Antwort ein']"
        ></v-text-field>
      </v-card-actions>
      <div  v-if="recursive">
      <card-post class="ml-5" :post="child" v-for="child in post.children" :key="child.id" :recursive="true"></card-post>
    </div>
    </v-card>
  </v-hover>
</template>


<script>
import RequestHandler from "../utils/RequestHandler";
export default {
  name: 'card-post',
  props: ["post", "recursive"],
  data: () => ({
    answer: false,
    answerText: "",
  }),
  methods: {
    setAnswer() {
      this.answer = true;
      this.$nextTick(() => this.$refs.answerInput.focus());
    },
    sendAnswer() {
      this.$nextTick(() => this.$refs.answerInput.blur());
      if (this.$refs.answerInput.validate()) {
        RequestHandler.createPost(this.answerText, this.post.id).then(
          (response) => {
            this.answer = false;
            this.answerText = "";
            console.log(response);
          }
        );
      }
    },
  },
};
</script>