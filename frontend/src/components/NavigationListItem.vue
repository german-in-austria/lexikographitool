<template>
  <v-list-item
      link
      :to="link"

  >
      <v-list-item-icon >
        <v-icon large>{{ icon }}</v-icon>
      </v-list-item-icon>

      <v-list-item-title >
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