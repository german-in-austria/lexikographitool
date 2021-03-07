<template>
  <v-app>
    <v-app-bar
      elevation="5"
      fixed
      color="primary lighten-1"
      flat
      height="90rem"
    >
      <v-container class="py-0 fill-height">
        <p class="text-h4 hidden-sm-and-down">
          {{ $vuetify.breakpoint.name }}LexicTool
        </p>
        <v-spacer class="hidden-sm-and-down"></v-spacer>
        <div class="hidden-lg-and-up" >
          <v-expand-x-transition mode="out-in"
          >
            <v-icon 
            style="position:fixed; top:rem"
            :key="1" v-if="!searchActive" @click="searchActive = true"
              >mdi-magnify</v-icon
            >
            <v-text-field
            style="position:fixed;top:0"

              :key="2"
              v-if="searchActive"
              label="Suche"
              class="mt-4"
              outlined
              append-icon="mdi-close"
              dense
              v-model="search"
              @click:append="searchActive = false"
              @keyup.enter="$router.push('/search/' + search)"
            ></v-text-field>
          </v-expand-x-transition>
        </div>
        <v-text-field
          label="Suche"
          class="pt-3 mr-2 hidden-md-and-down"
          outlined
          height="3vh"
          append-icon="mdi-send"
          dense
          v-model="search"
          @click:append="$router.push('/search/' + search)"
          @keyup.enter="$router.push('/search/' + search)"
        ></v-text-field>
        <v-spacer class="hidden-md-and-down"></v-spacer>
        <v-btn style="position:fixed; left:40vw" class="ml-2 mb-4" to="/card-create" v-if="authenticated">
          <span class="hidden-sm-and-down">Wort erstellen</span>
          <v-icon class="hidden-md-and-up"> mdi-plus</v-icon></v-btn
        >
        <v-spacer></v-spacer>

        <div v-if="!$vuetify.breakpoint.xs || !searchActive">
          <v-btn-toggle dense v-if="authenticated" class="ml-2 mb-4">
            <v-btn to="/account">
              <span class="hidden-sm-and-down">{{ user.username }}</span>
              <v-icon :right="!$vuetify.breakpoint.xs">mdi-cog</v-icon></v-btn
            >
            <v-btn><v-icon @click="signOut">mdi-logout</v-icon></v-btn>
          </v-btn-toggle>

          <v-btn v-else to="/login" class="mb-4">Login</v-btn>
        </div>
      </v-container>
    </v-app-bar>
    <v-main class="primary lighten-5">
      <v-container fluid class="mt-15">
        <v-bottom-navigation class="hidden-md-and-up" fixed>
          <v-btn color="deep-purple accent-4" to="/" icon>
            <v-icon>mdi-home-outline</v-icon>
          </v-btn>

          <v-btn color="deep-purple accent-4" to="/lexemes" icon>
            <v-icon>mdi-sofa-outline</v-icon>
          </v-btn>

          <v-btn color="deep-purple accent-4" to="/collections" icon>
            <v-icon>mdi-file-multiple-outline</v-icon>
          </v-btn>

          <v-btn color="deep-purple accent-4" to="/groups" icon>
            <v-icon>mdi-account-group-outline</v-icon>
          </v-btn>

          <v-btn color="deep-purple accent-4" to="/postings" icon>
            <v-icon>mdi-chat-processing-outline</v-icon>
          </v-btn>
        </v-bottom-navigation>
        <v-row>
          <Navigation
            class="hidden-sm-and-down"
            style="position: fixed; margin-top: 10vh"
          ></Navigation>

          <v-sheet
            elevation="3"
            min-height="87vh"
            :style="sheetStyle"
            rounded="lg"
          >
            <router-view :key="$route.fullPath" />
          </v-sheet>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Navigation from "@/components/Navigation";
import { mapGetters } from "vuex";
import { mapActions } from "vuex";

export default {
  components: { Navigation },
  title: "hallo",
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
    sheetStyle() {
      return this.$vuetify.breakpoint.sm | this.$vuetify.breakpoint.xs
        ? ""
        : "margin-right:5vw; padding: 5rem 8vw 0 8vw;;margin-left:12rem; width:80vw;";
    },
  },
};
</script>

<style scoped>
.centered-text {
  text-align: center;
}
</style>
