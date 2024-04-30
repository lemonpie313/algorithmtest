function solution(a) {
	let b = [];
	while (a>=3) {
		b.push(a%3);
		a = (a-(a%3))/3;
	}
	b.push(a);
	return b.reverse().reduce((acc,cur,idx) => {
		return acc+cur*(3**idx);
	},0)
}