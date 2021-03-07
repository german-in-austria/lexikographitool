<template>

  <v-sheet min-height="85vh" color="transparent" width="12rem">
    <v-list color="transparent">
      <NavigationListItem link="/" icon="mdi-home-outline" name="Start"></NavigationListItem>
      <v-divider></v-divider>
      <NavigationListItem v-if="false" link="/" icon="mdi-home-outline" name="Home"></NavigationListItem>
      <v-divider></v-divider>

      <NavigationListItem link="/Lexemes" icon="mdi-sofa-outline" name="Wörter"></NavigationListItem>
      <v-divider></v-divider>

      <NavigationListItem v-if="authenticated" link="/collections" icon="mdi-file-multiple-outline" name="Sammlungen"></NavigationListItem>
      <v-divider></v-divider>

      <NavigationListItem v-if="authenticated" link="/groups" icon="mdi-account-group-outline" name="Gruppen"></NavigationListItem>
      
      <v-divider></v-divider>

      <NavigationListItem v-if="authenticated" link="/postings" icon="mdi-chat-processing-outline" name="Fragen"></NavigationListItem>

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
        })
  }
}
</script>

<style scoped>

</style>