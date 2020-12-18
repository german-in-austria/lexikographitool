<template>
  <v-container>
    <v-subheader>
      {{ group.name }} <br />
      {{ group.description }}
    </v-subheader>

    <v-row no-gutters>
      <vcol>
        <v-list>
          <v-subheader>Mitglieder</v-subheader>
          <v-list-item>
            <v-combobox
              v-model="user"
              :items="users"
              item-text="username"
              label="Mitglied hinzufügen"
              hide-no-data
              :search-input.sync="loadUsers"
              :loading="isLoading"
              append-icon="mdi-plus"
              return-object="false"
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
      </vcol>

      <vcol>
        <v-list>
          <v-subheader>Sammlungen</v-subheader>
          <v-list-item>
            <v-combobox
              v-model="collectionAdd"
              :items="collectionsOwned"
              item-text="name"
              label="Sammlung zur Gruppe Hinzufügen"
              hide-no-data
              :search-input.sync="loadCollections"
              append-icon="mdi-plus"
              return-object="true"
              @click:append="addCollection()"
            ></v-combobox>
          </v-list-item>
          <v-list-item
            v-for="collection in group.collections"
            :key="collection.id"
          >
            <v-list-item-title>
              {{ collection.name }}
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </vcol>
    </v-row>
  </v-container>
</template>

<script>
import RequestHandler from "../utils/RequestHandler.js";
import Group from "../objects/Group.js";
export default {
  data: () => ({
    users: ["hoi"],
    user: "asd",
    username: "",
    group: new Group(),
    loadUsers: null,
    collectionsOwned: [],
    collectionAdd: '',
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
      ).then((response) => this.group.collections.push(response.data));
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

