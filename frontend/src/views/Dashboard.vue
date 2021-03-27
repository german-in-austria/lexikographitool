<template>
  <v-container style="max-width: 2000rem !important;" fluid>
    <div class="hidden-md-and-up">
    <p class="text-h4">{{ $t("dashboard.title") }}</p>
    <p class="text-h5">{{ $t("dashboard.myWords") }}</p>

    <div class="scrollmenu">
      <div v-for="(item,index) in myWords"
           :key="index" class="card" >
        <card-dialect :small="true" :card="item"></card-dialect>

      </div>
    </div>

    <p class="text-h5">{{ $t("dashboard.myCollections") }}</p>
    <div class="scrollmenu">
      <div class="card" style="min-width: 180px">
        <collection-create-button
        ></collection-create-button>
      </div>
      <div v-for="(item,index) in myCollections"
           :key="index" class="card">

        <card-collection style="padding-left: 10px" :collection="item"></card-collection>

      </div>
    </div>

      <p class="text-h5">{{ $t("dashboard.discover") }}</p>
      <div class="scrollmenu">

        <div v-for="(item,index) in randomLexemes"
             :key="index" class="card">

          <card-dialect :small="true" :card="item"></card-dialect>

        </div>
      </div>

    <p class="text-h5">{{ $t("dashboard.discover") }}</p>
    <div class="scrollmenu">

      <div v-for="(item,index) in posts"
           :key="index" class="card">

        <card-post :small="true" :post="item"></card-post>

      </div>
    </div>
    </div>

    <div class="hidden-sm-and-down"
         :style="$vuetify.breakpoint.lgAndUp ? ' height:85vh;margin-left:10rem;' : ' height:85vh;' + ' margin-top:3rem;'">

      <v-row no-gutters style="height: 100%">
        <v-col cols="3" style="height: 85%">
          <p class="text-h5">{{ $t("dashboard.myWords") }}</p>

          <v-hover v-slot="{ hover }">
            <v-card
                :to="'card-create'"
                class="mt-1 mr-5 mb-1"
                :elevation="hover ? 4 : 0"
                outlined
            >
              <v-card-actions class="justify-center"
              >
                <v-icon
                    size="48
"
                >mdi-plus
                </v-icon
                >
              </v-card-actions
              >
            </v-card>
          </v-hover>
          <perfect-scrollbar>
            <div v-for="card in myWords" :key="card.id">
              <card-dialect :card="card" class="mt-1 mr-5"></card-dialect>
            </div>
          </perfect-scrollbar>
        </v-col>
        <v-col cols="3" style="height: 85%">
          <p class="text-h5">{{ $t("dashboard.myCollections") }}</p>

          <collection-create-button
              class="mt-1 mr-5 mb-1"
          ></collection-create-button>
          <perfect-scrollbar>
            <div v-for="collection in myCollections" :key="collection.id">
              <card-collection
                  :collection="collection"
                  class="mt-1 mr-5"
              ></card-collection>
            </div>
          </perfect-scrollbar>
        </v-col>
        <v-col cols="3" style="height: 93%">
          <p class="text-h5">{{ $t("dashboard.discover") }}</p>

          <perfect-scrollbar>
            <div v-for="card in randomLexemes" :key="card.id">
              <card-dialect :card="card" class="mt-1 mr-5"></card-dialect>
            </div>
          </perfect-scrollbar>
        </v-col>
        <v-col cols="3" style="height: 100%">
          <p class="text-h5">{{ $t("dashboard.posts") }}</p>
          <perfect-scrollbar>
            <div v-for="post in posts" :key="post.id">
              <card-post :post="post" class="mt-1 mr-5"></card-post>
            </div>
          </perfect-scrollbar>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import axios from "axios";
import CardDialect from "@/components/CardDialect";
import CardCollection from "@/components/CardCollection";
import CollectionCreateButton from "@/components/CollectionCreateButton";
import CardPost from "@/components/CardPost";

export default {
  name: "Dashboard",
  components: {CardPost, CollectionCreateButton, CardCollection, CardDialect},
  data: () => ({
    myWords: [],
    myCollections: [],
    randomLexemes: [],
    posts: [],
    myWordsNext: null,
    myCollectionsNext: null,
    postsNext: null,
  }),
  mounted() {
    axios
        .get("/lexemes/?mine")
        .then((response) => {
          (this.myWords = response.data.results),
              this.myWordsNext = response.data.links.next;
        })

    axios
        .get("/collections/")
        .then((response) => {
          (this.myCollections = response.data.results),
              this.myCollectionsNext = response.data.links.next;
        })


    axios.get("/lexemes/random/")
        .then((response) => {
          (this.randomLexemes = response.data)
        })

    axios.get("/posts/?ordering=-date_created")
        .then((response) => {
          (this.posts = response.data.results),
              this.postsNext = response.data.links.next;

        })
  },

}
</script>

<style scoped>
.scrollmenu {
  overflow: auto;
  white-space: nowrap;
}

.card {

  display: inline-block;
  color: white;
  padding: 14px;
  text-decoration: none;
  max-width: 300px;
  vertical-align: middle;
}
.ps {
  height: 100%;
}
</style>