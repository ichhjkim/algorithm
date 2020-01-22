package ¹®ÀÚ¿­;

import java.util.Scanner;

public class Main {

	public static void main(String[] args){

	Scanner sc = new Scanner(System.in);
	String A = sc.next();
	String B = sc.next();
	
	int diff = B.length() - A.length();
	int min_result = 100;
	
	for (int d=0;d<diff+1;d++) {
		int result = 0;
		for (int i=0;i<A.length();i++) {
			if (B.charAt(d+i) != A.charAt(i)) {
				result++;
			}
		}
		if (min_result > result) {
			min_result = result;
		}
	}
	System.out.println(min_result);
	}
}
