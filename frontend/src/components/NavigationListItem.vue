<template>
  <v-list-item
      class="d-flex justify-center"
      color="black"
      link
      :to="link"

  >
    <v-col class="justify-center">
      <v-list-item-icon class="justify-center">
        <v-icon large>{{ icon }}</v-icon>
      </v-list-item-icon>

      <v-list-item-title class="">
        {{ name }}
      </v-list-item-title>
    </v-col>
  </v-list-item>
</template>

<script>
export default {
  name: "NavigationListItem",
  props:['link','icon','name']
}
</script>

<style scoped>

</style>