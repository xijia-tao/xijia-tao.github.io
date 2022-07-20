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
  [M-K\Delta t^2]v^{t+1}=Mv^t+f(x^t)\Delta t.
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
