function solution(s) {
	return (s%2==0)?"수박".repeat(s/2):"수박".repeat((s-1)/2)+"수";
}