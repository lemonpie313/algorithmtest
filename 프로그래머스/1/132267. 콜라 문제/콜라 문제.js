function solution(a, b, n) {
    let sum = 0;
    let last = 0;
    let num=0;
    while (n+last>=a) {

        let n_next = Math.floor((n+last)/a)*b;
        

        last = (n+last)%a;
        sum+=n_next;
        n=n_next;

        num+=1;
        
    }
    return sum;
}