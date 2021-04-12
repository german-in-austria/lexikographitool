<template>
  <v-container  fluid v-scroll="onScroll">
    <v-row>
      <v-col>
      <p class="text-h4">{{ $t("collections.title") }}</p>

      </v-col>
      <v-col class="col-auto">
        <v-menu left>
          <template v-slot:activator="{ on, attrs }">
            <v-icon v-bind="attrs" v-on="on">mdi-dots-vertical </v-icon>
          </template>
          <v-list>
            <collection-create-button class="d-inline-block"
                                      @created="collectionCreated"

            ><template v-slot="{dialog}">
              <v-list-item @click.stop="dialog.dialog=true">Neue Sammlung erstellen</v-list-item>

            </template></collection-create-button>
      <trash-can-dialog
          :itemList="collections"
          :collection="true"
      ></trash-can-dialog>
          </v-list>
        </v-menu>
      </v-col>
      </v-row>
      <v-row no-gutters>
        <i18n class="text-body-1" path="collections.description" tag="p">
          <template v-slot:createCollection>
            <collection-create-button class="d-inline-block"
                                      @created="collectionCreated"

            ><template v-slot="{dialog}">
              <a class="success--text" @click="dialog.dialog=true">{{$t("collections.createCollection")}}
              </a>
            </template></collection-create-button>
          </template>
        </i18n>
      </v-row>
    <v-row no-gutters class="pt-5">
      <v-text-field
          v-model="search"
          :label=' $t("general.search") '
          single-line
          clearable
          flat
          solo-inverted
          hide-details
          prepend-inner-icon="mdi-magnify"
          class="pr-5"
      ></v-text-field>
      <v-btn-toggle v-model="pub" mandatory :style="$vuetify.breakpoint.xs ? 'flex-direction: column;' : ''">
        <v-btn large :value="false"> {{ $t("collections.myCollections") }}</v-btn>
        <v-btn large :value="true">{{ $t("collections.publicCollections") }}</v-btn>
      </v-btn-toggle>
    </v-row>
    <v-row no-gutters>

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
      <p class="text-body-1" v-if="(!collections.length) & !!search">
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

  components: {CardCollection, CollectionCreateButton, TrashCanDialog},
  data: () => ({
    collections: [],
    search: "",
    pub: false,
    tab: null,
    next: null,
    timeout: null,
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

      clearTimeout(this.timeout);

      let self = this;
      this.timeout = setTimeout(function () {

        self.loadCollections();
      }, 500);
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
      this.collections.unshift(value);
      this.search = "";
    },

    onScroll(e) {
      console.log(this.next);
      if (
          e.target.scrollingElement.scrollTop + 400 >
          e.target.scrollingElement.scrollTopMax &&
          !!this.next
      ) {
        const next = this.next
        this.next = null
        Axios.get(next).then((response) => {
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