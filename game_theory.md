<!-- Top Navigation -->
* Game Theory
   * [Negotiations](/negotiations.md)
* [Python](/python.md)
* [Web Dev](/web-dev.md)
   * [CSS](/css-notes.md)

---

# Notes on Game Theory

These are my notes while taking ECON 159. Based on those I have created a little python tool to help solve payoff matrices. This helped me understand the topic better
[Repository](https://github.com/stevwyman/game_theory)

There are many fields where Game Theory could get applied, the most known are probably:

* [negotiations](/negotiations.md)
* military
* tennis

This is due to the strategic nature of Game Theory. It provides support for decision making processes.

---

* [Terminology](#terminology)
* [Equilibrium](#equilibrium)

---

Lessons:

Probably the most important lesson from game theory is that your decision impacts the decision findings process of others, which is also true for what others think you will decide.

If you understood this - go spend your time with something way more fun.

1. You should never play a strictly dominated strategy.
2. Rational play by rational players can lead to bad outcomes
3. To figure out what actions you should choose in a game, a good first step is to figure out what are your payoffs (what do you care about) and what are other players' payoffs.
4. If you do not have a dominated strategy, put yourself in your opponents' shoes to try to predict what they will do. For example, in their shoes, you would not choose a dominated strategy.
5. Do not choose a strategy that is never a best response (BR) to any belief.
6. If a mixed strategy is a BR, then each of the pure strategies in the mix must themselves be  BR. In particular, each must yield the same expected payoff.
7. We only ever have to check for strictly profitable *pure*-strategy deviation.
8. If (s^; s^) is not a NE then s^ is not evolutionarily stable. Or, equivalently: if s^ is evolutionarily stable, then (s^; s^) is a NE.
9. If (s^; s^) is a strict NE then s^ is evolutionarily stable.

### Takeaways

* [Cut and Choose](https://en.wikipedia.org/wiki/Divide_and_choose) How to divide fair.

## Terminology

Game theory is all about strategy. Hence playing and solving games is about finding strategies and best responses to other strategies. The field of game theory is quiet wide and so are the different games to be played. To structure this ecosystem a bit here is some terminology (jargon).

### Sequential and Simultaneous Games

The first intuition is differentiate those games by a timing matter, whereas sequential games are played by one taking a turn and *afterwards* the opponent makes his/her turn. A slightly better differentiation might be to **use information as criteria**.
In a sequential game, the players always know what the other player has chosen before their own move.
Taking two examples here: Tic Tac Toe and Rock Paper Scissors

* in [Tic Tac Toe](/some-games.md#TIc Tac Toe), each player can literally see what the other player has chosen and can make his choice based on that information
* in Rock Paper Scissors, the players simultaneously have to make a decision and do not know what the other is choosing

Therefore the games have different approaches for solving them. Parallel games can be used using payoff matrices and sequential games can be solved by backward induction.

### Zero-Sum Game vs Non-Zero-Sum Game

The theory of zero-sum games is vastly different from that of non-zero-sum games because an optimal solution can always be found. Below is a classification to start approaching a solution to those games. There are different ways to solve them and therefore we will look at all of them.

#### Zero-Sum Game

A zero-sum game is one in which no wealth is created or destroyed. So, in a two-player zero-sum game, whatever one player wins, the other loses. Therefore, the player share **no common interests**. So those games are also called a *strictly competitive games*.

Usually two or more players are possible and there we distinguish between games with perfect information and those without.

Examples for imperfect games

- Rock, Paper, Scissors. The game is played simultaneously and therefore the player does not know upfront, what the opponent does or chooses.
- TicTacToe. The game is played sequentially and therefore the player can respond on the choice of his/her opponent.

Strategies solving those games need to be distinguish between:

pure strategies -> sticking to one strategy out of the strategy set
mixed strategies -> randomization across the strategy set

For two-player finite zero-sum games, the different game theoretic solution concepts of Nash equilibrium, minimax, and maximin all give the same solution. If the players are allowed to play a mixed strategy, the game always has an equilibrium.

possible strategies solving those games:

- saddle point/minimax
- eliminating dominated strategies

In financial markets, options and futures are examples of zero-sum games, excluding transaction costs. For every person who gains on a contract, there is a counter-party who loses.

#### Non-Zero-Sum Game

A Non-Zero-Sum Game is a situation where one's win does not necessarily mean another's loss, and one's loss does not necessarily mean that the other party wins. In a Non-Zero-Sum Game, all parties could gain, or all parties could lose.

Therefore, in this scenario, players have **a common interest** and those games are called either *competitive or non-competitive*. Unfortunately the players will not always play forward a common interest, which then ends up in a so called dilemma.

Examples:

- Prisoner's Dilemma
- [Battle of the Sexes](/Game%20Theory/non-zero-games.md)
- Deadlock and Stag Hunt

### Domination

Strategies can dominate each other, hence the payoffs for one strategy can be better than others. We use the below definitions as they are relevant for selection of strategies and also for the removal ot them from payoff matrices.

#### Strict Domination

A strictly dominated strategy  for a player yields a strictly lower expected payoff that any other strategy available for the player (regardless of the stra)
A strictly dominant strategy for a player yields a strictly higher expected payoff than
any other strategy available to the player, regardless of the strategies chosen by
everyone else.

#### Weak Domination

A strategy that delivers an equal or worse outcome than an alternative strategy.

<p align="right">(<a href="#game-theory-top">back to top</a>)</p>
---

### Equilibrium

#### Nash-Equilibrium

The players are playing a best response to each other. No regrets - no individual can do strictly better by deviating, holding others fixed.

#### Pareto Optimum

Definition: An outcome is Pareto optimal if there is no other
outcome which would give both players a higher payoff or would give
one player the same payoff and the other player a higher payoff.

<p align="right">(<a href="#game-theory-top">back to top</a>)</p>
---

### Knowledge

There is a notion of *common* and *mutual* knowledge, but they are not the same. **Common** knowledge is the situation of I know, that you know, that I know, that you know ...

Whereas **mutual** knowledge only holds the information what others know about others.

<p align="right">(<a href="#game-theory-top">back to top</a>)</p>
---
