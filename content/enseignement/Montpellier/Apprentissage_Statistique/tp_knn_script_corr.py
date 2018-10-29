"""Created some day.

@authors:  salmon, gramfort, vernade
"""

from functools import partial  # useful for weighted distances
import numpy as np
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn import metrics
from scipy import stats
from sklearn import neighbors
from sklearn import datasets

# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from tp_knn_source import (rand_gauss, rand_bi_gauss, rand_tri_gauss,
                           rand_checkers, rand_clown, plot_2d, ErrorCurve,
                           frontiere_new, LOOCurve)


import seaborn as sns
from matplotlib import rc

plt.close('all')
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Computer Modern Roman']})
params = {'axes.labelsize': 12,
          'font.size': 16,
          'legend.fontsize': 16,
          'text.usetex': False,
          'figure.figsize': (8, 6)}
plt.rcParams.update(params)

sns.set_context("poster")
sns.set_palette("colorblind")
sns.set_style("white")
sns.axes_style()

############################################################################
#     Data Generation: example
############################################################################

# Q1
np.random.seed(42)  # fix seed globally

n = 100
mu = [1., 1.]
sigma = [1., 1.]
rand_gauss(n, mu, sigma)

n1 = 20
n2 = 20
mu1 = [1., 1.]
mu2 = [-1., -1.]
sigma1 = [0.9, 0.9]
sigma2 = [0.9, 0.9]
X1, y1 = rand_bi_gauss(n1, n2, mu1, mu2, sigma1, sigma2)

n1 = 50
n2 = 50
n3 = 50
mu1 = [1., 1.]
mu2 = [-1., -1.]
mu3 = [1., -1.]
sigma1 = [0.9, 0.9]
sigma2 = [0.9, 0.9]
sigma3 = [0.9, 0.9]
X2, y2 = rand_tri_gauss(n1, n2, n3, mu1, mu2, mu3, sigma1, sigma2, sigma3)

n1 = 50
n2 = 50
sigma1 = 1.
sigma2 = 5.
X3, y3 = rand_clown(n1, n2, sigma1, sigma2)

n1 = 150
n2 = 150
sigma = 0.1
X4, y4 = rand_checkers(n1, n2, sigma)

############################################################################
#     Displaying labeled data
############################################################################

plt.show()
plt.close("all")
plt.ion()
plt.figure(figsize=(15, 5))
plt.subplot(141)
plt.title('First data set')
plot_2d(X1, y1)

plt.subplot(142)
plt.title('Second data set')
plot_2d(X2, y2)

plt.subplot(143)
plt.title('Third data set')
plot_2d(X3, y3)

plt.subplot(144)
plt.title('Fourth data set')
plot_2d(X4, y4)

############################################################################
#     K-NN
############################################################################

# Q2 : Write your own implementation


class KNNClassifier(BaseEstimator, ClassifierMixin):
    """Home made KNN Classifier class."""

    def __init__(self, n_neighbors=1):

        self.n_neighbors = n_neighbors

    def fit(self, X, y):

        self.X_ = X
        self.y_ = y
        return self

    def predict(self, X):

        n_samples, n_features = X.shape
        # Compute all pairwise distances between X and self.X_ using e.g.:
        dist = metrics.pairwise.pairwise_distances(
            X, Y=self.X_, metric='euclidean', n_jobs=1)
        # Get indices to sort them
        idx_sort = np.argsort(dist, axis=1)
        # Get indices of neighbors
        idx_neighbors = idx_sort[:, :self.n_neighbors]
        # Get labels of neighbors
        y_neighbors = self.y_[idx_neighbors]

        # Find the predicted labels y for each entry in X
        # You can use the scipy.stats.mode function
        mode, _ = stats.mode(y_neighbors, axis=1)
        y_pred = np.asarray(mode.ravel(), dtype=np.intp)
        return y_pred

# Comparing your implementation with scikit-learn

# Focus on dataset 2
X_train = X2[::2]
Y_train = y2[::2].astype(int)
X_test = X2[1::2]
Y_test = y2[1::2].astype(int)

# n_neighbors = 1

n_neighbors = 1
knn = KNNClassifier(n_neighbors=n_neighbors)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)

sknn = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
sknn.fit(X_train, Y_train)
Y_pred_skl = sknn.predict(X_test)


print(np.allclose(Y_pred, Y_pred_skl))
# plt.ion()


# Q3 : test now all datasets
# From now on use the Scikit-Learn implementation

n_neighbors = 5  # the k in k-NN
knn = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)


# for data in [data1, data2, data3, data4]:
for X, y in [(X1, y1), (X2, y2), (X3, y3), (X4, y4)]:
    knn.fit(X, y)
    plt.figure()
    plot_2d(X, y)
    n_labels = np.unique(y).shape[0]
    frontiere_new(knn, X, y, w=None, step=50, alpha_choice=1,
                  n_labels=n_labels, n_neighbors=n_neighbors)

# Q4: Display the result when varying the value of K

plt.figure(figsize=(12, 8))
plt.subplot(3, 5, 3)
plot_2d(X_train, Y_train)
plt.xlabel('Samples')
ax = plt.gca()
ax.get_yaxis().set_ticks([])
ax.get_xaxis().set_ticks([])

