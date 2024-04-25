function solution(n) {
    let sum=0;
for (i=0;i<=n/2; i++) {
	if (n%i ==0) {
		sum+=i;
	}
}
    sum+=n;
    return sum;
}