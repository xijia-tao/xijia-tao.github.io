---
title: MA4270 Data Modelling and Computation Notes
date: 2022-11-21
math: true
slug: ma4270
---

## Ch 7. Boosting

- Decision stumps, where $\theta=\{s,k,\theta\_0\}$. $k=$ index of feature, $s=$ sign and $\theta\_0$ = threshold.

$$
h(\boldsymbol{x};\boldsymbol{\theta})=\text{sign}(s(x\_k-\theta\_0))
$$

Weighted decision function

$$
f\_M(\boldsymbol{x})=\sum\_{m=1}^M\alpha\_mh(\boldsymbol{x};\boldsymbol{\theta}\_m)
$$

Individual $h$ are called weak/base learners. AdaBoost helps find good $\{\boldsymbol{\theta}\_m,\alpha\_m\}$

### AdaBoost

$\boldsymbol{\hat{\theta}}\_m=\arg\min\_\theta\sum\_{t:y\_t\neq h(\boldsymbol{x};\boldsymbol{\theta})}w\_{m-1}(t)$

1. initialize weights $w\_0(t)=\frac{1}{n}$ for $t=1,\dots,n$ ($n=$ size of data set)

2. for $m=1,\dots,M$ do
   
   1. $\boldsymbol{\hat{\theta}}\_m=\arg\min\_\theta\sum\_{t:y\_t\neq h(\boldsymbol{x};\boldsymbol{\theta})}w\_{m-1}(t)$
   
   2. $\hat{\alpha}\_m=\frac{1}{2}\log\frac{1-\hat{\epsilon}\_m}{\hat{\epsilon}\_m}$, where $\hat{\epsilon}\_m$ is the minimal value attained in 2.1
   
   3. $w\_m(t)=\frac{1}{Z\_m}w\_{m-1}(t)e^{-y\_th(\boldsymbol{x}\_t;\hat{\boldsymbol{\theta}}\_m)\hat{\alpha}\_m}$, where $Z\_m$ is the sum of all unnormalized $w\_{m-1}(t)$

3. output: $f\_M(\boldsymbol{x})=\sum\_{m=1}^M\hat{\alpha}\_mh(\boldsymbol{x};\hat{\boldsymbol{\theta}}\_m) \to\hat{y}=\text{sign}(f\_M(\boldsymbol{x}))$

Note: one can observe that the test error still decreases when training error reaches 0. This is because AdaBoost is implicitly minimizing the margin, hence making the classifier more robust.

## Ch 8. Concentration

**Hoeffding's inequality** Let $Z=X\_1+\cdots+X\_n$, where the $X\_i$ are independent and supported on $[a\_i,b\_i]$. Then

$$
\mathbb{P}[\frac{1}{n}\vert Z-\mathbb{E}[Z]\vert >\epsilon]\leq2\exp(-\frac{2n\epsilon^2}{\frac{1}{n}\sum\_{i=1}^n(b\_i-a\_i)^2})
$$

## Ch 9. Theory

- $\mathcal{D}=\{(\boldsymbol{x}\_i,y\_i)\}^n\_{i=1},(\boldsymbol{x}\_i,y\_i)\sim P\_{XY}$

- possible classifiers $f(\boldsymbol{x})$ make up the function class $\mathcal{F}$

