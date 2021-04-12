<template>
  <v-app>
    <v-container fluid v-scroll="onScroll">
      <div class="sticky1">
        <v-row>
          <v-col><p class="text-h4">Wörterecke</p></v-col>
          <v-col class="col-auto">
            <v-btn-toggle v-model="view" dense>
              <v-btn>
                <v-icon>mdi-view-grid</v-icon>
              </v-btn>
              <v-btn>
                <v-icon>mdi-view-headline</v-icon>
              </v-btn>
            </v-btn-toggle>
          </v-col>
        </v-row>
      </div>
      <v-row no-gutters><p class="text-body-1">
        {{ $t("lexemes.desciption") }}
      </p></v-row>
      <div class="sticky2">
        <search-bar v-on:input="search = $event"></search-bar>
      </div>
      <v-row no-gutters v-if="!view">
        <v-col
            cols="12"
            sd="6"
            md="6"
            lg="4"
            v-for="(item, index) in items"
            :key="index"
        >
          <card-dialect class="ma-5" :card="item"></card-dialect>
        </v-col>
      </v-row>
      <v-row no-gutters v-else>
        <v-simple-table>
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
            <tr v-for="(item, index) in items" :key="index">
              <td>{{ item.dialectWord }}</td>
              <td>{{ item.word }}</td>
              <td>{{ item.description }}</td>
              <td>{{ item.variety }}</td>
              <td><span>{{ item.origin.name }}</span><span v-if="!!item.origin.state">, {{ item.origin.state }}</span>
              </td>
              <td>
                <CollectionAddLexeme :card-id="item.id"></CollectionAddLexeme>
              </td>
              <td>
                <a @click="$router.push('/lexeme/' + item.id)">alle Infos</a>
              </td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";
import CardDialect from "../components/CardDialect.vue";
import SearchBar from "../components/SearchBar.vue";
import CollectionAddLexeme from "../components/CollectionAddLexeme.vue";

export default {
  components: {CardDialect, SearchBar, CollectionAddLexeme},
  data: () => ({
    items: [],
    pageCount: 0,
    count: 0,
    loaing: true,
    page: 1,
    search: "ordering=-date_created",
    next: null,
    view: 0,
    headers: [
      {text: "Lemma", value: "dialectWord"},
      {text: "hochdeutsche Bedeutung", value: "word"},
      {text: "Bedeutung", value: "description"},
      {text: "Varietät", value: "variety"},
      {text: "Ursrpung", value: "origin"},
      {text: "", value: "info"},
      {text: "", value: "addToCollection"},
    ],
    scroller: {},
    timeout: null,
  }),
  mounted() {
    this.loadFromApi();
  },
  watch: {
    search() {

      clearTimeout(this.timeout);

      let self = this;
      this.timeout = setTimeout(function () {
        // enter this block of code after 1 second
        // handle stuff, call search API etc.
        self.page = 1;
        self.loadFromApi();
      }, 500);

    },
  },
  methods: {
    loadFromApi() {
      this.loading = true;
      axios
          .get("/lexemes/?page=" + this.page + "&" + this.search)
          .then((response) => {
            this.items = response.data.results;
            this.pageCount = response.data.total_pages;
            this.count = response.data.count;
            this.next = response.data.links.next;
          })
          .finally(() => (this.loading = false));
    },
    onScroll(e) {
      console.log(e.target.scrollingElement.clientHeight);
      if (
          e.target.scrollingElement.scrollTop + 400 >
          e.target.scrollingElement.scrollTopMax &&
          !!this.next
      ) {

        this.next = null
        this.page += 1;
        axios
            .get("/lexemes/?page=" + this.page + "&" + this.search)
            .then((response) => {
              this.items = this.items.concat(response.data.results);
              this.pageCount = response.data.total_pages;
              this.count = response.data.count;
              this.next = response.data.links.next;
            })
            .finally(() => (this.loading = false));
      }
    },
  },
};
</script>

<style>
.sticky1 {
  background-color: white;
  height: 70px;
  position: sticky;
  top: 5.6rem;
  z-index: 3;
}

.sticky2 {
  background-color: white;
  position: sticky;
  top: 9.6rem;
  z-index: 2;
}
</style>