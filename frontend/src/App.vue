<template>
  <Main></Main>
</template>

<script>

// import 'vuetify/dist/vuetify.min.css'

import Main from "@/views/Main";

export default {
  components: {Main},
  name: 'App',
  head() {
    return {
      title: "Wortgut",
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {hid: 'og:title', name: 'og:title', content: 'Wortgut'},
        {hid: 'og:site_name', name: 'og:site_name', content: 'Wortgut'},
        {hid: 'og:type', name: 'og:type', content: 'website'},
        {hid: 'og:image', name: 'og:image', content: 'https://lex.dioe.at/img/IamDioeLogo.475528a1.png'},
        {hid: 'og:description', name: 'og:type', content: 'In jedem von uns steckt ein/e Lexikograph/in!'},
        {hid: 'og:url', name: 'og:url', content: 'https://lex.dioe.at/'},
      ]
    }
  },
  // metaInfo(){
  //   return{
  //   title: 'Wortgut',
  //   titleTemplate: '%s',
  //   meta: [
  //     // OpenGraph data (Most widely used)
  //     {property: 'og:title', content: 'Wortgut'},
  //     {property: 'og:site_name', content: 'Wortgut.'},
  //     // The list of types is available here: http://ogp.me/#types
  //     {property: 'og:type', content: 'website'},
  //     // Should the the same as your canonical link, see below.
  //     {property: 'og:url', content: 'https://lex.dioe.at/'},
  //     {property: 'og:image', content: 'https://lex.dioe.at/img/IamDioeLogo.475528a1.png'},
  //     // Often the same as your meta description, but not always.
  //     {property: 'og:description', content: 'In jedem von uns steckt ein/e Lexikograph/in!'},
  //
  //     // Twitter card
  //     {name: 'twitter:site', content: 'https://lex.dioe.at/'},
  //     {name: 'twitter:title', content: 'Wortgut'},
  //     {name: 'twitter:description', content: 'In jedem von uns steckt ein/e Lexikograph/in!'},
  //     // Your twitter handle, if you have one.
  //
  //     // Google / Schema.org markup:
  //     {itemprop: 'name', content: 'Wortgut'},
  //     {itemprop: 'description', content: 'In jedem von uns steckt ein/e Lexikograph/in!'},
  //     {itemprop: 'image', content: 'https://lex.dioe.at/img/IamDioeLogo.475528a1.png'}
  //   ]}
  // }
}
</script>

<style>
p {
  text-align: justify;
}
</style>