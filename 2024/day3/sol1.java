import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class sol1 {
    public static void main(String[] args) throws IOException {
        System.out.println("hello");
        Integer res = 0;

        BufferedReader br;
        try {
            br = new BufferedReader(new FileReader("input.txt"));
            String line;
            String lines = "";
            while ((line = br.readLine()) != null) {
                lines = lines + line;
            }


            String[] sp = lines.split("don't\\(\\).*?do\\(\\)");
            print(sp.length);
            print("");
            for ( int i = 0; i < sp.length; i++){
                res += exectuteLine(sp[i]);
            }
            
        } 
                
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
  

        System.out.println(res);

    }


    public static int exectuteLine(String line){
        int res = 0;
        String regex = "mul\\(\\d+,\\d+\\)";

        // Compile the regex
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(line);

        // Collect matches
        while (matcher.find()) {
            res += calculate(matcher.group());
        }                        
        return res;
    }

    public static int calculate(String s){
        String[] parts = s.split(",");
        int a = Integer.parseInt(parts[0].split("mul\\(")[1]);
        int b = Integer.parseInt(parts[1].split("\\)")[0]);
        return a*b;
    }

    public static void print(Object x ){
        System.out.println(x);
    }

 


    

    
}
