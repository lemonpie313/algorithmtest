function solution(n)
{
    let a = (n+"").split("");
    let sum=0;
    for (i of a) {
        sum+=Number(i);
    }
    return sum;
}