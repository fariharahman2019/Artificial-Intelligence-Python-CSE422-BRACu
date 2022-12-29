import java.io.*;
import java.util.*;

public class Level3 {
    static int v; //vertices
    static int graph[][];
    static int lina_pos=0;
    static int[] a;
    static int participants=0;
  
    public static void main(String[] args){
        Graph();
        Arrays.sort(a);
        int start=a[a.length-1];
        bfs(graph,start,lina_pos);
    }
  
    public static void Graph(){
        try{
            String str;
            FileReader fr = new FileReader("C:\\Users\\mahad\\Desktop\\Level3.txt");
            BufferedReader obj = new BufferedReader(fr);
            str = obj.readLine();
            v = Integer.parseInt(str);
            graph = new int[v][v];
            str = obj.readLine();
            int edge = Integer.parseInt(str);
            for (int i=0;i<edge;i++){
                str=obj.readLine();
                StringTokenizer st = new StringTokenizer(str, " ");
                int token1 = Integer.parseInt(st.nextToken());
                int token2 = Integer.parseInt(st.nextToken());
                graph[token1][token2] = 1;
            }
            String start = obj.readLine();
            lina_pos = Integer.parseInt(start);
            String start0=obj.readLine();
            participants=Integer.parseInt(start0);
            a=new int[participants];
            for (int i=0;i<participants;i++){
                String start1=obj.readLine();
                a[i]=Integer.parseInt(start1);
            }
        }
        catch (IOException e){
            System.out.println("WRONG");
        }
    }
  
    public static void bfs (int [][] a,int start,int end){
        String color[]=new String[v+1];
        int parent[]=new int[v+1];
        int distance[]=new int[v+1];
        Queue<Integer> q=new LinkedList<>();
        for (int i=0;i<v;i++){
            color[i]="White";
            distance[i]=9999999;
            parent[i]=-1;
        }
        color[start]="Gray";
        distance[start]=0;
        parent[start]=-1;
        q.add(start);
        while (!q.isEmpty()){
            int u=q.remove();
            for (int i=0; i<v; i++){
                if((color[i].equals("White")) && (graph[u][i]==1)){
                    color[i]="Gray";
                    distance[i]=distance[u]+1;
                    parent[i]=u;
                    q.add(i);
                }
            }
            color[u]="Black";
        }
        printBfs(distance,parent,end);
    }
  
    public static void printBfs(int [] distance,int [] parent,int end){
        for (int i=0;i<v;i++){
            if(i==end){
                System.out.println("Minimum Number of Moves ==> " + distance[i]+".");
            }
        }
    }
}