function solution(a) {
    let cnt = 0;
    while (a!=1) {
        if (cnt>=500) {
            return -1;
        }
        if (a%2==0) {
            a = a/2;
        } else {
            a = a*3+1;
        }
        cnt+=1;
    }
    return cnt;
}