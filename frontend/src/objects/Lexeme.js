export default class Lexeme{
    constructor(word, description, dialectWord, kind, dialect,originId) {
        this.word =word;
        this.description = description;
        this.dialectWord =dialectWord;
        this.kind =kind;
        this.dialect = dialect;
        this.origin = originId
    }
}