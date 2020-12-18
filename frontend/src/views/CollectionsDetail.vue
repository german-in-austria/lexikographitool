<template>
    <v-list>
    <v-subheader>
        {{collection.name}}
    </v-subheader>
    <div v-for="lexeme in collection.lexemes"
     :key="lexeme.word">

    <v-list-item class="item"
    :to="'/lexeme/' + lexeme.id">    
    
     {{lexeme.dialectWord}}   
     {{lexeme.word}}
     {{lexeme.description}}
    </v-list-item>

    </div>
    </v-list>
</template>

<script>
import RequestHandler from '../utils/RequestHandler.js'
import Collection from '../objects/Collection.js'
export default {
    data: () =>({
        collection: new Collection()
    }),
    mounted(){
        RequestHandler.getCollection(this.$route.params.id).then( (response) =>{
            this.collection = response.data
        }
        )
    }
    
}


</script>

<style scoped>
 .item {
    margin: 5px;
    border-radius: 4px;
  }
  .item:hover {
    background: lightgray;
  }
</style>