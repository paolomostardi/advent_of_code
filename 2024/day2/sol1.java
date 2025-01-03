import java.io.*;

public class sol1 {
    public static void main(String[] args) throws IOException {
        System.out.println("hello");
        Integer res = 0;

        BufferedReader br;
        try {
            br = new BufferedReader(new FileReader("input.txt"));
            String line;
            
            while ((line = br.readLine()) != null) {
                String[] a = line.split(" ");
                if (isSafe(a,line,true)){
                    res++;
                }
            }

        } 
        
        
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
  

        System.out.println(res);

    }

    public static Integer mInt(String s){
        return Integer.parseInt(s);
    }


    public static boolean isSafe(String[] a, String line, boolean remove){

        boolean growing = ( mInt(a[0]) < mInt(a[1]) );

        for (int i = 0; i < a.length - 1; i++ ){
            Integer a1 = mInt(a[i]);
            Integer a2 = mInt(a[i + 1]);
            
            boolean growingButNot = (growing && a1 > a2 );
            boolean notGrowingButNot = (!growing && a1 < a2);
            boolean TooMuch = (Math.abs(a1 - a2 ) > 3);
            boolean equal = (a1 == a2);

            if (growingButNot || notGrowingButNot || TooMuch || equal){

                if (remove){
                    boolean iHateMySelf = false;
                    for ( int j = 0; j < a.length; j++){
                            iHateMySelf = iHateMySelf || isSafe(deleteElement(j, a), line, false);
                        } 
                    return iHateMySelf;
                    }
                else{


                    System.out.println("----------------------------------------------");
                    System.out.print(i);
                    System.out.println(" " + growingButNot + 
                    ",  " + notGrowingButNot + 
                    ",  " + TooMuch + 
                    ",  " + equal);

                    System.out.println(line + ",  " + growing + ",  " + a1 + ",  " + a2 );

                    for ( int j = 0; j < a.length; j++){
                        System.out.print(a[j] + " ");
                    }
                    
                    System.out.println("");


                    System.out.println("----------------------------------------------");

                    return false;
                }
            }


        }

        return true;
        
    }


    public static String[] deleteElement(int index, String[] array){
        String[] newArray = new String[array.length - 1];
        for (int i = 0, j = 0;i < array.length; i++ )
        {
            if (i != index){
                newArray[j++] = array[i];
            }
        }
        
        return newArray; 
    }


    
}
