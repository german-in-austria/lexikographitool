export default class Lexeme{
    constructor(word, description, dialectWord, kind,originId,sensitive,variety) {
        this.word =word;
        this.description = description;
        this.dialectWord =dialectWord;
        this.kind =kind;
        this.origin = originId,
        this.variety = variety
    }
}