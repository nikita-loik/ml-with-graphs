print(f"\t===Poetry Env Test===")
import sys
import scipy as sp
import numpy as np
import networkx as nx
import pandas as pd
import matplotlib
print(
    f"\n\tSystem Version {sys.version}"
    f"\n\tSciPy {sp.version.version}"
    f"\n\tNumPy {np.version.version}"
    f"\n\tNetworkX {nx.__version__}"
    f"\n\tPandas {pd.__version__}"
    f"\n\tMatplotlib {matplotlib.__version__}"
    )
import torch
print(
    f"\n\tPyTorch {torch.__version__}"
    f"\n\tCUDA {torch.version.cuda}")
import torch_geometric
print(f"\tPyG {torch_geometric.__version__}")
import deepsnap
print(f"\n\tDeepSNAP {deepsnap.__version__}")
import torch_scatter
import torch_sparse
import torch_cluster
import torch_spline_conv
print(
    f"\n\tTorch Scatter {torch_scatter.__version__}"
    f"\n\tTorch Sparse {torch_sparse.__version__}"
    f"\n\tTorch Cluster {torch_cluster.__version__}"
    f"\n\tTorch-Spline-Conv {torch_spline_conv.__version__}"
    )
print(f"\t=====================")
