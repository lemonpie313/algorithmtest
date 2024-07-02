function solution(progresses, speeds) {
    const ans = [];
    const arr = progresses.reduce((acc, cur, idx, arr) => {
        const day = Math.ceil((100-cur)/speeds[idx]);
        if (day>acc[0]) {
            ans.push(acc.length);
            acc = [day];
            return acc;
        }
        acc.push(Math.ceil((100-cur)/speeds[idx]));
        return acc;
    }, []);
    if (arr.length!=0) {
        ans.push(arr.length);
    }
    return ans;
}