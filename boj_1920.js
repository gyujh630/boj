//백준 1920번: 수 찾기

//입력
const input = require('fs').readFileSync('ex.txt').toString().trim().split('\n');
const n_arr = input[1].split(' ').map(v=>+v);
const m_arr = input[3].split(' ').map(v=>+v);

const n_set = new Set(n_arr); //집합으로 전환

const result = [];

m_arr.forEach(m => { //m 배열 순회
    if(n_set.has(m)){
        result.push(1);
    }
    else result.push(0);
});

console.log(result.join('\n'));