<template>
  <div>
    <v-row no-gutters>
      <v-col >
        <p class="text-h5 ">meine Wörter</p>
        <div v-for="card in ownCards" :key="card.id">
          <card-dialect :card="card" class="ma-5" ></card-dialect>
        </div>
      </v-col>
      <v-col>
        <p class="text-h5">meine Sammlungen</p>
        <collection-create-button class="ma-5" @created=collectionCreated></collection-create-button>

        <div v-for="collection in collections" :key="collection.id">
          <card-collection :collection="collection" class="ma-5"></card-collection>
        </div>
      </v-col>
      <v-col>
        <p class="text-h5">allgemeines Wörterbuch</p>
        <div v-for="card in cards" :key="card.id">
          <card-dialect :card="card" class="ma-5"></card-dialect>
        </div>
      </v-col>
      <v-col>
        <p class="text-h5">aktuelle Aufrufe</p>
        <v-textarea
          label="neuer Aufruf"
          v-model="postText"
          outlined
          rows="3"
          row-height="25"
          no-resize
          append-icon="mdi-send"
          @click:append="createPost"
          class="ma-5"
        ></v-textarea>
        <div v-for="post in posts" :key="post.id">
        <card-post :post="post" class="ma-5"></card-post>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import CardDialect from "../components/CardDialect.vue";
import CardCollection from "../components/CardCollection.vue";
import CardPost from '../components/CardPost.vue';
import CollectionCreateButton from '../components/CollectionCreateButton.vue';

export default {
  components: { CardDialect, CardCollection, CardPost, CollectionCreateButton },

  data: () => ({
    cards: [],
    ownCards: [],
    collections: [],
    posts: [],
    postText: '',
  }),

  async created() {
    RequestHandler.getCards().then((response) => (this.cards = response.data));
    RequestHandler.getCollections().then(
      (response) => (this.collections = response.data)
    );
    RequestHandler.getCardsCreated().then(
      (response) => (this.ownCards = response.data)
    );
    RequestHandler.getPosts().then((response) => (this.posts = response.data));
  },
  methods:{
      createPost(){
        RequestHandler.createPost(this.postText, null).then((response)=>{
            this.postText = ''
            this.posts.push(response.data)
        });
      },
      
    collectionCreated(value){
      this.collections.push(value)
    },
  }
};
</script>

