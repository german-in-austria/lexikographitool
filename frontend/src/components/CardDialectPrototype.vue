<template>
<div>
<v-fade-transition>
    <v-card v-click-outside="clickoutside" outlined style="z-index:3" :class="isActive ? 'elevation-5 transition-swing' : ''" max-width="21rem">
      
      <v-card-text>
        <v-text-field
          @focus="isActive = true"
          solo
          dense
          flat
          class="display-1 text--primary"
          placeholder="Tschutta!"
          v-model="dialectWord"
          required
          hint="Füge hier das Stichwort / spannende Wort, das du angeben möchtest ein."
        ></v-text-field>
            <p
              style="height: 1rem"
              class="text-body-2"
            >
              Beschreibung: 

              <v-text-field
              
          @focus="isActive = true"
                solo
                flat
                dense
        ref="description"

                placeholder="Fußball spielen"
                style="display: inline-block"
                v-model="description"
              />
            </p>

        
        <p >
          Varietät:
          <v-text-field
          @focus="isActive = true"
           solo flat dense style="display:inline-block;" placeholder="vorarlbergerisch"
            v-model="dialect"
          />
        </p>

      </v-card-text>
      <v-card-actions>
        <v-btn icon>
          <v-icon>mdi-thumb-up-outline</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-heart-outline</v-icon>
        </v-btn>
        <v-fab-transition>
        <v-btn v-if="isActive && !!this.dialectWord && !!this.description"  color="primary" dark absolute bottom right fab @click="save">
          <v-icon>mdi-content-save</v-icon>
        </v-btn>
        </v-fab-transition>
      </v-card-actions>
      <v-snackbar
      v-model="snackbarSuccessful"
      :timeout="2000"
      color="success"
      top
    >
      Wort hinzugefügt!
    </v-snackbar>
    </v-card>
    </v-fade-transition>
    <v-overlay
    :value="isActive"  :z-index="2"></v-overlay>
    
 </div>
</template>
<script>
import axios from "axios";
export default {
  data: () => ({
    word:'',
    dialectWord:'',
    dialect: '',
    description:'',
    snackbarSuccessful: false,
    dialectWordActive:false,
    descriptionActive:false,
    variatyActive:false,
    isActive:false,

  }),
  methods: {
    checklength(object) {
      if (object.value.length == 0) {
        object.value = "Text einfügen";
      }
      
    },
    clickoutside(){
        this.isActive=false
      },
    save() {
      console.log('hoi')
      axios
        .post("lexeme/", {
          dialectWord: this.dialectWord,
          description: this.description,
        })
        .then((response) => {
          this.$router.push("/lexeme/" + response.data.lexeme);
          this.snackbarSuccessful = true;
        });
    },
   },
  // computed:{
  //   isActive(){
  //     return this.dialectWordActive || this.descriptionActive ||this.variatyActive
      
  //     }
  // },
  
};
</script>
