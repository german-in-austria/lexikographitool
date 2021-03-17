<template>

  <div style="position: relative">
    <v-btn style="z-index: 5" to="/card-create" class="btn-round " width="5rem" height="5rem" fab x-large  elevation="0"  fixed >
      <v-icon>mdi-plus</v-icon>
    </v-btn>
  <v-bottom-navigation fixed style="z-index: 4">

    <v-btn  to="/lexemes" icon>
      <v-icon>mdi-sofa-outline</v-icon>
    </v-btn>

    <v-btn  to="/collections" icon>
      <v-icon>mdi-file-multiple-outline</v-icon>
    </v-btn>

    <v-btn disabled color="deep-purple accent-4" to="/" icon>
      <v-icon>mdi-home-outline</v-icon>
    </v-btn>

    <v-btn  to="/groups" icon>
      <v-icon>mdi-account-group-outline</v-icon>
    </v-btn>

    <v-btn to="/postings" icon>
      <v-icon>mdi-chat-processing-outline</v-icon>
    </v-btn>
  </v-bottom-navigation>
  </div>
</template>

<script>
export default {
name: "NavigationMobile"
}
</script>

<style scoped>

.btn-round{
  bottom: -13px;
  margin: auto;
  left: 0;
  right: 0;

  border-style: solid;
  border-width: thin;
  border-color: lightgray;
}
</style>

