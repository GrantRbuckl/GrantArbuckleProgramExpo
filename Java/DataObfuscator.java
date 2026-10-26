import java.util.Scanner;
import java.lang.StringBuilder;
public class DataObfuscator {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter data: ");
        String data = ui.nextLine();
        System.out.println("Enter length to reveal at the end: ");
        int revealLen = Integer.parseInt(ui.nextLine());
        if(isValidInput(data,revealLen)==true) {
            System.out.println(obfuscateData(data,revealLen));
        }
        else{
            System.out.println("Invalid length.");
        }
        ui.close();
    }
    
    public static String obfuscateData(String data, int revealedLength) {
        StringBuilder obfuscated = new StringBuilder();
        for(int i=0;i<data.length();i++) {
            if(i<(data.length()-revealedLength)){
                obfuscated.append("*");
            }
            else{
                obfuscated.append(data.charAt(i));
            }
        }
        return obfuscated.toString();
    }
    
    public static boolean isValidInput(String data, int revealedLength) {
        if(data.length()>=revealedLength) {
            return true;
        }
        else {
            return false;
        }
    }
}