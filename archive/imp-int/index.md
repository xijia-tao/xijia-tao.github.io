---
title: Implicit Integration
date: 2022-07-20
categories: ["Physics"]
slug: imp-int
math: true
---

## Introduction

Recall the explicit sympletic Euler integrator

$$
v(t+\Delta t)=v(t)+\Delta t\cdot M^{-1}f(x(t), t)\\
x(t+\Delta t)=x(t)+\Delta t\cdot v(t+\Delta t).
$$

The implicit formuation is

$$
\begin{cases}
v(t+\Delta t)=v(t)+\Delta t\cdot M^{-1}f(x(t+\Delta t), t+\Delta t)\\
x(t+\Delta t)=x(t)+\Delta t\cdot v(t+\Delta t). \tag{$\ast$}
\end{cases}
$$

The only difference is that in the implicit version, forces are evaluated at $t+\Delta t$.

## Generic Solver

A dynamic system for soft bodies can be represented by

$$
K(x-x_0)+D(\dot{x})+M\ddot{x}=f_{ext},
$$

where K := stiffness matrix, $x_0$ := rest state, D := damping matrix and M := mass matrix. Note that $M\ddot{x}$ represents some resultant force. Doing some algebraic manipulations will give us the force $f=f_{ext}-Kx+Kx_0-D\dot{x}$. Substituting this into $(\ast)$ and rearranging, we get

$$
(M+\Delta t^2K+\Delta tD)v(t+\Delta t)=Mv(t)+\Delta t(-K(x(t)-x_0)+f_{ext}).
$$

This is a linear system in the form $Ax=b$. Given $A$ and $b$, we easily find $x$, i.e. $v(t+\Delta t)$ here.

## Cloth Simulation

For simplicity, we rewrite $(\ast)$ as follows. Assume a cloth in a 3D space has n nodes. Then $x,v\in\mathbb{R}^{3n},M\in\mathbb{R}^{3n\times3n}$.

$$
\begin{cases}
Mv^{t+1}=Mv^t+f(x^{t+1})\Delta t\\
x^{t+1}=x^t+v^{t+1}\Delta t
\end{cases}\implies
Mv^{t+1}=Mv^t+f(x^t+v^{t+1}\Delta t)\Delta t
$$

### Newton-Raphson Solver

- The general way to solve our system is to use the Newton-Raphson method
  
  - start at a guess for the unknown $v^{t+1}$
  
  - iteratively improve this guess

- To this end, the equations are linearised at the current state and the resulting linear system is solved to find a better approximation

- Linearising at the current state
  
  $$
  \begin{align*}
Mv^{t+1}&=Mv^t+[f(x^t)+\frac{\delta}{\delta x}f(x^t)\cdot(v^{t+1}\Delta t)]\Delta t\\
&=Mv^t+f(x^t)\Delta t+Kv^{t+1}\Delta t^2,
\end{align*}
  $$
  
  where $K$ is the Jacobian of the forces (aka stiffness matrix) $\in\mathbb{R}^{3n\times3n}$. It contains the derivatives of all 3n force components w.r.t. all 3n position components.

- Per time step
  
  - linearise once
  
  - use the current velocities as initial guess $v^{t+1}$

- Rearranging gives
  
  $$
  [M-K\Delta t^2]v^{t+1}=Mv^t+f(x^t)\Delta t.\tag{$\ast\ast$}
  $$
  
  Then the linear equation can be solved with e.g. *conjugate gradients*, *Jacobi solver*, etc.

## Implicit Integration Summary

At each time step

- K is set to zero

- for each spring connecting node i and j
  
  - add 4 3x3 sub-matrices at positions (3i, 3i), (3i, 3j), (3j, 3i) and (3j, 3j) into global K

- evaluate RHS vector b

- solve linear system for $v^{t+1}$

- update positions x

## Actually Solving Ax=b | Jacobi Method

