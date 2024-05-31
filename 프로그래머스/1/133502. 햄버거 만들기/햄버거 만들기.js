function solution(s) {
  let answer = 0;
  const stack = [];
  
  for (let i = 0; i < s.length; i++) {
      stack.push(s[i]);
      
      if (stack.length >= 4) {
          const burger = stack.slice(-4).join("");
          
          if (burger === '1231') {
              stack.splice(-4);
              answer += 1;
          }
      }
  }
  
  return answer;
}