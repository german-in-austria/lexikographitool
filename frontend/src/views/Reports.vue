<template>
  <v-container fluid >
    <v-row no-gutters>
      <span class="text-h3">Meldungen</span>
    </v-row>
    <v-row no-gutters class="pt-5">
      <v-simple-table>
        <template v-slot:default>
          <thead>
          <tr>
            <th class="text-left">
              Lexeme
            </th>
            <th class="text-left">
              gemeldet von
            </th>
            <th class="text-left">
              Nachricht
            </th>
            <th class="text-left">
              bearbeiten
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
              v-for="item in reports"
              :key="item.name"
              @click="$router.push('/lexeme/' + item.lexeme.id)"
              :style="item.active  ? '': 'opacity: 30%'"
              >
            <td >{{ item.lexeme.dialectWord }}</td>
            <td>{{ item.report_from }}</td>
            <td>{{ item.message }}</td>
            <td><lexeme-edit-dialog :lexeme="item.lexeme"></lexeme-edit-dialog></td>
            <td v-if="item.active & item.already_changed">Vorsicht! Wort wurde zwischenzeitlich geändert</td>
            <td><v-btn @click.stop="deactivate(item)"><v-icon>mdi-check</v-icon></v-btn></td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-row>
  </v-container>
</template>

<script>
import Axios from "axios";
import LexemeEditDialog from "@/components/LexemeEditDialog";

export default {
name: "Reports",
  components: {LexemeEditDialog},
  data:()=>({
    reports:[],
  }),
mounted() {
  Axios.get('reports/?ordering=-date_created').then(response =>{
    this.reports = response.data.results
  })
},
methods:{
  deactivate(report){
    Axios.put('report/deactivate/' + report.id + '/').then(()=>report.active =false)
  }
}}
</script>

<style scoped>

</style>