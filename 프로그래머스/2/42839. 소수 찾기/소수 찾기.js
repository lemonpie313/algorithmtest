function solution(numbers) {
    const stack = [];
    
    const prime = (num) => {
        const sqrt = Math.floor(Math.sqrt(num));
        
        for (let i = 2; i <= sqrt; i += 1) {
            if (num % i === 0) {
                return false;
            }
        }
        return true;
    }
    
    const makeANum = (num, idx) => {
        if (num.length === numbers.length) return;
        
        for (let i = 0; i < numbers.length; i += 1) {
            if (idx.indexOf(i) !== -1) continue;
            
            const newNum = num + numbers[i];
            
            if (stack.indexOf(parseInt(newNum)) === -1 && parseInt(newNum) >= 2) {
                const isPrime = prime(parseInt(newNum));
                
                if (isPrime) {
                    stack.push(parseInt(newNum));
                }
            }
            makeANum(newNum, [...idx, i]);
        }
    }
    
    makeANum('', []);
    
    return stack.length;
}