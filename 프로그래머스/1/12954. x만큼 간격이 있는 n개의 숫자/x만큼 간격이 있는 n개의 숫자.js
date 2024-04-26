function solution (x, n) {
	let a = x;
	let b = [x];
	for (let i=0; i<n-1; i++) {
		a+=x;
		b.push(a);
	}
	return b;
}