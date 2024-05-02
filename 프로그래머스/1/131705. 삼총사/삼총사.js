function solution (s) {
    let len = s.length;
    let cnt=0;
    for (let i=0; i<len; i++){
        for (let j=i+1; j<len; j++){
            for (let k=j+1; k<len; k++) {
                if (s[i]+s[j]+s[k]==0) {
                    cnt+=1;
                }
            }
        }
    }
    return cnt;
}
