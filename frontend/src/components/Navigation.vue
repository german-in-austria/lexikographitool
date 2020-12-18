<template>
  <v-sheet rounded="lg">
    <v-list color="transparent">
      <NavigationListItem link="/" icon="mdi-home-outline" name="Startseite"></NavigationListItem>
      <NavigationListItem v-if="authenticated" link="/collections" icon="mdi-file-multiple-outline" name="Sammlungen"></NavigationListItem>
      <NavigationListItem v-if="authenticated" link="/groups" icon="mdi-account-group-outline" name="Gruppen"></NavigationListItem>
      <NavigationListItem link="/dataset" icon="mdi-layers-triple-outline" name="Datenbank"></NavigationListItem>
      <NavigationListItem v-if="authenticated" link="/aufruf" icon="mdi-chat-processing-outline" name="Aufruf starten"></NavigationListItem>
      <NavigationListItem v-if="authenticated" link="/account" icon="mdi-account-settings-outline" name="Profil"></NavigationListItem>
      <NavigationListItem v-if="authenticated" link="/card-create" icon="mdi-plus" name="Wort hinzufügen"></NavigationListItem>


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