<template>
  <v-row justify="center">
    <v-dialog
        v-model="dialog"
        max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            v-bind="attrs"
            v-on="on"
        >
          Login
        </v-btn>
      </template>
      <div>
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
                <v-form ref="loginForm" v-model="valid" lazy-validation>
                  <v-row>
                    <v-col cols="12">
                      <v-text-field v-model="loginEmail" :rules="loginEmailRules" label="E-mail"
                                    required></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <v-text-field v-model="loginPassword" :append-icon="show1?'eye':'eye-off'"
                                    :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'"
                                    name="input-10-1" label="Password" hint="Passwort braucht mindestens 8 Zeichen"
                                    counter @click:append="show1 = !show1"></v-text-field>
                    </v-col>
                    <v-col class="d-flex" cols="12" sm="6" xsm="12">
                    </v-col>
                    <v-spacer></v-spacer>
                    <v-col class="d-flex" cols="12" sm="3" xsm="12" align-end>
                      <v-btn x-large block :disabled="!valid" color="success" @click="login"> Login</v-btn>
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
                                    required></v-text-field>
                    </v-col>
                    <v-col cols="4">
                      <v-combobox
                          v-model="locZip"
                          :items="locations"
                          item-text="zipcode"
                          label="Postleitzahl"
                          hide-no-data
                          menu-props="closeOnClick"
                          :return-object="true"
                          append-icon=""
                          required
                          :search-input.sync="searchzip"
                          @change="change(locZip)"

                      ></v-combobox>
                    </v-col>
                    <v-col cols="4">
                      <v-combobox
                          v-model="locPlace"
                          :items="locations"
                          item-text="place"
                          label="Gemeinde"
                          hide-no-data
                          menu-props="closeOnClick"
                          append-icon=""
                          required
                          :search-input.sync="searchplace"
                          @change="change(locPlace)"

                      ></v-combobox>
                    </v-col>
                    <v-col cols="4">
                      <v-combobox
                          v-model="locState"
                          :items="locations"
                          item-text="state"
                          label="Bundesland"
                          hide-no-data
                          menu-props="closeOnClick"
                          append-icon=""
                          required
                          @change="change(locState)"

                      ></v-combobox>
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

      </div>
    </v-dialog>
  </v-row>
</template>

<script>
import Login from "@/objects/Login";
import Register from "@/objects/Register";
import {mapActions} from 'vuex'
import axios from "axios";

export default {
  data: () => ({
    dialog: false,
    tab: null,
    tabs: [
      {name: "Login", icon: "mdi-account"},

      {name: "Register", icon: "mdi-account-outline"},

    ],
    valid: true,
    age: 21,
    email: "",
    password: "",
    username: "",
    verify: "",
    locPlace: "",
    locId: "",
    locZip: {state: '', zipcode: '', place: ''},
    locState: "",
    locations: [],
    searchzip: null,
    searchplace: null,
    loginPassword: "",
    loginEmail: "",
    loginEmailRules: [
      v => !!v || "Required",
      v => /.+@.+\..+/.test(v) || "E-mail ist ungültig"
    ],
    emailRules: [
      v => !!v || "Required",
      v => /.+@.+\..+/.test(v) || "E-mail ist ungültig"
    ],
    show1: false,
    rules: {
      required: value => !!value || "Required.",
      min: v => (v && v.length >= 8) || "mindestens 8 Zeichen"
    }
  }),
  computed: {
    passwordMatch() {
      return () => this.password === this.verify || "Password stimmen nicht überein";
    }
  },
  methods: {
    validate() {
      if (this.$refs.loginForm.validate()) {
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
        this.signIn(new Login(this.loginEmail, this.loginPassword))
      }
    },
    register() {
      if (this.$refs.registerForm.validate()) {
        this.signUp(new Register(this.username, this.email, this.password, this.password, this.locId, this.age))

      }
    },
    ...mapActions({
      signIn: 'auth/signIn',
      signUp: 'auth/register',

    }),
    reload: function (search) {
      //Lazily load input items
      axios.get('http://127.0.0.1:8000/origin/' + search + '/')
          .then(res => {
            this.locations = res.data
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => (this.isLoading = false))
    },
    updateParent: function () {
      this.$emit('inputData', this.zip)
    },
    change(obj) {
      if (typeof obj == 'object') {
        this.locZip = obj.zipcode
        this.locPlace = obj.place
        this.locState = obj.state
        this.locId = obj.id
      }
    }
  },
  watch: {
    searchplace() {
      // Items have already been loaded
      if (this.searchplace.length <= 1) {
        this.items = []
        return
      }
      if (this.searchplace.length > 2) return
      this.isLoading = true
      this.reload(this.searchplace)

    },
    searchzip() {
      // Items have already been loaded
      if (this.searchzip.length != 1) return

      this.isLoading = true
      this.reload(this.searchzip)

    }
  },
}
</script>

<style scoped>

</style>