// 백준 1158: 요세푸스 문제

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin
});

rl.question('', (input) => {
    input = input.trim().split(' ');
    input = input.map(item => parseInt(item));
    void answer(input);
    rl.close();
});

function answer(input) {
    const n = input[0]; //사람 수
    var k = input[1]; //순번

    //Queue 생성
    const queue = new Queue();

    for(i=1; i<=n; i++){
        queue.enqueue(i);
    }

    //삭제되는 순서를 저장할 List 생성
    const arr = [];

    for(i=0; i<n; i++){ 
        k = k%n;
        if(k == 0){
            k = n;
        }
        for(j=0; j<k; j++){  //k번째 인덱스까지 삭제 -> dequeue를 k번 + enqueue는 k-1번
            var temp = queue.dequeue();
            if(j!=k-1){  //k번째 인덱스가 아니라면 (큐에 다시 추가)
                queue.enqueue(temp);
            }
            else{        //k번째 인덱스라면 (큐에 다시 추가하지 않음. 답안 리스트에 추가)
                arr.push(temp);
            }
        }
    }

    console.log(`<${arr.join(", ")}>`);
}


//Queue 구현
class Queue {
    constructor() {
        this.queue = [];
    }

    enqueue(item) {
        this.queue.push(item);
    }

    dequeue() {
        return this.queue.shift();
    }

    isEmpty() {
        return this.queue.length === 0;
    }

    front() {
        return this.queue[0];
    }

    clear() {
        this.queue = [];
    }

    length() {
        return this.queue.length;
    }
}