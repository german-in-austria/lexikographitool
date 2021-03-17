export default class Lexeme {
    constructor(word, description, dialectWord, kind, originId, sensitive, variety, source) {
        this.word = word;
        this.description = description;
        this.dialectWord = dialectWord;
        this.kind = kind;
        this.origin = originId;
        this.variety = variety;
        this.source = source;
    }
}