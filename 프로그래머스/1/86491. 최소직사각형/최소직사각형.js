function solution(t) {
    let [a,b]=t.reduce(([i,j],cur,idx) => {
        let curr=cur.sort((a,b)=>{return b-a});
        return [Math.max(i, curr[0]), Math.max(j, curr[1])]
    },[0,0])
    return a*b;
}