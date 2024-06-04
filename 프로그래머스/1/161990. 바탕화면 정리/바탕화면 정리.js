function solution(wallpaper) {

  const a = wallpaper.length;
  const b = wallpaper[0].length;

  let [i, j, k, l] = wallpaper.reduce(
    (acc, cur, idx, arr) => {
      curArr = cur.split("");
      let [i, j, k, l] = acc;
      if (cur.includes("#")) {
        if (idx < i) {
          i = idx;
        }
        if (idx > k) {
          k = idx;
        }
        while (cur.split("").includes("#")) {
          if (cur.indexOf("#") < j) {
            j = cur.indexOf("#");
          }
          if (cur.indexOf("#") > l) {
            l = cur.indexOf("#");
          }
          cur = cur.replace("#", ".");
            arr[idx] = cur;
        }
      }
      return [i, j, k, l];
    },
    [a, b, 0, 0]
  );

  return [i, j, k + 1, l + 1];
}