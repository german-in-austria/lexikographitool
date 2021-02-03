<template>
  <v-btn-toggle
      v-bind:value="value"
      @change="$emit('input',$event)"
      color="deep-purple accent-3"
      mandatory
  >
    <v-btn
        v-for="item in items"
        :key="item.id"
        :value="item.value"
    >
      {{item.name}}
    </v-btn>
  </v-btn-toggle>
</template>

<script>
export default {
name: "InputButtonGroup",
  props:['value','items'],
  data:()=>({
  }),
  computed:{
  buttonValue: function (){
    return this.value
  }
  }
}
</script>

<style scoped>

</style>