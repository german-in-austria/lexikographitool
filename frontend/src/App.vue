<template>
   <Main ></Main>
</template>

<script>

// import 'vuetify/dist/vuetify.min.css'

import Main from "@/views/Main";
export default {
  components: {Main},
  created () {
    document.title = "Wortgut";
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css? family=Lato:300,400,700&display=swap');
</style>