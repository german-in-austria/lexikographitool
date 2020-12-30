<template>
  <div>
    <div v-if="authenticated">
      <home-logged-in></home-logged-in>
    </div>
    <div v-else>
      <perfect-scrollbar>
      <v-row>
        
        <v-col cols="12" sd="4" md="3" v-for="card in cards" :key="card.id">
          <CardDialect :card="card" class="ma-0"></CardDialect>
        </v-col>
      </v-row>
        </perfect-scrollbar>

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
.ps{
  height: 820px;
}
</style>