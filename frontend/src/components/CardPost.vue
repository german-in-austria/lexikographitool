<template>
  <v-dialog v-model="dialog" width="500">
    <template v-slot:activator="{ on, attrs }">
      <v-hover v-slot="{ hover }">
        <v-card
          :elevation="hover ? 5 : 0"
          outlined
          class="transition-swing"
          :color="color + ' lighten-4'"
        >
          <v-card-subtitle style="height: 70px">
            <p class="text--primary">
              <v-icon> mdi-account</v-icon>{{ post.author.username }}
            </p>
            <p
              style="margin-left: 5px; margin-top: -15px"
              class="text--accent-1 text--secondary"
            >
              {{ dateCreated }}
            </p>
          </v-card-subtitle>
          <v-card-text v-if="!edit">
            <p class="text-body-1">{{ post.text }}</p>
            <p
              style="margin-top: -18px"
              class="text--disabled"
              v-if="post.edited"
            >
              bearbeitet
            </p>
          </v-card-text>
          <v-card-text v-else>
            <v-textarea
              rows="2"
              solo
              flat
              dense
              v-model="newText"
              @keyup.enter="updatePost"
            ></v-textarea>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-icon v-bind="attrs" v-on="on">mdi-comment </v-icon>

            <v-menu left>
              <template v-slot:activator="{ on, attrs }">
                <v-icon
                  style="position: absolute; top: 6px; right: 6px"
                  v-bind="attrs"
                  v-on="on"
                  >mdi-dots-vertical
                </v-icon>
              </template>
              <v-list>
                <v-list-item
                  v-if="post.is_author"
                  @click="
                    newText = post.text;
                    edit = !edit;
                  "
                  >{{ $t("postings.edit") }}</v-list-item
                >
                <v-list-item v-if="post.is_author" @click="deletePost">{{
                  $t("postings.delete")
                }}</v-list-item>
                  <report-dialog :item="post" kind="post"></report-dialog>
                
              </v-list>
            </v-menu>
          </v-card-actions>
        </v-card>
      </v-hover>
    </template>
    <v-card>
      <v-card-title :class="color + ' lighten-4'">
        {{ $t("postings.commentTitle") }}
      </v-card-title>

      <v-card-text>
        <p
          v-if="!!children && children.length == 0"
          v-html="
            $t('postings.noCommentMessage', { user: post.author.username })
          "
        ></p>
        <div v-for="(answer, index) in children" :key="index">
          <v-list-item-subtitle class="font-weight-bold">{{
            answer.author.username
          }}</v-list-item-subtitle>

          <v-list-item-title>{{ answer.text }}</v-list-item-title>
        </div>
      </v-card-text>
      <v-spacer></v-spacer>
      <v-card-actions class="overflow-x-hidden">
        <v-textarea
          class="post-textarea"
          v-model="answerText"
          rows="1"
          auto-grow
          placeholder="Kommentieren ..."
          dense
          outlined
          @keyup.enter="sendAnswer"
        ></v-textarea>
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
import moment from "moment";
import ReportDialog from "@/components/ReportDialog";

export default {
  name: "card-post",
  components: { ReportDialog },
  props: ["post"],
  data: () => ({
    answer: false,
    answerText: "",
    dialog: false,
    children: null,
    edit: false,
    newText: "",
  }),
  methods: {
    sendAnswer() {
      RequestHandler.createPost(this.answerText, this.post.id).then(
        (response) => {
          this.answer = false;
          this.answerText = "";
          this.children.push(response.data);
        }
      );
    },
    updatePost() {
      Axios.put("/post/" + this.post.id + "/", { text: this.newText });
      this.edit = false;
      this.post.edited = true;
      this.post.text = this.newText;
    },
    deletePost() {
      Axios.delete("post/" + this.post.id + "/");
      this.$emit("deleted");
    },
    reportsPost() {
      Axios.delete("post/" + this.post.id + "/");
      this.$emit("deleted");
    },
  },
  watch: {
    dialog() {
      Axios.get("posts/" + this.post.id + "/").then(
        (response) => (this.children = response.data)
      );
    },
    "post.text": function (val) {
      this.newText = val;
    },
  },
  computed: {
    color() {
      const crypto = require("crypto");
      const hash = crypto
        .createHash("sha1")
        .update(this.post.id + this.post.author)
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
    dateCreated() {
      moment.locale("de");
      return moment(this.post.date_created).fromNow();
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