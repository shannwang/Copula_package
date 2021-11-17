# Copula Packages

### Package info
Package name: copula_density-pkg
Version: 0.0.1
Author: Shanshan Wang
Author email: shanshan.wang@uni-due.de
Description: this package is used to calcualte and draw copula density of two correlated time series.
Autho


**Python requires** version >=3.6

### Install
pip install copula_density-pkg

### Uninstall
pip uninstall copula_density-pkg

### How to use
from copula_package import copula_density

### Functions


<ul>
    <li> <strong>copula_density.sampling_two_corr_time_series(mean,cov,n)</strong> <br/>
        function: sample two correlated time series<br/>
        mean: a list of two mean values for two time series, respectively, e.g., mean = (1, 2)<br/>
        cov: a 2-d array of diagonal covariances between two time series, e.g., cov = [[1, 1], [1, 2]]<br/>
        n: the length of each time series<br/>
        return x, y, z <br/>
        x: a list of time series<br/>
        y: a list of time series<br/>
        z: a pandas dataframe for x and y<br> <br/>
    </li>
    <li> <strong>copula_density.draw_histogram(x,n_bins,label_x)</strong><br/>
        function: draw historgram of a time series, where the hight of histogram shows the probability density<br/>
        x: a list of time series<br/>
        n_bins: the number of bins in the histogram<br/>
        label_x: a string for the label of x axis in the figure<br/>
        return: none <br/><br/>
    </li>
    <li> <strong>copula_density.draw_joint_distribution(z,label_x,label_y)</strong><br/>
        function: draw joint distribution of two time series
        z: a pandas dataframe with two columns, where each column contains a time series<br/>
        label_x: a string for the label of x axis in the figure<br/>
        label_y: a string for the label of y axis in the figure<br/>
        return: none <br/><br/>
    </li>
    <li> <strong>copula_density.qrank_data(x)</strong><br/>
        function: calculate the quantile of ranking data x<br/>
        x: a list of time series<br/>
        return: qx <br/>
        qx: a list of quantiles <br/><br/>
    </li>
    <li> <strong>copula_density.calc_copula_density(qx,qy,nx,ny)</strong><br/>
        function: calculate copula density of two time series<br/>
        qx: a list of quantiles <br/>
        qy: a list of quantiles <br/>
        nx: the number of bins for qx <br/>
        nx: the number of bins for qy <br/>
        return: cop_den <br>
        cop_den: a $nx\times ny$ 2-dimentional array of copula densities<br/><br/>
    </li>
    <li> <strong>copula_density.draw_heatmap(matrix,label_x,label_y)</strong><br/>
        function: draw heatmap for copula densities<br/>
        matrix: 2-dimensional array of copula densities<br/>
        label_x: a string for the label of x axis in the figure<br/>
        label_y: a string for the label of y axis in the figure<br/>
        return: none <br/><br/>
    </li>
    <li> <strong>copula_density.draw_surface(matrix,label_x,label_y)</strong><br/>
        function: draw surface for copula densities<br/>
        matrix: 2-dimensional array of copula densities<br/>
        label_x: a string for the label of x axis in the figure<br/>
        label_y: a string for the label of y axis in the figure<br/>
        return: none <br/><br/>
    </li>
    <li> <strong>copula_density.draw_bar3d(matrix,label_x,label_y)</strong><br/>
        function: draw 3-dimensional bars for copula densities<br/>
        matrix: 2-dimensional array of copula densities<br/>
        label_x: a string for the label of x axis in the figure<br/>
        label_y: a string for the label of y axis in the figure<br/>
        return: none <br/><br/>
    </li>
</ul>
  


