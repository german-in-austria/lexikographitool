<template>
  <v-card outlined>
    <v-card-title>{{ post.text }}</v-card-title>
    <v-card-actions v-if="!answer">
      <v-icon> mdi-account</v-icon>
      <span>{{ post.author.username }}</span>
      <v-spacer> </v-spacer>
      <v-icon @click="setAnswer">mdi-comment</v-icon>
    </v-card-actions>
    <v-card-actions v-else>
      <v-text-field
      v-model="answerText"
        ref="answerInput"
        outlined
        @keydown.esc="answer = false"
        append-icon="mdi-send"
        @click:append="sendAnswer"
        required
        :rules="[(v) => !!v || 'Bitte gib eine Antwort ein']"
      ></v-text-field>
    </v-card-actions>
  </v-card>
</template>


<script>
import RequestHandler from "../utils/RequestHandler";
export default {
  props: ["post"],
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