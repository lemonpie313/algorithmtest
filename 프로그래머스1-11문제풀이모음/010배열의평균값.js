function solution(numbers) {
    let answer=0;
    for (let i of numbers) {
        answer += i;
    }
    answer = answer/(numbers.length);
    return answer;
}