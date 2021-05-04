import ObjectsToCsv from "objects-to-csv";

export default {

    async convert(lexemes,name) {


        const csv = new ObjectsToCsv(lexemes.map(val => this.format(val)));
        //csv.toDisk('./test.csv');

        const hiddenElement = document.createElement('a');
        hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(await csv.toString());
        hiddenElement.target = '_blank';
        hiddenElement.download = name + '.csv';
        hiddenElement.click();


    },
    format(obj) {
        const newObj = {};
        newObj.categories = obj.categories.map(val => val.category).join(',')
        newObj.examples = obj.examples.map(val => val.example).join(',')
        newObj.pronunciations = obj.pronunciations.map(val => val.pronunciation).join(',')
        newObj.etymologies = obj.etymologies.map(val => val.etymology).join(',')
        newObj.kind = obj.kind
        newObj.dialectWord = obj.dialectWord
        newObj.word = obj.word
        newObj.description = obj.description
        newObj.variety = obj.variety
        newObj.genus = obj.genus
        newObj.origin = obj.origin?.name
        newObj.source = obj.source

        return newObj
    }
}


