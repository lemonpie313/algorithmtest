function solution(s, n) {

    return n.map((cur) => {
        return s.slice(cur[0]-1, cur[1]).sort((a,b)=>a-b)[cur[2]-1];
    })
}