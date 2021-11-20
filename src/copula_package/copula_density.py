'''Copulas package main module

..moduleauthor:: Shanshan Wang
..Email: shanshan.wang@uni-due.de
..moduleauthor:: Juan Camilo Henao Londono
..Email: juan.henao-londono@uni-due.de
'''

# ----------------------------------------------------------------------------
# Modules

import numpy as np  # type: ignore
import pandas as pd  # type: ignore

import functions  # type: ignore

# ----------------------------------------------------------------------------


def main() -> None:
    """Main function of the package.

    Returns:
        None
    """

    # Compute correlated time series
    # input parameters
    mean: np.ndarray = np.array([1, 2])
    # diagonal covariance
    cov: np.ndarray = np.array([[1, 1], [1, 2]])
    # length time series
    n: int = 10000
    time_series_df: pd.DataFrame = \
        functions.sampling_two_corr_time_series(mean, cov, n)

    n_bins=50
    # nx=30 # number of bins for qx
    # ny=30 # number of bins for qy
    # label_x='x'
    # label_y='y'
    # # calcualte and plot
    # draw_histogram(x,n_bins,label_x)
    # draw_histogram(y,n_bins,label_y)
    # draw_joint_distribution(z,label_x,label_y)
    # qx=qrank_data(x)
    # qy=qrank_data(y)
    # cop_den=calc_copula_density(qx,qy,nx,ny)
    # # draw empirical copula density in three ways
    # label_qx='Quantile(x)'
    # label_qy='Quantile(y)'
    # draw_heatmap(cop_den,label_qx,label_qy)
    # draw_surface(cop_den,label_qx,label_qy)
    # draw_bar3d(cop_den,label_qx,label_qy)
    # # save data
    # df_cop_den= pd.DataFrame(cop_den)
    # df_cop_den.to_csv('cop_den.csv', index=False, header=False)

# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()