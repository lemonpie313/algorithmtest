function solution(a, num) {
    let b = a.filter((i) => {
        return (i%num==0);
    }).sort((a,b)=>{
        return a-b;
    });
    return ((b.length==0)?([-1]):b);
}