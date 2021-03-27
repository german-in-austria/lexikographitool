<template>
  <v-app :style="authenticated ? '' : 'background-color: lightcyan'">
<AppBar v-if="authenticated"></AppBar>

    <v-main style="min-height: 48rem">
      <v-container fluid class="mt-15" >

        <navigation-mobile  v-if="authenticated" class="hidden-md-and-up" ></navigation-mobile>
        <v-row>
          <Navigation
              v-if="authenticated"
              class="hidden-sm-and-down"
              style="position: fixed;"
          ></Navigation>

          <v-container
              :style="$route.fullPath == '/dashboard' ? 'margin-top: 3rem;' : 'max-width: 50rem; margin-top: 3rem;' + ' '"
              rounded="lg"
          >

            <router-view :key="$route.fullPath"/>

          </v-container>
        </v-row>
      </v-container>
    </v-main>

    <Footer v-if="authenticated" style="margin-top: 200px"></Footer>
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
  title: "hallo",
  computed: {
    sheetStyle() {
      return this.$vuetify.breakpoint.sm | this.$vuetify.breakpoint.xs
          ? ""
          : "margin-right:5vw; padding: 5rem 5vw 0 5vw;;margin-left:12rem; width:80vw;";
    },
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
