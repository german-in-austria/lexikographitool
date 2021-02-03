<template>
  <v-row justify="center">
    <v-dialog
        v-model="dialog"
        persistent
        max-width="50vh"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-icon
            size="30px"
            v-bind="attrs"
            v-on="on"
        >
          mdi-cog
        </v-icon>
      </template>
      <v-card>
        <v-card-title class="headline">
          Einstellungen
        </v-card-title>
        <v-card-text>
          <v-text-field v-model="name" label="Sammlungsname"></v-text-field>
          <v-text-field v-model="description"></v-text-field>
          <v-text-field v-model="organization" label="Organisation"></v-text-field>
          <v-switch v-model="pub">öffentlich</v-switch>
          <v-combobox v-model="categories" item-text="category" :items="categoryList" multiple
                      :return-object="false"></v-combobox>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="green darken-1"
              text
              @click="dialog = false"
          >
            Disagree
          </v-btn>
          <v-btn
              color="green darken-1"
              text
              @click="update"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import axios from "axios";

export default {
  name: "CollectionSettingsDialog",
  props: ['collection'],
  data: function () {
    return {
      dialog: false,
      description: '',
      categories: [],
      categoryList: [],
      organization:'',
      pub:false,
      name: '',


    }

  },
  watch: {
    dialog(visible) {
      if (visible) {
        this.name = this.collection.name
        this.description = this.collection.description
        this.pub = this.collection.public
        this.organization = this.collection.organization
        this.categories = this.collection.categories
      }
    }
  },
  methods: {
    update() {
      axios.put('collection/' + this.collection.id + '/', {
        'id': this.collection.id,
        'name': this.name,
        'description': this.description,
        'organization': this.organization,
        'public': this.pub,
        'categories':this.categories
      }).then(() => {
        this.collection.name = this.name
        this.collection.description = this.description
        this.collection.categories = this.categories
        this.collection.public = this.pub
        this.collection.organization = this.organization
        this.dialog = false
      })

    }
  },
  mounted() {
    RequestHandler.searchCategories('').then(response => this.categoryList = response.data)
  }

}
</script>

<style scoped>

</style>