function solution(s) {
	if (s.length == 1) {
		return [-1];
	}
	let min = Math.min(...s);
	return s.filter((i) => { return i!=min; })
}