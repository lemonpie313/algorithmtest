function solution(s) {
	let allsum = 45;
	s.forEach((i) => {
		allsum-=i;
	})
	return allsum;
}