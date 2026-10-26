import java.util.Scanner;
import java.util.Random;
import java.lang.StringBuilder;
import java.util.ArrayList;
public class GeneratePassword {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);

        // Task #2 - Secure Password Generator
        System.out.println("How long do you want the password? ");
        int leng = Integer.parseInt(ui.nextLine());
        System.out.println(generatePassword(leng));
        ui.close();
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
                 sb = new StringBuilder();
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
            return finalList;
            
    }
}

