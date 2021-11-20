'''Copulas package functions module.

Functions to compute and draw copula density with two correlated time series.

..moduleauthor:: Shanshan Wang
..Email: shanshan.wang@uni-due.de
..moduleauthor:: Juan Camilo Henao Londono
..Email: juan.henao-londono@uni-due.de
'''

# ----------------------------------------------------------------------------
# Modules

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore
import scipy.stats as ss  # type: ignore

# ----------------------------------------------------------------------------


def sampling_two_corr_time_series(mean: np.ndarray,
                                  cov: np.ndarray,
                                  n: int) -> pd.DataFrame:
    """Compute two correlated time series.

    Args:
        mean (np.ndarray): one dimensional array with the mean values of the
        two time series (i.e. np.array([1, 2])).
        cov (np.ndarray): two dimensional array with the diagonal covariances
        (i.e. np.array([[1, 1], [1, 2]]))
        n (int): length of the time series.

    Returns:
        pd.DataFrame: two correlated times series.
    """

    # Obtain the values of the correlated time series
    val = np.random.multivariate_normal(mean,cov,n)

    return pd.DataFrame(val, columns=['x', 'y'])

# ----------------------------------------------------------------------------


def draw_histogram(x,n_bins,label_x):
    # histograms of the data
    fig, axes=plt.subplots(figsize=(7,4))
    sns.histplot(data=x, bins=n_bins,stat='density').set(title='probability density distribution', xlabel=label_x,ylabel='pdf')
    plt.savefig('hist_of_'+label_x+'.png',dpi=300, transparent=False, format='png', bbox_inches='tight')
    plt.close(fig)

def draw_joint_distribution(z,label_x,label_y):
    # joint distribution of x and y
    fig, axes=plt.subplots(figsize=(8,6))
    sns.jointplot(data=z, kind="scatter", x=label_x, y=label_y)
    plt.savefig('joint_distribution.png',dpi=300, transparent=False, format='png', bbox_inches='tight')
    plt.close(fig)

def qrank_data(x):
    # quantiles of ranks of variables x and y
    rx=ss.rankdata(x)
    qx=(rx-0.5)/len(x)
    return qx

def calc_copula_density(qx,qy,nx,ny):
    # calculate empirical copula density
    xmin=0
    xmax=1
    ymin=0
    ymax=1
    cop_dens=np.histogram2d(qx, qy, bins=(nx, ny), range=[[xmin, xmax], [ymin, ymax]],density=True)    # with density=True, normalize quantiles qx and qy
    return cop_dens[0]

def draw_heatmap(matrix,label_x,label_y):
    # draw a two dimensional array in a heatmap
    fig=plt.figure(figsize=(8,6))
    nx=ny=len(matrix)
    xticklist=range(0,nx,2)
    xticklabels=[format(xt/nx,'.2f') for xt in xticklist]
    yticklist=range(0,ny,2)
    yticklabels=[format(yt/ny,'.2f') for yt in yticklist]
    sns.heatmap(matrix,cmap='jet').set(title='copula density', xlabel=label_x, ylabel=label_y, xticks=xticklist,yticks=yticklist, xticklabels=xticklabels, yticklabels=yticklabels);
    plt.savefig('heatmap_cop_den.png',dpi=300, transparent=False, format='png', bbox_inches='tight')
    plt.close(fig)

def draw_surface(matrix,label_x,label_y):
    # draw the empirical copula density in a surface plot
    nx=ny=len(matrix)
    X, Y = np.meshgrid(range(nx), range(ny))
    fig = plt.figure(figsize=(12,8))
    ax = plt.axes(projection='3d')
    mycmap = plt.get_cmap('jet')
    surf1=ax.plot_surface(X, Y, matrix, cmap = mycmap)
    xticklist=range(0,nx,2)
    xticklabels=[format(xt/nx,'.2f') for xt in xticklist]
    yticklist=range(0,ny,2)
    yticklabels=[format(yt/ny,'.2f') for yt in yticklist]
    plt.xlabel('\n\n '+label_x)
    plt.ylabel('\n\n '+label_y)
    plt.xticks(xticklist,xticklabels,rotation=45)
    plt.yticks(yticklist,yticklabels,rotation=135)
    ax.set_zlabel('copula density')
    fig.colorbar(surf1, ax=ax, shrink=0.3, aspect=8)
    plt.savefig('surface_cop_den.png',dpi=300, transparent=False, format='png', bbox_inches='tight')
    plt.close(fig)

def draw_bar3d(matrix,label_x,label_y):
    # draw copula density in 3-dimensional bar chart
    # Construct arrays for the anchor positions of the nx*ny bars.
    nx=ny=len(matrix)
    xpos, ypos = np.meshgrid(range(nx), range(ny))
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0
    # Construct arrays with the dimensions for the nx*ny bars.
    dx = dy = 1 * np.ones_like(zpos)
    dz = matrix.ravel()
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(projection='3d')
    colors = plt.cm.jet(matrix.flatten()/float(matrix.max()))
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', color=colors)
    xticklist=range(0,nx,2)
    xticklabels=[format(xt/nx,'.2f') for xt in xticklist]
    yticklist=range(0,ny,2)
    yticklabels=[format(yt/ny,'.2f') for yt in yticklist]
    plt.xlabel('\n\n '+label_x)
    plt.ylabel('\n\n '+label_y)
    plt.xticks(xticklist,xticklabels,rotation=45)
    plt.yticks(yticklist,yticklabels,rotation=135)
    ax.set_zlabel('copula density')
    plt.savefig('bar3d_cop_den.png',dpi=300, transparent=False, format='png', bbox_inches='tight')
    plt.close(fig)


def main():
    pass


if __name__ == "__main__":
    main()