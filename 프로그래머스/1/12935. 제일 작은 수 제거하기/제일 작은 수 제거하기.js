function solution(s) {
	let min = Math.min(...s);
	return (s.length==1)?[-1]:s.filter((i) => { return i!=min; })
}