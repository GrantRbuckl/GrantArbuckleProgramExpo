import java.util.Scanner;
import java.util.Random;
import java.lang.StringBuilder;
import java.util.ArrayList;
public class CaesarCipher {
    
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        
        // Task #1 - Caesar Cipher
        
        System.out.println("What is your message? ");
        String message = ui.nextLine();
        System.out.println("How much would you like it shifted? ");
        int shift = Integer.parseInt(ui.nextLine());
        
        System.out.println("Would you like to encrypt or decrypt? (e/d) ");
        String answer = ui.nextLine();
         if(answer.equals("e")) {
            String lastly = encrypt(message,shift);
            System.out.println(lastly);
        }
        else if(answer.equals("d")){
            String lastly = decrypt(message,shift);
            System.out.println(lastly);
        }
        

    }
        public static String encrypt(String message,int amount) {   //Credit to Max O'Didily on YouTube, I had the basis but I learned the StringBuilder class from him
        StringBuilder sb = new StringBuilder();
        message = message.toLowerCase();
        for(int i=0; i<message.length();i++){
            char c = message.charAt(i);
            if(Character.isLetter(c)) {
                c = (char)  ((c - 'a' + amount + 26) % 26 + 'a');
            }
                sb.append(c);
        }
        return sb.toString();
    }
        
    public static String decrypt(String message,int amount) {   //Credit to Max O'Didily on YouTube, I had the basis but I learned the StringBuilder class from him
        StringBuilder sb = new StringBuilder();
        message = message.toLowerCase();
        for(int i=0; i<message.length();i++){
            char c = message.charAt(i);
            if(Character.isLetter(c)) {
                c = (char)  ((c - 'a' - amount + 26) % 26 + 'a');
            }
                sb.append(c);
        }
        return sb.toString();
    }
    
    public static String generatePassword(int length){
            Random randy = new Random();
            Scanner ui = new Scanner(System.in);
            StringBuilder sb = new StringBuilder();
            String alphabetL = "abcdefghijklmnopqrstuvwxyz";
            String alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            String special = "!@#$%^&*";
            String numbers = "1234567890";
            String starter = "@Dm1n!";
            String[] types = {alphabetL,alphabetU,special,numbers};
            ArrayList<String> passwList = new ArrayList();
            sb.append(starter);
            String user = "c";
            while(user!=("quit") && user!=("q")) {
                    for(int i=0; i<length; i++) {
                        String current = "";
                        int choose = randy.nextInt(0,types.length);
                        if(choose==0){
                            current = alphabetL;
                        }
                        else if(choose==1) {
                            current = alphabetU;
                        }
                        else if(choose==2) {
                            current = special;
                        }
                        else if(choose==3) {
                            current = numbers;
                        }
                        char passChar = current.charAt(randy.nextInt(0,current.length()));
                        sb.append(passChar);
                    }
                System.out.println("Create or quit? (c/q) ");
                user = ui.nextLine();
                if(user.equals("q") || user.equals("quit")){
                    break;
                }
                else if(user.equals("c")||user.equals("create")){
                    passwList.add(sb.toString());
                }
            }
            String finalList = String.join("\n",passwList);
            System.out.println(finalList);
            return finalList;
            
    }
}

