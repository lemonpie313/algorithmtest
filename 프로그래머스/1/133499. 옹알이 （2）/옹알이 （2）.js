function solution(babbling) {
  let babs = ["aya", "ye", "woo", "ma"];

  let sols = function (babs, cur) {
	//console.log("---------------");
	//console.log("cur: "+cur);
    if (cur.length == 0) {
      //console.log("종결");
      return 1;
    }
    for (let bab of babs) {
      let cur2 = cur.slice(bab.length, cur.length);
      if (
        cur.indexOf(bab) == 0 &&
        (cur2.indexOf(bab) != 0 || cur2.length == 0)
      ) {
		//console.log("통과");
		//console.log(cur2);
        return sols(babs, cur2);
      }
    }
	return 0;
  };


  return babbling.reduce((acc, cur) => {
	return acc+sols(babs, cur);
  }, 0);

}