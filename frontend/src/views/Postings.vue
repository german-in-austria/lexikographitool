<template>
  <v-container fluid >
    <v-row>
      <v-col >
        <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Suche"
            single-line
            class="pa-5"
        ></v-text-field>
        <v-row no-gutters>
        <v-col cols="12" sd="6" md="4" v-for="(post, index) in posts" :key="index">
          <card-post :post="post" class="ma-1"></card-post>
        </v-col>
        </v-row>
      </v-col>

      <v-divider vertical ></v-divider>
      <v-col cols="3">
        <v-subheader>Meine Aufrufe</v-subheader>
        <v-col cols="12" v-for="(post, index) in myposts" :key="index">
          <card-post :post="post" class="ma-1"></card-post>
        </v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import CardPost from "@/components/CardPost";

export default {
  name: "Postings"
  ,
  components: {CardPost},
  data: () => ({
    posts: [],
    myposts: [],
    search:''
  }),
  async created() {
    RequestHandler.getPosts().then((response) => (this.posts = response.data));
    RequestHandler.getOwnPosts().then((response) => (this.myposts = response.data));
  },
  watch:{
    search: function (){
      RequestHandler.getPostsFiltered(this.search).then(response=>this.posts = response.data)
}
  }
}
</script>

<style scoped>

</style>