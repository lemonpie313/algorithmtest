function solution(n) {
	n=String(n).split("");
	n=n.sort((a,b) => { return Number(b)-Number(a)});
	let a="";
	for (i of n) {
		a+=i;
	}
	return Number(a);
}