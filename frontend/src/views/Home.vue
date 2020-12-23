<template>
  <div>
    <div v-if="authenticated">
      <home-logged-in></home-logged-in>
    </div>
    <div v-else>
      <v-row>
        <v-col cols="12" sd="4" md="4" v-for="card in cards" :key="card.id">
          <CardDialect :card="card"></CardDialect>
        </v-col>
        
      </v-row>
    </div>
  </div>
</template>

<script>
import CardDialect from "@/components/CardDialect";
import RequestHandler from "@/utils/RequestHandler";
import { mapGetters } from "vuex";
import HomeLoggedIn from "./HomeLoggedIn.vue";

export default {
  name: "Home",
  components: { CardDialect, HomeLoggedIn },
  data: () => ({
    cards: [],
  }),

  beforeRouteEnter(to, from, next) {
    RequestHandler.getCards().then((response) =>
      next((vm) => {
        vm.cards = response.data;
      })
    );
  },
  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
    }),
  },
};
</script>

<style scoped>
</style>