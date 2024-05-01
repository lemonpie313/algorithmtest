function solution (s) {
    let ss = "";
    s.split(" ").forEach((i) => {
        i = i.split("");
        for (let a in i) {
            if (a%2==0) {
                ss+=(i[a].toUpperCase());
            } else {
                ss+=(i[a].toLowerCase());
            }
        }
        ss+=" ";
    });
    return ss.slice(0, ss.length-1);

}