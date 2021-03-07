<template>
  <v-container fluid v-if="group">
    <v-row no-gutters>

      <v-col cols='12' sm='8'>
      <v-row>
        <v-col cols="8">
        <p class="text-h3">{{ group.name }}</p>
        <p class="text-h5">{{ group.description }}</p>
        <p class="text-h5">{{ group.organization }}</p>
        </v-col>
        <v-col>
        <v-btn v-if="!group.is_owner" @click="leaveGroup">Gruppe verlassen</v-btn>
        <group-settings-dialog :group="group" v-if="group.is_owner"></group-settings-dialog>
        </v-col>
      </v-row>
        <v-row no-gutters class="mt-5">
          <v-col cols="12" sd="6" md="4" v-if="group.can_create_collection"
          >
            <collection-create-button
                v-if="group.can_create_collection"
                :group='true'
                :organization='group.organization'
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
      <v-divider  :vertical="!$vuetify.breakpoint.xs" style="height:83vh" class="mx-5"></v-divider>
      <v-col cols="12" sm='3' >
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
          <v-list-item v-for="(member,index) in group.members" :key="member.username">
            <v-list-item-title>
              {{ member.username }}
            </v-list-item-title>
            <v-list-item-icon v-if="group.is_owner" ><v-icon @click="removeMember(member.username,index)">mdi-delete</v-icon></v-list-item-icon>
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
import axios from 'axios'
export default {
  components: {GroupSettingsDialog, CardCollection, CollectionCreateButton},
  data: () => ({
    snackbar: false,
    users: [],
    user: "",
    username: "",
    group: '',
    loadUsers: null,
    collectionAdd: "",
    inviteLink: "",
  }),
  mounted() {
    RequestHandler.getGroup(this.$route.params.id).then((response) => {
      this.group = response.data;
      if(this.group.is_owner)
        RequestHandler.getInvite(this.$route.params.id).then(response => {
          this.inviteLink = 'https://lex.dioe.at/groups/join/' + this.$route.params.id + '/' + response.data
        })
    });


  },
  methods: {
    addMember() {
      RequestHandler.addMemberToGroup(this.$route.params.id, this.user).then(
          (response) => (this.group = response.data)
      );
    },
    removeMember(user,listindex){
      axios.delete('group/'+this.$route.params.id + '/' + user +'/').then(()=>{
        this.group.members.splice(listindex,1)
      })
    
    },
    leaveGroup(){
      axios.post('group/leave/' +this.group.id+'/')
    },
    collectionCreated(value) {
      this.group.collections.push(value)
      axios.put('/collection/group/'+value.id+'/'+this.group.id+'/').then(()=>
        this.$router.push("/collections/" + value.id)

      )
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

