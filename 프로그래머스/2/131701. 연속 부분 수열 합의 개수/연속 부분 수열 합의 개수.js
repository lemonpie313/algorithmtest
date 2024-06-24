function solution(elements) {
  elements.push(...elements);
  let acc = new Set();
  for (let i=0; i<elements.length/2; i++) {
    let sum = 0;
    for (let j = 0; j < (elements.length-1) / 2; j++) {
      sum+=elements[i+j];
      acc.add(sum);
    }
  }
  return acc.size;
      
}