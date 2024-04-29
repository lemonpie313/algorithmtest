function solution(seoul) {
    let a = seoul.findIndex((a) => {
        return (a=='Kim');
    })
    return ("김서방은 " + a + "에 있다");
}