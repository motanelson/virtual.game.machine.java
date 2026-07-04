public class whiles {
    public static void main(String argv[]){
         int n=0;
         System.out.println("\033c\033[47;31m\nyou score?\n");
         while(n<10){
             System.out.println(n);
             n++;
         }
    }
    public static void init(String argv[]){
         main(argv);
    }

}
