function solution(a,b) {
    let month = [31,29,31,30,31,30,31,31,30,31,30,31];
    let date=0;
    for (i=0;i<a-1;i++) {
        date+=month[i];
    }
    let today=(date+b)%7;
    let week = ['THU','FRI','SAT','SUN','MON','TUE','WED'];
    return week[today];
}