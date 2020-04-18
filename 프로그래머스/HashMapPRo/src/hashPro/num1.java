package hashPro;

import java.util.HashMap;
import java.util.Map;

public class num1 {
	public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        final String answer= "";
        for(int i=0; i<participant.length; i++) {
        	if (map.get(participant[i]) == null) {
        		map.put(participant[i], 1);
        	} else {
        		map.replace(participant[i], map.get(participant[i])+1);
        	}
        }
        for(int j=0;j<completion.length;j++) {
        	map.replace(participant[j], map.get(participant[j])-1);
        }

		System.out.println(map);
		map.forEach((key, value) -> {
			
			if(value == 1) {
				answer = key;
			}
		}
		
				);
        return answer;
    }
}
