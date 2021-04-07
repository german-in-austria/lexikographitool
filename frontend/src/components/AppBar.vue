<template>
  <div>
    <v-app-bar fixed flat height="90rem" outlined>
      <v-app-bar-nav-icon
        class="hidden-md-and-up"
        @click="drawer = true"
      ></v-app-bar-nav-icon>

      <template v-slot:img="{ props }">
        <v-img
          style="float: right"
          v-bind="props"
          :src="require('@/assets/colorPeople.png')"
          max-width="800px"
        ></v-img>
      </template>

      <v-img
        class="hidden-sm-and-down"
        :src="require('@/assets/IamDioeLogo.png')"
        alt="LOGO"
        contain
        height="100%"
        max-width="200px"
        style="background-color: rgb(255, 255, 255, 0.4)"
      ></v-img>

      <v-spacer class="hidden-sm-and-down"></v-spacer>
      <p class="hidden-sm-and-down text-h3 logocolor--text font-weight-bold mt-2" >WORTGUT</p>
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
        @click:append="doSearch"
        @keyup.enter="doSearch"
        background-color="rgb(255, 255, 255, 0.7)"
      ></v-text-field>
  <v-spacer></v-spacer>
      <div
        class="hidden-sm-and-down"
        v-if="!$vuetify.breakpoint.xs || !searchActive"
      >
        <v-btn-toggle dense v-if="authenticated" class="ml-2 mb-4">
          <v-btn to="/account">
            <span class="hidden-sm-and-down">{{ user.username }}</span>
            <v-icon :right="!$vuetify.breakpoint.xs">mdi-cog</v-icon>
          </v-btn>
          <v-btn>
            <v-icon @click="signOut">mdi-logout</v-icon>
          </v-btn>
        </v-btn-toggle>

        <v-btn outlined v-else to="/login" class="mb-4">Login</v-btn>
      </div>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" app fixed temporary>
      <v-list nav dense>
        <v-list-item-group
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item to="/">
            <v-list-item-icon>
              <v-icon>mdi-home-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Start</v-list-item-title>
          </v-list-item>
          <v-divider v-if="authenticated"></v-divider>

          <v-list-item to="/dashboard" v-if="authenticated">
            <v-list-item-icon>
              <v-icon>mdi-view-dashboard-variant-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Pinnwand</v-list-item-title>
          </v-list-item>

          <v-divider v-if="authenticated"></v-divider>
           <v-list-item to="/account" v-if="authenticated">
            <v-list-item-icon>
              <v-icon>mdi-cog-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Einstellungen</v-list-item-title>
          </v-list-item>

          <v-list-item v-if="isSuperUser" to="/reports">
            <v-list-item-icon>
              <v-icon>mdi-alert-decagram</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Start</v-list-item-title>
          </v-list-item>
          <v-divider></v-divider>

          <v-list-item v-if="authenticated"  @click="signOut">
            <v-list-item-icon>
              <v-icon>mdi-logout</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Abmelden</v-list-item-title>
          </v-list-item>

          <v-list-item v-if="!authenticated"  to="/login">
            <v-list-item-icon>
              <v-icon>mdi-login</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Einloggen</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "AppBar",

  data: () => ({
    drawer: false,
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
    doSearch(){
      this.$router.push('/search/' + this.search)
      this.search=''

    }
  },
  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      user: "auth/user",
      isSuperUser: "auth/isSuperUser",
    }),
  },
};
</script>

<style scoped>
</style>