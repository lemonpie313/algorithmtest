function solution(id_list, report, k) {
  const ans = new Array(id_list.length);
  ans.fill(0) 
  const report_list = {}
    
  id_list.forEach((user)=>{
      report_list[user] = []
  })
  
  report.forEach((user)=>{
      const [user_id, report_id] = user.split(' ')
      if(!report_list[report_id].includes(user_id)){
          report_list[report_id].push(user_id)
      }        
  })
  
  for(const key in report_list){
      if(report_list[key].length >= k){
          report_list[key].forEach((user)=>{
              ans[id_list.indexOf(user)] += 1
          })
      }
  }
  return ans;
}