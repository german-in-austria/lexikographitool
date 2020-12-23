import axios from "axios";
import Etymology from "@/objects/Etymology";
import Pronunciation from "@/objects/Pronunciation";
import DExample from "@/objects/DExample";
import Category from "@/objects/Category";


let methods = {
    getCards() {
        return axios.get('cards/')
    },
    postLexeme(lexeme) {
        return axios.post('lexeme/', lexeme)
    },
    postDialect(dialect) {
        return axios.post('dialect/', dialect)
    },
    postEtymologies(etymologies, wordid) {
        etymologies.forEach((item) => {
            const obj = new Etymology(item, wordid);
            axios.post('etymology/', obj).catch(err => {
                console.log(err)
            })
        })
    },
    postPronunciations(pronunciations, wordid) {
        pronunciations.forEach((item) => {
            const obj = new Pronunciation(item, wordid);
            axios.post('pronunciation/', obj).catch(err => {
                console.log(err)
            })
        })
    },
    postExamples(examples, wordid) {
        examples.forEach((item) => {
            const obj = new DExample(item, wordid);
            axios.post('example/', obj).catch(err => {
                console.log(err)
            })
        })
    },
    searchLexemesByWord(word) {
        return axios.get('lexemes_simple/?search=' + word)
    },
    searchDialects(dialect) {
        return axios.get('dialects/?search=' + dialect)
    },
    getFirsLexemeByName(word) {
        return axios.get('lexeme_by_word/' + word + '/')
    },
    searchCategories(category) {
        return axios.get('categories/?search=' + category)
    },
    createDialect(dialect) {
        return axios.post('dialect/', dialect)
    },
    addCategoriesWithLexeme(categories, lexemeId) {
        categories.forEach((item) => {
            const obj = new Category(item);
            axios.post('category/' + lexemeId + '/', obj).catch(err => {
                console.log(err)
            })
        })


    },
    login(login) {
        return axios.post('account/login/', login)
    },
    register(register) {
        console.log(register)
        return axios.post('account/register/', register)
    },
    createCollection(collection) {
        return axios.post('collection/', collection)
    },
    getCollections() {
        return axios.get('collections/')
    },
    addLexemeToCollection(collectionId, lexemeId) {
        return axios.put('collection/' + collectionId + '/' + lexemeId + '/')
    },
    getCollection(collectionId) {
        return axios.get('collection/' + collectionId + '/')
    },
    getLexeme(lexemeId) {
        return axios.get('lexeme/' + lexemeId + '/')
    },
    createGroup(group) {
        return axios.post('group/', group)
    },
    getMyGroups() {
        return axios.get('groups/')
    },
    getGroup(groupId) {
        return axios.get('group/' + groupId + '/')
    },
    addMemberToGroup(groupId, userId) {
        return axios.put('group/' + groupId + '/' + userId + '/')
    },
    addGroupToCollection(collectionId, groupId) {
        return axios.put('collection/group/' + collectionId + '/' + groupId + '/')
    }
    ,
    getUsersByUsername(username) {
        return axios.get('account/users/' + username + '/')
    }
    ,
    getCollectionsByOwner() {
        return axios.get('collections/owner/')
    },
    getCardsCreated(){
        return axios.get('own_cards/')
    }

}

export default methods