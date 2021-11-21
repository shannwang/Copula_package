# Copula density

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&r=r&type=6e&v=0.0.3&x2=0)](https://github.com/Naereen/StrapDown.js)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)

## Contributors
 - Shanshan Wang [GitHub](https://github.com/shannwang)
 - Juan Henao [GitHub](https://github.com/juanhenao21)
 
## Motivation of the project
By carrying out a simple python package with the function of copula density, this project aims to let contributors be familar with the process of collaboratively developing and managaing scientific packages with open source. Such practice will be of benefit to contributors' future projects. 

## Package info

**Package name**: copuladensity-pkg<br/>
**Version**: 0.0.3<br/>
**License**: MIT License<br/>
**Description**: this package is used to calcualte and draw copula density of two correlated time series.<br/>
**Python requires** version >=3.6<br/>
**Webpage**: https://pypi.org/project/copuladensity-pkg/

### Install
pip install copuladensity-pkg

### Uninstall
pip uninstall copuladensity-pkg

### Prerequisites
For `Python`, all the packages needed to run the analysis are in the `requirements.txt` file.

### How to use
After installing this package, import the functions to your python program by
~~~
from copula_package import copula_density
~~~

### An example

~~~
from copula_package import copula_density 
~~~

Sample two time series x and y
~~~
mean = (1, 2)
cov = [[1, 1], [1, 2]]
n=10000
z=copula_density.sampling_two_corr_time_series(mean,cov,n) 
x=z.x
y=z.y
~~~

Draw histogram of x and y
~~~
n_bins=50
label_x='x'
label_y='y'
copula_density.draw_histogram(x,n_bins,label_x)
copula_density.draw_histogram(y,n_bins,label_y)
~~~
*The expected figures*<br/>
<img src="https://github.com/shannwang/Copula_package/blob/main/images/hist_of_x.png?raw=true" height="300"> <img src="https://github.com/shannwang/Copula_package/blob/main/images/hist_of_y.png?raw=true" height="300">

Draw joint distribution of x and y
~~~
copula_density.draw_joint_distribution(z,label_x,label_y)
~~~
*The expected figure*<br/>
<img src="https://github.com/shannwang/Copula_package/blob/main/images/joint_distribution.png?raw=true" width="600"> 

Calculate quantiles
~~~
qx=copula_density.qrank_data(x)
qy=copula_density.qrank_data(y)
~~~

Calcualte copula density
~~~
nx=20
ny=20
cop_den=copula_density.calc_copula_density(qx,qy,nx,ny)
~~~

Draw copula density with heatmap
~~~
label_qx='Quantile(x)'
label_qy='Quantitle(y)'
copula_density.draw_heatmap(cop_den,label_qx,label_qy)
~~~
*The expected figure*<br/>
<img src="https://github.com/shannwang/Copula_package/blob/main/images/heatmap_cop_den.png?raw=true" width="600"> 

Draw copula density with surface
~~~ 
copula_density.draw_surface(cop_den,label_qx,label_qy)
~~~
*The expected figure*<br/>
<img src="https://github.com/shannwang/Copula_package/blob/main/images/surface_cop_den.png?raw=true" width="600"> 

Draw copula density in 3-demensional bars
~~~ 
copula_density.draw_bar3d(cop_den,label_qx,label_qy)
~~~
*The expected figure*<br/>
<img src="https://github.com/shannwang/Copula_package/blob/main/images/bar3d_cop_den.png?raw=true" width="600"> 


## References


* Shanshan Wang and Thomas Guhr. Local Fluctuations of the Signed Traded Volumes and the Dependencies of Demands: A Copula Analysis, [J. Stat. Mech. 2018, 033407 (2018)](http://stacks.iop.org/1742-5468/2018/i=3/a=033407), preprint: [arXiv:1706.09240](http://arxiv.org/abs/1706.09240).

* Marcel Wollschläger and Rudi Schäfer. Impact of nonstationarity on estimating and modeling empirical copulas of daily stock returns, [Journal of Risk 19, 1-23 (2016)](https://doi.org/10.21314/JOR.2016.342), preprint: [arXiv:1506.08054](http://arxiv.org/abs/1506.08054)

* M.C. Münnix and R. Schäfer. A Copula Approach on the Dynamics of Statistical Dependencies in the US Stock Market, [Physica A 390, 4251 (2011)](http://dx.doi.org/10.1016/j.physa.2011.06.032) , preprint: [arXiv:1102.1099](http://arxiv.org/abs/1102.1099)

## Acknowledgments

Research Group Guhr - [Website](http://www.theo.physik.uni-duisburg-essen.de/tp/ags/guhr_dir/index.html)
