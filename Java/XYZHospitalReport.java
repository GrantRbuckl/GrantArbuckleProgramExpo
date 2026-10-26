import java.util.Scanner;
public class XYZHospitalReport {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Please enter your first name: ");
        String first = scanner.nextLine();
        System.out.println("Please enter your last name: ");
        String last = scanner.nextLine();
        System.out.println("Please enter your street address: ");
        String address = scanner.nextLine();
        System.out.println("Please enter your city: ");
        String city = scanner.nextLine();
        System.out.println("Please enter your state: ");
        String state = scanner.nextLine();
        System.out.println("Please enter your ZIP (ZIP+4 preferred): ");
        String zip = scanner.nextLine();
        System.out.println("Please enter your amount owed (numbers only): ");
        String owed = scanner.nextLine();
        System.out.println("Please enter your payment amount (numbers only): ");
        String payment = scanner.nextLine();
        System.out.println("Please enter your payment date: ");
        String date = scanner.next();

        System.out.printf("\t\t\t\t\tXYZ Community Hospital\n===================================================================================================\n");
        System.out.printf("\n\tName\t\tAddress\t\t\t\tPayment Information\n");
        System.out.printf("\nLast\tFirst\tAddressLine1\tCity, State\tZip\tAmount Owed\tPayment Amt\tPayment Date\n");
        System.out.printf("\n===================================================================================================\n");
        System.out.printf(last+" "+first+"\t"+address+"   "+city+", "+state+"\t"+zip+"\t$"+owed+"\t$"+payment+"\t"+date);


        scanner.close();
    }
}