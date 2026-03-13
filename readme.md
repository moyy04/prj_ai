Ce projet modélise et résout les problèmes classiques à l’aide du solveur Talos StateGraph.
Chaque problème est décrit dans un fichier XML contenant les variables d’état, l’état initial, l’état final et la table des transitions valides.

Problèmes :
1. Loup – Chèvre – Salade : traverser une rivière sans que le loup mange la chèvre ou la chèvre la salade.
2. Die Hard (seaux d’eau) : mesurer exactement 4 litres avec des seaux de 5L et 3L.
3. Problème des wagons : inverser la position de deux wagons à l’aide d’une locomotive et de voies de garage.

Exécution : 
```bash
java -cp talosExamples-0.4.1-SNAPSHOT-jar-with-dependencies.jar StateGraph -n N -print 1 -crossingRiver true -file fichier.xml