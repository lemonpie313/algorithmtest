function solution(s) {
	let len = s.length-4;
	let a = s.substr(len, 4);
	let ans="";
	for (let i=0; i<len; i++) {
		ans+="*";
	}
	ans+=a;
	return ans;	
}