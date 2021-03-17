<template>
  <v-app>
<AppBar></AppBar>
    <v-main>
      <v-container fluid class="mt-15">

        <navigation-mobile class="hidden-md-and-up" ></navigation-mobile>
        <v-row>
          <Navigation
              class="hidden-sm-and-down"
              style="position: fixed;"
          ></Navigation>

          <v-container
              :style="sheetStyle"
              rounded="lg"
          >

            <router-view :key="$route.fullPath"/>
          </v-container>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Navigation from "@/components/Navigation";
import NavigationMobile from "@/components/NavigationMobile";
import AppBar from "@/components/AppBar";

export default {
  components: {AppBar, NavigationMobile, Navigation},
  title: "hallo",
  computed: {
    sheetStyle() {
      return this.$vuetify.breakpoint.sm | this.$vuetify.breakpoint.xs
          ? ""
          : "margin-right:5vw; padding: 5rem 5vw 0 5vw;;margin-left:12rem; width:80vw;";
    },
  },
};
</script>

<style scoped>
.centered-text {
  text-align: center;
}
</style>
