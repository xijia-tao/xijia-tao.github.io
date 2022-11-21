---
title: COMP3270 Artificial Intelligence Course Notes
date: 2022-05-11
categories: ["Course Notes", "Artificial Intelligence"]
math: true
slug: comp3270
---

The post gives some keypoints on the course content of COMP3270 Artificial Intelligence @HKU, 2021-22 semester 2. It can be used as a directional material for those who are interested in (the more traditional side of) AI, or for revision purposes to future attendants of this course.

## Search

1. uninformed search (BFS, DFS, UCS)
2. informed search (greedy, A*)
   - A* TSA is optimal iff admissible
   - A* GSA is optimal iff consistent (which implies admissible)
   - consistency: h(a) - h(c) <= cost(a to c) / f value (sum) along a path never decreases
3. local search
   - cost of neighboring states (randomly)
   - find local minimum
4. constraint satisfaction - csp
   - backtracking search (DFS, 1 variable at a time, only legal assignments at each point)
   - improvements
     - forward checking (cross off values given the current config)
     - constraint propagation ac-3 (repeatedly enforce, arc consistency iff some valid y in head for all x in tail)
     - variable ordering (mrv -> min remaining values; most degree ~ tie-breaker)
     - value ordering (lcv -> least constraining value, rules out the fewest )
5. adversarial search (minimax, dls, utility)
   - horizon effect: unavoidable damage with a low depth limit, delay -> more damage
   - $\alpha-\beta$ pruning: 
     - $\alpha:=$ best explored option along path to root for max
     - initialize $\alpha=-\infty, \beta=\infty$
     - max value function: is terminal -> return utility value
     - for each action, `v = max(v, min-value(s', alpha, beta))`
     - if $v\geq\beta$, then return $v$
     - `alpha=max(alpha, v)`
     - finally return $v$
   - expectimax: replace min nodes with chance nodes by computing the weighted average of children
   - expectiminimax: environment is an extra random agent that moves after each min/max agent

## MDP

1. MDP: S, A, T(s, a, s') = P(s' \mid  s, a), R(s, a, s'), s0, optional terminal state
2. stationarity (sequences with the same start state have the same order without it) implies only two ways to assign utilities to sequences
   - additive rewards
   - discounted rewards
3. $V(s), Q(s, a), \pi(s)$
4. time-limited values save computation for no / unreachable terminal states
5. value iteration: $V_{k+1}(s)\leftarrow \max_a\sum_{s'}T(s, a, s')[R(s, a, s')+\gamma V_{k}(s')]$ with $V_0=0$, repeat until convergence
   - slow: $O(S^2A)$ per iteration
   - policy converges long before values
6. policy iteration: do several passes that update utilities with fixed policy; a new policy is chosen with one-step lookahead (like policy extraction)
7. policy evaluation: utilities for a fixed policy $V^\pi(s)=\sum_{s'}T(s, \pi(s), s')[R(s, \pi, s') + \gamma V^\pi(s')]$ (use method similar to value iteration as above / use linear solver since max is gone)
8. policy extraction: (mini-)expectimax on V*, i.e. one-step lookahead / directly from Q

## RL

1. TD-learning
   - sample = $R(s,\pi(s), s')+\gamma V^\pi(s')$
   - update: $V^\pi(s)\leftarrow (1-\alpha)V^\pi(s)+\alpha[\text{sample}]$
2. Q-learning
   - sample = $R(s,a,s')+\gamma\max_{a'}Q(s',a')$
   - update: $Q(s,a)\leftarrow (1-\alpha)Q(s,a)+\alpha[\text{sample}]$
3. exploration function
   - epsilon-greedy: explore a fixed amount
   - explore areas whose badness is not (yet) established, eventually stop exploring
   - $f(u,n)=u+k/n$
   - $Q(s,a)\leftarrow R(s,a,s')+\gamma\max_{a'}f(Q(s',a'),N(s',a'))$
   - propagate bonus back to states that lead to unknown states
   - minimize regret (difference between rewards and optimal rewards)
4. approximate Q-learning
   - weights $w_i$ and features $f_i$, linear combination
   - difference = $[r+\gamma\max_{a'}Q(s',a')]-Q(s,a)$
   - update: $w_i\leftarrow w_i+\alpha[\text{difference}]f_i(s,a)$
   - pro: experience is summed up in a few powerful numbers
   - con: states may share features but actually be very different in value

## MM

1. mini-forward algorithm: time t-1 to t
1. stationary distributions $P_\infty(X)$

## HMM

1. definition
   - initial distribution $P(X_1)$
   - transitions $P(X_t \mid  X_{t-1})$
   - emissions $P(E_t \mid  X_t)$
2. belief state $B_t(X)=P(X_t\mid e_1,\dots,e_t)=P(X_t\mid e_{1:t})$
   - passage of time: $B'(X_{t+1}):=P(X_{t+1}\mid e_{i:t})=\sum_{x_t}P(X_{t+1}\mid x_t)B(x_t)$
   - $B(X_{t+1})\propto P(e_{t+1}\mid X_{t+1})B'(X_{t+1})$
   - then renormalize $\to$ beliefs reweighted by likelihood of evidence
3. particle filtering 
   - comes in when the dimension of X too big to use exact inference (e.g. continuous)
   - elapse time: $x'=\text{sample}(P(X'\mid x))$ 
   - observe: $w(x)=P(e\mid x),\ B(x)\propto P(e\mid x)B'(X)$ then renormalize
   - resample: select prior samples in proportion to their likelihood
4. forward algorithm (sum of paths)
   - $f_t[x_t]=P(x_t,e_{1:t})=P(e_t\mid x_t)\sum_{x_{t-1}}P(x_t\mid x_{t-1})f_{t-1}[x_{t-1}]$
   - get most likely explanation by taking argmax over $x_t$
5. Viterbi algorithm (best path)
   - take max instead of sum

## Bayes Nets

1. conditional independence: d-separation![](d-sep.png)

## NLP

1. word2vec
   - iterate through every word of the whole corpus
   - predict surrounding words using word vectors
     - $P(o\mid c)=\frac{\exp(u^T_ov_c)}{\sum_{w\in V}\exp(u_w^Tv_c)}$
     - $J(\theta)$ cost function, a sum of negative log probabilities
2. gradient descent: update all $\theta$ using all windows
3. stochastic gradient descent
   - repeatedly sample windows, and update after each one
   - $\nabla J(\theta)\in \mathbb{R}^{2dV}$ is sparse (2dV as every word can appear as a center or context word)
   - update at most 2m+1 word vectors
