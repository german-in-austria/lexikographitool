<template>
  <v-dialog v-model="dialog" scrollable max-width="60vh">
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" elevation="0" large> {{$t("collectionDetail.addWords")}} </v-btn>
    </template>
    <v-card height="80vh">
      <v-card-title>{{$t("collectionDetail.addWords")}}</v-card-title>

      <v-card-text>
        <v-text-field label="Suche" v-model="search">{{$t("general.search")}}</v-text-field>
      </v-card-text>
      <v-card-text v-scroll.self="onScroll">
        <v-list>
          <v-list-item v-if="loading">
            <v-progress-circular
              :size="50"
              color="primary"
              indeterminate
            ></v-progress-circular>
          </v-list-item>
          <v-list-item v-for="(item, index) in items" :key="index">
            <v-scroll-y-transition mode="out-in">
            <v-icon key=1  v-if="!item.in_collection" @click="addToCollection(item)"
              >mdi-plus</v-icon>
            <v-icon key=2 v-else @click="removeFromCollection(item)"
              >mdi-delete</v-icon
            >
            ></v-scroll-y-transition>

            <span class="font-weight-bold">{{ item.dialectWord }}</span
            >, {{ item.word }} {{ item.description }}
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
  props: ["collection","lexemes"],
  data: () => ({
    dialog: false,
    items: [],
    loading: true,
    search: "",
    page: 1,
    next: null,
  }),
  watch: {
    dialog(visible) {
      this.page = 1;
      if (visible) {
        (this.loading = true),
          axios
            .get(
              "/lexemes/?page=" +this.page
                +"&search=" +
                "&in_collection=" +
                this.collection.id
            )
            .then((response) => {
              (this.items = response.data.results),
                // this.pageCount = response.data.total_pages,
                (this.count = response.data.count),
                (this.loading = false);
              this.next = response.data.links.next;
            });
      }
    },
    search(keyword) {
      this.page=1
      this.loading = true;
      axios
        .get(
          "/lexemes/?page=" +
            this.page +
            "&search=" +
            keyword +
            "&in_collection=" +
            this.collection.id
        )
        .then((response) => {
          (this.items = response.data.results),
            // this.pageCount = response.data.total_pages,
            (this.count = response.data.count),
            (this.loading = false);
          this.next = response.data.links.next;
        });
    },
  },
  methods: {
    addToCollection(item) {
      RequestHandler.addLexemeToCollection(this.collection.id, item.id).then(
        () => {
          item.in_collection = true;
          this.lexemes.push(item);
        }
      );
    },
    removeFromCollection(item) {
      axios.delete(`collection/${this.collection.id}/${item.id}/`).then(() => {
        item.in_collection = false;
        var index = this.lexemes
          .map(function (e) {
            return e.id;
          })
          .indexOf(item.id);
        this.lexemes.splice(index, 1);
      });
    },
    onScroll(e) {
      
      if (e.target.scrollTop === e.target.scrollTopMax && !!this.next) {
        this.page += 1;
        axios
          .get("/lexemes/?page=" + this.page + "&" + this.search+
                "&in_collection=" +
                this.collection.id)
          .then((response) => {
            (this.items = this.items.concat(response.data.results)),
              (this.pageCount = response.data.total_pages),
              (this.count = response.data.count);
            this.next = response.data.links.next;
          })
          .finally(() => (this.loading = false));
      }
    },
  },
};
</script>

<style scoped>
</style>