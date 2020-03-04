import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main17181_야구_순열2 {
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

		players = new int[8];
		for (int x=0; x < 8; x++) {
			players[x] = x+1;
		}
		max_result = -1;
		perm(0, players);
		System.out.println(max_result);
		
		
	}
	static int[] players;
	static int max_result;
	
	public static void perm(int depth, int[] candi) {
		if(depth == 8) {
			int[] gameplayer = new int[9];
			for (int i=0;i<9;i++) {
				if (i < 3) {
					gameplayer[i] = candi[i];
				} else if (i > 3) {
					gameplayer[i]= candi[i-1];
				}
			}	
			
			int result;
			result = play(gameplayer);
			
			if( max_result < result) {
				max_result = result;
			}
		}
		else {
			for (int i=depth; i < 8; i++) {
				int temp = candi[depth];
				candi[depth] = candi[i];
				candi[i] = temp;
				perm(depth+1, candi);
				candi[i] = candi[depth];
				candi[depth] = temp;

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
