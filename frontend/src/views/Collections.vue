<template>
  <div>
    <v-row>
      <v-col cols="12" sd="4" md="4">
        <v-hover v-slot="{ hover }">
          <v-card
            @click.prevent="dialog = true"
            :elevation="hover ? 12 : 2"
            class="mx-auto"
            max-width="300"
          >
            <v-card-actions class="justify-center"
              ><v-icon
                size="48
"
                >mdi-plus</v-icon
              ></v-card-actions
            >
          </v-card>
        </v-hover>
      </v-col>
      <v-col
        cols="12"
        sd="4"
        md="4"
        v-for="collection in collections"
        :key="collection.id"
      >
        <card-collection :collection="collection"></card-collection>
       
        
      </v-col>
    </v-row>

    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title>
          <span class="headline">Neue Sammlung</span>
        </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="collectionTitle"
            label="Titel"
            required
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click.prevent="createCollection"
            >erstellen
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import Collection from "@/objects/Collection";
import CardCollection from '../components/CardCollection.vue';
export default {
  name: "Collections",
 
  components: { CardCollection },
  data: () => ({
    collections: [],
    dialog: false,
    collectionTitle: "",
  }),
  methods: {
    createCollection() {
      RequestHandler.createCollection(
        new Collection(this.collectionTitle)
      ).then((response) => this.collections.push(response.data));
      this.dialog = false;
      this.collectionTitle = "";
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