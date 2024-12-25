import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;

public class GamePanel extends JPanel implements ActionListener{

    static final int SCREEN_WIDTH = 800;
    static final int SCREEN_HEIGHT = 800;
    static final int UNIT_SIZE = 25;
    static final int GAME_UNITS = (SCREEN_WIDTH*SCREEN_HEIGHT)/UNIT_SIZE;
    static final int DELAY = 150;
    final int x[] = new int[GAME_UNITS];
    final int y[] = new int[GAME_UNITS];
    int bodyparts = 3;
    int appleeaten;
    int applex;
    int appley;
    char direction = 'R';
    boolean running;
    Timer timer;
    Random random;
    

    GamePanel(){
        random = new Random();
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(Color.BLACK);
        this.setFocusable(true);
        this.addKeyListener(new mykeyadapter());
        startgame();
    }

    public void startgame(){
        newapple();
        running = true;
        timer = new Timer(DELAY, this);
        timer.start();
    }

    public void paintComponent(Graphics g){
        super.paintComponent(g);
        draw(g);
    }

    public void draw(Graphics g){

        if(running){
            // for(int i=0;i<SCREEN_HEIGHT/UNIT_SIZE;i++){
            //     g.drawLine(i*UNIT_SIZE, 0, i*UNIT_SIZE, SCREEN_HEIGHT);
            //     g.drawLine(0, i*UNIT_SIZE, SCREEN_WIDTH, i*UNIT_SIZE);
            // }
            g.setColor(Color.red);
            g.fillOval(applex, appley, UNIT_SIZE, UNIT_SIZE);

            for(int i=0; i<bodyparts;i++){
                if(i==0){
                    g.setColor(Color.green);
                    g.fillRect(x[i], y[i], UNIT_SIZE, UNIT_SIZE);
                }
                else{
                    //g.setColor(new Color(45,180,0));
                    g.setColor(new Color(random.nextInt(255), random.nextInt(255), random.nextInt(255)));
                    g.fillRect(x[i], y[i], UNIT_SIZE, UNIT_SIZE);
                }
            }
            g.setColor(Color.red);
            g.setFont(new Font("Ink Free", Font.BOLD, 40));
            FontMetrics metrics = getFontMetrics(g.getFont());
            g.drawString("SCORE: "+appleeaten,(SCREEN_WIDTH-metrics.stringWidth("SCORE: "+appleeaten))/2,g.getFont().getSize());
        }
        else{
            gameover(g);
        }
    }

    public void newapple(){
        int availableWidth = (SCREEN_WIDTH - 4 * UNIT_SIZE) / UNIT_SIZE;
        int availableHeight = (SCREEN_HEIGHT - 4 * UNIT_SIZE) / UNIT_SIZE;
        applex = (random.nextInt(availableWidth) + 2) * UNIT_SIZE;
        appley = (random.nextInt(availableHeight) + 2)* UNIT_SIZE;
    }

    public void move(){
        for(int i = bodyparts; i>0;i--){
            x[i] = x[i-1];
            y[i] = y[i-1];
        }
        switch(direction){
            case 'U':
                y[0] = y[0] - UNIT_SIZE;
                break;
            case 'D':
                y[0] = y[0] + UNIT_SIZE;
                break;
            case 'L':
                x[0] = x[0] - UNIT_SIZE;
                break;
            case 'R':
                x[0] = x[0] + UNIT_SIZE;
                break;
        }
    }

    public void checkapple(){
        if((x[0]==applex)&&(y[0]==appley)){
            bodyparts++;
            appleeaten++;
            newapple();
            int newDelay = (int) (DELAY * (1.0 / (bodyparts * 0.2)));
            timer.setDelay(newDelay);
        }
    }

    public void checkcollision(){
        for(int i=bodyparts;i>0;i--){
            if((x[0]==x[i])&&(y[0]==y[i])){ //head body collision
                running = false;
            }
        }
        if(x[0] < 0){  //LEFT border
            x[0] = SCREEN_WIDTH;
        }
        if(x[0] > SCREEN_WIDTH){  //rigt border
            x[0] = 0;
        }
        if(y[0] < 0){    //top border
            y[0] = SCREEN_HEIGHT;
        }
        if(y[0] > SCREEN_HEIGHT){  //BOTTOMboRDER
            y[0] = 0;
        }
        if(!running){
            timer.stop();
        }
    }

    public void gameover(Graphics g){
        g.setColor(Color.red);
        g.setFont(new Font("Ink Free", Font.BOLD, 75));
        FontMetrics metrics1 = getFontMetrics(g.getFont());
        g.drawString("Game Over",(SCREEN_WIDTH-metrics1.stringWidth("Game Over"))/2,SCREEN_HEIGHT/2);
        g.setFont(new Font("Ink Free", Font.BOLD, 20));
        FontMetrics metrics2 = getFontMetrics(g.getFont());
        g.drawString("Press Spacebar to Play Again",(SCREEN_WIDTH-metrics2.stringWidth("Press Spacebar to Play Again"))/2,SCREEN_HEIGHT/2 + 50);
        g.setFont(new Font("Ink Free", Font.BOLD, 40));
        FontMetrics metrics = getFontMetrics(g.getFont());
        g.drawString("SCORE: "+appleeaten,(SCREEN_WIDTH-metrics.stringWidth("SCORE: "+appleeaten))/2,g.getFont().getSize());

    }

    public void resetGame() {
        running = true;
        appleeaten = 0;
        bodyparts = 3;
        direction = 'R';
        for (int i = 0; i < x.length; i++) {
            x[i] = 0;
            y[i] = 0;
        }
        newapple();
        timer.setDelay(DELAY);
        timer.start();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (running) {
            move();
            checkapple();
            checkcollision();
        } else {
            // Rest
            if (e.getSource() instanceof KeyEvent) {
                KeyEvent keyEvent = (KeyEvent) e.getSource();
                if (keyEvent.getKeyCode() == KeyEvent.VK_SPACE) {
                    resetGame();
                }
            }
        }
        repaint();
    }

    public class mykeyadapter extends KeyAdapter{
        @Override
        public void keyPressed(KeyEvent e){
            switch(e.getKeyCode()){
            case KeyEvent.VK_LEFT:
                if (direction!='R') {
                    direction = 'L';
                }
                break;
            case KeyEvent.VK_RIGHT:
                if (direction!='L') {
                    direction = 'R';
                }
                break;
            case KeyEvent.VK_UP:
                if (direction!='D') {
                    direction = 'U';
                }
                break;
            case KeyEvent.VK_DOWN:
                if (direction!='U') {
                    direction = 'D';
                }
                break;
            case KeyEvent.VK_SPACE:
                if (!running) {
                    resetGame();
                }
                break;
            }
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Snake Game");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(SCREEN_WIDTH, SCREEN_HEIGHT);
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);
        frame.add(new GamePanel());
        frame.setVisible(true);
    }
}             