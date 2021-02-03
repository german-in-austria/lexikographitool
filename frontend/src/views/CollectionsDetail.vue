<template>
  <v-container fluid>
    <v-row no-gutters>
      <v-col cols="8">
        <p ><span class="text-h4">{{ collection.name }}</span> <span v-if="collection.public" style="color: red"> (öffentlich)</span></p>
        <p class="text-h5">{{ collection.description }}</p>
        <p class="text-h8">{{ collection.organization }}</p>
        <p ><span class="text-h8">Kategorien:</span> <span class="text-h8" :key="index" v-for="(category,index) in collection.categories">{{category}} </span></p>

      </v-col>
      <v-col>
        <collection-settings-dialog :collection="collection"></collection-settings-dialog>
      </v-col>
      <v-col cols="12">
        <v-row no-gutters>

        <v-col cols="8">
          <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Suche"
              single-line
              class="pa-5"
          ></v-text-field>
        </v-col>
        <v-col cols="2">
          <collection-add-lexeme-dialog :collection="collection"></collection-add-lexeme-dialog>
        </v-col></v-row>
        <v-row no-gutters>
          <v-col v-for="card in lexemes"
                 :key="card.word">
            <card-dialect :card="card" class="mt-1 mr-5"></card-dialect>


          </v-col>
        </v-row>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import RequestHandler from '../utils/RequestHandler.js'
import Collection from '../objects/Collection.js'
import CardDialect from "@/components/CardDialect";
import CollectionSettingsDialog from "@/components/CollectionSettingsDialog";
import CollectionAddLexemeDialog from "@/components/CollectionAddLexemeDialog";

export default {
  components: {CollectionAddLexemeDialog, CollectionSettingsDialog, CardDialect},
  data: () => ({
    collection: new Collection(),
    search: '',
    lexemes: [],
  }),
  mounted() {
    RequestHandler.getCollection(this.$route.params.id).then((response) => {
          this.collection = response.data
          this.lexemes = this.collection.lexemes
        }
    )
  },
  watch: {
    search() {
      if (!this.search) this.lexemes = this.collection.lexemes
      else
        this.lexemes = this.collection.lexemes.filter(word =>
            word.word?.match(new RegExp(this.search, "i")) ||
            word.description?.match(new RegExp(this.search, "i")) ||
            word.dialectWord?.match(new RegExp(this.search, "i")))
    }
  }

}


</script>

<style scoped>
.item {
  margin: 5px;
  border-radius: 4px;
}

.item:hover {
  background: lightgray;
}
</style>