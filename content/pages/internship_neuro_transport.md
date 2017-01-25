title: internship-multitask-transport
sortorder: 8
category: internship

### Project

Multi-task regression consists in inferring jointly multiple regression
models for different prediction tasks. The intuition is that a single joint
estimation outperforms several estimations carried out independently if tasks share some
similarities, which happens typically when different subsets of features are useful for all regression tasks. This intuition led to several seminal contributions in the machine learning literature,
e.g. multi-task Lasso or Multi-task Feature
Learning (MTFL) (Argyriou et al. 2006, Obozinski et al. 2006)

However, this assumption of common features between all tasks can be too
restrictive. For instance, in the context of functional brain imaging, where features
map to brain regions, the multitask assumption implies that the exact same locations
are active for all human brains. This assumption is clearly not realistic
(Gramfort et. al. 2015).

Various works have attempted to tackle the problem with more or less
ad-hoc methods (Kozunov et. al. 2015). The idea of this research project will be to develop a new approach to multi-task regression using regularization terms that will be defined using optimal transport theory, taking advantage of recent computational progress in the numerical computation of Wasserstein distances and their derivatives (Cuturi 2013, Gramfort et. al. 2015, Cuturi et al. 2016).

We will carry out validation experiments and adequate benchmarking starting first with simulations.
We will then work with the open dataset from (Wakeman et al. 2015)
and start from a [preliminary analysis](http://mne-tools.github.io/mne-biomag-group-demo/).

**Required skills:** The successful candidate will have background knowledge
in machine learning and optimization at the master level (M2), as well as
interest in application of data science. Knowledge of scientific computing in Python (Numpy, Scipy)
is encouraged, since we will rely on the [MNE](http://martinos.org/MNE) for data analysis (Gramfort et al. 2014).

### Location and supervision

Internship will take place at INRIA Saclay (Turing building) and ENSAE ParisTech
and will be supervised my [Marco Cuturi](http://marcocuturi.net/) and myself.

### To apply

Send me an [email](contact.html)

### Bibliography

[1] Andreas Argyriou, Theodoros Evgeniou, and Massimiliano Pontil. Multi-task feature learning. In P. B. Schölkopf, J. C. Platt, and T. Hoffman, editors, Advances in Neural Information Processing Systems 19, pages 41–48. MIT Press, 2007.

[2] Marco Cuturi. Sinkhorn distances: Lightspeed computation of optimal transport. In Advances in Neural Information Processing Systems 26, pages 2292– 2300, 2013.

[3] Marco Cuturi and Gabriel Peyré. A smoothed dual approach for variational wasserstein problems. SIAM Journal on Imaging Sciences, 9(1):320–343, 2016.

[4] Alexandre Gramfort, Martin Luessi, Eric Larson, Denis A. Engemann, Daniel Strohmeier, Christian Brodbeck, Lauri Parkkonen, and Matti S. Hämäläinen. MNE software for processing MEG and EEG data. NeuroImage, 86(0):446 – 460, 2014.

[5] Alexandre Gramfort, Gabriel Peyré, and Marco Cuturi. Fast optimal transport averaging of neuroimaging data. In Proc. IPMI 2015, July 2015.

[6] Vladimir V. Kozunov and Alexei Ossadtchi. GALA: group analysis leads to accuracy, a novel approach for solving the inverse problem in exploratory analysis of group meg recordings. Frontiers in Neuroscience, 9:107, 2015.

[7] Guillaume Obozinski and Ben Taskar. Multi-task feature selection. In International Conference on Machine Learning (ICML 2006). Workshop of structural Knowledge Transfer for Machine Learning, 2006.

[8] Daniel Wakeman and Richard Henson. A multi-subject, multi-modal human neuroimaging dataset. Scientific Data, 2:150001 EP –, Jan 2015.