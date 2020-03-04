import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main17281_¾ß±¸ {
	static int N;
	static int[][] scores;
	
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(bf.readLine());
		scores = new int[N][9];
		for (int i=0;i<N; i++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			for (int j=0; j <9; j++) {
				scores[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		visited = new boolean[10];
		players = new int[9];
		max_result = -1;
		perm(0, players);
		System.out.println(max_result);
		
		
	}
	static boolean[] visited;
	static int[] players;
	static int max_result;
	
	public static void perm(int depth, int[] candi) {
		if(depth == 9) {
			int[] gameplayer = candi.clone();
			int result;
			result = play(gameplayer);
			
			if( max_result < result) {
				max_result = result;
			}
		}
		else if (depth==3) {
			perm(depth+1, candi);
		}
		else {
			for (int i=1; i < 9; i++) {
				if (visited[i] != true) {
					candi[depth] = i;
					visited[i] = true;
					perm(depth+1, candi);
					visited[i] = false;
				}
			}
		}
	}
	public static int play(int[] candi) {
		
		int stage = 0;
		int res = 0;
		int idx = 0;
		while (stage < N) {
			int[] base = new int[3];
			int out = 0;
			while (true) {
				int temp = candi[idx];
				
				if (scores[stage][temp] == 0) {
					out++;
				} 
				else if (scores[stage][temp] == 1) {
					res += base[2];
					base[2] = base[1];
					base[1] = base[0];
					base[0] = 1;
				}
				else if (scores[stage][temp] == 2) {
					res += (base[2]+base[1]);
					base[2] = base[0];
					base[1] = 1;
					base[0] = 0;
				}
				else if (scores[stage][temp] == 3) {
					res += (base[0]+base[1]+base[2]);
					base[0] = 0;
					base[1] = 0;
					base[2] = 1;
				}
				else {
					res += (base[0]+base[1]+base[2]+1);
					base[0] = 0;
					base[1] = 0;
					base[2] = 0;
				}
				idx++;
				if (idx > 8) {
					idx = 0;
				}
				if (out == 3) {
					break;
				}
	
			} stage++;
		}
		return res;
	}
	
}
