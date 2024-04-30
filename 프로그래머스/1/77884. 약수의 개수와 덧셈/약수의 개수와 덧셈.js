function solution(a,b) {
	let sum=0;
	for (i=a; i<=b; i++) {
		if (Number.isInteger(Math.sqrt(i))) {
			sum-=i;
		} else{
			sum+=i;
		};
	}
	return sum;
}