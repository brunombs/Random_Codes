public class Main {
    public static void main(String[] args) {
        int n1 = 5;
        int n2 = 3;
        int n3 = 4;
        int n4 = 5;
        int n5 = 7;

        System.out.println("Numbers:");
        System.out.println("");
        boolean result = (n1 == n2);
        System.out.println(n1 + " equals to " + n2 + "? " + result);
        result = (n1 == n4);
        System.out.println(n1 + " equals to " + n4 + "? " + result);
        result = (n2 == n5);
        System.out.println(n2 + " equals to " + n5 + "? " + result);
        result = (n4 == n3);
        System.out.println(n4 + " equals to " + n3 + "? " + result);
        result = (n3 == n4);
        System.out.println(n3 + " equals to " + n5 + "? " + result);

        System.out.println("");
        
        if (n1 > n2){
            System.out.println(n1 + " is greater than " + n2);
        } else if (n1 < n2){
            System.out.println(n1 + " is less than " + n2);
        } else {
            System.out.println(n1 + " is equal to " + n2);
        }

        if (n2 > n3){
            System.out.println(n2 + " is greater than " + n3);
        } else if (n2 < n3){
            System.out.println(n2 + " is less than " + n3);
        } else {
            System.out.println(n2 + " is equal to " + n3);
        }

        if (n3 > n4){
            System.out.println(n3 + " is greater than " + n4);
        } else if (n3 < n4){
            System.out.println(n3 + " is less than " + n4);
        } else {
            System.out.println(n3 + " is equal to " + n4);
        }

        if (n4 > n5){
            System.out.println(n4 + " is greater than " + n5);
        } else if (n4 < n5){
            System.out.println(n4 + " is less than " + n5);
        } else {
            System.out.println(n4 + " is equal to " + n5);
        }

        if (n4 > n1){
            System.out.println(n4 + " is greater than " + n1);
        } else if (n4 < n1){
            System.out.println(n4 + " is less than " + n1);
        } else {
            System.out.println(n4 + " is equal to " + n1);
        }

        System.out.println("");
        System.out.println("Countries:");
        System.out.println("");
        String country1 = "Brazil";
        String country2 = "Ireland";
        String country3 = "United Kingdom";
        String country4 = "Brazil";
        String country5 = "France";

        result = country1.equals(country2);
        System.out.println(country1 + " equals to " + country2 + "? " + result);
        result = country1.equals(country4);
        System.out.println(country1 + " equals to " + country4 + "? " + result);
        result = country2.equals(country5);
        System.out.println(country2 + " equals to " + country5 + "? " + result);
        result = country4.equals(country3);
        System.out.println(country4 + " equals to " + country3 + "? " + result);
        result = country1.toLowerCase().equals(country4);
        System.out.println(country1.toLowerCase() + " equals to " + country4 + "? " + result);
    }
}