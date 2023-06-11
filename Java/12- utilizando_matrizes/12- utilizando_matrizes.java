class Main {
    public static void main(String[] args) {
        int [][] matriz = { {9, 8, 7} , {5, 3,2}, {6, 6, 7} };

        int[] maior_linha = new int[3];
        int[] menor_coluna = new int[3];

        for (int i=0; i<3; i++)
            maior_linha[i] = 0;

        for (int i=0; i<3; i++)
            menor_coluna[i] = 10;

        // encontrar o maior elemento na linha 0
        for(int i=0; i<3; i++)
            if(matriz[0][i] > maior_linha[0])
                maior_linha[0] = matriz[0][i];

        // encontrar o maior elemento na linha 1
        for(int i=0; i<3; i++)
            if(matriz[1][i] > maior_linha[1])
                maior_linha[1] = matriz[1][i];

        // encontrar o maior elemento na linha 2
        for(int i=0; i<3; i++)
            if(matriz[2][i] > maior_linha[2])
                maior_linha[2] = matriz[2][i];

        // encontrar o menor elemento na coluna 0
        for(int i=0; i<3; i++)
            if(matriz[i][0] < menor_coluna[0])
                menor_coluna[0] = matriz[i][0];

        // encontrar o menor elemento na coluna 1
        for(int i=0; i<3; i++)
            if(matriz[i][1] < menor_coluna[1])
                menor_coluna[1] = matriz[i][1];

        // encontrar o menor elemento na coluna 2
        for(int i=0; i<3; i++)
            if(matriz[i][2] < menor_coluna[2])
                menor_coluna[2] = matriz[i][2];

        for(int i=0; i<3; i++)
            for(int j=0; j<3; j++)
                if(maior_linha[i] == menor_coluna[j])
                    System.out.println("Ponto de sela: " + maior_linha[i]);
    }
}