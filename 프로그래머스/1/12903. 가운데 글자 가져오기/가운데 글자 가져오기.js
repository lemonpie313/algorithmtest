function solution(s) {
	if (s.length%2==0) {
		let i = s.length/2;
		a = s.substr(i-1,2);
		return a;
	}
	let i = (s.length-1)/2;
	return s[i];

}