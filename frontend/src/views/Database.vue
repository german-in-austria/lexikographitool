<template>
  <div>
      <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Suche"
          single-line
          class="pa-5"
      ></v-text-field>
    <v-data-table
        :headers="headers"
        :items="items"
        :search="search"
        :items-per-page="14"
        height="71vh"
        :server-items-length="count"
        :options.sync="options"
        :loading="loading"
    >
      <template #item.info="{ item }">
        <v-icon @click="navigate(item)">
          mdi-dots-horizontal
        </v-icon>

      </template>
      <template #item.addToCollection="{ item }">
        <CollectionAddLexeme :card-id="item.id"></CollectionAddLexeme>

      </template>

      <v-data-footer :disable-items-per-page="true" :disable-pagination="true">

      </v-data-footer>
    </v-data-table>
  </div>
</template>

<script>
import RequestHandler from "../utils/RequestHandler";
import CollectionAddLexeme from "@/components/CollectionAddLexeme";
// import router from "../router"
export default {
  components: {CollectionAddLexeme},
  data: () => ({
    pageCount: 0,
    count: 0,
    page: 1,
  loading: true,
    options: {},
    headers: [
      {text: "Dialektwort", value: "dialectWord"},
      {text: "Wort", value: "word"},
      {text: "Bedeutung", value: "description"},
      {text: "Dialekt", value: "dialect"},
      {text: "Ursrpung", value: "origin"},
      {text: "", value: "info"},
      {text: "", value: "addToCollection"},
    ],
    items: [],
    search: '',
  }), watch: {
    search:{handler () {
        this.options.page=1
        this.loadFromApi()
      },
      deep: true,},
    options: {
      handler () {
        this.loadFromApi()
      },
      deep: true,
    },
  },
  methods: {
    navigate(item) {
      this.$router.push('/lexeme/' + item.id)
    },
    loadFromApi() {
      this.loading = true
      RequestHandler.getLexemes(this.options.page,this.search).then((response) => {

            this.items = response.data.results,
                this.pageCount = response.data.total_pages,
                this.count = response.data.count
          }
      ).finally(()=>this.loading=false)
      ;
    }
  },
  beforeRouteEnter(to, from, next) {
    RequestHandler.getLexemes(1,'').then((response) =>
        next((vm) => {
          (vm.items = response.data.results,
              vm.pageCount = response.data.total_pages,
              vm.count = response.data.count,
          vm.loading = false);
        })
    );
  }
}
;
</script>
<style>
.v-data-footer__select{
  display:none;
}
</style>
