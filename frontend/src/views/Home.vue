<template>
  <div>
    <v-row>

      <v-col cols="12" sd="4" md="4"  v-for="card in cards"
             :key="card.id" >

        <CardDialect

            :card="card"></CardDialect>


      </v-col>
    </v-row>
  </div>
</template>

<script>
import CardDialect from "@/components/CardDialect";
import RequestHandler from "@/utils/RequestHandler"

export default {
  name: "Home",
  components: {CardDialect},
  data: () =>  ({
    cards : [],
  }),

  mounted() {
    RequestHandler.getCards()
    .then(response => (
        this.cards = response.data
    ))
  }
}
</script>

<style scoped>

</style>