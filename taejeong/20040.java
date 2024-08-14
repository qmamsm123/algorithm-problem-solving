import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
  static int N, M;
  static int[] parent;

  public static void main(String[] args) throws Exception {
    System.setIn(new FileInputStream("./res/input.txt"));
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    parent = new int[N];
    initialize();

    int cycle = 0;
    for (int m = 1; m <= M; m++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int result = union(a, b);
      if (result == -1 && cycle == 0) {
        cycle = m;
      }
    }

    System.out.println(cycle);
  }

  static void initialize() {
    for (int i = 0; i < N; i++) {
      parent[i] = i;
    }
  }

  static int find(int here) {
    if (parent[here] == here) {
      return here;
    }
    return parent[here] = find(parent[here]);
  }

  static int union(int a, int b) {
    int rootA = find(a);
    int rootB = find(b);
    if (rootA == rootB) {
      return -1; // 사이클 형성
    }
    return parent[rootA] = rootB;
  }
}
