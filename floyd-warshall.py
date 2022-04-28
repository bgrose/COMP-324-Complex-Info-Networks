dist = [[0,1,1,7,7,7,7],
        [1,0,1,1,7,7,7],
        [1,1,0,1,7,7,7],
        [7,1,1,0,1,7,7],
        [7,7,7,1,0,1,7],
        [7,7,7,7,1,0,1],
        [7,7,7,7,7,1,0]]
for k in range(7):
      print("intermediate vertex",k+1)
      for u in range(7):
            for v in range(7):
                  if (dist[u][v] > (dist[u][k] + dist[k][v])):
                        dist[u][v] = dist[u][k] + dist[k][v]
                        print("Changed  dist[",u+1,",",v+1,"]  to ",dist[u][v])
      for x in range(7):
            for y in range(7):
                  print(dist[x][y],end=" ")
            print()     
      print()
      input()