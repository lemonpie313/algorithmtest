function solution(topping) {
  const cakeA = {}
  const cakeB = new Set()

  let cnt = 0;

  for (let i = 0; i < topping.length; i++) {        
      if (cakeA[topping[i]]) {
          cakeA[topping[i]]++
      } else {
          cakeA[topping[i]] = 1      
      }
  }
  let cakeATopping = Object.keys(cakeA).length;
  for (let i = 0; i < topping.length; i++) {
      cakeB.add(topping[i])
      cakeA[topping[i]]--

      if (!cakeA[topping[i]]) {
          cakeATopping--
      }
      if (cakeB.size === cakeATopping) {
          cnt+=1;
      }
  }


  return cnt;
}