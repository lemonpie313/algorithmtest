function solution(nums) {
    let arr = [];
    for (let i=0; i<nums.length-2; i++) {
        for (let j=i+1; j<nums.length-1;j++) {
            for (let k=j+1; k<nums.length; k++) {
                arr.push(nums[i]+nums[j]+nums[k]);

            }
        }
    }

    let answer = arr.reduce((acc,cur)=> {
        for (let b=2; b<=cur/2; b++) {
            if (cur%b==0) {
                return acc;
            }
        }
        return acc+1;
    },0)
    
    return answer;
}