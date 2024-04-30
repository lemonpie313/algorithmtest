function solution(a,b) {
	let arr=[];
	for (let i=0; i<=a; i++) {
		if (a%i==0 & b%i==0) {
			arr[0] = i;
		}
	}
	arr[1] = a*b/arr[0];
	return arr;
}