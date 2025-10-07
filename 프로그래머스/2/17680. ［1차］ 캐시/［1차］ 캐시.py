from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)
    cache = deque([])
    time = 0
    for i in range(len(cities)):
        city = cities[i].lower()
        if city not in cache:
            time += 5   
            if len(cache)==cacheSize:
                cache.popleft()
            cache.append(city)
        else:
            time += 1
            cache.remove(city)
            cache.append(city)
        
            
    return time