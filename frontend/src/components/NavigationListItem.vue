<template>
  <v-list-item
      link
      :to="link"
  >
        <v-icon >{{ icon }}</v-icon>
      <v-list-item-title class="ml-5 hidden-md-and-down">
        {{ name }}
      </v-list-item-title>
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