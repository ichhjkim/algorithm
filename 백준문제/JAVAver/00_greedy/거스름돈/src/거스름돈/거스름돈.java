package °Å½º¸§µ·;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class °Å½º¸§µ· {
	public static void main(String[] args) throws IOException{
		int num;
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		num = Integer.parseInt(bf.readLine());
		num = 1000 - num;
		int count = 0;
		while (num > 0) {
			if (num >= 500) {
				num -= 500;
				count++;
			} else if (num >= 100) {
				num -= 100;
				count++;
			} else if (num >= 50) {
				num -= 50;
				count++;
			} else if (num >= 10) {
				num -= 10;
				count++;
			} else if (num>=5) {
				num -= 5;
				count++;
			} else if (num>=1) {
				num -= 1;
				count++;
			}
		}
		System.out.println(count);
	}

}
