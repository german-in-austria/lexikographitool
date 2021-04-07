<template>
  <v-app>
<AppBar></AppBar>

    <v-main style="min-height: 48rem">
      <v-container fluid class="mt-15" >

        <navigation-mobile  class="hidden-md-and-up" ></navigation-mobile>
        <v-row>
          <Navigation
              
              class="hidden-sm-and-down"
              style="position: fixed;"
          ></Navigation>

          <v-container
              :style="$route.fullPath == '/dashboard' ? 'margin-top: 3rem;' : ' max-width: 56rem; margin-top: 3rem;' + ' '"
              rounded="lg"
          >

            <router-view :key="$route.fullPath"/>

          </v-container>
        </v-row>
      </v-container>
    </v-main>

    <Footer style="margin-top: 200px"></Footer>
  </v-app>
</template>

<script>
import Navigation from "@/components/Navigation";
import NavigationMobile from "@/components/NavigationMobile";
import AppBar from "@/components/AppBar";
import {mapGetters} from "vuex";
import Footer from "@/components/Footer";

export default {
  components: {Footer, AppBar, NavigationMobile, Navigation},
  computed: {

    ...mapGetters({
      authenticated: "auth/authenticated",
    }),
  },
};
</script>

<style scoped>
.centered-text {
  text-align: center;
}
</style>
