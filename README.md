### Image Segmentation Tool 
<p align = "justify">
In this project,  Flask framework was used to deploy an image segmentation tool that divides an image to a number of components. 
</p>

#### 
<p align = "center">
	<img src = "https://github.com/rojinnew/image_segmentation/blob/master/segments.png">
</p>

#### Kmeans 
In this work, all similar points were clustered together and their values were substitued with the mean values which were calculated based on Kmeans clustering.
<p>
The objective function for Kmeans clustering could be written as:
</p>
<p align = "center">
	<img src = "https://github.com/rojinnew/image_segmentation/blob/master/f1.png" width = 400>
</p>
<p>
x<sub>ij</sub> are rgb values.
</p>
r<sub>ij</sub> in {0, 1} assigned as 1 ,if only sample i assigned to cluster j. Otherwise it is 0.  At each iteration, in the first step we keep the cluster centers fixed and assign each data point to the closest cluster center. This assignment could be written as:
<p align = "center">
	<img src = "https://github.com/rojinnew/image_segmentation/blob/master/f2.png" width =600>
</p>
We can form clusters S<sub>1</sub> ,..., S<sub>k</sub> using the value assigned to r<sub>ij</sub>.
In the second step we keep r<sub>ij fixed and we minimize the objective function with respect to <img src="https://render.githubusercontent.com/render/math?math=\mu_k".
<p align = "center">
	<img src = "https://github.com/rojinnew/image_segmentation/blob/master/f3.png" width=500>
</p>
As long as algorithm does not converge (algorithm converges when assignment not change or maximum iteration reached), in both step, we minimized the J.


You can access the image segmentation tool using the following link:
<p align = "left">
https://colorclustering.herokuapp.com/
</p>
 
#### Running 
You can install the required libraries listed in requirements.txt and start up the server in that src directory using the following command: 
 
python app.py 
 
http://localhost:5000/
