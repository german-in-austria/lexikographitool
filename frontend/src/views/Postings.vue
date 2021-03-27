<template>
  <v-container fluid v-scroll='onScroll'>
    <v-row>
      <v-col>
        <p class="text-h3">Fragen</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-row>
          <v-col cols="12" sd="6" md="4">
            <v-textarea outlined class="post-textarea" placeholder="Stell der Community eine Frage!" v-model="newPost"
                        auto-grow

                        rows="6"
                        append-icon="mdi-send"
                        @click:append="createPost"></v-textarea>
          </v-col>
        </v-row>

        <v-scale-transition group class="row">
          <v-col cols="12" sd="6" md="4" v-for="(post,index) in posts" :key="post.id">
            <card-post :post="post" @deleted="removeFromList(index)"></card-post>
          </v-col>
        </v-scale-transition>
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
    next:null,
  }),
  async created() {
    RequestHandler.getPosts().then((response) => {
      this.posts = response.data.results
    this.next = response.data.links.next
  })
  RequestHandler.getOwnPosts().then((response) => (this.myposts = response.data));
}
,
watch: {
  search: function () {
    RequestHandler.getPostsFiltered(this.search).then(response => this.posts = response.data)
  }
}
,
methods: {
  createPost()
  {
    Axios.post('post/', {text: this.newPost}).then(response => this.posts.push(response.data))
  }
,
  removeFromList(index)
  {
    this.posts.splice(index, 1);
  }
,
  onScroll(e)
  {
    console.log(this.next);
    if (
        e.target.scrollingElement.scrollTop + 400 >
        e.target.scrollingElement.scrollTopMax &&
        !!this.next
    ) {
      const next = this.next
      this.next = null;

      Axios.get(next).then((response) => {
        this.posts = this.posts.concat(response.data.results);
        this.next = response.data.links.next
      });
    }
  }
,
}
}
</script>

<style scoped>
.post-textarea {
  max-height: 250px;
  overflow-y: auto;
}

.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */
{
  opacity: 0;
  transform: translateY(30px);
}
</style>