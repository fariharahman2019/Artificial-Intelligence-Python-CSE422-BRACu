import java.io.*;
import java.util.*;

public class Level1 {
    static int lina_pos=0;
    
    public static void main(String args[]){
        try{
            String str;
            FileReader fr = new FileReader("C:\\Users\\mahad\\Desktop\\Level1.txt");
            BufferedReader obj = new BufferedReader(fr);
            str = obj.readLine();
            int v = Integer.parseInt(str);
            int graph[][] = new int[v][v];
            str = obj.readLine();
            int total_edges=Integer.parseInt(str);
            for(int i=0;i<total_edges;i++){
                str = obj.readLine();
                StringTokenizer st = new StringTokenizer(str," ");
                int token1 = Integer.parseInt(st.nextToken());
                int token2 = Integer.parseInt(st.nextToken());
                graph [token1][token2] = 1; 
            }
            str = obj.readLine();
            lina_pos=Integer.parseInt(str);
            
            bfs(graph,0,lina_pos);
        }
        catch(IOException e){
            System.out.println("File not found");
        }

    }
    
    public static void bfs(int a[][],int s,int end){
        String color[]=new String[a.length];
        int parent[]=new int[a.length];
        int distance[]=new int[a.length];
        Queue<Integer> list=new LinkedList<>();
        for(int i=0;i<a.length;i++){
            color[i]="White";
            distance[i]=9999999;
            parent[i]=-1;
        }
        color[s]="Gray";
        distance[s]=0;
        parent[s]=-1;
        list.add(s);
        while(!list.isEmpty()){
            int u=list.poll();
            
            for(int j=1;j<a.length;j++){
                if(a[u][j]==1 && color[j].equals("White")){
                    color[j]="Gray";
                    distance[j]=distance[u]+1;
                    parent[j]=u;
                    list.add(j);
                }
            }
            color[u]="Black";
        }
        print(parent,distance,lina_pos);
        
    }
    
    private static void print(int p[],int d[],int l){
        System.out.println("Minimum Number of moves : "+d[l]);
    }
}
