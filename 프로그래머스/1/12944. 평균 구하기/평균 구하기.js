function solution(arr) {
    let sum=0;
    for (i of arr) {
        sum+=i;
    }
    return sum/arr.length;
    
}