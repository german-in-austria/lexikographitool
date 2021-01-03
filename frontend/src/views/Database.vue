<template>
  <v-card>
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Suche"
        single-line
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="items"
      :search="search"
    >
      <template #item.info="{ item }">
        <v-icon  @click="navigate(item)">
          mdi-dots-horizontal
        </v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import RequestHandler from "../utils/RequestHandler";
// import router from "../router"
export default {
  data: () => ({
    headers: [
      { text: "Dialektwort", value: "dialectWord" },
      { text: "Wort", value: "word" },
      { text: "Bedeutung", value: "description" },
      { text: "Dialekt", value: "dialect" },
      { text: "Ursrpung", value: "origin" },
      { text: "", value: "info" },
    ],
    items: [],
    search: null,
  }),
  methods:{
      navigate(item){
          console.log(item)
          this.$router.push('/lexeme/' +item.id)
      }
  },
  beforeRouteEnter(to, from, next) {
    RequestHandler.getLexemes(1).then((response) =>
      next((vm) => {
        (vm.items = response.data.results), console.log(response);
      })
    );
  }
};
</script>