- risk/test error $R(f)=\mathbb{E}[l(y,f(\boldsymbol{x})]$ gives the Bayes-optimal classifier

- $f\_{erm}=\arg\min\_{f\in\mathcal{F}}R\_n(f)$ training error $R\_n(f)=\frac{1}{n}\sum\_{i=1}^nl(y\_i,f(\boldsymbol{x}\_i))$

- test error = training error + generalization error

### PAC Learning

To ensure small generalization error, PAC (probably approximately correct) learning seeks to attain a risk within a small value of that chieved by the best $f$ in $\mathcal{F}$.

Given $l$, $\mathcal{F}$ is PAC-learnable if there exists an algorithm $\mathcal{A}(\mathcal{D}\_n)$ and a function $\bar{n}(\epsilon,\delta)$ such that: for any $P\_{XY}$ and any $\epsilon,\delta\in(0,1)$, if $n\geq\bar{n}(\epsilon,\delta)$, then the following holds with probability at least $1-\delta$:

$$
R(\hat{f})\leq\min\_{f\in\mathcal{F}}R(f)+\epsilon
$$

$1-\delta\to$ probably correct, $\epsilon\to$ approximately correct, $\bar{n}\to$ sample complexity.

### Finite Function Class

**Theorem** for any bounded loss function in $[0,1]$, any finite function class $\mathcal{F}$ is PAC-learnable with sample complexity $\bar{n}(\epsilon,\delta)=\frac{2}{\epsilon^2}\log\frac{2\\mid \mathcal{F}\\mid }{\delta}$.

*Proof*: taking the algorithm to be ERM (empirical risk minimization), apply Hoeffding's inequality

$$
P[\\mid R(f)-R\_n(f)\\mid \geq\epsilon\_0]\leq2e^{-2n\epsilon\_0^2}.
$$

We cannot simply substitute $f=f\_{erm}$ because the later is not fixed, but rather a random variable depending on $\mathcal{D}$. For finite $\mathcal{F}$,

$$
\mathcal{P}[\bigcup\_{f\in\mathcal{F}}\{\\mid R(f)-R\_n(f)\\mid >\epsilon\_0\}]\leq2\\mid \mathcal{F}\\mid e^{-2n\epsilon\_0^2}
$$

By setting the RHS to a target $\delta$, we find the sufficient $n$ as $\frac{1}{2\epsilon\_0^2}\log\frac{2\\mid \mathcal{F}\\mid }{\delta}$. Assume the probability $1-\delta$ event occurs, namely $\mid R(f)-R\_n(f)\mid \leq\epsilon\_0$ for all $f\in\mathcal{F}$. Letting $f^*$ be the function that minimizes $R(f)$, we have

$$
\begin{align*}
R(f\_{erm})-R(f^\*)&=(R(f\_{erm})-R\_n(f\_{erm}))+(R\_n(f\_{erm})-R\_n(f^\*))+(R\_n(f^\*)-R(f^\*)) \\\
&\leq\epsilon\_0+0+\epsilon\_0=2\epsilon\_0
\end{align*}
$$

Setting $\epsilon\_0=\frac{\epsilon}{2}$ gives the desired bound, and yields $n=\frac{2}{\epsilon^2}\log\frac{2\mid \mathcal{F}\mid }{\delta}$ .

### Infinite Case & VC Dimension

**Intuition** even with infinitely many hypotheses, there may be only finitely many effective hypotheses.

**Definitions**

- Growth function/shattering number $S\_n(\mathcal{F})=\sup\_{\boldsymbol{x}\_1,\dots,\boldsymbol{x}\_n}\\mid \{(f(\boldsymbol{x}\_1),\dots,f(\boldsymbol{x}\_n)):f\in\mathcal{F}\}\\mid $
  
  - This is an integer between $1$ and $2^n$.

- VC dimension $d\_{VC}=d\_{VC}(\mathcal{F})$ is the largest $k$ such that $S\_k(\mathcal{F})=2^k$. If $S\_k(\mathcal{F})=2^k$ for all $k$, then we define $d\_{VC}=\infty$.
  
  - A set of such $k$ points is said to be shattered by $\mathcal{F}$.

*Sauer's lemma*: 

$$ 
S\_n(\mathcal{F})\leq\sum\_{i=1}^{d\_{VC}}\begin{pmatrix}n\\\i\end{pmatrix}
$$

. For $n\leq d\_{VC},S\_n(\mathcal{F})=2^n$. Otherwise, $S\_n(\mathcal{F})\leq(\frac{d\_{VC}}{n})^{d\_{VC}}$. A slightly weaker bound is $S\_n(\mathcal{F})\leq(n+1)^{d\_{VC}}$.

**Theorem** if $d\_{VC}<\infty$, then $\mathcal{F}$ is PAC-learnable under the 0-1 loss with sample complexity

$$
\bar{n}(\epsilon,\delta)=C\cdot\frac{d\_{VC}+\log\frac{1}{\epsilon}}{\epsilon^2}
$$

for some constant $C$. Conversely, if $d\_{VC}=\infty$, then $\mathcal{F}$ is not PAC-leranable.

- Hence, $d\_{VC}$ serves as a fundamental measure of richness of the function class – to get good generalization, it suffices to have $n\gg d\_{VC}$ samples.

- Even if $d\_{VC}$ is infinite, efficient learning might be possible for a given data distribution $P\_{XY}$. The VC theory only establishes the difficulty of worst-case distributions.

**Examples**

- rectangular classifier: $d\_{VC}=4$

- linear classifier w/ and w/o an offset in dimnension $d$: $d\_{VC}=d$ or $d+1$

## Ch 11. Unsupervised

### Clustering

Given the number of clusters $K$, clustering is the task of seeking a partition of the data set $\mathcal{D}\_1\cup\dots\cup\mathcal{D}\_K$, as well as an associated set of cluster centers $\boldsymbol{\mu},\dots,\boldsymbol{\mu}\_K$, such that the sum of distances

$$
J(\{\mathcal{D}\_j\}\_{j=1}^K, \{\mathcal{\mu}\_j\}\_{j=1}^K)=\sum^K\_{j=1}\sum\_{\boldsymbol{x}\in\mathcal{D}\_j}\mid \mid \boldsymbol{x}-\boldsymbol{\mu}\_j\mid \mid ^2
$$

are minimized. This problem is NP-hard in general.

**K-means**

Minimize $J$ by alternatively fixing $\boldsymbol{\mu}\_j$ and $\mathcal{D}\_j$ until convergence.

1. $\mathcal{D}\_j=\{\boldsymbol{x}\in\mathcal{D}:j={\arg\min}\_{j'=1,\dots,K}\mid \mid \boldsymbol{x}-\boldsymbol{\mu}\_{j'}\mid \mid ^2\}$
2. $\boldsymbol{\mu}\_j=\frac{1}{\mid \mathcal{D}\_j}\sum\_{\boldsymbol{x}\in\mathcal{D}\_j}\boldsymbol{x}$.

cannot gaurantee the solution found is optimal, but since $J$ decreases after each iteration,  we must converge to a local minimum.

*Problems* tends to favor similar-size clusters; cannot detect clusters other than the ball-like ones

### Distribution Learning

**Parametric** methods consider classes of distributions $p(\boldsymbol{x};\boldsymbol{\theta})$. The learning algorithm (MLE) finds some $\hat{\boldsymbol{\theta}}$, and the estimate of the distribution is $\hat{p}(\boldsymbol{x})=p(\boldsymbol{x};\hat{\boldsymbol{\theta}})$, i.e.,

$$
\hat{\boldsymbol{\theta}}={\arg\max}\_\theta\prod^n\_{t=1}p(\boldsymbol{x}\_t;\boldsymbol{\theta})
$$

unbiased estimate: $\mathbb{E}[\hat{\boldsymbol{\theta}}]=\boldsymbol{\theta}^*$

compare with the supervised case: $p(y\mid \boldsymbol{x};\boldsymbol{\theta})$

**Non-parametric** methods: K-nearest neighbors (supervised), kernel density estimation (data point increase the density more in the nearby regions, like a smooth version of a histogram)
