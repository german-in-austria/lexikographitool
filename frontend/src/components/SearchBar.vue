<template>
  <div style="background-color: white">
    <v-row no-gutters>
      <v-col>
        <v-row no-gutters>
          <v-col cols="12">{{ $t("searchbar.search") }}</v-col>
          <v-col>
            <v-select dense
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
          <v-col>
            <v-text-field
                dense

                v-model="search"
                label="Suche"
                :disabled="field.disabled"
                flat
                solo-inverted
                hide-details
            ></v-text-field>
          </v-col>
          <v-col class="hidden-xs-only">
            <v-btn
                @click="addToFilter"
                :disabled="field.disabled || !search"
                color="primary"
                height="38px"
            >
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
      <v-col
      >
        <v-row no-gutters>
          <v-col cols="12">{{ $t("searchbar.orderby") }}</v-col>

          <v-col>
            <v-select
                dense
                label="Sortieren nach"
                :items="orderItems"
                v-model="orderBy"
                :return-object="true"
                flat
                solo-inverted
                hide-details
                prepend-inner-icon="mdi-sort-variant"
                style="max-width: 10rem"
            ></v-select>
          </v-col>
          <v-col>
            <v-btn-toggle dense v-model="sortDesc" mandatory>
              <v-tooltip v-model="show" bottom max-width="20vh">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn v-on="on" v-bind="attrs" depressed :value="false">
                    <v-icon>mdi-arrow-up</v-icon>
                  </v-btn>
                </template>
                {{ $t("searchbar.ascending") }}
              </v-tooltip>
              <v-tooltip v-model="show" bottom max-width="20vh">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn v-on="on" v-bind="attrs" depressed :value="true">
                    <v-icon>mdi-arrow-down</v-icon>
                  </v-btn>
                </template>
                {{ $t("searchbar.descending") }}
              </v-tooltip>
            </v-btn-toggle>
          </v-col>
        </v-row>
      </v-col
      >
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
  data: function () {
    return {
      show: false,
      selectItems: [
        {text: this.$t("card.lemma"), value: "dialectWord", disabled: false},
        {text: this.$t("card.lexeme"), value: "word", disabled: false},
        {text: this.$t("card.meaning"), value: "description", disabled: false},
        {text: this.$t("card.category"), value: "categories__category", disabled: false},
        {text: this.$t("card.variety"), value: "variety", disabled: false},

        // { text: this.$t("card.kind"), value: "kind", disabled: false },
      ],
      orderItems: [
        {text: this.$t("card.lemma"), value: "content__dialectWord"},
        {text: this.$t("card.lexeme"), value: "content__word"},
        {text: this.$t("searchbar.created_at"), value: "date_created"},
      ],
      filters: [],
      field: {text: this.$t("card.lemma"), value: "dialectWord", disabled: false},
      search: "",
      sortDesc: true,
      orderBy: {text: this.$t("searchbar.created_at"), value: "date_created"},
    }
  },
  methods: {
    addToFilter() {
      const index = this.selectItems.findIndex(
          (x) => x.value === this.field.value
      );
      this.selectItems[index].disabled = true;
      this.field.disabled = true;
      this.filters.push({field: this.field, value: this.search});
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
      if (this.filters.length !== 0)
        this.filters.forEach((item) => {
          requestString +=
              "content__" + item.field.value + "__icontains=" + item.value + "&";
        });
      //add current search to filters
      if (!this.field.disabled)
        requestString =
            requestString +
            "content__" +
            this.field.value +
            "__icontains=" +
            this.search +
            "&";

      //add ordering
      requestString += this.orderingString;
      return requestString;
    },
  },
};
</script>