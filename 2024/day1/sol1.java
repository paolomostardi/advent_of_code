import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class sol1 {
    public static void main(String[] args) throws IOException {
        System.out.println("hello");
        Integer res = 0;

        BufferedReader br;
        try {
            br = new BufferedReader(new FileReader("input.txt"));
            String line;
            ArrayList<Integer> a1 = new ArrayList<>();
            ArrayList<Integer> a2 = new ArrayList<>();
            
            while ((line = br.readLine()) != null) {
                String[] a = line.split(" ");
                System.out.println(a[3]);
                a1.add(Integer.parseInt(a[0]));
                a2.add(Integer.parseInt(a[3]));
                
                
            }
        
            a1.sort(null);
            a2.sort(null);
            
            for(int i = 0; i < a1.size(); i++){
                res += a1.get(i) * Collections.frequency(a2, a1.get(i));
            }
        } 
        
        
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
  

        System.out.println(res);

    }
}
