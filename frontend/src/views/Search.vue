<template>
  <v-container fluid>
    <p class="text-h3">Suche nach: {{ $route.params.search }}</p>
    <v-list v-if="lexemes.length != 0">
      <v-list-item-subtitle>Wörter</v-list-item-subtitle>
      <v-list-item
        v-for="(lexeme, index) in lexemes"
        :key="index"
        @click="$router.push('/lexeme/' + lexeme.id)"
      >
        <v-list-item-title
          >{{ lexeme.dialectWord }} {{ lexeme.word }},{{ lexeme.description }}
        </v-list-item-title>
      </v-list-item>
      <v-list-item v-if="!!lexemesNext">
        <v-btn text @click="loadMoreLexemes"> Mehr..</v-btn>
      </v-list-item>
    </v-list>
    <v-list v-if="collections.length != 0">
      <v-list-item-subtitle>Sammlungen</v-list-item-subtitle>
      <v-list-item
        v-for="(collection, index) in collections"
        :key="index"
        @click="$router.push('/collections/' + collection.id)"
      >
        <v-list-item-title
          >{{ collection.name }} {{ collection.description }}
        </v-list-item-title>
      </v-list-item>
      <v-list-item v-if="!!collectionNext">
        <v-btn text @click="loadMoreCollections"> Mehr..</v-btn>
      </v-list-item>
    </v-list>

    <v-list v-if="groups.length != 0">
      <v-list-item-subtitle>Gruppen</v-list-item-subtitle>
      <v-list-item
        v-for="(group, index) in groups"
        :key="index"
        @click="$router.push('/groups/' + group.id)"
      >
        <v-list-item-title
          >{{ group.name }} {{ group.description }}
        </v-list-item-title>
      </v-list-item>
     <v-list-item v-if="!!groupsNext">
        <v-btn text @click="loadMoreGroups"> Mehr..</v-btn>
      </v-list-item>
    </v-list>
    <p v-if="groups.length + collections.length + lexemes.length===0">{{$t("search.noResults")}}</p>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    lexemes: [],
    lexemesNext: null,
    collections: [],
    collectionNext: null,
    groups: [],
    groupsNext: null,
  }),
  mounted() {
    axios
      .get("lexemes/?search=" + this.$route.params.search + "&page_size=5")
      .then((response) => {
        this.lexemes = response.data.results;
        this.lexemesNext = response.data.links.next;
      });

    axios
      .get(
        "collections/?search=" +
          this.$route.params.search +
          "&page_size=5"
      )
      .then((response) => {
        this.collections = response.data.results;
        this.collectionsNext = response.data.links.next;
      });

    axios
      .get(
        "groups/public/?search=" + this.$route.params.search + "&page_size=5"
      )
      .then((response) => {
        this.groups = response.data.results;
        this.groupsNext = response.data.links.next;
      });
  },
  methods: {
    loadMoreLexemes() {
      axios.get(this.lexemesNext).then((response) => {
        this.lexemes = this.lexemes.concat(response.data.results);
        this.lexemesNext = response.data.links.next;
      });
    },
    loadMoreCollections() {
      axios.get(this.collectionsNext).then((response) => {
        this.collections = this.collections.concat(response.data.results);
        this.collectionsNext = response.data.links.next;
      });
    },
    loadMoreGroups() {
      axios.get(this.groupsNext).then((response) => {
        this.groups = this.groups.concat(response.data.results);
        this.groupsNext = response.data.links.next;
      });
    },
  },
};
</script>