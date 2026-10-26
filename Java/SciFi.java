import java.util.Scanner;
public class SciFi {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        
        System.out.println("What is your first name? ");
        String first = scanner.nextLine();
        System.out.println("What is your last name? ");
        String last = scanner.nextLine();
        System.out.println("What city are you from? ");
        String city = scanner.nextLine();
        System.out.println("What school are you from? ");
        String school = scanner.nextLine();
        System.out.println("What is your pet's name? ");
        String pet = scanner.nextLine();
        System.out.println("What is your sibling's name? ");
        String sibling = scanner.nextLine();

        System.out.printf("\tfirst: "+first+"\n\tlast: "+last+"\n\tcity: "+city+"\n\tschool: "+school+"\n\tpet: "+pet+"\n\tsib: "+sibling+"\n");
        String firstSci = first.substring(0,2)+last.substring(last.length()-3,last.length());
        String lastSci = city.substring(0,3)+school.substring(school.length()-3,school.length());
        String origin = pet.substring(0,2)+sibling.substring(sibling.length()-2,sibling.length());


        System.out.println("Howdy "+firstSci+" "+lastSci+" from "+origin+"!");



        
        scanner.close();
    }

}