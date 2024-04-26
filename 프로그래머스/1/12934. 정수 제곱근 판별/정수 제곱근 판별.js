function solution(n) {
	for (let i=1; i<=n; i++) {
		if (n==i**2) {
			return (i+1)**2;
		}
	}
	return -1;
}