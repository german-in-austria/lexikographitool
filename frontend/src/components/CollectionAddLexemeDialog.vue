<template>
  <v-dialog
      v-model="dialog"
      max-width="60vh"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
          v-bind="attrs"
          v-on="on"
      >
        weitere Wörter suchen
      </v-btn>
    </template>
    <v-card
        height="80vh">
      <v-card-text>
        <v-card-title></v-card-title>

        {{ search }}
        <v-text-field label="Suche" v-model="search"> Suchen</v-text-field>
        <v-list>
          <v-list-item v-if="loading">
            <v-progress-circular
                :size="50"
                color="primary"
                indeterminate
            ></v-progress-circular>
          </v-list-item>
          <v-list-item v-for="(item,index) in items" :key="index">
            <v-icon v-if="!item.in_collection" @click="addToCollection(item)">mdi-plus</v-icon>
            <v-icon v-else @click="removeFromCollection(item)">mdi-delete</v-icon>
            <span class="font-weight-bold">{{ item.dialectWord }}</span>, {{ item.word }} {{ item.description }}

          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import axios from "axios";

export default {
  name: "CollectionAddLexemeDialog",
  props: ['collection'],
  data: () => ({
    dialog: false,
    items: [],
    loading: true,
    search: '',
  }),
  watch: {
    dialog(visible) {
      if (visible) {
        this.loading = true,
            axios.get('/lexemes/?page=' + 1 + '&search=' + '&collection=' + this.collection.id).then((response) => {
              this.items = response.data.results,
                  // this.pageCount = response.data.total_pages,
                  this.count = response.data.count,
                  this.loading = false
            })

      }
    },
    search(keyword) {
      this.loading = true,
          axios.get('/lexemes/?page=' + 1 + '&search=' + keyword + '&collection=' + this.collection.id).then((response) => {
            this.items = response.data.results,
                // this.pageCount = response.data.total_pages,
                this.count = response.data.count,
                this.loading = false
          })
    }
  },
  methods: {
    addToCollection(item) {
      RequestHandler.addLexemeToCollection(this.collection.id, item.id).then(() => {
            item.in_collection = true
            this.collection.lexemes.push(item)
          }
      )
    },
    removeFromCollection(item) {
      axios.delete(`collection/${this.collection.id}/${item.id}/`).then(() => {
        item.in_collection = false
        var index = this.collection.lexemes.map(function(e) { return e.id; }).indexOf(item.id);
        this.collection.lexemes.splice(index, 1);
      })
    }
  }
}
</script>

<style scoped>

</style>