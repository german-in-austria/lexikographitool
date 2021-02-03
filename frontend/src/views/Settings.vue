<template>
  <v-card class="px-4" flat>
    <v-card-text>
      <v-form ref="registerForm" v-model="valid" lazy-validation>
        <v-row>
          <v-col cols="12">
            <v-text-field readonly v-model="email"  label="E-mail" ></v-text-field>

          </v-col>
          <v-col cols="12">
            <v-text-field readonly v-model="username" label="Benutzername"
                          ></v-text-field>
          </v-col>
          <v-col cols="4">
            <location-combo-box v-model="location" ></location-combo-box>
          </v-col>

          <v-col cols="12">
            <v-text-field v-model="password" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                          :type="show1 ? 'text' : 'password'" :rules="[rules.min]"
                          name="input-10-1" label="neues Passwort" hint="mindestens 8 Zeichen" counter
                          @click:append="show1 = !show1"></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field block v-model="verify" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                          :rules="[rules.min, passwordMatch]" :type="show1 ? 'text' : 'password'"
                          name="input-10-1" label="Passwort erneut eingeben" counter
                          @click:append="show1 = !show1"></v-text-field>
          </v-col>
          <v-spacer></v-spacer>
          <v-col class="d-flex ml-auto" cols="12" sm="3" xsm="12">
            <v-btn x-large block :disabled="!valid" color="success" @click.prevent="save()">Speichern</v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
import LocationComboBox from "@/components/LocationComboBox";
import axios from "axios";
import RequestHandler from "@/utils/RequestHandler";
export default {
name: "Settings",
  components: {LocationComboBox},
  data: () => ({
    valid:true,
    location:'',
    age: 21,
    email: "",
    password: "",
    username: "",
    verify: "",
    show1:false,
    show2:false,
    rules: {
      required: value => !!value || "Required.",
      min: v => (v && (v.length >= 8) || !v) || "mindestens 8 Zeichen"
    }
  }),
  created() {
    axios.get('account/me/').then(response=>{
      this.username = response.data.username
      this.email = response.data.email
      this.location=response.data.home
    })
  },

  computed: {
    passwordMatch() {
      return () => this.password === this.verify || "Passwörter stimmen nicht überein";
    }
  },
  methods:{
  save (){
    if (this.$refs.registerForm.validate()) {
      RequestHandler.updateAccount({'email':this.email, 'username':this.username,'home':this.location,'age':18})
      if(!!this.password && !!this.valid)
        RequestHandler.updatePassword({'email':this.email, 'username':this.username,'password':this.password,'password2':this.verify})


    }
  }
  }

}
</script>

<style scoped>

</style>