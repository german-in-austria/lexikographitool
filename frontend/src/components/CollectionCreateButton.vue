<template>
  <div>
    <v-hover v-slot="{ hover }">
      <v-card
        @click.prevent="dialog = true"
        :elevation="hover ? 4 : 0"
        class="mx-auto"
        outlined
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
    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title>
          <span class="headline">Neue Sammlung</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="createForm">
            <v-text-field
              v-model="collectionTitle"
              label="Titel"
              required
              :rules="[(v) => !!v || 'Deine Sammlung braucht einen Titel']"
            ></v-text-field>
            <v-text-field
              v-model="collectionDescription"
              label="Beschreibung"
            ></v-text-field>
          </v-form>
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

export default {
  name: "CollectionCreateButton",

  data: () => ({
    dialog: false,
    collectionTitle: "",
    collectionDescription: "",
  }),
  methods: {
    createCollection() {
      if (this.$refs.createForm.validate()) {
        RequestHandler.createCollection(
          new Collection(this.collectionTitle, this.collectionDescription)
        ).then((response) => this.$emit('created',response.data));
        this.dialog = false;
        this.collectionTitle = "";
      }
    },
  },
};
</script>