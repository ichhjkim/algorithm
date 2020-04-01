import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public interface Main_6549 {

	
	
	public static void main(String[] args) throws Exception {
		int C;
		int[] nums;
		int max_result = 0;
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			StringTokenizer str = new StringTokenizer(bf.readLine());
			
			C = Integer.parseInt(str.nextToken());
			nums = new int[C];
			if ( C != 0) {
				for(int k=0; k<C;k++) {
					nums[k] = Integer.parseInt(str.nextToken());
					max_result = 0;
					
					for (int i=0; i<C;i++) {
						int h = nums[i];
						int st = h;
						int time = C-i;
						int result = 0;
						boolean flag = true;
						if(st*time < max_result) {
							continue;
						} else {
							while (time > 0) {
								time--;
								result = st;
								for (int x=i+1;x<C;x++) {
									if(st <= nums[x]) {
										result += st;
									} else {
										st = nums[x];
										if (max_result < result) {
											max_result = result;
										}
										flag = false;
										break;
									}
								}
							}
						if (flag == true) {
							if (max_result < result) {
								max_result = result;
							}
						}
						}
						
					}
				}
				System.out.println(max_result);	
			} else {
				break;
			}
		}

		
		
	
	}
}
