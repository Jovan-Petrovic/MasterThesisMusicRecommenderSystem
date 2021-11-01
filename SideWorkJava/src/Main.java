import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        // path to fma_small dataset (actual audio files dataset)
        File root = new File("C:\\Users\\proudsourceit\\Desktop\\Datasets\\fma_small");
        List<Integer> list = new ArrayList<>();
        for (File f : root.listFiles()) {
            try {
                for (File f1 : f.listFiles()) {
                    System.out.println(Integer.parseInt(f1.getName().substring(0, 6)));
                    list.add(Integer.parseInt(f1.getName().substring(0, 6)));
                }
            } catch (NullPointerException e) {

            }
        }
        // path to place you want to write track ids from fma_small dataset
        File newFile = new File("C:\\Users\\proudsourceit\\IdeaProjects\\jovan-master-side-work\\indexes.txt");
        FileWriter writer = new FileWriter(newFile);
        for (int i : list) {
            writer.write(i + "\n");
        }
        writer.close();
    }
}
