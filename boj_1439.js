//백준 1439번: 수 찾기

//입력
const s = require('fs').readFileSync('ex.txt').toString().trim();

let count = 0;

for(let i=0; i<s.length-1; i++){
    console.log(s[i+1]);
    if(s[i] != s[i+1]) count += 1;
}

console.log(Math.floor((count+1)/2))