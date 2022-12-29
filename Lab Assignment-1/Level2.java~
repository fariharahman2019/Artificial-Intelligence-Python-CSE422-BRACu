import java.io.*;
import java.util.*;


public class Level2 {
    static int lina_pos=0;
    static int nora_pos=0;
    static int lara_pos=0;
    
    public static void main(String args[]){
        try{
            String str;
            FileReader fr = new FileReader("C:\\Users\\mahad\\Desktop\\Level2.txt");
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
                graph [token2][token1] = 1;
            }
            str = obj.readLine();
            lina_pos=Integer.parseInt(str);
            str = obj.readLine();
            nora_pos=Integer.parseInt(str);
            str = obj.readLine();
            lara_pos=Integer.parseInt(str);
            
            int m=bfs(graph,nora_pos,lina_pos);
            int n=bfs(graph,lara_pos,lina_pos);
            
            if(m<n){
                System.out.println("Nora");
            }else{
                System.out.println("Lara");
            }
        }
        catch(IOException e){
            System.out.println("File not found");
        }

    }
    
    public static int bfs(int a[][],int s,int end){
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
            
            for(int j=0;j<a.length;j++){
                if(a[u][j]==1 && color[j].equals("White")){
                    color[j]="Gray";
                    distance[j]=distance[u]+1;
                    parent[j]=u;
                    list.add(j);
                }
            }
            color[u]="Black";
        }
        return(distance[lina_pos]);
        
    }
}