Based on $(\ast\ast)$, set A and b accordingly. At iteration $l$, denote $x:=v^l,x\prime=v^{l+1}$. Start with $v^0:=v^t$ (this is an abuse of notation though, I hope it's clear to the reader).

- Ideally when A is diagonally dominant,
  
  $$
  x\prime=x+\omega D^{-1}(b-Ax),
  $$
  
  where $\omega$ is some constant between 0 and 0.5 and $D$ is the diagonal entries of A.

- Each iteration gives a better estimate of $v^{t+1}$.

- Stop iterating after some user-defined criterion and we're done.

## Fast Simulation with Implicit Integration

### Limitation of Solving Directly

Let's change the notation a (large) bit and get another **re**presentation of Netwon's second law $f=ma$,

$$
q_{n+1}-2q_n+q_{n-1}=h^2M^{-1}f(q_{n+1}).\tag{$\ast\ast\ast$}
$$

Here, $q_n$ is the state (i.e. positions) of a system at timestep $n$ and $h$ is $\Delta t$. The equation follows naturally from $(\ast)$. We want to solve it for the new state $q_{n+1}$.

The classical recipe for solving the nonlinear system involves linearization of the forces,

$$
f(q_{n+1})\approx f(q_n)+(\Delta f|_{q_n})(q_{n+1}-q_n).
$$

Recall that $\Delta f|_{q_n}=\Delta f=-\Delta^2E$ (E is the energy potential function) is just the stiffness matrix $K$. After some derivations, we end up with a linear system $Ax=b$ as before. Requirements on A are

1. must be computed every timestep

2. positive semi-definite

### Converting into an Optimization Problem

Denote $x:=q_{n+1}$ and $y:=2q_n-q_{n-1}$. Convert $(\ast\ast\ast)$ to

$$
M(x-y)=h^2f(x).
$$

Note that the solutions $x$ of this equation correspond to critical points of some function $g(x)$, specifically

$$
g(x)=\frac{1}{2}(x-y)^TM(x-y)+h^2E(x),
$$

which leads to the optimization problem, known as *variational implicit Euler*,

$$
\min_xg(x)
$$

### Optimized Implicit Solver

**Idea**

> Reformulate the energy potential E in a way that will allow us to employ a block
> coordinate descent method.

The point here being that we will be able to compute velocities of the next time step much faster: We will now look at how to build the system matrix just once and re-use it throughout simulation.

---

The crucial components of E are spring potentials $\frac{1}{2}k(\Vert p_1-p_2\Vert-r)^2$.

It can be reformulated into a minimization problem, namely

$$
(\Vert p_1-p_2\Vert-r)^2=\min_{\Vert d\Vert=r}\Vert(p_1-p_2)-d\Vert^2
$$

Upon summing all the contributions of all springs, we get

$$
\frac{1}{2}\sum_ik_i\Vert p_{i_1}-p_{i_2}-d_i\Vert^2=\frac{1}{2}x^TLx-x^TJd
$$

After some calculations, we can plug the derived $E(x)$ to the objective function $g(x)$. The final optimizatoin problem is 

$$
\min_{x\in\mathbb{R}^{3m},\ d\in U}\frac{1}{2}x^T(M+h^2L)x-h^2x^TJd+x^Tb.
$$

Then we can do block coordinate descent to get an estimate of the desired $x$.

1. Set initial guess $x=y=2q_n-q_{n-1}$

2. Do local step
   
   - Given $x$, find optimal rotations for all springs to get $d$ (i.e. set all $d$'s to spring-aligned vector)

3. Do global step
   
   - Given $d$, solve $(M+h^2L)x=My+h^2Jd+h^2f_{ext}$

### Advantages of the New Linear System

- The system matrix is symmetric positive definite
  
  - Your numerical solver will always succeed in finding a solution for Ax=b

- The system matrix A is constant as long as the timestep, particle masses, spring stiffness, and connectivity remain unchanged
  
  - Can pre-compute sparse Cholesky factorization, which makes the linear system solve very fast
