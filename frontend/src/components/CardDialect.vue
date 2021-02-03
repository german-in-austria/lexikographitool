<template>
  <div>
    <v-hover v-slot="{ hover }">
      <v-card :elevation="hover ? 2 : 0" outlined :to="'/lexeme/' + card.id">
        <v-card-text>
          <div>{{ card.word }}</div>
          <p class="display-1 text--primary">
            {{ card.dialectWord }}
          </p>
          <div v-if="card.description">
            Beschreibung: {{ card.description }}
          </div>
          <div v-if="card.examples.length">
            Beispiel:
            <div v-for="example in card.examples" :key="example.id">
              {{ example.example }}
            </div>
          </div>
          <br />
          <p>Dialekt: {{ card.dialect }}</p>
        </v-card-text>
        <v-card-actions>
          <v-btn icon>
            <v-icon>mdi-thumb-up-outline</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-thumb-down-outline</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn icon v-if="!card.in_favorites" @click.prevent="addToFavorites">
            <v-icon >mdi-heart-outline</v-icon>
          </v-btn>
          <v-btn icon v-else @click.prevent="removeFromFavorites">
            <v-icon color="red">mdi-heart</v-icon>
          </v-btn>
            <CollectionAddLexeme :cardId="card.id"></CollectionAddLexeme>

          <v-btn icon>
            <v-icon>mdi-share-variant</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-hover>



  </div>
</template>


<script>
import RequestHandler from "../utils/RequestHandler.js";
import CollectionAddLexeme from "@/components/CollectionAddLexeme";
export default {
  components: {CollectionAddLexeme},
  props: ["card"],
  name: "CardDialect",
  data: () => ({
    collectionsDialog: false,
    collections: [],
  }),
  methods: {
    openCollectionDialog() {
      this.collectionsDialog = true;
      RequestHandler.getCollections().then((response) => {
        this.collections = response.data;
      });
    },
    addToFavorites(){
      RequestHandler.addLexemeToFavorite(this.card.id).then(()=>this.card.in_favorites = true)
    },
    removeFromFavorites(){
      RequestHandler.removeLexemeFromFavorite(this.card.id).then(()=>this.card.in_favorites = false)

    },
  },
};
</script>

<style scoped>
</style>