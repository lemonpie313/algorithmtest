function solution(price, money, count) {
	let b = (price*(count+1)*count/2)-money;
	return (b>0)?b:0;
}