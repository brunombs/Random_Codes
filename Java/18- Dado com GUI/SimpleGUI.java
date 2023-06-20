import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleGUI extends JFrame {
    private JButton button;

    public SimpleGUI() {
        // Configurações básicas da janela
        setTitle("Programa Simples");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Criação do botão
        button = new JButton("Clique aqui");
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Simulação de dado
                int dado = (int) (Math.random() * 6) + 1;
                JOptionPane.showMessageDialog(null, "Número sorteado: " + dado);
            }
        });

        // Adiciona o botão à janela
        getContentPane().setLayout(new FlowLayout());
        getContentPane().add(button);
    }

    public static void main(String[] args) {
        // Cria e exibe a janela
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                SimpleGUI gui = new SimpleGUI();
                gui.setVisible(true);
            }
        });
    }
}
