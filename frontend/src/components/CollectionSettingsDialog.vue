<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="30rem" scrollable>
      <template v-slot:activator="{ on, attrs }">
        <v-icon size="30px" v-bind="attrs" v-on="on"> mdi-cog </v-icon>
      </template>
      <v-card>
        <v-card-title class="headline"> Einstellungen 
        <v-spacer></v-spacer>

          <v-btn color="error" right x-small text @click="deleteCollection"> Sammlung löschen </v-btn>

        </v-card-title>
        
        <v-divider></v-divider>
        <v-card-text>
          <collection-properties-form :collection="col" :group="!!collection.group"></collection-properties-form>
        </v-card-text>
        <v-divider></v-divider>

        <v-card-actions>
          <v-btn text @click="dialog = false"> Verwerfen </v-btn>
          <v-btn text @click="update"> Änderungen speichern </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import axios from "axios";
import CollectionPropertiesForm from './CollectionPropertiesForm.vue';

export default {
  components: { CollectionPropertiesForm },
  name: "CollectionSettingsDialog",
  props: ["collection"],
  data: function () {
    return {
      dialog: false,
      col:{}
    };
  },
  watch: {
    dialog(visible) {
      if (visible) {
        this.col.name = this.collection.name;
        this.col.description = this.collection.description;
        this.col.pub = this.collection.public;
        this.col.organization = this.collection.organization;
        this.col.categories = this.collection.categories;
        this.col.canAddLexemePublic = this.collection.can_add_lexemes_public;
        this.col.canRemoveLexemePublic = this.collection.can_remove_lexemes_public;
        this.col.canAddLexemeGroup = this.collection.can_add_lexemes_group;
        this.col.canRemoveLexemeGroup = this.collection.can_remove_lexemes_group;
        this.col.group = this.collection.group;
      }
    },
  },
  methods: {
    update() {
      axios
        .put("collection/" + this.collection.id + "/", {
          id: this.collection.id,
          name: this.col.name,
          description: this.col.description,
          organization: this.col.organization,
          public: this.col.pub,
          categories: this.col.categories,
          can_add_lexemes_group: this.col.canAddLexemeGroup,
          can_remove_lexemes_group: this.col.canRemoveLexemeGroup,
          can_add_lexemes_public: this.col.canAddLexemePublic,
          can_remove_lexemes_public: this.col.canRemoveLexemePublic,
        })
        .then(() => {
          this.collection.name = this.col.name;
          this.collection.description = this.col.description;
          this.collection.categories = this.col.categories;
          this.collection.public = this.col.pub;
          this.collection.organization = this.col.organization;
          this.collection.can_add_lexemes_group = this.col.canAddLexemeGroup;
          this.collection.can_remove_lexemes_group = this.col.canRemoveLexemeGroup;
          this.collection.can_add_lexemes_public = this.col.canAddLexemePublic;
          this.collection.can_remove_lexemes_public = this.col.canRemoveLexemePublic;
          this.dialog = false;
        });
    },
    deleteCollection() {
      axios.delete("collection/" + this.collection.id + "/").then(() => {
        this.dialog = false;
        this.$router.push("/collections");
      });
    },
  }
};
</script>

<style scoped>
</style>