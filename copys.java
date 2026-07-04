public class copys {
    public static void main(String argv[]){
         String s1="hello world....\n";
         String s2="";
         s2=s1;
         System.out.println("\033c\033[47;31m\nyou score?\n");
         System.out.println(s2);
    }
    public static void init(String argv[]){
         main(argv);
    }

}
