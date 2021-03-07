<template>
  <div>
    <v-radio-group
            v-model="favorite"
            mandatory
        >
    <v-row no-gutters v-for="(item, i) in items" :key="i" class="text-fields-row">
      <v-radio
              :value="item"
            ></v-radio>
      <v-col cols="6">
        <input-location v-model="item.value"></input-location>
      </v-col>
      <v-col><v-icon @click="remove(i)" class="mt-7">mdi-delete</v-icon> </v-col>
    </v-row>
      <v-col><v-btn @click="addLine">zusätzlichen Ort hinzufügen</v-btn> </v-col>
    </v-radio-group>
  </div>

</template>
<script>
import InputLocation from "./InputLocation";

export default {
  name: "SettignsLocationMultiple",
  props: ["value", "label"],
  components: { InputLocation },
  data: () => ({
    favorite:{ "value": { "id": 18774, "zipcode": "6710", "place": "Nenzinger Himmel", "state": "Vorarlberg" } } ,
    initFav: false,
  }),
  methods: {
    addLine() {
      this.value.push({ value: { id: -1, zipcode: "", place: "" } });
    },
    remove(index) {
      this.items.splice(index, 1);
    },
  },
  computed: {
    items() {
      if (this.value.length === 0)
        return [{ value: { id: -1, zipcode: "", place: "" } }];
      return this.value;
    },
  },
  watch:{
    favorite(){
      console.log('asd')
      this.$emit('inputFav',this.favorite)
    }
  }
};
</script>