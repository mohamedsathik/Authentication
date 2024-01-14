import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.border.*;
import javax.xml.transform.Source;

class Base{
    public static String FILENAME;
    public static String PASSWORD;
    public static String COLOR_PATTERN;
    public static boolean STATUS;
    public static <E extends Comparable<E>>E[] shuffle(E[] array){
        Random rand = new Random();
		for (int i = 0; i < array.length; i++) {
			int randomIndexToSwap = rand.nextInt(array.length);
			E temp = array[randomIndexToSwap];
			array[randomIndexToSwap] = array[i];
			array[i] = temp;
		}
        return array;
    }    
    public static void startProcess(){
        try{
            if(STATUS){
                String cmd = "python3 Encrypt.py " + FILENAME + " " + Keccak256.hexDigest(PASSWORD+COLOR_PATTERN);
                Runtime.getRuntime().exec(cmd);
            }else{
                String cmd = "python3 Decrypt.py " + FILENAME + " " + Keccak256.hexDigest(PASSWORD+COLOR_PATTERN);
                Runtime.getRuntime().exec(cmd);
            }
        }catch(Exception e){}
    }
}

class RoundBtn implements Border 
{
    private int r;
    RoundBtn(int r) {
        this.r = r;
    }
    public Insets getBorderInsets(Component c) {
        return new Insets(this.r+1, this.r+1, this.r+2, this.r);
    }
    public boolean isBorderOpaque() {
        return true;
    }
    public void paintBorder(Component c, Graphics g, int x, int y, 
    int width, int height) {
        g.drawRoundRect(x, y, width-1, height-1, r, r);
    }
}

class PainBackground extends JPanel{
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
        int w = getWidth(), h = getHeight();
        Color color1 = Color.decode("#ff6d6e");
        Color color2 = Color.decode("#ffc071");
        GradientPaint gp = new GradientPaint(0, 0, color1, w, h, color2);
        g2d.setPaint(gp);
        g2d.fillRect(0, 0, w, h);
    }
}

class ColorPassword extends JFrame implements ActionListener{
    JButton b1,b2,b3,b4,b5,b6,b7,b8,b9;
    JPanel frame;
    JLabel label;
    String[] color = {"#000000","#800080","#DFFF00","#000080","#00FFFF","#FF0000","#FF00FF","#CD5C5C","#C0C0C0"};
    ColorPassword(){
        color = Base.shuffle(color);
        System.out.print(color);
        frame = new PainBackground();
        frame.setLayout(null);
        label = new JLabel("Select Color");
        label.setFont(new Font("sans-serif",Font.BOLD,25));
        label.setForeground(Color.WHITE);
        label.setBounds( 260,10,700,30);
        b1 = new JButton();
        b2 = new JButton();
        b3 = new JButton();
        b4 = new JButton();
        b5 = new JButton();
        b6 = new JButton();
        b7 = new JButton();
        b8 = new JButton();
        b9 = new JButton();
        b1.setBounds(200,100,80,80);
        b2.setBounds(300,100,80,80);
        b3.setBounds(400,100,80,80);
        b4.setBounds(200,200,80,80);
        b5.setBounds(300,200,80,80);
        b6.setBounds(400,200,80,80);
        b7.setBounds(200,300,80,80);
        b8.setBounds(300,300,80,80);
        b9.setBounds(400,300,80,80);
        b1.setBackground(Color.decode(color[0]));
        b2.setBackground(Color.decode(color[1]));
        b3.setBackground(Color.decode(color[2]));
        b4.setBackground(Color.decode(color[3]));
        b5.setBackground(Color.decode(color[4]));
        b6.setBackground(Color.decode(color[5]));
        b7.setBackground(Color.decode(color[6]));
        b8.setBackground(Color.decode(color[7]));
        b9.setBackground(Color.decode(color[8]));
        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);
        b5.addActionListener(this);
        b6.addActionListener(this);
        b7.addActionListener(this);
        b8.addActionListener(this);
        b9.addActionListener(this);
        frame.add(label);
        frame.add(b1);
        frame.add(b2);
        frame.add(b3);
        frame.add(b4);
        frame.add(b5);
        frame.add(b6);
        frame.add(b7);
        frame.add(b8);
        frame.add(b9);
        getContentPane().add(frame);
        setSize(700,500);
        this.setTitle("FileCrypt");
        setLocationRelativeTo(null);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent e){
        Object s = e.getSource();
        if(s == b1 ){
            Base.COLOR_PATTERN = b1.getBackground()+"";
            this.dispose();
            Base.startProcess();
        }else if(s == b2){
            Base.COLOR_PATTERN = b2.getBackground()+"";
            this.dispose();
            Base.startProcess();
        }else if(s == b3){
            Base.COLOR_PATTERN = b3.getBackground()+"";
            this.dispose();
            Base.startProcess();
        }else if( s == b4){
            Base.COLOR_PATTERN = b4.getBackground()+"";
            this.dispose();
            Base.startProcess();
        }else if(s == b5 ){
            Base.COLOR_PATTERN = b5.getBackground()+"";
            this.dispose();
            Base.startProcess();
        }else if(s == b6){
            Base.COLOR_PATTERN = b6.getBackground()+"";
            this.dispose();
            Base.startProcess();
        }else if(s == b7 ){
            Base.COLOR_PATTERN = b7.getBackground()+"";
            this.dispose();
            Base.startProcess();
        }else if(s == b8 ){
            Base.COLOR_PATTERN = b8.getBackground()+"";
            this.dispose();
            Base.startProcess();
        }else if( s == b9){
            Base.COLOR_PATTERN = b9.getBackground()+"";
            this.dispose();
            Base.startProcess();
        }
        
    }
}

