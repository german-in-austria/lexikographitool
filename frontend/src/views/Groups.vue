<template>
  <v-container fluid v-scroll='onScroll'>
    <v-row no-gutters>
      <span class="text-h3">Gruppen</span>
    </v-row>
    <v-row no-gutters class="pt-5">
      <v-text-field
        v-model="search"
        label="Suche"
        single-line
        clearable
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-magnify"
        class='pr-5'
      ></v-text-field>
      <v-btn-toggle v-model="pub" mandatory :style="$vuetify.breakpoint.xs ? 'flex-direction: column;' : ''">
        <v-btn large :value="false"> Meine Gruppen </v-btn>
        <v-btn large :value="true"> öffentliche Gruppen </v-btn>
      </v-btn-toggle>

      <trash-can-dialog :itemList="groups" :group="true"></trash-can-dialog>
    </v-row>
    <v-row no-gutters>
      <v-col cols="12" sd="4" md="3" v-if="!pub" class="pa-3">
          <group-create-button></group-create-button>
      </v-col>
      <v-col
        cols="12"
        sd="4"
        md="3"
        v-for="group in groups"
        :key="group.id"
        class="pa-3"
      >
        <v-hover v-slot="{ hover }">
          <v-card
            :to="'/groups/' + group.id"
            :elevation="hover ? 4 : 0"
            class="mx-auto"
            outlined
          >
            <v-card-title>{{ group.name }}</v-card-title>
            <v-card-text>{{ group.description }}</v-card-text>
          </v-card>
        </v-hover>
      </v-col>
      <p class="text-body-1" v-if="(groups.length == 0) & !!search">
        Keine Treffer
      </p>
    </v-row>
    
  </v-container>
</template>

<script>
import TrashCanDialog from "../components/TrashCanDialog.vue";
import Axios from "axios";
import GroupCreateButton from '../components/GroupCreateButton.vue';

export default {
  components: { TrashCanDialog,  GroupCreateButton },
  name: "Group",
  data: () => ({
    groups: [],
    next: null,
    search: "",
    pub: false,
    tab: null,
    groupTitle: "",
    groupDescription: "",

    timeout:null,
  }),
  methods: {
    
    loadGroups() {
      const public_python_param = this.pub ? "True" : "False";
      Axios.get(
        "groups/public/?page=1&page_size=25&public=" +
          public_python_param +
          "&search=" +
          this.search
      ).then((response) => {
        this.groups = response.data.results;
        this.next = response.data.links.next;
      });
    },
    onScroll(e) {
      console.log(this.next);
      if (
        e.target.scrollingElement.scrollTop ===
          e.target.scrollingElement.scrollTopMax &&
        !!this.next
      ) {
        Axios.get(this.next).then((response) => {
          this.groups = this.groups.concat(response.data.results);
          this.next = response.data.links.next;
        });
      }
    },
  },
  mounted() {
    Axios.get("groups/public/?page=1&public=False&page_size=25").then((response) => {
      this.groups = response.data.results;
      this.next = response.data.links.next;
    });
  },
  watch: {
    pub() {
      this.loadGroups();
    },
    search() {
      clearTimeout(this.timeout);

      let self = this;
      this.timeout = setTimeout(function () {
        
        self.loadGroups();
      }, 500);

    },
  },
};
</script>

<style scoped>
</style>