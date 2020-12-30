<template>
  <div>
    <v-row>
      <v-col cols="12" sd="4" md="3"> 
        <collection-create-button @created=collectionCreated></collection-create-button>
      </v-col>
      <v-col
        cols="12"
        sd="4"
        md="3"
        v-for="collection in collections"
        :key="collection.id"
      >
        <card-collection :collection="collection"></card-collection>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import CardCollection from "../components/CardCollection.vue";
import CollectionCreateButton from '../components/CollectionCreateButton.vue';
export default {
  name: "Collections",

  components: { CardCollection, CollectionCreateButton },
  data: () => ({
    collections: [],
  }),
  methods:{
    collectionCreated(value){
      this.collections.push(value)
    },
  },
  beforeRouteEnter(to, from, next) {
    RequestHandler.getCollections().then((response) =>
      next((vm) => {
        (vm.collections = response.data), console.log(response);
      })
    );
  },
};
</script>

<style scoped>
</style>