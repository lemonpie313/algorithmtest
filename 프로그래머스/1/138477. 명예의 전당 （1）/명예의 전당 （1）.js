function solution(k,s) {
    return s.map((_,idx) => {
        return s.slice(0,idx+1).sort((a,b)=>b-a).slice(0,k);
    }).map((cur)=> {
        return cur[cur.length-1];
    })
}