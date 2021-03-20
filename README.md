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
<p align = "center" width = "200px">
	<img src = "https://github.com/rojinnew/image_segmentation/blob/master/kmeans.png">
</p>

<p>
To show this we show in both steps of K-means we decrease the cost.
The objective function given could be written as:
</p>

<p>
<img src="https://render.githubusercontent.com/render/math?math=\textrm{minimum}_{\mu_1,...,\mu_k,S_1,...,S_k}\sum_{j=1}^k\sum_{i=1}^n r_{ij}\|x_i-\mu_j\|_2^2.">
</p>
<p>
<img src="https://render.githubusercontent.com/render/math?math=r_{ij} \in \{0,1\}.r_{ij} \text{assigned as 1 ,if only sample i assigned to cluster j. Otherwise it is 0.}">
</p>

At each iteration, in the first step we keep the cluster centers fixed and assign each data point to the closest cluster center. This assignment could be written as:

<img src="https://render.githubusercontent.com/render/math?math= r_{ik} = \begin{cases} \end{cases}">

<img src="https://render.githubusercontent.com/render/math?math= r_{ik} = \begin{cases} 1, &\text{ if }  k = \argmin_{r_{ij} } \| x_i - \mu_j \|^2   \quad\quad : \forall i \in {1 \cdots n} , j \in {1 \cdots k} \\ 0,              & \text{otherwise} \end{cases}">





You can access the image segmentation tool using the following link:
<p align = "left">
https://colorclustering.herokuapp.com/
</p>
 
#### Running 
You can install the required libraries listed in requirements.txt and start up the server in that src directory using the following command: 
 
python app.py 
 
http://localhost:5000/
