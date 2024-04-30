function solution(s) {
	return ((s.length==4||s.length==6) && !(s.split("").map((i)=>Number(i)).some((i)=> {return Number.isNaN(i)})));
}