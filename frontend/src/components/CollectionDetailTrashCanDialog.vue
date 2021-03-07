<template>
  <v-dialog v-model="dialog" scrollable max-width="60vh">
    <template v-slot:activator="{ on, attrs }">
      <v-btn class="pl-5" v-bind="attrs" v-on="on" large outlined>  Papierkorb </v-btn>
    </template>
    <v-card height="80vh">
      <v-card-title>Papierkorb</v-card-title>


      <v-card-text>
        <v-list>
          <v-list-item v-if="loading">
            <v-progress-circular
              :size="50"
              color="primary"
              indeterminate
            ></v-progress-circular>
          </v-list-item>
          <v-list-item v-for="(item, index) in items" :key="index">
            <v-icon @click="restore(item, index)">mdi-plus</v-icon>
            <span class="font-aweight-bold">{{ item.dialectWord }}</span
            >, {{ item.word }} {{ item.description }}
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";
import RequestHandler from "@/utils/RequestHandler";
export default {
  props: ["collectionId", "lexemes"],
  data: () => ({
    dialog: false,
    items: [],
    loading: true,
  }),
  watch: {
    dialog() {
      axios
        .get("collection_lexemes_deleted/" + this.collectionId + "/")
        .then(
          (response) => ((this.items = response.data), (this.loading = false))
        );
    },
  },
  methods: {
    restore(item, index) {
      RequestHandler.addLexemeToCollection(this.collectionId, item.id).then(
        () => {
          this.lexemes.push(item);
          this.items.splice(index, 1);
        }
      );
    },
  },
};
</script>