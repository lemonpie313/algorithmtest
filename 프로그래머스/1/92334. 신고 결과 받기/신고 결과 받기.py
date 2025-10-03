def solution(id_list, report, k):
    reportnum = {i:0 for i in id_list}
    mailnum = {i:0 for i in id_list}
    report = list(set(report))
    
    for i in range(len(report)):
        report[i] = report[i].split()
        reportnum[report[i][1]] += 1
    
    reportedlist = [key for key, value in reportnum.items() if value>=k]
    for i in range(len(report)):
        if report[i][1] in reportedlist:
            mailnum[report[i][0]] += 1
        
    return list(mailnum.values())