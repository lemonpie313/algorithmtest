function solution(n, lost, reserve) {
    lost.sort((a,b)=>a-b);
    for (i in lost) {
        if (reserve.includes(lost[i])) {
            reserve[reserve.indexOf(lost[i])] = -1;
            lost[i] = -1;
        }
    }
    for (i in lost) {
        let [borrow1, borrow2] = [lost[i]-1, lost[i]+1];
        if (reserve.includes(borrow1) || lost[i]==-1) {
            continue;
        } else if (reserve.includes(borrow2)) {
            reserve[reserve.indexOf(borrow2)] = -1;
        } else {
            n-=1;
        }
    }
    return n;
}