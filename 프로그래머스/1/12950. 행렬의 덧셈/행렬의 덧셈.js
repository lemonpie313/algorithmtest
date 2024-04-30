function solution(a,b) {
	let c = [];
	for (let i in a) {
		c.push([]);
		for (j in a[i]) {
			c[i].push(a[i][j]+b[i][j]);
		}
	}
	return c;
}