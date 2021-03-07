<template>
  <v-container fluid  v-scroll="onScroll">
    <v-row no-gutters>
      <p class="text-h3">Sammlungen</p>
      <p class="text-body-1">
        Hier kannst du Sammlungen erstellen um verschiedenste Wörter zu sammeln
        und zu orden. Schau auch nach welche interessanten Sammlungen andere
        Mietglieder bereits erstellt und öffentlich gemacht haben
      </p>
    </v-row>
    <v-row no-gutters class="pt-5">
      <v-text-field
        v-model="search"
        label="Suche"
        single-line
        clearable
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-magnify"
        class="pr-5"
      ></v-text-field>
      <v-btn-toggle v-model="pub" mandatory :style="$vuetify.breakpoint.xs ? 'flex-direction: column;' : ''" >
        <v-btn large :value="false" > Meine Sammlungen </v-btn>
        <v-btn large :value="true" > öffentliche Sammlungen </v-btn>
      </v-btn-toggle>
      <trash-can-dialog
        :itemList="collections"
        :collection="true"
      ></trash-can-dialog>
    </v-row>
    <v-row no-gutters>
      <v-col cols="12" sd="4" md="3" v-if="!pub" class="pa-3">
        <collection-create-button
          @created="collectionCreated"
        ></collection-create-button>
      </v-col>
      <v-col
        cols="12"
        sd="4"
        md="3"
        v-for="collection in collections"
        :key="collection.id"
        class="pa-3"
      >
        <card-collection :collection="collection"></card-collection>
      </v-col>
      <p class="text-body-1" v-if="(collections.length == 0) & !!search">
        Keine Treffer
      </p>
    </v-row>
  </v-container>
</template>

<script>
import CardCollection from "../components/CardCollection.vue";
import CollectionCreateButton from "../components/CollectionCreateButton.vue";
import TrashCanDialog from "../components/TrashCanDialog.vue";
import Axios from "axios";
export default {
  name: "Collections",

  components: { CardCollection, CollectionCreateButton, TrashCanDialog },
  data: () => ({
    collections: [],
    search: "",
    pub: false,
    tab: null,
    next: null,
  }),
  mounted() {
    Axios.get("/collections/?public=False").then((response) => {
      this.collections = response.data.results;
      this.next = response.data.links.next;
    });
  },
  watch: {
    pub() {
      this.loadCollections();
    },
    search() {
      this.loadCollections();
    },
  },
  methods: {
    loadCollections() {
      //true in python is True
      const public_python_param = this.pub ? "True" : "False";
      Axios.get(
        "/collections/?search=" +
          this.search +
          "&public=" +
          public_python_param
      ).then((response) => {
        this.collections = response.data.results;
        this.next = response.data.links.next;
      });
    },

    collectionCreated(value) {
      this.collections.push(value);
      this.search = "";
    },

    onScroll(e) {
      console.log(this.next);
      if (
        e.target.scrollingElement.scrollTop ===
          e.target.scrollingElement.scrollTopMax &&
        !!this.next
      ) {
        Axios.get(this.next).then((response) => {
          this.collections = this.collections.concat(response.data.results);
          this.next = response.data.links.next;
        });
      }
    },
  },
};
</script>

<style scoped>

</style>