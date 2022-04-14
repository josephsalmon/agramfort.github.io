title: HAX606X - Convex optimization (2020-...)
sortorder: 0
category: course
iscourse: true
isfull: true
slug: HAX606X-full


This is an undergraduate course (in French!) introducing standard techniques from convex optimization. Numerical elements are provided in Python and are written with [Tanguy Lefort](https://tanglef.github.io/).

<br>
<center>
![Mexican hat](images/mexican_hat.svg "Mexican hat"){ width=70% }
</center>
<br>


## References

- *Mathematics for Machine Learning*; Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong; [mml-book.pdf](https://mml-book.github.io/book/mml-book.pdf)

- *Introduction à l'analyse numérique matricielle et à l'optimisation*; G. Ciarlet

- *Fragments d’Optimisation Différentiable - Théories et Algorithmes*; Jean Charles Gilbert
[.pdf](https://hal.inria.fr/hal-03347060/document)

## TP

1. Introduction: [tp1_sujet.pdf](enseignement/Montpellier/HAX606X/TP/tp1_sujet.pdf), code Python associé [tp1.py](enseignement/Montpellier/HAX606X/TP/tp1.py)
   
2. Méthode de la sécante / méthode du nombre d'or: [tp2_sujet.pdf](enseignement/Montpellier/HAX606X/TP/tp2_sujet.pdf)

3. Méthode de descente de gradient et variantes: [tp3_sujet.pdf](enseignement/Montpellier/HAX606X/TP/tp3_sujet.pdf), [dico_math_functions.py](enseignement/Montpellier/HAX606X/TP/dico_math_functions.py), [widget_convergence.py](enseignement/Montpellier/HAX606X/TP/widget_convergence.py), [widget_level_set.py](enseignement/Montpellier/HAX606X/TP/widget_level_set.py)

4. Méthode de descente de gradient projeté : [tp4_sujet.pdf](enseignement/Montpellier/HAX606X/TP/tp4_sujet.pdf), [script_season.py](enseignement/Montpellier/HAX606X/TP/script_season.py)


<br>
<br>
<br>
<br>

## Cheat Sheet
This work is deeply inspired and adapted from the great work by Nicolas Rougier: [https://github.com/rougier/numpy-tutorial](https://github.com/rougier/numpy-tutorial)


| Code                 | Result        |
|----------------------|-----------|
| <pre> x = np.zeros(9) </pre>         | <image src = "enseignement/Montpellier/HAX606X/figures/create-zeros-1.svg" width="200px"></image>        |
| <pre> x = np.ones(9)</pre>          | <image src = "enseignement/Montpellier/HAX606X/figures/create-ones-1.svg" width="200px"></image>         |
| <pre> x = np.full(9, 0.5)</pre>          | <image src = "enseignement/Montpellier/HAX606X/figures/create-full-1.svg" width="200px"></image>         |
| <pre> x = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0])</pre> |  <image src = "enseignement/Montpellier/HAX606X/figures/create-list-1.svg" width="200px"></image>|
| <pre> x = np.arange(9)</pre>        | <image src = "enseignement/Montpellier/HAX606X/figures/create-arange-1.svg" width="200px"></image>           |
| <pre> x = rng.random(9)</pre>        | <image src = "enseignement/Montpellier/HAX606X/figures/create-uniform-1.svg" width="200px"></image>           |


### Creation: matrix cases


| Code                 | Result        |
|----------------------|-----------|
|<pre>M = np.ones((5, 9)) </pre> | <image src = "enseignement/Montpellier/HAX606X/figures/create-ones-2.svg" width="200px"></image> |
|<pre>M = np.zeros((5, 9))</pre> | <image src = "enseignement/Montpellier/HAX606X/figures/create-zeros-2.svg" width="200px"></image> |
|<pre> M = np.array(<br>&nbsp;&nbsp;&nbsp;&nbsp;[<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.0, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]<br>&nbsp;&nbsp;&nbsp;&nbsp;]<br>)</pre>|<image src = "enseignement/Montpellier/HAX606X/figures/create-list-2.svg" width="200px"></image>
|<pre> M = arange(5 * 9).reshape(5, 9)</pre> | <image src = "enseignement/Montpellier/HAX606X/figures/create-arange-2.svg" width="200px"></image>|
|<pre> M = rng.random(9)</pre>        | <image src = "enseignement/Montpellier/HAX606X/figures/create-uniform-2.svg" width="200px"></image>           |
|<pre> M = np.eye(5, 9)</pre>        | <image src = "enseignement/Montpellier/HAX606X/figures/create-eye-2.svg" width="200px"></image>           |
|<pre> M = np.diag(np.arange(5)) </pre>        | <image src = "enseignement/Montpellier/HAX606X/figures/create-diag-2.svg" width="200px"></image>           |
|<pre> M = np.diag(np.arange(3), k=2) </pre>        | <image src = "enseignement/Montpellier/HAX606X/figures/create-diagk-2.svg" width="200px"></image>           |



### Creation: tensor cases

| Code                 | Result        |
|----------------------|-----------|
| <pre>T = np.zeros((3, 5, 9))</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/create-zeros-3.svg" width="200px"></image>        |
| <pre>T = np.ones((3, 5, 9))</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/create-ones-3.svg" width="200px"></image>        |
| <pre>T = np.arange(3 * 5 * 9).reshape(3, 5, 9)</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/create-arange-3.svg" width="200px"></image>        |
| <pre>T = rng.random((3, rows, cols))</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/create-uniform-3.svg" width="200px"></image>        |



## Matrix reshaping


| Code                 | Result        |
|----------------------|-----------|
| <pre>M = np.zeros((3, 4)); M[2, 2] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/reshape-M.svg" width="200px"></image>        |
| <pre>M = M.reshape(4, 3)</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/reshape-M-reshape(4,3).svg" width="200px"></image>        |
| <pre>M = M.reshape(12, 1)</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/reshape-M-reshape(12,1).svg" width="200px"></image>        |
| <pre>M = M.reshape(1, 12)</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/reshape-M-reshape(1,12).svg" width="200px"></image>        |
| <pre>M = M.reshape(6, 2)</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/reshape-M-reshape(6,2).svg" width="200px"></image>        |
| <pre>M = M.reshape(2, 6)</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/reshape-M-reshape(2,6).svg" width="200px"></image>        |



## Slicing

Start from a zero matrix and get the following simple slicing operations:

</br>
</br>


| Code                 | Result        |
|----------------------|-----------|
| <pre>M = np.zeros((5, 9)) </pre>         | <image src = "enseignement/Montpellier/HAX606X/figures/slice-M.svg" width="200px"></image>        |
| <pre>M[...] = 1 </pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[...].svg" width="200px"></image>        |
| <pre>M[:, ::2] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[:,::2].svg" width="200px"></image>        |
| <pre>M[::2, :] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[::2,:].svg" width="200px"></image>        |
| <pre>M[1, 1] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[1,1].svg" width="200px"></image>        |
| <pre>M[:, 0] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[:,0].svg" width="200px"></image>        |
| <pre>M[0, :] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[0,:].svg" width="200px"></image>        |
| <pre>M[2:, 2:] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[2:,2:].svg" width="200px"></image>        |
| <pre>M[:-2, :-2] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[:-2,:-2].svg" width="200px"></image>        |
| <pre>M[2:4, 2:4] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[2:4,2:4].svg" width="200px"></image>        |
| <pre>M[::2, ::2] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[::2,::2].svg" width="200px"></image>        |
| <pre>M[3::2, 3::2] = 1</pre>         |  <image src = "enseignement/Montpellier/HAX606X/figures/slice-M[3::2,3::2].svg" width="200px"></image>        |


