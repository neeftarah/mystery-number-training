import java.util.Scanner;
import java.io.*;
import java.util.ArrayList;


public class MysteryNumber
{
    public static void main(String[] args) throws InterruptedException
    {
        BufferedReader br;
        Scanner sc             = new Scanner(System.in);
        Integer nb_files       = 0;
        ArrayList<String> lang = new ArrayList<String>();
        File[] langFiles       = new File[0];

        // 1. Show splash sreen for 3s
        clearConsole();
        System.out.println("/******************************************************************************\\");
        System.out.println("|                                  WELCOME TO                                  |");
        System.out.println("|                                MYSTERY NUMBER                                |");
        System.out.println("\\******************************************************************************/");
        Thread.sleep(1000);

        // 2. Select a langage
        clearConsole();
        File file = new File("../locales/");
        try {
            Integer i = 0;
            nb_files = file.listFiles().length;
            langFiles = new File[nb_files];
            for(File nom : file.listFiles()){
                if(nom.isFile() && nom.getName().endsWith(".txt")) {
                    i++;
                    langFiles[i - 1] = nom;
                    try {
                        Scanner scfile = new Scanner(nom);
                        System.out.println(i + ". " + scfile.nextLine());
                    } catch (FileNotFoundException e) {}
                }
            }
        } catch (NullPointerException e) {}

        try {
            Scanner scanner = new Scanner(langFiles[sc.nextInt() - 1]);
            while (scanner.hasNextLine()) {
                lang.add(scanner.nextLine());
            }
            scanner.close();
        } catch (FileNotFoundException e) {}

        // 3. Select game mode
        clearConsole();
        System.out.println(lang.get(1));
        System.out.println("1. " + lang.get(2));
        System.out.println("2. " + lang.get(3));
        Integer mode = sc.nextInt();

        // 4. Players name...


        // 5. Select a difficulty...


        // Ask for the maximum number for the personalized difficulty


        // Set standard maximum number

        // Start game loop


    }

    public final static void clearConsole()
    {
    	final String ANSI_CLS = "\u001b[2J";
        final String ANSI_HOME = "\u001b[H";
        System.out.print(ANSI_CLS + ANSI_HOME);
        System.out.flush();
    }
}
