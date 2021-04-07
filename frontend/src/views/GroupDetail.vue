<template>
  <v-container fluid v-if="group">
    <v-row no-gutters>
      <v-col cols="12" >
        <v-row no-gutters>
          <v-col col="12">
            <p class="text-h3">{{ group.name }}</p>
            <p class="text-body-2">{{ group.organization }}</p>
            <p class="text-body-1">{{ group.description }}</p>
          </v-col>
          <v-col align="right" cols="1">
            <v-menu left v-if="group.is_member">
              <template v-slot:activator="{ on, attrs }">
                <v-icon v-bind="attrs" v-on="on">mdi-dots-vertical </v-icon>
              </template>
              <v-list>
                <group-settings-dialog
                  :group="group"
                  v-if="group.is_owner"
                ></group-settings-dialog>
                <GroupDetailMemberDialog v-if="group.is_member" :group="group"></GroupDetailMemberDialog>
                <group-detail-invitation-link-dialog v-if="group.is_owner"></group-detail-invitation-link-dialog>
                <v-list-item v-if="!group.is_owner" @click="leaveGroup"
                  ><span class="error--text">{{
                    $t("groupDetails.leaveGroup")
                  }}</span></v-list-item
                >
                <v-list-item @click="deleteGroup" v-if="group.is_owner"
                  ><span class="error--text">{{
                    $t("groupDetails.deleteGroup")
                  }}</span></v-list-item
                >
              </v-list>
            </v-menu>
            <v-btn outlined v-if="!group.is_member & group.can_join & !group.requires_password" @click="join">Gruppe beitreten</v-btn>
            <group-detail-join-with-password-dialog v-if="!group.is_member & group.can_join & group.requires_password" :group="group"></group-detail-join-with-password-dialog>
          </v-col>
        </v-row>
        <v-row no-gutters class="mt-5">
          <v-col cols="12" sd="6" md="4" v-if="group.can_create_collection">
            <collection-create-button
              v-if="group.can_create_collection"
              :group="true"
              :organization="group.organization"
              @created="collectionCreated"
              class="ma-1"
            ></collection-create-button>
          </v-col>
          <v-col
            md="4"
            sd="6"
            v-for="collection in group.collections"
            :key="collection.id"
          >
            <card-collection
              :collection="collection"
              class="ma-1"
            ></card-collection>
          </v-col>
        </v-row>
      </v-col>


    </v-row>

  </v-container>
</template>

<script>
import RequestHandler from "../utils/RequestHandler.js";
import CardCollection from "../components/CardCollection";
import CollectionCreateButton from "../components/CollectionCreateButton";
import { mapGetters } from "vuex";
import GroupSettingsDialog from "@/components/GroupSettingsDialog";
import axios from "axios";
import GroupDetailMemberDialog from "@/components/GroupDetailMemberDialog";
import GroupDetailInvitationLinkDialog from "@/components/GroupDetailInvitationLinkDialog";
import GroupDetailJoinWithPasswordDialog from "@/components/GroupDetailJoinWithPasswordDialog";
export default {
  components: {
    GroupDetailJoinWithPasswordDialog,
    GroupDetailInvitationLinkDialog,
    GroupDetailMemberDialog, GroupSettingsDialog, CardCollection, CollectionCreateButton },
  data: () => ({
    snackbar: false,
    users: [],
    user: "",
    username: "",
    group: "",
    loadUsers: null,
    collectionAdd: "",
    inviteLink: "",
    password:'',
  }),
  mounted() {
    RequestHandler.getGroup(this.$route.params.id).then((response) => {
      this.group = response.data;
      if (this.group.is_owner)
        RequestHandler.getInvite(this.$route.params.id).then((response) => {
          this.inviteLink =
            "https://lex.dioe.at/groups/join/" +
            this.$route.params.id +
            "/" +
            response.data;
        });
    });
  },
  methods: {

    leaveGroup() {
      axios.post("group/leave/" + this.group.id + "/").then(()=>this.$router.go());
    },
    collectionCreated(value) {
      this.group.collections.push(value);
      axios
        .put("/collection/group/" + value.id + "/" + this.group.id + "/")
        .then(() => this.$router.push("/collections/" + value.id));
    },


    deleteGroup() {
      axios.delete("group/" + this.group.id + "/").then(() => {
        this.$router.push("/groups/");
      });
    },
    join() {
      axios.post('join/' + this.$route.params.id + '/', {
        password: this.password
      }).then(() => this.$router.go())

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
  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      userSignedIn: "auth/user",
    }),
  },
};
</script>

