function solution(s) {
    s = s.split(" ").map((cur) => Number(cur));
    return String(Math.min(...s))+" " +String(Math.max(...s));
}