<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <p class="text-h4">{{ $t("highscore.title") }}</p>

      </v-col>
    </v-row>
    <v-row>
      <v-col>
      <v-card outlined>
        <v-card-title>Insgesamt</v-card-title>
      <v-simple-table>
        <template v-slot:default>
          <thead>
          <tr>
            <th class="text-left">
              Position
            </th>
            <th class="text-left">
              Benutzer
            </th>
            <th class="text-left">
              angelegte Begriffe
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
              v-for="(item,index) in highscoreList"
              :key="item.name"
          >
            <td>{{ index+1 }}</td>
            <td>{{ item.username }}</td>
            <td>{{ item.count }}</td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
      </v-card>
      </v-col>
      <v-col>
        <v-card outlined>
          <v-card-title>In den letzten zwei Wochen</v-card-title>
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th class="text-left">
                  Position
                </th>
                <th class="text-left">
                  Benutzer
                </th>
                <th class="text-left">
                  angelegte Begriffe
                </th>
              </tr>
              </thead>
              <tbody>
              <tr
                  v-for="(item,index) in highscoreListLastTwoWeeks"
                  :key="item.name"
              >
                <td>{{ index +1}}</td>
                <td>{{ item.username }}</td>
                <td>{{ item.count }}</td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
name: "Highscore",
  data:()=>({
    highscoreList:[],
    highscoreListLastTwoWeeks:[]
  }),
  mounted() {
    axios.get("highscore/").then(response => this.highscoreList = response.data.results)
    axios.get("highscore/?daysPast=14").then(response => this.highscoreListLastTwoWeeks = response.data.results)
  }
}
</script>

<style scoped>

</style>