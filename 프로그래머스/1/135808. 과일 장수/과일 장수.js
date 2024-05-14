function solution(k,m,score) {
    let sum=0;
    let i=1;
    score.sort().reverse();
    while (i*m<=score.length) {
    sum+=(score[i*m-1]*m);
    i+=1;
    }
    return sum;
}