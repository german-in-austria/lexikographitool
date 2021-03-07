<template>
  <div style="background-color: white">
    <v-row no-gutters>
      <v-col cols="12" sd="8">
      <v-row>

        <v-col cols="5" sd="3">
          <v-select
            label="Suche nach"
            :items="selectItems"
            v-model="field"
            :return-object="true"
            flat
            solo-inverted
            hide-details
            prepend-inner-icon="mdi-magnify"
          ></v-select>
        </v-col>
        <v-col cols="7" sd="5">
          <v-text-field
            v-model="search"
            label="Suche"
            :disabled="field.disabled"
            flat
            solo-inverted
            hide-details
            prepend-inner-icon="mdi-magnify"
          ></v-text-field>
        </v-col>
        <v-col cols="5" sd="1" class="hidden-xs-only">
          <v-btn
            @click="addToFilter"
            :disabled="field.disabled || !search"
            color="primary"
            large
            >zusätzlicher Filter</v-btn
          >
        </v-col>
        </v-row>
      </v-col>
      <v-col cols="12" sm="4" class="hidden-xs-only">
        <v-row>
        <v-col>
        <v-select
          label="Sortieren nach"
          :items="orderItems"
          v-model="orderBy"
          :return-object="true"
          flat
          solo-inverted
          hide-details
          prepend-inner-icon="mdi-sort-variant"
        ></v-select>
        </v-col>
        <v-col>
        <v-btn-toggle v-model="sortDesc" mandatory>
          <v-btn large depressed :value="false">
            <v-icon>mdi-arrow-up</v-icon>
          </v-btn>
          <v-btn large depressed :value="true">
            <v-icon>mdi-arrow-down</v-icon>
          </v-btn>
        </v-btn-toggle>
        </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row>
      <v-chip
        v-for="(filter, index) in filters"
        :key="index"
        class="ma-2"
        close
        @click:close="removeFromFilters(index)"
      >
        {{ filter.field.text }} : {{ filter.value }}
      </v-chip>
    </v-row>
  </div>
</template>
<script>
export default {
  name: "SearchBar",
  data: () => ({
    selectItems: [
      { text: "Dialektwort", value: "dialectWord", disabled: false },
      { text: "Bedeutung", value: "description", disabled: false },
      { text: "hochdeutscher Begriff", value: "word", disabled: false },
      { text: "Dialekt", value: "dialect__dialect", disabled: false },
      { text: "Wortart", value: "kind", disabled: false },
      { text: "Kategorie", value: "categories__category", disabled: false },
      { text: "Wortart", value: "kind", disabled: false },
      { text: "Wortart", value: "kind", disabled: false },
    ],
    orderItems: [
      { text: "Dialektwort", value: "dialectWord" },
      { text: "hochdeutscher Begriff", value: "word" },
      { text: "Neuste", value: "date_created" },
    ],
    filters: [],
    field: { text: "Dialektwort", value: "dialectWord", disabled: false },
    search: "",
    sortDesc: "",
    orderBy: { text: "Neuste", value: "date_created" },
  }),
  methods: {
    addToFilter() {
      const index = this.selectItems.findIndex(
        (x) => x.value === this.field.value
      );
      this.selectItems[index].disabled = true;
      this.field.disabled = true;
      this.filters.push({ field: this.field, value: this.search });
    },
    removeFromFilters(index) {
      const ind = this.selectItems.findIndex(
        (x) => x.value === this.filters[index].field.value
      );
      this.selectItems[ind].disabled = false;
      this.field.disabled = false;

      this.filters.splice(index, 1);
    },
  },
  watch: {
    requestString() {
      this.$emit("input", this.requestString);
    },
  },
  computed: {
    orderingString() {
      if (this.sortDesc) return "ordering=-" + this.orderBy.value;
      return "ordering=" + this.orderBy.value;
    },
    requestString() {
      var requestString = "";
      //Add all saved filters to string
      if (this.filters.length != 0)
        this.filters.forEach((item) => {
          requestString +='content__' + item.field.value + "__icontains=" + item.value + "&";
        });
      //add current search to filters
      if (!this.field.disabled)
        requestString =
          requestString + 'content__' + this.field.value + "__icontains=" + this.search + "&";

      //add ordering
      requestString += this.orderingString;
      return requestString;
    },
  },
};
</script>