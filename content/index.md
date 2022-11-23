---
title: MA4270 Data Modelling and Computation Notes
date: 2022-11-21
math: true
slug: ma4270
---

## Ch 7. Boosting

- Decision stumps, where $\theta=\{s,k,\theta_0\}$. $k=$ index of feature, $s=$ sign and $\theta_0$ = threshold.

$$
h(\boldsymbol{x};\boldsymbol{\theta})=\text{sign}(s(x_k-\theta_0))
$$

Weighted decision function

$$
f_M(\boldsymbol{x})=\sum_{m=1}^M\alpha_mh(\boldsymbol{x};\boldsymbol{\theta}_m)
$$

Individual $h$ are called weak/base learners. AdaBoost helps find good $\{\boldsymbol{\theta}_m,\alpha_m\}$

### AdaBoost

$\boldsymbol{\hat{\theta}}_m=\arg\min_\theta\sum_{t:y_t\neq h(\boldsymbol{x};\boldsymbol{\theta})}w_{m-1}(t)$

1. initialize weights $w_0(t)=\frac{1}{n}$ for $t=1,\dots,n$ ($n=$ size of data set)

2. for $m=1,\dots,M$ do
   
   1. $\boldsymbol{\hat{\theta}}\_m=\arg\min\_\theta\sum_{t:y_t\neq h(\boldsymbol{x};\boldsymbol{\theta})}w_{m-1}(t)$
   
   2. $\hat{\alpha}_m=\frac{1}{2}\log\frac{1-\hat{\epsilon}_m}{\hat{\epsilon}_m}$, where $\hat{\epsilon}_m$ is the minimal value attained in 2.1
   
   3. $w\_m(t)=\frac{1}{Z\_m}w\_{m-1}(t)e^{-y\_th(\boldsymbol{x}\_t;\hat{\boldsymbol{\theta}}\_m)\hat{\alpha}\_m}$, where $Z_m$ is the sum of all unnormalized $w_{m-1}(t)$

3. output: $f_M(\boldsymbol{x})=\sum_{m=1}^M\hat{\alpha}_mh(\boldsymbol{x};\hat{\boldsymbol{\theta}}_m) \to\hat{y}=\text{sign}(f_M(\boldsymbol{x}))$

Note: one can observe that the test error still decreases when training error reaches 0. This is because AdaBoost is implicitly minimizing the margin, hence making the classifier more robust.

## Ch 8. Concentration

**Hoeffding's inequality** Let $Z=X_1+\cdots+X_n$, where the $X_i$ are independent and supported on $[a_i,b_i]$. Then

$$
\mathbb{P}[\frac{1}{n}\vert Z-\mathbb{E}[Z]\vert >\epsilon]\leq2\exp(-\frac{2n\epsilon^2}{\frac{1}{n}\sum_{i=1}^n(b_i-a_i)^2})
$$

## Ch 9. Theory

- $\mathcal{D}=\{(\boldsymbol{x}_i,y_i)\}^n_{i=1},(\boldsymbol{x}_i,y_i)\sim P_{XY}$

- possible classifiers $f(\boldsymbol{x})$ make up the function class $\mathcal{F}$

