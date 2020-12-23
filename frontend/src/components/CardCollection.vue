<template>
  <div>
    <v-hover v-slot="{ hover }">
      <v-card
        :to="'/collections/' + collection.id"
        :elevation="hover ? 12 : 2"
        class="mx-auto"
        max-width="300"
      >
        <v-card-title>{{ collection.name }}</v-card-title>
      </v-card>
    </v-hover>
  </div>
</template>
<script>
export default {
    data: () =>({
    }),
    props: ['collection']
};
</script>