class Password extends JFrame implements ActionListener,KeyListener{
    JPanel frame;
    JLabel label;
    JButton submit;
    JTextField ipassword;
    String ltext;
    Font f = new Font("sans-serif",Font.BOLD,25);
    Password(){
        if(Base.STATUS) ltext = "Set Password";
        else ltext = "Enter Password";
        frame = new PainBackground();
        frame.setLayout(null);
        label = new JLabel(ltext);
        label.setFont(f);
        label.setForeground(Color.WHITE);
        label.setBounds( 230,130,700,30);
        ipassword = new JPasswordField();
        ipassword.setBounds(200,200,300,30);
        ipassword.setFont(f);
        ipassword.addKeyListener(this);
        submit = new JButton("Select");
        submit.setBounds( 300,200,100,30);
        submit.setFont(new Font("sans-serif",Font.BOLD,15));
        submit.setCursor(new Cursor(Cursor.HAND_CURSOR));
        submit.addActionListener(this);
        frame.add(ipassword);
        frame.add(label);
        frame.add(submit);
        setSize(700,500);
        this.setTitle("FileCrypt");
        add(frame);
        setLocationRelativeTo(null);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent e){}
    public void keyPressed(KeyEvent e){}
    public void keyTyped(KeyEvent e){}
    public void keyReleased(KeyEvent e){
        if(e.getKeyCode()==KeyEvent.VK_ENTER){
            Base.PASSWORD = ipassword.getText();
            new ColorPassword();
            this.dispose();
        }
    }
}

class SelectFile extends JFrame implements ActionListener{
    String ltext;
    JPanel frame;
    JLabel label;
    JButton select;
    Font f = new Font("sans-serif",Font.BOLD,22);
    SelectFile(){
        if(Base.STATUS) ltext = "Select File to encrypt";
        else ltext = "Select File to decrypt";
        frame = new PainBackground();
        frame.setLayout(null);
        label = new JLabel(ltext);
        label.setFont(f);
        label.setForeground(Color.WHITE);
        label.setBounds( 250,130,700,30);
        select = new JButton("Select");
        select.setBounds( 300,200,100,30);
        select.setFont(new Font("sans-serif",Font.BOLD,15));
        select.setCursor(new Cursor(Cursor.HAND_CURSOR));
        select.addActionListener(this);
        frame.add(label);
        frame.add(select);
        setSize(700,500);
        this.setTitle("FileCrypt");
        add(frame);
        setLocationRelativeTo(null);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent e){
        JFileChooser file = new JFileChooser();
        file.setMultiSelectionEnabled(true);
        file.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES);
        file.setFileHidingEnabled(false);
        if (file.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
         java.io.File f = file.getSelectedFile();
         Base.FILENAME =  f.getPath();
         new Password();
         this.dispose();
      }
    }
}

class Home extends JFrame implements ActionListener{
    JPanel frame;
    JLabel label;
    JButton encrypt,decrypt;
    int w,h;
    Font f = new Font("sans-serif",Font.BOLD,22);
    Home(){
        frame = new PainBackground();
        frame.setLayout(null);
        label = new JLabel("Do you want to encrypt or decrypt File ?");
        label.setFont(f);
        label.setForeground(Color.WHITE);
        label.setBounds( 120,130,700,30);
        encrypt = new JButton("Encrypt");
        encrypt.setBounds( 170,200,170,40);
        encrypt.setFont(new Font("sans-serif",Font.BOLD,15));
        encrypt.setCursor(new Cursor(Cursor.HAND_CURSOR));
        decrypt = new JButton("Decrypt");
        decrypt.setBounds( 390,200,170,40);
        decrypt.setFont(new Font("sans-serif",Font.BOLD,15));
        decrypt.setCursor(new Cursor(Cursor.HAND_CURSOR));
        encrypt.addActionListener(this);
        decrypt.addActionListener(this);
        frame.add(label);
        frame.add(encrypt);
        frame.add(decrypt);
        setSize(700,500);
        this.setTitle("FileCrypt");
        add(frame);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e){
        if(e.getSource() == encrypt){
            Base.STATUS = true;
            new SelectFile();
            this.dispose();
        }else if(e.getSource() == decrypt){
            Base.STATUS = false;
            new SelectFile();
            this.dispose();
        }
    }
}


public class FileCrypt {
    public static void main(String[] args) {
        Base.STATUS = true;
        new Home();
    }
}
