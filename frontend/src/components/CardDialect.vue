<template>
  <div>
    <v-hover v-slot="{ hover }">
      <v-card :elevation="hover ? 2 : 0" outlined :to="'lexeme/' + card.id">
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
          <v-btn icon @click.prevent="openCollectionDialog()">
            <v-icon>mdi-plus</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-share-variant</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-hover>

    <v-dialog v-model="collectionsDialog" width="500">
      <v-list>
        <v-subheader>Meine Sammlungen</v-subheader>
        <v-list-item v-for="collection in collections" :key="collection.id">
          <v-list-item-title>
            {{ collection.name }}
          </v-list-item-title>
          <v-list-item-icon>
            <v-btn icon @click.prevent="addLexemeToCollection(collection.id)">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-list-item-icon>
        </v-list-item>
      </v-list>
    </v-dialog>
  </div>
</template>


<script>
import RequestHandler from "../utils/RequestHandler.js";
export default {
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
        console.log(response);
      });
    },
    addLexemeToCollection(collectionId) {
      RequestHandler.addLexemeToCollection(collectionId, this.card.id).then();
    },
  },
};
</script>

<style scoped>
</style>