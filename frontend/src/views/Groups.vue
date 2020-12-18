<template>
  <div>
    <v-row>
      <v-col cols="12" sd="4" md="4">
        <v-hover v-slot="{ hover }">
        <v-card
        @click.prevent="dialog = true"
:elevation="hover ? 12 : 2"
            class="mx-auto"
            max-width="300"
        >
          <v-card-actions class="justify-center"><v-icon size="48
" >mdi-plus</v-icon></v-card-actions>
        </v-card>
        </v-hover>
      </v-col>
      <v-col cols="12" sd="4" md="4"  v-for="group in groups"
             :key="group.id" >
             <v-hover v-slot="{ hover }">
        <v-card

        :to="'/groups/' + group.id" 
            :elevation="hover ? 12 : 2"
            class="mx-auto"
            max-width="300">
          <v-card-title>{{group.name}}</v-card-title>
          <v-card-text>{{group.description}}</v-card-text>
        </v-card>
             </v-hover>
      </v-col>
    </v-row>



    <v-dialog
        v-model="dialog"
        width="500"
    >
      <v-card>
        <v-card-title>
          <span class="headline">Neue Gruppe</span>
        </v-card-title>
        <v-card-text>
          <v-text-field
              v-model="groupTitle"
              label="Titel"
              required
          ></v-text-field>
          <v-text-field
              v-model="groupDescription"
              label="Beischreibung"
              required
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="blue darken-1"
              text
              @click.prevent="createGroup()"
          >erstellen
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import RequestHandler from "@/utils/RequestHandler";
import Group from "@/objects/Group";

export default {
  name: "Group",
  data: () => ({
    groups:[],
    dialog: false,
    groupTitle:'',
    groupDescription:'',
  }),
  methods: {
    createGroup(){
      RequestHandler.createGroup(new Group(this.groupTitle,this.groupDescription)).then(
        (response) => this.groups.push(response.data)
      )
      this.dialog = false
      this.groupTitle = ''
      this.groupDescription = ''
    }
  },
  created(){
      RequestHandler.getMyGroups()
          .then(response => (
              this.groups = response.data
          ))
  }
}
</script>

<style scoped>

</style>