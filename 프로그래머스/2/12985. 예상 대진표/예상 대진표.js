function solution(n, a, b) {
  let abin = String((a-1).toString(2));
  let bbin = String((b-1).toString(2));
  console.log(abin);
  console.log(bbin);
  if (abin.length>bbin.length) {
    bbin = "0".repeat(abin.length-bbin.length) + bbin;
  } else if (abin.length<bbin.length) {
    abin = "0".repeat(bbin.length-abin.length) + abin;
  }
  for (let i=0; i<abin.length; i++) {
    if (abin[i]!=bbin[i]) {
      return abin.length - i;
    }
  }
}