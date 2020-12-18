<template>
  <v-row>
    <v-col>
     <v-autocomplete
          v-model="zip"
          :items="items"
          :loading="isLoading"
          hide-no-data
          hide-selected
          item-text="place"
          label="Ort"
          return-object
          @change="updateParent"
          :search-input.sync="searchplace"
          append-icon=""
  :rules="[v => !!v || 'Ort muss angegeben werde']"
  required

     ></v-autocomplete>
    </v-col>
    <v-col>
      <v-autocomplete
          v-model="zip"
          :items="items"
          :loading="isLoading"
          hide-no-data
          hide-selected
          item-text="zipcode"
          :search-input.sync="searchzip"
          append-icon=""

          label="Plz"
          return-object
          @change="updateParent"

  :rules="[v => !!v || 'Ort muss angegeben werde']"
  required
      ></v-autocomplete>
    </v-col>
  </v-row>
</template>

<script>

export default {
  name: "CardCreateLocation",
  data: () =>({
    zips: [],
    items: [],
    isLoading: false,
    zip: '',
    searchplace: null,
    descriptionLimit: 60,
    searchzip: null
  }),
  methods:{
    reload: function(search){
      //Lazily load input items
      fetch('http://127.0.0.1:8000/origin/'+ search +'/')
          .then(res => res.clone().json())
          .then(res => {
            this.items = res
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => (this.isLoading = false))
    },
    updateParent: function(){
      this.$emit('inputData', this.zip)
    }
  },
  watch: {
    searchplace () {
      // Items have already been loaded
      if (this.searchplace.length <= 1){
        this.items = []
        return
      }
      if (this.searchplace.length > 2) return
      this.isLoading = true
      this.reload(this.searchplace)

    },
    searchzip () {
      // Items have already been loaded
      if (this.searchzip.length != 1) return

      this.isLoading = true
      this.reload(this.searchzip)

    }
  },
}
</script>

<style scoped>

</style>