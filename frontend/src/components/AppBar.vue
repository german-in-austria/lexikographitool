<template>
  <v-app-bar
      fixed
      flat
      height="90rem"
      outlined

  >

    <template v-slot:img="{ props }">
      <v-img
          style="float: right"
          v-bind="props"
          :src="require('@/assets/colorPeople.png')"
          max-width="800px"

      ></v-img>
    </template>

    <v-img class="hidden-sm-and-down" :src="require('@/assets/IamDioeLogo.png')" alt="LOGO" contain height="100%" max-width="200px"
    style="background-color: rgb(255,255,255,0.4)"></v-img>

      <v-spacer></v-spacer>

      <v-text-field
          label="Suche"
          class="pt-3 mr-2"
          outlined
          height="3vh"
          append-icon="mdi-send"
          dense
          v-model="search"
          style="width: 50%; max-width: 20rem"
          @click:append="$router.push('/search/' + search)"
          @keyup.enter="$router.push('/search/' + search)"
          background-color="rgb(255, 255, 255, 0.7)"
      ></v-text-field>
      <v-spacer></v-spacer>

      <div v-if="!$vuetify.breakpoint.xs || !searchActive">
        <v-btn-toggle dense v-if="authenticated " class="ml-2 mb-4">
          <v-btn to="/account">
            <span class="hidden-sm-and-down">{{ user.username }}</span>
            <v-icon :right="!$vuetify.breakpoint.xs">mdi-cog</v-icon>
          </v-btn
          >
          <v-btn>
            <v-icon @click="signOut">mdi-logout</v-icon>
          </v-btn>
        </v-btn-toggle>

        <v-btn v-else to="/login" class="mb-4">Login</v-btn>
      </div>
  </v-app-bar>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "AppBar",

  data: () => ({
    search: "",
    searchActive: false,
  }),
  methods: {

    signOut() {
      this.signOutAction();
      this.$router.replace({
        name: "home",
      });
    },
    ...mapActions({
      signOutAction: "auth/signOut",
    }),
  },
  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      user: "auth/user",
    }),
  }
}
</script>

<style scoped>

</style>