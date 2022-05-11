import scvelo as scv
import numpy as np
import pytest

def test_high_var_subset():
    adata = scv.datasets.simulation(random_seed=1, n_vars=8)
    bdata = adata.copy()
    scv.pp.filter_and_normalize(adata, n_top_genes=5, subset_highly_variable=True)
    scv.pp.filter_and_normalize(bdata, n_top_genes=5, subset_highly_variable=False)
    scv.pp.pca(adata)
    scv.pp.pca(bdata)
    scv.pp.moments(adata, use_rep="pca")
    scv.pp.moments(bdata, use_rep="pca")
    scv.tl.velocity_graph(adata)
    scv.tl.velocity_graph(bdata)
    bdata._inplace_subset_var(bdata.var["highly_variable"])
    assert np.allclose(adata.layers["Ms"][0], bdata.layers["Ms"][0])
    assert np.allclose(adata.layers["velocity"][0], bdata.layers["velocity"][0])
    assert np.allclose(
        adata.uns["velocity_graph"].data[:5], bdata.uns["velocity_graph"].data[:5])
    

 
   