for n_neighbors in range(1, 11):
    knn = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, Y_train)
    plt.subplot(3, 5, 5 + n_neighbors)

    n_labels = np.unique(y).shape[0]
    frontiere_new(knn, X, y, w=None, step=50, alpha_choice=1,
                  n_labels=n_labels, colorbar=False, samples=False,
                  n_neighbors=n_neighbors)
    plt.draw()  # update plot

plt.tight_layout()


# Q5 : Scores on train data
n_neighbors = 1
knn = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
knn.fit(X_train, Y_train)

print("Training error=" + str(1 - knn.score(X_train, Y_train)))
print("Test     error=" + str(1 - knn.score(X_test, Y_test)))


# Q6 : Scores on left out data

n1 = n2 = 200
sigma = 0.1
data4 = rand_checkers(2 * n1, 2 * n2, sigma)

X_train = X4[::2]
Y_train = y4[::2].astype(int)
X_test = X4[1::2]
Y_test = y4[1::2].astype(int)


plt.figure()
error_curve = ErrorCurve(k_range=range(1, 51))
error_curve.fit_curve(X_train, Y_train, X_test, Y_test)
error_curve.plot()
# error_curve = ErrorCurve(k_range=range(1, 50, 1))
collist = ['blue', 'grey', 'red', 'purple', 'orange', 'salmon', 'black',
           'fuchsia']


sigma = 0.1
plt.figure()
range_n_samples = [100, 500, 1000]
niter = len(range_n_samples)
for n in range(niter):
    n1 = n2 = range_n_samples[n]
    X_train, Y_train = rand_checkers(n1, n2, sigma)
    X_test, Y_test = rand_checkers(n1, n2, sigma)
    error_curve.fit_curve(X_train, Y_train, X_test, Y_test)
    error_curve.plot(color=collist[n % len(collist)], maketitle=False)

plt.legend(["training size : %d" % n for n in range_n_samples],
           loc='upper left')


plt.figure()
n_neighbors = 40
knn = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
knn.fit(X_train, Y_train)

frontiere_new(knn, X_train, Y_train, w=None, step=50, alpha_choice=1)


############################################################################
#     Digits data
############################################################################

# Q8 : test k-NN on digits dataset

# The digits dataset
digits = datasets.load_digits()

print(type(digits))
# A Bunch is a subclass of 'dict' (dictionary)
# help(dict)
# see also "http://docs.python.org/2/library/stdtypes.html#mapping-types-dict"

print(digits.keys())
print(digits.target[:50])
print(len(digits.data))
print(digits.data[0])
print(digits['data'][0])
print(digits['images'][0])
print(digits.data[0] == digits['data'][0])


plt.close()
plt.figure()
for idx, (img, lbl) in enumerate(list(zip(digits.images,
                                          digits.target))[10:20]):
    plt.subplot(2, 5, idx + 1)
    plt.axis('off')
    plt.imshow(img, cmap=plt.cm.gray_r, interpolation='None')
    plt.title('Training: %i' % lbl)

n_samples = len(digits.data)

X_digits_train = digits.data[:n_samples // 2]
Y_digits_train = digits.target[:n_samples // 2]
X_digits_test = digits.data[n_samples // 2:]
Y_digits_test = digits.target[n_samples // 2:]

plt.figure()
plt.hist(Y_digits_test, normed=True)
plt.title('Labels frequency')

knn = neighbors.KNeighborsClassifier(n_neighbors=30)
knn.fit(X_digits_train, Y_digits_train)

score = knn.score(X_digits_test, Y_digits_test)
Y_digits_pred = knn.predict(X_digits_test)
print(score)


# Q9 : Compute confusion matrix

CM = metrics.confusion_matrix(Y_digits_test, Y_digits_pred)
print(CM)

CM_norm = 1.0 * CM / CM.sum(axis=1)[:, np.newaxis]
print(CM_norm)
plt.figure()
plt.matshow(CM_norm, cmap=plt.cm.Spectral_r, interpolation='none')
plt.xlabel("Predicted")
plt.ylabel("True")
# NOTE: this can be connected with the visualization provided in:
# http://josephsalmon.eu/enseignement/TELECOM/MDI720/PCA.ipynb


# Q10 : Estimate k with cross-validation
# Have a look at the class  'LOOCurve', defined in the source file.

plt.figure()
loo_curv = LOOCurve(k_range=list(range(1, 50, 5)))
loo_curv.fit_curve(X=digits.data, y=digits.target)

print(loo_curv.cv_scores)
loo_curv.plot()


# Q11: Weighted k-NN over old dataset:

def weights(dist, h=0.1):
    """Return array of weights, exponentially small w.r.t. the distance.

    Parameters
    ----------
    dist : a one-dimensional array of distances.

    Returns
    -------
    weight : array of the same size as dist
    """
    # TODO
    return np.exp(-dist ** 2 / h)


n_neighbors = 5
wknn = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors,
                                      weights=partial(weights, h=0.01))
wknn.fit(X_train, Y_train)

plt.figure()
plot_2d(X_train, Y_train)
frontiere_new(wknn, X_train, Y_train, w=None, step=50, alpha_choice=1)
