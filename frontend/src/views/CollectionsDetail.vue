<template>
  <v-container fluid v-scroll="onScroll">
    <v-row no-gutters>
      <v-col cols="8">
        <p>
          <span class="text-h4">{{ collection.name }}</span>
          <span v-if="collection.public" style="color: red"> (öffentlich)</span>
        </p>
        <p class="text-h5">{{ collection.description }}</p>
        <p class="text-h8">{{ collection.organization }}</p>
        <p>
          <span class="text-h8">Kategorien:</span>
          <span
              class="text-h8"
              :key="index"
              v-for="(category, index) in collection.categories"
          >{{ category }}
          </span>
        </p>
      </v-col>
      <v-col>
        <collection-settings-dialog
            v-if="collection.is_owner"
            :collection="collection"
        ></collection-settings-dialog>
      </v-col>
      <v-col cols="12">
        <v-row no-gutters>
          <v-text-field
              v-model="search"
              label="Suche"
              clearable
              flat
              solo-inverted
              hide-details
              prepend-inner-icon="mdi-magnify"
          ></v-text-field>
          <v-spacer></v-spacer>
          <collection-add-lexeme-dialog
              :collection="collection"
              :lexemes="lexemes"
              v-if="collection.can_add_lexeme_to_collection"
          ></collection-add-lexeme-dialog>
          <collection-detail-trash-can-dialog
              v-if="collection.is_owner"
              :collectionId="collection.id"
              :lexemes="lexemes"
          ></collection-detail-trash-can-dialog>
        </v-row>
        <v-row no-gutters>
          <p v-if="lexemes.length == 0" class="pa-10 text-body-1">
            Diese Sammlung ist leer. Fülle sie mit deinen Lieblingswörtern!
          </p>
          <v-scale-transition group class="row">
            <v-col
                cols="auto"
                class="px-2 py-4"
                v-for="(card,index) in lexemes"
                :key="card"
            >

              <card-dialect :card="card" class="mt-1 mr-5">
                <template slot="button">
                  <v-btn
                      v-if="collection.can_remove_lexeme_from_collection"
                      small
                      absolute
                      top
                      right
                      fab
                      color="error"
                      @click.prevent="removeLexeme(card,index)"
                  >
                    <v-icon small>mdi-delete</v-icon>
                  </v-btn>
                </template>
              </card-dialect>
            </v-col>
          </v-scale-transition>

        </v-row>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
import RequestHandler from "../utils/RequestHandler.js";
import Collection from "../objects/Collection.js";
import CardDialect from "@/components/CardDialect";
import CollectionSettingsDialog from "@/components/CollectionSettingsDialog";
import CollectionAddLexemeDialog from "@/components/CollectionAddLexemeDialog";
import CollectionDetailTrashCanDialog from "@/components/CollectionDetailTrashCanDialog";
import axios from "axios";

export default {
  components: {
    CollectionAddLexemeDialog,
    CollectionSettingsDialog,
    CollectionDetailTrashCanDialog,
    CardDialect,
  },
  data: () => ({
    collection: new Collection(),
    search: "",
    lexemes: [],
    next: null,
  }),
  mounted() {
    RequestHandler.getCollection(this.$route.params.id).then((response) => {
      this.collection = response.data;
    });
    axios
        .get("lexemes/?page=1&collection=" + this.$route.params.id)
        .then((response) => {
          this.lexemes = response.data.results;
          this.next = response.data.links.next;
        });
  },
  watch: {
    search() {
      axios
          .get(
              "lexemes/?page=1&search=" +
              this.search +
              "&collection=" +
              this.$route.params.id
          )
          .then((response) => {
            this.lexemes = response.data.results;
            this.next = response.data.links.next;
          });
    },
  },
  methods: {
    removeLexeme(card, index) {
      console.log(index);
      this.lexemes.splice(index, 1);

      axios.delete("collection/" + this.collection.id + "/" + card.id + "/");
    },

    onScroll(e) {
      if (
          e.target.scrollingElement.scrollTop ===
          e.target.scrollingElement.scrollTopMax &&
          !!this.next
      ) {
        axios.get(this.next).then((response) => {
          this.lexemes = this.lexemes.concat(response.data.results);
          this.next = response.data.links.next;
        });
      }
    },
  },
};
</script>

<style scoped>
.item {
  margin: 5px;
  border-radius: 4px;
}

.item:hover {
  background: lightgray;
}

/* This is for documentation purposes and will not be needed in your application */
.v-btn--example {
  bottom: 0;
  position: absolute;
  margin: 0 0 16px 16px;
}

.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */
{
  opacity: 0;
  transform: translateY(30px);
}
</style>