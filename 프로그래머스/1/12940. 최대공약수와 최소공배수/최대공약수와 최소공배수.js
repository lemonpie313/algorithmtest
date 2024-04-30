function solution(a,b) {
	function greatestCommonDivisor(a, b) {
        return b ? greatestCommonDivisor(b, a % b) : Math.abs(a); //Math.abs() : 절댓값
    }
    function leastCommonMultipleOfTwo(a, b) {
        return (a * b) / greatestCommonDivisor(a, b);
    }

    return [greatestCommonDivisor(a, b), leastCommonMultipleOfTwo(a, b)];
}