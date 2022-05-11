import scvelo as scv
import matplotlib.pyplot as plt
import numpy as np

def recover_dynamics(data, var_names, max_iter = 100):
    return scv.tl.recover_dynamics(data, var_names=var_names, max_iter=max_iter)

def plot_genes(data, basis):
    scv.pl.scatter(data, basis=basis, vkey='dynamics', fontsize=18)

def plot_contour(data, var_name, max_iter, x, y, c, n):
    dm = recover_dynamics(data, var_name, max_iter=max_iter)
    dm.plot_profile_contour(x_sight=x, y_sight=y, contour_levels=c, num=n)
    

def plot_validation_likelihood(dentategyrus):
    top_genes = dentategyrus.var.sort_values('fit_likelihood', ascending=False).index
    rnd_genes = np.random.choice(dentategyrus.var_names, size=dentategyrus.n_vars)
    full_graph = dentategyrus.uns['dynamical_velocity_graph'].A
    adj = full_graph / full_graph > 0
    n_genes = np.array([10, 30, 300, 500, 800, 1000])
    rhos = []
    rhos_med = []
    for n in n_genes:
        if n == 0: 
            rhos_med.extend([0])
        else:
            idx = dentategyrus.var_names.isin(top_genes[:n])

            vgraph = scv.VelocityGraph(dentategyrus[:, idx], vkey='dynamical_velocity') 
            vgraph.compute_cosines()

            rho = scv.utils.vcorrcoef(full_graph * adj, vgraph.graph.A * adj)

            rhos.extend([rho])
            rhos_med.extend([np.nanmedian(rho)])

    rhos = np.array(rhos)
    rhos_med = np.array(rhos_med)

    ax = scv.pl.scatter(x=n_genes, y=rhos_med, size=1000, show=False, ylim=[.75, 1.04], fontsize=24)
    ax.plot(n_genes, rhos_med, color='grey', linewidth=5)
    #ax.set_yticklabels([.8, .9, .95, 1])