import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

class Main {
    static Map<Integer, List<Integer>> indexA = new HashMap<>();
    static Map<Integer, List<Integer>> indexB = new HashMap<>();

    public static void main(String args[]) throws Exception {

        for (int i = 1; i <= 100; i++) {
            indexA.put(i, new ArrayList<>());
            indexB.put(i, new ArrayList<>());
        }

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            int key = sc.nextInt();
            indexA.get(key).add(i);
        }
        int M = sc.nextInt();
        for (int i = 0; i < M; i++) {
            int key = sc.nextInt();
            indexB.get(key).add(i);
        }

        List<Integer> Ans = new ArrayList<>();

        int aLastIndex = -1, bLastIndex = -1;
        int number = 100, i = 0, j = 0;
        while (number > 0) {
            List<Integer> aIndexes = indexA.get(number);
            List<Integer> bIndexes = indexB.get(number);

            if (i == aIndexes.size() || j == bIndexes.size()) {
                number--;
                i = 0;
                j = 0;
                continue;
            }

            int aIndex = aIndexes.get(i);
            int bIndex = bIndexes.get(j);
            if (aIndex > aLastIndex && bIndex > bLastIndex) {
                Ans.add(number);
                aLastIndex = aIndex;
                bLastIndex = bIndex;
                i++;
                j++;
            } else if (aIndex < aLastIndex) {
                i++;
            } else {
                j++;
            }
        }

        System.out.println(Ans.size());
        System.out.println(Ans.stream().map(String::valueOf).collect(Collectors.joining(" ")));

        sc.close();
    }
}