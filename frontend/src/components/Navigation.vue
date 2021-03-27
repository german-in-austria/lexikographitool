<template>

  <v-sheet height="100vh" style="border-right: solid; border-right-width: 1px;
   border-color: lightgray" width=auto >
    <v-list color="transparent" class="mt-15">
      <NavigationListItem link="/neuerStart" icon="mdi-home-outline" name="Start"></NavigationListItem>
      <v-divider></v-divider>
      <NavigationListItem v-if="false" link="/" icon="mdi-home-outline" name="Home"></NavigationListItem>
      <v-divider></v-divider>

      <NavigationListItem link="/Lexemes" icon="mdi-sofa-outline" name="Wörter"></NavigationListItem>
      <v-divider></v-divider>
      <NavigationListItem v-if="authenticated" link="/dashboard" icon="mdi-view-dashboard-variant-outline" name="Pinnwand"></NavigationListItem>
      <v-divider></v-divider>
      <NavigationListItem v-if="authenticated" link="/collections" icon="mdi-file-multiple-outline" name="Sammlungen"></NavigationListItem>
      <v-divider></v-divider>

      <NavigationListItem v-if="authenticated" link="/groups" icon="mdi-account-group-outline" name="Gruppen"></NavigationListItem>
      
      <v-divider></v-divider>

      <NavigationListItem v-if="authenticated" link="/postings" icon="mdi-chat-processing-outline" name="Fragen"></NavigationListItem>
      <v-divider></v-divider>

      <NavigationListItem v-if="authenticated" link="/card-create" icon="mdi-plus" name="Wort erstellen"></NavigationListItem>
      <v-divider></v-divider>

      <NavigationListItem v-if="isSuperUser" link="/reports" icon="mdi-alert-decagram" name="Meldungen"></NavigationListItem>

    </v-list>
  </v-sheet>
</template>

<script>
import {mapGetters} from 'vuex'
import NavigationListItem from "@/components/NavigationListItem";

export default {
  name: "Navigation",
  components: {NavigationListItem},
  data: () => ({
    
  }),
  computed: {
    ...mapGetters(
        {
          authenticated: 'auth/authenticated',
          isSuperUser: 'auth/isSuperUser',
        })
  }
}
</script>

<style scoped>

</style>