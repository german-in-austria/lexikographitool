<template>
  <v-dialog
      v-model="dialog"

      max-width="600px">
    <template v-slot:activator="{ on, attrs }">

      <v-icon
          v-bind="attrs"
          v-on="on"
          v-on:click.prevent="load()">mdi-plus</v-icon>
    </template>
      <v-list>
        <v-subheader>Meine Sammlungen {{cardId}}</v-subheader>
        <v-list-group
            :value="false"
            no-action
            sub-group
            v-for="group in groups"
            :key="group.id"
        ><template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title>{{ group.name }}</v-list-item-title>
          </v-list-item-content>
        </template>

          <v-list-item
              v-for="collection in group.collections"
              :key="collection.id"
              link
          >
            <v-list-item-title v-text="collection.name"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-if="collection.in_collection" @click="add(collection)">mdi-check</v-icon>
              <v-icon v-else @click="add(collection)">mdi-plus</v-icon>
            </v-list-item-icon>
          </v-list-item>

        </v-list-group>
      </v-list>
  </v-dialog>

</template>

<script>
import RequestHandler from "@/utils/RequestHandler";

export default {
name: "CollectionAddLexeme",
  props: ["cardId"],
  data:()=>({
    dialog:false,
    groups:[],
  }),
  methods:{
  load(){
    RequestHandler.getGroupsWithCollections(this.cardId).then(response=>this.groups=response.data)
  },
    add(collection){
      collection.in_collection=true
      RequestHandler.addLexemeToCollection(collection.id, this.cardId);

    }
  }
}
</script>

<style scoped>

</style>