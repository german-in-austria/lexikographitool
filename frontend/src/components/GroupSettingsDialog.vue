<template>
  <v-row justify="center">
    <v-dialog
        v-model="dialog"
        persistent
        max-width="80vh"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-icon
            size="30px"
            v-bind="attrs"
            v-on="on"
        >
          mdi-cog
        </v-icon>
      </template>
      <v-card>
        <v-card-title class="headline">
          Einstellungen
        </v-card-title>
        <v-card-text>
          <v-text-field v-model="name" label="Gruppenname"></v-text-field>
          <v-text-field v-model="description" label="Beschreibung"></v-text-field>
          <v-text-field v-model="organization" label="Organisation"></v-text-field>
          <v-switch v-model="pub">öffentlich</v-switch>

          Bearbeitungsrechte:
          Mitglieder
          <v-switch v-model="membersCreate" label="können Sammlungen erstellen"></v-switch>
          <v-switch v-model="membersEdit" label="können Wörter der Sammlung hinzufügen und entfernen"></v-switch>
          Jeder:
          <v-switch v-model="pub" label="kann Grupe sehen"></v-switch>

          <v-switch v-model="allCreate" label="kannSammlungen erstellen" :disabled="!pub"></v-switch>
          <v-switch v-model="allEdit" label="kann Wörter der Sammlung hinzufügen und entfernen" :disabled="!pub"></v-switch>

          Beitreten:
          <v-switch v-model="needPassword" label="Zum Beitreten wird ein Passwort benötigt"></v-switch>
          <v-text-field v-model="password" label="Passwort" :disabled="!needPassword"></v-text-field>

        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="green darken-1"
              text
              @click="dialog = false"
          >
            Verwerfen
          </v-btn>
          <v-btn
              color="green darken-1"
              text
              @click="update"
          >
            Änderungen speichern
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import axios from "axios";

export default {
  name: "GroupSettingsDialog",
  props: ['group'],
  data: function () {
    return {
      dialog: false,
      description: '',
      categories: [],
      categoryList: [],
      organization:'',
      pub:false,
      name: '',

      membersCreate:false,
      membersEdit:false,
      allCreate:false,
      allEdit:false,
      needPassword:false,
      password:'',
      settingsId: ''
    }

  },
  watch: {
    dialog(visible) {
      if (visible) {
        this.name = this.group.name
        this.description = this.group.description
        this.organization = this.group.organization

      }
    }
  },
  methods: {
    update() {
      axios.put('group/settings/' + this.settingsId + '/', {
        'id': this.settingsId,
        'members_createCollection': this.membersCreate,
        'members_add_remove_lexemes': this.membersEdit,
        'public_add_remove_lexemes': this.allEdit,
        'public_createCollection': this.allCreate,
        'need_password':this.needPassword,
        'join_password':this.password,
        'public':this.pub
      }).then(() => {
        this.dialog=false
      })

      axios.put('group/' + this.group.id + '/', {
        'id': this.group.id,
        'name': this.name,
        'description': this.description,
        'settings': this.settingsId,
        'organization': this.organization,
      }).then(() => {
        this.dialog=false
        this.group.name = this.name
        this.group.description = this.description
        this.group.organization = this.organization
      })

    }
  },
  mounted() {
    axios.get('group/settings/' + this.group.settings + '/').then(response=>{
      this.settingsId = response.data.id
      this.membersCreate=response.data.members_createCollection
      this.membersEdit=response.data.members_add_remove_lexemes
      this.allCreate=response.data.public_createCollection
      this.allEdit=response.data.public_add_remove_lexemes
      this.needPassword=response.data.need_password
      this.password=response.data.join_password
      this.pub=response.data.public
    })
  }

}
</script>

<style scoped>

</style>