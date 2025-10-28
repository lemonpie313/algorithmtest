import java.util.*;
class Solution {
    public String solution(String m, String[] musicinfos) {
        
        int maxLength = 0;
        String best = "(None)";

        m = m.replace("C#", "c");
        m = m.replace("D#", "d");
        m = m.replace("F#", "f");
        m = m.replace("G#", "g");
        m = m.replace("A#", "a");
        m = m.replace("B#", "b");
        
        Map<String, Integer> musicDuration = new HashMap<>();
        
        // Map<String, String> musicDict = new HashMap<>();
        
        for (String musicInfo: musicinfos) {
            
            String[] musicInfoArr = musicInfo.split("\\,");
            
            String[] musicStartArr = musicInfoArr[0].split("\\:");
            String[] musicEndArr = musicInfoArr[1].split("\\:");
            String musicTitle = musicInfoArr[2];
            
            int duration = Integer.parseInt(musicEndArr[1]) + Integer.parseInt(musicEndArr[0])*60 - Integer.parseInt(musicStartArr[1]) - Integer.parseInt(musicStartArr[0]) * 60;            
            
            String music = musicInfoArr[3];
            
            music = music.replace("C#", "c");
            music = music.replace("D#", "d");
            music = music.replace("F#", "f");
            music = music.replace("G#", "g");
            music = music.replace("A#", "a");
            music = music.replace("B#", "b");
            
            if (musicDuration.keySet().contains(musicTitle)) {
                musicDuration.put(musicTitle, musicDuration.get(musicTitle)+duration);
            } else {
                musicDuration.put(musicTitle, duration);
                // musicDict.put(musicTitle, music);
            }
            
            String fullMusic = "";
            
            for (int j = 0; j<duration/music.length(); j++) {
                fullMusic += music;
            }
            fullMusic += music.substring(0, duration%music.length());
            
            if (fullMusic.contains(m) && maxLength < musicDuration.get(musicTitle)) {
                best = musicInfoArr[2];
                maxLength = musicDuration.get(musicTitle);
            }
            
            
        }
        
        return best;
    }
}