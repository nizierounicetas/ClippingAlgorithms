# ClippingAlgorithms
![image](https://user-images.githubusercontent.com/79499100/236895971-3447e2a0-7e8c-4496-b539-24c67f46d804.png)
![image](https://user-images.githubusercontent.com/79499100/236895297-06818bab-8838-430b-8114-f080c358ec80.png)

A graphical application that uses matplotlib and tkinter to demonstrate the work of the implemented cutoff algorithms:
- <b>Liang Barskiy</b> for segments;
    <br>To apply the algorithm you need to create a txt file with the next structure:
    ```
    [number of segments]
    [pairs of (x, y) coordinates of the beggining and the end of the semgents]
    [left-bottom and right-top (x, y) coordinates of the of the cutting off rectangle]
    ```
- <b>Sutherland Hodgman</b> for polygons;
  <br>To apply the algorithm you need to create a txt file with the next structure:
    ```
    [number of polygon vertexes]
    [pairs of (x, y) coordinates of the vertexes]
    [[number of clipping polygon vertexes]
    [pairs of (x, y) coordinates of the vertexes]
    ```
Examples of files are in <b>./tests/</b>.
