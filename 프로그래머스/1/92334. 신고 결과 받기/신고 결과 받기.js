function solution(id_list, report, k) {
  const ans = new Array(id_list.length);
  ans.fill(0) 
  const report_list = {}
    
  id_list.map((user)=>{
      report_list[user] = [] //key로 userid를 value로 빈 배열을 가지는 객체
  })
  
  report.map((user)=>{
      const [user_id, report_id] = user.split(' ')
      if(!report_list[report_id].includes(user_id)){
          report_list[report_id].push(user_id)
      }        
  })
  
  for(const key in report_list){
      if(report_list[key].length >= k){ //이용정지 유저
          report_list[key].map((user)=>{
              ans[id_list.indexOf(user)] += 1
          })
      }
  }
  return ans;
}