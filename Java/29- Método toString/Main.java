public class Main {
    public static void main(String[] args) {
        String primeira = "Java";
        String segunda = "Python";
        String terceira = new String("Csharp");

        System.out.println(primeira.toUpperCase());
        System.out.println(segunda.toLowerCase());
        System.out.println(terceira.length());

        //comparar a primeira com a segunda string
        boolean result = primeira.equals(segunda);
        System.out.println("Primeira é igual a segunda? " + result);

        //comparar a segunda com a terceira
        result = segunda.equals(terceira);
        System.out.println("Segunda é igual a terceira? " + result);
    }
}