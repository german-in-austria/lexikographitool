<template>
  <div>
    <v-row no-gutters>
      <v-col>
        <p class="text-h5">meine Wörter</p>
        <div v-for="card in ownCards" :key="card.id">
          <card-dialect :card="card"></card-dialect>
        </div>
      </v-col>
      <v-col>
        <p class="text-h5">meine Sammlungen</p>
        <div v-for="collection in collections" :key="collection.id">
          <card-collection :collection="collection"></card-collection>
        </div>
      </v-col>
      <v-col>
        <p class="text-h5">allgemeines Wörterbuch</p>
        <div v-for="card in cards" :key="card.id">
          <card-dialect :card="card"></card-dialect>
        </div>
      </v-col>
      <v-col>
        <p class="text-h5">aktuelle Aufrufe</p>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import CardDialect from "../components/CardDialect.vue";
import CardCollection from '../components/CardCollection.vue';

export default {
  components: { CardDialect, CardCollection },

  data: () => ({
    cards: [],
    ownCards: [],
    collections: [],
  }),
  
  async created() {
    RequestHandler.getCards().then((response) => this.cards =  response.data);
    RequestHandler.getCollections().then((response) => this.collections =  response.data);
    RequestHandler.getCardsCreated().then((response) => this.ownCards =  response.data);
  },
};
</script>