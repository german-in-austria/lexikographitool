<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <p class="text-h3">Fragen</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>

        <!--        <v-text-field-->
        <!--            v-model="search"-->
        <!--            append-icon="mdi-magnify"-->
        <!--            label="Suche"-->
        <!--            single-line-->
        <!--            class="pa-5"-->
        <!--        ></v-text-field>-->
        <v-row no-gutters>
          <v-col cols="12" sd="6" md="4">
            <v-textarea outlined class="post-textarea" placeholder="Stell der Community eine Frage!" v-model="newPost"
                        auto-grow

                        rows="6"
                        append-icon="mdi-send"
                        @click:append="createPost"></v-textarea>
          </v-col>
          <v-col cols="12" sd="6" md="4" v-for="(post, index) in posts" :key="index">
            <card-post :post="post" ></card-post>
          </v-col>
        </v-row>
      </v-col>


    </v-row>
  </v-container>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import CardPost from "@/components/CardPost";
import Axios from "axios";

export default {
  name: "Postings"
  ,
  components: {CardPost},
  data: () => ({
    posts: [],
    myposts: [],
    search: '',
    newPost: '',
  }),
  async created() {
    RequestHandler.getPosts().then((response) => (this.posts = response.data));
    RequestHandler.getOwnPosts().then((response) => (this.myposts = response.data));
  },
  watch: {
    search: function () {
      RequestHandler.getPostsFiltered(this.search).then(response => this.posts = response.data)
    }
  },
  methods: {
    createPost() {
      Axios.post('post/', {text: this.newPost}).then(response => this.posts.push(response.data))
    }
  }
}
</script>

<style scoped>
.post-textarea {
  max-height: 250px;
  overflow-y: auto;
}
</style>