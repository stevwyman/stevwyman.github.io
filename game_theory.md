# Some information on Game Theory

## Terminology

### Zero-Sum Game vs Non-Zero-Sum Game

The theory of zero-sum games is vastly different from that of non-zero-sum games because an optimal solution can always be found.

Below is a classification to start approacing a solution to those games. There are different ways to solve them and therefore we will look at all of them.

#### Zero-Sum Game

A zero-sum game is one in which no wealth is created or destroyed. So, in a two-player zero-sum game, whatever one player wins, the other loses. Therefore, the player share **no common interests**. So those games are also called a *strictly competitive games*.

Usually two or more players are possible and there we distinguish between games with perfect information and those without.

Examples for imperfect games

- Rock, Paper, Scissors. The game is played simulataneously and therefore the player does not know upfront, what the oponent does or chooses.
- TicTacToe. The game is played sequentially and therefore the player can respond on the choise of his/her opponent.

Strategies solving those games need to be distinguish between:

pure strategies -> sticking to one stratgey out of the strategy set
mixed strategies -> randomization across the stratgy set

For two-player finite zero-sum games, the different game theoretic solution concepts of Nash equilibrium, minimax, and maximin all give the same solution. If the players are allowed to play a mixed strategy, the game always has an equilibrium.

possible strategies solving those games:

- saddle point/minimax
- eliminating dominated strategies

In financial markets, options and futures are examples of zero-sum games, excluding transaction costs. For every person who gains on a contract, there is a counter-party who loses.

#### Non-Zero-Sum Game

A Non-Zero-Sum Game is a situation where one's win does not necessarily mean another's loss, and one's loss does not necessarily mean that the other party wins. In a Non-Zero-Sum Game, all parties could gain, or all parties could lose.

Therefore, in this scenario, players have **a common interest** and those games are called either *competitive or non-competitive*. Unfortunatly the players will not always play forward a common interest, which then ends up in a so called dilemma.

Examples:

- Prisoner's Dilemma
- [Battle of the Sexes](/Game%20Theory/non-zero-games.md)
- Deadlock and Stag Hunt

### Equilibrium

#### Nash-Equilibrium

#### Pareto Optimum

Deinition: An outcome is Pareto optimal if there is no other
outcome which would give both players a higher payoff or would give
one player the same payoff and the other player a higher payoff.
