<template>
  <v-app >
    <v-app-bar

        color="white"
        flat
    >
      <v-container class="py-0 fill-height">
        <v-avatar
            v-if="authenticated"
            class="mr-10"
            color="grey darken-1"
            size="32"
        ></v-avatar>
        <p v-if="authenticated">{{user.username}}</p>


        <v-spacer></v-spacer>

        <v-responsive  max-width="260">
          <v-btn
              v-if="authenticated"
              @click="signOut"
          >
            Logout
          </v-btn>
          <v-btn v-else to="/login">Login</v-btn>

<!--          <Login v-else></Login>-->

        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3 " >
      <v-container  fluid ml-10>
        <v-row>
          <v-col cols="2">
            <Navigation></Navigation>
          </v-col>

          <v-col>
            <v-sheet
                min-height="85vh"
                max-height="85vh"
                class="mr-15"
                rounded="lg"
            >
              <router-view/>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Navigation from "@/components/Navigation";
import {mapGetters} from "vuex";
import {mapActions} from "vuex";

export default {
  components: {Navigation},
  title:'hallo',
  methods:{
    signOut(){
      this.signOutAction()
      this.$router.replace(({
        name: 'home'
      }))
    },
    ...mapActions(
        {
          signOutAction: 'auth/signOut'
        }
    )
  },
  computed: {
    ...mapGetters(
        {
          authenticated: 'auth/authenticated',
          user: 'auth/user',
        }),

  }

}
</script>

<style>
/*-webkit-appearance: none;*/

</style>