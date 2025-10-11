def solution(m, musicinfos):
    guess = ["", 0]
    m = list(m)
    for i in range(len(m)):
        if m[i] == "#":
            m[i] = ""
            m[i-1] = m[i-1].lower()
    
    m = "".join(m)
    

    for i in range(len(musicinfos)):
        info = musicinfos[i].split(",")
        song = list(info[3])
        for j in range(len(song)):
            if song[j] == "#":
                song[j] = ""
                song[j-1] = song[j-1].lower()
        info[3] = "".join(song)
            
        starttime = info[0].split(":")
        endtime = info[1].split(":")
        duration = int(endtime[1])-int(starttime[1]) + (int(endtime[0])-int(starttime[0]))*60
        
        music = info[3]*(duration//len(info[3]))+info[3][:(duration%len(info[3]))]
        
        if m in music:
            if duration > guess[1]:
                guess = [info[2], duration]
    return guess[0] if guess[0] else "(None)"