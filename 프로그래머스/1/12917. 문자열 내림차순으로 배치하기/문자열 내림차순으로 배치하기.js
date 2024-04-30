function solution(a) {
	let b = "";
	a = a.split("").sort().reverse();
	a.forEach((i) => b=b+i )
	return b;
}