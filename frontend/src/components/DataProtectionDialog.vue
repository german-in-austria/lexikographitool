<template>
    <v-dialog v-model="dialog" scrollable max-width="60vh">
    <template v-slot:activator="{ on, attrs }">
      <a v-bind="attrs">Datenschutrichtlinien</a>
    </template>
    <v-card height="80vh">
    </v-card>
    </v-dialog>

</template>

<script>
export default {
    
}
</script>