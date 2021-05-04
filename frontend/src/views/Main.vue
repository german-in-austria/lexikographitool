<template>
  <v-app>
    <AppBar ></AppBar>
    <v-main style="min-height: 48rem">
      <v-container fluid class="mt-15">

        <navigation-mobile style="z-index: 6" class="hidden-md-and-up"></navigation-mobile>
        <v-row>
          <Navigation
              v-model="collapsedNav"
              class="hidden-sm-and-down"
              style="position: fixed;"
          ></Navigation>

          <v-container
              class="containerContent"
              :style="cssVars"
              fluid

          >
            <router-view :key="$route.fullPath"/>

          </v-container>
        </v-row>
      </v-container>
    </v-main>

    <Footer style="margin-top: 200px; z-index: 5"></Footer>
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
  data: () => ({
    collapsedNav: false
  }),
  computed: {

    ...mapGetters({
      authenticated: "auth/authenticated",
    }),
    styleClass() {
      if (!this.collapsedNav) return "notcollapsed"
      return "collapsed"
    },
    cssVars() {
      if (this.$vuetify.breakpoint.smAndDown)
        return {'--margin-left': 0 + 'px', '--padding': 1 + 'rem' }
      if (!this.collapsedNav) return {'--margin-left': 200 + 'px', '--padding': 2 + 'rem'}
      return {'--margin-left': 70 + 'px', '--padding': 2 + 'rem'}
    }
  },
};
</script>

<style scoped>
.containerContent {
  margin-left: var(--margin-left);
  transition: all 0.2s;
  padding: var(--padding);
  padding-top: 2rem;

}

</style>
