'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function encryption(s) {
    let root = Math.sqrt(s.length);
    let rows = Math.floor(root);
    let columns = Math.ceil(root);
    let arr = [];
    let result = "";
    let k = 0;
    if (rows * columns < s.length) {
        rows++;
    }
    for (let i = 0; i < rows; i++) {
    arr[i] = [];  
    for (let j = 0; j < columns; j++) {
        if (k < s.length) {
            arr[i][j] = s[k];
            k++;
        } else {
            arr[i][j] = ''; 
        }
    }
}
    for(let i=0;i<columns;i++){
        for(let j=0;j<rows;j++){
            result += arr[j][i];
        }
        result+=" ";
    }
    return result;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const result = encryption(s);

    ws.write(result + '\n');

    ws.end();
}