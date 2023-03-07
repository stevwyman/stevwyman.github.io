<!-- Top Navigation -->
* Game Theory
   * [Negotiations](/negotiations.md)
   * [Some Games](/gt-games.md)
   * [Representation](/gt-representation.md)
   * *Strategies for solving*
* [Python](/python.md)
* [Web Dev](/web-dev.md)

---

# Iterated deletion of (weakly) dominated strategies

# Minimax Strategy

The Minimax algorithm is the most well-known strategy of play of two-player, zero-sum games. The minimax theorem was proven by John von Neumann in 1928. Minimax is a strategy of always minimizing the maximum possible loss which can result from a choice that a player makes. Before we examine minimax, though, let's look at some of the other possible algorithms.

## Maximin

Maximin is solely a one-person game strategy, i.e. a principle which may be used when a person's "competition" is nature, or chance. Whereas the maximax principle is ultra-optimistic, expecting the best possible payoff, the maximin is ultra-pessimistic, expecting the worst possible payoff. It involves choosing the best of the worst possible outcomes.

A simple example of a slot machine game may be used. A player has only two choices to make -- to gamble or not to gamble. If he gambles, he risks losing his bet (say, $1), but also has a chance to win the maximum payoff (say, $10,000). If he does not gamble, he can neither win nor lose.

According to the maximin principle, the player should never gamble, because he faces a risk of losing $1. It is clear that the maximin principle is quite inefficient, since it discourages taking any risks, no matter how high the reward may be.

### Theorem (Minimax theorem (von Neumann, 1928))
>In any finite, two-player, zero-sum game, in any Nash equilibrium each player receives a payoff that is equal to both his maxmin value and his minmax value.

## Correlated Equilibrium

