def solution(survey, choices):
    allcategories = ['R','T','C','F','J','M','A','N']
    surveydict = {i:0 for i in allcategories}
    num = len(survey)
    for i in range(num):
        category = list(survey[i])
        choice = choices[i]
        if choice<4:
            surveydict[category[0]] += 4-choice
        elif choice>4:
            surveydict[category[1]] += choice-4
    
    result = ""
    for i in range(4):
        a = 2*i
        b = a + 1
        if surveydict[allcategories[a]] >= surveydict[allcategories[b]]:
            result+=allcategories[a]
        else:
            result+=allcategories[b]
            
    return result