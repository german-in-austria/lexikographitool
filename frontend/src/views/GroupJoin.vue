<template>
<vcontainer fluid>
  <v-card>
    Möchtest du der Gruppe '{{ group.name }}' beitreten?
    <v-card-actions>
      <v-btn
          elevation="2"
          @click="join"
      >Beitreten
      </v-btn>
    </v-card-actions>
  </v-card></vcontainer>
</template>

<script>
import Group from "@/objects/Group";
import RequestHandler from "@/utils/RequestHandler";
import axios from 'axios'

export default {
  name: "GroupJoin",
  data: () => ({
    group: new Group(),
  }),
  mounted() {
    axios.get('/groupname/'+this.$route.params.id +'/').then((response) => {
      this.group = response.data;
    });
  },
  methods: {
    join() {
      RequestHandler.joinGroup(this.$route.params.id,this.$route.params.hash).then(()=>this.$router.push('/groups/' + this.$route.params.id))

    },
  }
}
</script>

<style scoped>

</style>