- risk/test error $R(f)=\mathbb{E}[l(y,f(\boldsymbol{x})]$ gives the Bayes-optimal classifier

- $f_{erm}=\arg\min_{f\in\mathcal{F}}R_n(f)$ training error $R_n(f)=\frac{1}{n}\sum_{i=1}^nl(y_i,f(\boldsymbol{x}_i))$

- test error = training error + generalization error

### PAC Learning

To ensure small generalization error, PAC (probably approximately correct) learning seeks to attain a risk within a small value of that chieved by the best $f$ in $\mathcal{F}$.

Given $l$, $\mathcal{F}$ is PAC-learnable if there exists an algorithm $\mathcal{A}(\mathcal{D}_n)$ and a function $\bar{n}(\epsilon,\delta)$ such that: for any $P_{XY}$ and any $\epsilon,\delta\in(0,1)$, if $n\geq\bar{n}(\epsilon,\delta)$, then the following holds with probability at least $1-\delta$:

$$
R(\hat{f})\leq\min_{f\in\mathcal{F}}R(f)+\epsilon
$$

$1-\delta\to$ probably correct, $\epsilon\to$ approximately correct, $\bar{n}\to$ sample complexity.

### Finite Function Class

**Theorem** for any bounded loss function in $[0,1]$, any finite function class $\mathcal{F}$ is PAC-learnable with sample complexity $\bar{n}(\epsilon,\delta)=\frac{2}{\epsilon^2}\log\frac{2\|\mathcal{F}\|}{\delta}$.

*Proof*: taking the algorithm to be ERM (empirical risk minimization), apply Hoeffding's inequality

$$
P[\|R(f)-R_n(f)\|\geq\epsilon_0]\leq2e^{-2n\epsilon_0^2}.
$$

We cannot simply substitute $f=f_{erm}$ because the later is not fixed, but rather a random variable depending on $\mathcal{D}$. For finite $\mathcal{F}$,

$$
\mathcal{P}[\bigcup_{f\in\mathcal{F}}\{\|R(f)-R_n(f)\|>\epsilon_0\}]\leq2\|\mathcal{F}\|e^{-2n\epsilon_0^2}
$$

By setting the RHS to a target $\delta$, we find the sufficient $n$ as $\frac{1}{2\epsilon_0^2}\log\frac{2\|\mathcal{F}\|}{\delta}$. Assume the probability $1-\delta$ event occurs, namely $|R(f)-R_n(f)|\leq\epsilon_0$ for all $f\in\mathcal{F}$. Letting $f^*$ be the function that minimizes $R(f)$, we have

$$
\begin{align*}
R(f_{erm})-R(f^*)&=(R(f_{erm})-R_n(f_{erm}))+(R_n(f_{erm})-R_n(f^*))+(R_n(f^*)-R(f^*)) \\
&\leq\epsilon_0+0+\epsilon_0=2\epsilon_0
\end{align*}
$$

Setting $\epsilon_0=\frac{\epsilon}{2}$ gives the desired bound, and yields $n=\frac{2}{\epsilon^2}\log\frac{2|\mathcal{F}|}{\delta}$ .

### Infinite Case & VC Dimension

**Intuition** even with infinitely many hypotheses, there may be only finitely many effective hypotheses.

**Definitions**

- Growth function/shattering number $S_n(\mathcal{F})=\sup_{\boldsymbol{x}_1,\dots,\boldsymbol{x}_n}\|\{(f(\boldsymbol{x}_1),\dots,f(\boldsymbol{x}_n)):f\in\mathcal{F}\}\|$
  
  - This is an integer between $1$ and $2^n$.

- VC dimension $d_{VC}=d_{VC}(\mathcal{F})$ is the largest $k$ such that $S_k(\mathcal{F})=2^k$. If $S_k(\mathcal{F})=2^k$ for all $k$, then we define $d_{VC}=\infty$.
  
  - A set of such $k$ points is said to be shattered by $\mathcal{F}$.

*Sauer's lemma*: $S_n(\mathcal{F})\leq\sum_{i=1}^{d_{VC}}\begin{pmatrix}n\\i\end{pmatrix}$. For $n\leq d_{VC},S_n(\mathcal{F})=2^n$. Otherwise, $S_n(\mathcal{F})\leq(\frac{d_{VC}}{n})^{d_{VC}}$. A slightly weaker bound is $S_n(\mathcal{F})\leq(n+1)^{d_{VC}}$.

**Theorem** if $d_{VC}<\infty$, then $\mathcal{F}$ is PAC-learnable under the 0-1 loss with sample complexity

$$
\bar{n}(\epsilon,\delta)=C\cdot\frac{d_{VC}+\log\frac{1}{\epsilon}}{\epsilon^2}
$$

for some constant $C$. Conversely, if $d_{VC}=\infty$, then $\mathcal{F}$ is not PAC-leranable.

- Hence, $d_{VC}$ serves as a fundamental measure of richness of the function class – to get good generalization, it suffices to have $n\gg d_{VC}$ samples.

- Even if $d_{VC}$ is infinite, efficient learning might be possible for a given data distribution $P_{XY}$. The VC theory only establishes the difficulty of worst-case distributions.

**Examples**

- rectangular classifier: $d_{VC}=4$

- linear classifier w/ and w/o an offset in dimnension $d$: $d_{VC}=d$ or $d+1$
