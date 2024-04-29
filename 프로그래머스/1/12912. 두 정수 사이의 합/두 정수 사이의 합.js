function solution(a, b) {
    let ab = (b-a>0) ? (b-a) : (a-b);
    return (a+b)*(ab+1)/2;
}