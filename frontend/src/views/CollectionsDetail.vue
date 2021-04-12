<template>
  <v-container fluid v-scroll="onScroll">
    <v-row no-gutters>
      <v-col cols="8">
        <p>
          <printer-tool  :cards="lexemes"></printer-tool>

          <span class="text-h4">{{ collection.name }}</span>
          <span v-if="collection.public" style="color: red">
            ({{ $t("general.public") }})</span
          >
        </p>
        <p class="text-h5">{{ collection.description }}</p>
        <p class="text-h8">{{ collection.organization }}</p>
        <p v-if="collection.categories.length !== 0">
          <span class="text-h8">Kategorien:</span>
          <span
            class="text-h8"
            :key="index"
            v-for="(category, index) in collection.categories"
            >{{ category }}
          </span>
        </p>
      </v-col>

      <v-col class="col-auto" v-if="collection.is_owner">
        <v-menu left>
          <template v-slot:activator="{ on, attrs }">
            <v-icon v-bind="attrs" v-on="on">mdi-dots-vertical </v-icon>
          </template>
          <v-list>
            <v-list-item @click="print">{{$t("collectionDetail.print")}}</v-list-item>
              <collection-settings-dialog
                :collection="collection"
              ></collection-settings-dialog>
            <collection-detail-trash-can-dialog

              :collectionId="collection.id"
              :lexemes="lexemes"
            ></collection-detail-trash-can-dialog>
            <v-list-item @click="deleteCollection"><span class="error--text">{{$t("collectionDetail.deleteCollection")}}</span></v-list-item>
          </v-list>
        </v-menu>
      </v-col>
      </v-row>
        <v-row no-gutters >
          <v-text-field
            v-model="search"
            :label="$t('general.search')"
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
          <v-spacer></v-spacer>
            <v-btn-toggle v-model="view" dense>
              <v-btn>
                <v-icon>mdi-view-grid</v-icon>
              </v-btn>
              <v-btn>
                <v-icon>mdi-view-headline</v-icon>
              </v-btn>
            </v-btn-toggle>
        </v-row>
        <v-row no-gutters v-if="!view">
          <p v-if="lexemes.length === 0" class="pa-10 text-body-1">
            {{ $t("collectionDetail.collectionEmpty") }}
          </p>
          <v-scale-transition group class="row">
            <v-col
              cols="auto"
              class="px-2 py-4"
              v-for="(card, index) in lexemes"
              :key="card.id"
            >
              <card-dialect :card="card" class="mt-1 mr-5">
                <template
                  slot="menuItem"
                  v-if="collection.can_remove_lexeme_from_collection"
                >
                  <v-list-item @click="removeLexeme(card, index)">
                    {{ $t("card.removeFromCollection") }}
                  </v-list-item>
                </template>
              </card-dialect>
            </v-col>
          </v-scale-transition>
        </v-row>

    <v-row no-gutters v-else>
      <v-simple-table id="printMe">
        <template v-slot:default>
          <thead>
          <tr>
            <th
                class="text-left"
                v-for="(header, index) in headers"
                :key="index"
            >
              {{ header.text }}
            </th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(item, index) in lexemes" :key="index">
            <td>{{ item.dialectWord }}</td>
            <td>{{ item.word }}</td>
            <td>{{ item.description }}</td>
            <td>{{ item.variety }}</td>
            <td><span>{{ item.origin.name }}</span><span v-if="!!item.origin.state">, {{ item.origin.state }}</span>
            </td>
            <td v-if="!printing">
              <a @click="$router.push('/lexeme/' + item.id)">alle Infos</a>
            </td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-row>
  </v-container>
</template>

<script>
import RequestHandler from "../utils/RequestHandler.js";
import Collection from "../objects/Collection.js";
import CardDialect from "@/components/CardDialect";
import PrinterTool from "@/components/PrinterTool";
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
    PrinterTool,
  },
  data: () => ({
    collection: new Collection(),
    search: "",
    lexemes: [],
    next: null,
    view:false,
    headers: [
      {text: "Lemma", value: "dialectWord"},
      {text: "hochdeutsche Bedeutung", value: "word"},
      {text: "Bedeutung", value: "description"},
      {text: "Varietät", value: "variety"},
      {text: "Ursrpung", value: "origin"},
      {text: "", value: "info"},
    ],
    printing : false,
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
        e.target.scrollingElement.scrollTop + 400 >
          e.target.scrollingElement.scrollTopMax &&
        !!this.next
      ) {
        const next = this.next;
        this.next = null;
        axios.get(next).then((response) => {
          this.lexemes = this.lexemes.concat(response.data.results);
          this.next = response.data.links.next;
        });
      }
    },
    deleteCollection() {
      axios.delete("collection/" + this.collection.id + "/").then(() => {
        this.dialog = false;
        this.$router.push("/collections");
      });
    },
    print() {
      this.printing=true;
      this.view = true;

      // Use nextTick to trigger the print on next update
      this.$nextTick(() => {
        this.$htmlToPaper("printMe", null, () => {
          console.warn("done");
          this.printing = false; // hide the <p> tag when printing is done
        });
      });
    },
  },
};
</script>

<style scoped>
</style>