function solution(s) {
    return s.split("").map((cur, idx) => {
        if (idx==0) {
            return -1;
        }
        for (let i=idx-1; i>=0; i--) {
            if (s[i]==cur) {
                return idx-i;
            }
        }
        return -1;
    });
}