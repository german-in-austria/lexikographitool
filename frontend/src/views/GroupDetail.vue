<template>
  <v-container fluid v-if="group">
    <v-row no-gutters>

      <v-col>
      <v-row>
        <v-col cols="8">
        <p class="text-h3">{{ group.name }}</p>
        <p class="text-h5">{{ group.description }}</p>
        </v-col>
        <v-col>
        <group-settings-dialog :group="group" v-if="group.is_owner"></group-settings-dialog>
        </v-col>
      </v-row>
          <v-combobox
            v-model="collectionAdd"
            :items="collectionsOwned"
            item-text="name"
            label="Sammlung zur Gruppe Hinzufügen"
            hide-no-data
            append-icon="mdi-plus"
            :return-object="true"
            @click:append="addCollection()"
            v-if="group.is_owner & false"
        ></v-combobox>
        <v-row no-gutters class="mt-5">
          <v-col cols="12" sd="6" md="4" v-if="group.can_create_collection"
          >
            <collection-create-button
                @created="collectionCreated"
                class="ma-1"
            ></collection-create-button>
          </v-col>
          <v-col md="4" sd="6"
                 v-for="collection in group.collections" :key="collection.id">
            <card-collection
                :collection="collection"
                class="ma-1"
            ></card-collection>
          </v-col>
        </v-row>
      </v-col>
      <v-divider vertical style="height:83vh" class="mx-5"></v-divider>
      <v-col cols="3" class="ml-auto">
        <v-list>

          <v-list-item v-if="group.is_owner">
            <v-text-field v-model="inviteLink" id="tocopy"
                          append-icon="mdi-content-copy"
                          @click:append="copyText"
                          outlined
                          readonly
                          label="Einladungs-Link"></v-text-field>

          </v-list-item>
          <v-subheader class="text-h6">Mitglieder</v-subheader>
          <v-list-item>
            <v-list-item-title>
              {{ group.owner.username }}
            </v-list-item-title>
          </v-list-item>
          <v-list-item v-for="member in group.members" :key="member.username">
            <v-list-item-title>
              {{ member.username }}
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
    <v-snackbar
        v-model="snackbar"
        :timeout="1000"
        color="info"
    >
      Kopiert
    </v-snackbar>
  </v-container>
</template>

<script>
import RequestHandler from "../utils/RequestHandler.js";
import CardCollection from "../components/CardCollection";
import CollectionCreateButton from "../components/CollectionCreateButton";
import {mapGetters} from "vuex";
import GroupSettingsDialog from "@/components/GroupSettingsDialog";

export default {
  components: {GroupSettingsDialog, CardCollection, CollectionCreateButton},
  data: () => ({
    snackbar: false,
    users: [],
    user: "",
    username: "",
    group: '',
    loadUsers: null,
    collectionsOwned: [],
    collectionAdd: "",
    inviteLink: "",
  }),
  mounted() {
    RequestHandler.getGroup(this.$route.params.id).then((response) => {
      this.group = response.data;
      if(this.group.os_owner)
        RequestHandler.getInvite(this.$route.params.id).then(response => {
          this.inviteLink = 'https://lex.dioe.at/groups/join/' + this.$route.params.id + '/' + response.data
        })
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
    copyText() {
      let input = document.getElementById("tocopy");
      input.select();
      document.execCommand("copy");
      this.snackbar = true;
    }
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
    }
  },
  computed: {
    ...mapGetters(
        {
          authenticated: 'auth/authenticated',
          userSignedIn: 'auth/user',
        }),
  },
}

</script>

