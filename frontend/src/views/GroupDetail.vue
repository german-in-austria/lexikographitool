<template>
  <v-container>
    <v-row no-gutters>
      <v-col>
        <span class="text-h3">{{ group.name }}</span>
        <span class="text-h5">{{ group.description }}</span>

        <v-combobox
          v-model="collectionAdd"
          :items="collectionsOwned"
          item-text="name"
          label="Sammlung zur Gruppe Hinzufügen"
          hide-no-data
          append-icon="mdi-plus"
          :return-object="true"
          @click:append="addCollection()"
        ></v-combobox>
        <v-row no-gutters>
          <v-col cols="12" sd="4" md="3">
            <collection-create-button
              @created="collectionCreated"
              class="ma-1"
            ></collection-create-button>
          </v-col>
          <v-col md="3" sd="4"
          v-for="collection in group.collections" :key="collection.id">
            <card-collection
              :collection="collection"
              class="ma-1"
            ></card-collection>
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="4" class="ml-auto">
        <v-list>
          <v-subheader class="text-h6">Mitglieder</v-subheader>
          <v-list-item>
            <v-combobox
              v-model="user"
              :items="users"
              item-text="username"
              label="Mitglied hinzufügen"
              hide-no-data
              :search-input.sync="loadUsers"
              append-icon="mdi-plus"
              :return-object="false"
              @click:append="addMember()"
            >
            </v-combobox>
          </v-list-item>
          <v-list-item v-for="member in group.members" :key="member.username">
            <v-list-item-title>
              {{ member.username }}
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import RequestHandler from "../utils/RequestHandler.js";
import Group from "../objects/Group.js";
import CardCollection from "../components/CardCollection";
import CollectionCreateButton from "../components/CollectionCreateButton";
export default {
  components: { CardCollection, CollectionCreateButton },
  data: () => ({
    users: [],
    user: "",
    username: "",
    group: new Group(),
    loadUsers: null,
    collectionsOwned: [],
    collectionAdd: "",
  }),
  mounted() {
    RequestHandler.getGroup(this.$route.params.id).then((response) => {
      this.group = response.data;
    });
    RequestHandler.getCollectionsByOwner().then((response) => {
      this.collectionsOwned = response.data;
    });
  },
  methods: {
    addMember() {
      RequestHandler.addMemberToGroup(this.$route.params.id, this.user).then(
        (response) => (this.group = response.data)
      );
    },
    addCollection() {
      RequestHandler.addGroupToCollection(
        this.collectionAdd.id,
        this.$route.params.id
      ).then((response) => {
        this.group.collections.push(response.data);
        this.collectionAdd = "";
      });
    },
    collectionCreated(value) {
      this.collectionAdd = value;
      this.addCollection();
    },
  },
  watch: {
    loadUsers() {
      this.user = this.loadUsers;
      if (this.loadUsers.length != 1) return;
      this.isLoading = true;
      RequestHandler.getUsersByUsername(this.loadUsers)
        .then((response) => (this.users = response.data))
        .catch((err) => {
          console.log(err);
        })
        .finally(() => (this.isLoading = false));
    },
  },
};
</script>

