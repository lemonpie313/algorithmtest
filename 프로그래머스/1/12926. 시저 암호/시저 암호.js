function solution(s,n) {
    
    s = s.split("").map((cur) => {
        let index = cur.charCodeAt();
        if (index>=65 && index <=90) {
            index=(index+n<=90)?(index+n):(index+n-90+64);
            return String.fromCharCode(index);
        } else if (index>=97 && index<=122) {
            index=(index+n<=122)?(index+n):(index+n-122+96);
            return String.fromCharCode(index);
        } else {
            return String.fromCharCode(index);
        }
    }).join("");

    return s;
}