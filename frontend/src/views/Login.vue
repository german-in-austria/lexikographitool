<template>

  <v-container fluid>
    <v-tabs v-model="tab" icons-and-text grow>

      <v-tab v-for="i in tabs" :key="i.name">
        <v-icon large>{{ i.icon }}</v-icon>
        <div class="caption py-1">{{ i.name }}</div>
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab" reverse>
      <v-tab-item key="Login">
        <v-card class="px-4">
          <v-card-text>
            <v-form ref="loginForm" @submit="login" v-model="valid" lazy-validation onsubmit="return false">
              <v-row>
                <v-col cols="12">
                  <v-text-field v-model="loginEmail" :rules="loginEmailRules" label="E-mail"
                                required></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field v-model="loginPassword" :append-icon="show1?'eye':'eye-off'"
                                :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'"
                                name="input-10-1" label="Passwort" hint="Passwort braucht mindestens 8 Zeichen"
                                counter @click:append="show1 = !show1"></v-text-field>
                </v-col>
                <v-col class="d-flex" cols="12" sm="6" xsm="12">
                </v-col>
                <v-spacer></v-spacer>
                <v-col class="d-flex" cols="12" sm="3" xsm="12" align-end>
                  <v-btn x-large block :disabled="!valid" color="success" type="submit"> Login</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item key="Register">
        <v-card class="px-4" flat>
          <v-card-text>
            <v-form ref="registerForm" v-model="valid" lazy-validation>
              <v-row>
                <v-col cols="12">
                  <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field v-model="username" :rules="[rules.required]" label="Benutzername"
                                required hint="ist öffentlich sichtbar" persistent-hint></v-text-field>
                </v-col>
                <v-col cols="12">
                  <input-location v-model="location"></input-location>
                </v-col>
                <v-col cols="12">
                  <v-text-field v-model="password" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'"
                                name="input-10-1" label="Passwort" hint="mindestens 8 Zeichen" counter
                                @click:append="show1 = !show1"></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field block v-model="verify" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                :rules="[rules.required, passwordMatch]" :type="show1 ? 'text' : 'password'"
                                name="input-10-1" label="Passwort erneut eingeben" counter
                                @click:append="show1 = !show1"></v-text-field>
                </v-col>

                <v-spacer></v-spacer>
                <v-col class="d-flex ml-auto" cols="12" sm="3" xsm="12">
                  <v-btn x-large block :disabled="!valid" color="success" @click="register">Register</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
    <v-snackbar
      v-model="snackbarSuccessful"
      :timeout="2000"
      color="success"
      top
    >
    {{successMessage}}

    </v-snackbar>
    
    <v-snackbar
      v-model="snackbarFailure"
      :timeout="2000"
      color="error"
      top
    >
         {{failureMessage}}

    </v-snackbar>
  </v-container>
</template>

<script>
import Login from "@/objects/Login";
import Register from "@/objects/Register";
import {mapActions} from 'vuex'
import RequestHandler from "@/utils/RequestHandler";
import InputLocation from '../components/InputLocation.vue';

export default {
  components: { InputLocation },
  data: () => ({
    successMessage:'Erfolgreich',

    snackbarSuccessful: false,
    snackbarFailure: false,
    failureMessage:'Fehler!',
    dialog: false,
    tab: null,
    tabs: [
      {name: "Login", icon: "mdi-account"},

      {name: "Registrieren", icon: "mdi-account-outline"},

    ],
    valid: true,
    age: 21,
    email: "",
    password: "",
    username: "",
    verify: "",
    location:{id:-1,place:null,zip:null},
    loginPassword: "",
    loginEmail: "",
    loginEmailRules: [
      v => !!v || "wird benötigt",
      v => /.+@.+\..+/.test(v) || "E-mail ist ungültig"
    ],
    emailRules: [
      v => !!v || "wird benötigt",
      v => /.+@.+\..+/.test(v) || "E-mail ist ungültig"
    ],
    show1: false,
    rules: {
      required: value => !!value || "wird benötigt",
      min: v => (v && v.length >= 8) || "mindestens 8 Zeichen"
    }
  }),
  computed: {
    passwordMatch() {
      return () => this.password === this.verify || "Passwörter stimmen nicht überein";
    }
  },
  methods: {
    validate() {
      if (this.$refs.loginForm.validate()) {
        //
        //
        // submit form to server/API here...
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    login() {
      if (this.$refs.loginForm.validate()) {
        this.signIn(new Login(this.loginEmail, this.loginPassword)).then(() => {
              if(this.$route.query.nextUrl)
                this.$router.push(this.$route.query.nextUrl)
          else
                this.$router.push('/')
            }
        ).catch(()=>{
          this.failureMessage = 'Benutzername oder Passwort stimmen nicht!'
          this.snackbarFailure = true
        })

    }
  },
  register() {
    if (this.$refs.registerForm.validate()) {
      if(this.location.id == -1)
        //first create new location, then register
        RequestHandler.createLocation(this.location.zip,this.location.place,this.location.state).then((response)=>{
          this.signUp(new Register(this.username, this.email, this.password, this.password, response.data.id, this.age)).then(() => {
                if(this.$route.query.nextUrl)
                  this.$router.push(this.$route.query.nextUrl)
                else
                  this.$router.push('/')
              }
          ).catch(()=>{
          this.failureMessage = 'Benutzername oder Passwort stimmen nicht!'
          this.snackbarFailure = true
        })
            }

        )
      else
        this.signUp(new Register(this.username, this.email, this.password, this.password, this.location.id, this.age)).then(() => {
              if(this.$route.query.nextUrl)
                this.$router.push(this.$route.query.nextUrl)
              else
                this.$router.push('/')
            }
        ).catch(()=>{
          this.failureMessage = 'Benutzername oder Passwort stimmen nicht!'
          this.snackbarFailure = true
        })

    }
  },
  ...mapActions({
    signIn: 'auth/signIn',
    signUp: 'auth/register',

  }),
  updateParent: function () {
    this.$emit('inputData', this.zip)
  },},
}
</script>

<style scoped>

</style>