import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.Arrays; 

public class Solution {

    // Complete the arrayManipulation function below.
    static long arrayManipulation(int n, int[][] que,int m) {
        long arr[]=new long[n+1];
        Arrays.fill(arr,0);

        for(int i=0;i<m;i++){
            arr[que[i][0]-1]+=que[i][2];
            try{
                arr[que[i][1]]-=que[i][2];
            }catch(Exception e){
                int t=0;
            }
        }

        long pre=0;
        for(int i=0;i<n;i++){
            pre+=arr[i];
            arr[i]=pre;
        }

         
        //long r=
        return Arrays.stream(arr).max().getAsLong();

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nm = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nm[0]);

        int m = Integer.parseInt(nm[1]);

        int[][] queries = new int[m][3];

        for (int i = 0; i < m; i++) {
            String[] queriesRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 3; j++) {
                int queriesItem = Integer.parseInt(queriesRowItems[j]);
                queries[i][j] = queriesItem;
            }
        }

        long result = arrayManipulation(n, queries,m);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
