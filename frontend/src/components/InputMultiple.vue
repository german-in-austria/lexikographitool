<template>
  <div>
    <div
        v-for="(item, i) in items"
        :key="i"
        class="text-fields-row"
    >
      <v-text-field
          :label="label"
          v-model="item.value"
          @input="$emit('input',items)"
          :append-icon="i ===items.length-1 ? 'mdi-plus':undefined"
          :append-outer-icon="'mdi-delete-outline'"
          @click:append-outer="remove(i)"
          @click:append="addLine"
      ></v-text-field>
    </div>
  </div>
</template>

<script>


export default {
  name: "InputMultiple",
  props: ['value', 'label'],
  data: () => ({
    text: null,
    asdf: [''],
    // items: ['']
  }),
  methods: {
    addLine() {
      this.value.push({value:''})
    },
    remove(index) {
      this.items.splice(index, 1)
    },
  },
    watch: {
    value(){
      // this.items = [{value:this.value}]
    }
    },
  computed: {
    items(){
      if (this.value.length=== 0)
        return [{value:''}]
      return this.value
    }

  },
  mounted() {
    // this.value =[{value:''}]
  }

}
</script>

<style scoped>
.text-fields-row {
  display: flex;
}
</style>