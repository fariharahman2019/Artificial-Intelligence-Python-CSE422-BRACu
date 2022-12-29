import java.io.*;
import java.util.*;

public class Level4 {
    static int graph[][];
    static int v;
    static String color[];
    static int d[];
    static int f[];
    static int p[];
    static int time=0;
    
    public static void main(String args[]){
        try{
            String str;
            FileReader fr = new FileReader("C:\\Users\\mahad\\Desktop\\Level4.txt");
            BufferedReader obj = new BufferedReader(fr);
            str = obj.readLine();
            v = Integer.parseInt(str);
            graph = new int[v][v];
            str = obj.readLine();
            int total_edges=Integer.parseInt(str);
            for(int i=0;i<total_edges;i++){
                str = obj.readLine();
                StringTokenizer st = new StringTokenizer(str," ");
                int token1 = Integer.parseInt(st.nextToken());
                int token2 = Integer.parseInt(st.nextToken());
                graph [token1][token2] = 1; 
            }
            dfs();
            for(int i=0;i<v;i++){
                System.out.println("u: "+i+" d[u]: "+d[i]+"  f[u]: "+f[i]+" p[u]: "+p[i]);
            }
        }
        catch(IOException e){
            System.out.println("File not found");
        }
    }
    
    static void dfs(){
        color=new String[v];
        d = new int[v];
        f=new int[v];
        p= new int[v];
        for(int i=0;i<v;i++){
            color[i]="White";
            p[i]=-1;
        }
        for(int i=0;i<v;i++){
            if(color[i]=="White"){
                dfs_visit(i);
            }
        }
    }
    
    static void dfs_visit(int u){
        color[u]="Gray";
        time = time + 1;
        d[u]=time;
        for(int j=0;j<v;j++){
            if(graph[u][j]==1 && color[j]=="White"){
                p[j]=u;
                dfs_visit(j);
            }
        }
        color[u]="Black";
        time=time+1;
        f[u]=time;
    }
}