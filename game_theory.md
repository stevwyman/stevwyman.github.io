<!-- Top Navigation -->
* *Game Theory*
   * [Negotiations](/negotiations.md)
   * [Some Games](/gt-games.md)
   * [Representation](/gt-representation.md)
   * [Strategies for solving](/gt-strategies.md)
* [Python](/python.md)
* [Web Dev](/web-dev.md)

---

# Notes on Game Theory

These are my notes while taking ECON 159. Based on those I have created a little python tool to help solve payoff matrices. This helped me understand the topic better
[Repository](https://github.com/stevwyman/game_theory)

There are many fields where Game Theory could get applied, the most known are probably:

* [negotiations](/negotiations.md)
* military (Cortes or William te conqueror)
* tennis, soccer (penalty shot)

This is due to the strategic nature of Game Theory. It provides support for decision making processes.

---
<a id="game-theory-top"></a>
* [Sequential vs Simultaneous](#sequential-and-simultaneous-games)
* [Zero-Sum vs Non-Zero-Sum](#zero-sum-game-vs-non-zero-sum-game)
* [Domination](#domination)
* [Equilibrium](#equilibrium)
* [Strategies](#strategies)
* [Knowledge](#knowledge)

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

Repeated games are not equal to Stochastic games -> see also Markov Decision Process

Learning in Game Theory
* Fictitious Play
* No-regret Learning

<p align="right">(<a href="#game-theory-top">back to top</a>)</p>

---

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

<p align="right">(<a href="#game-theory-top">back to top</a>)</p>

---

### Coalition Games

**Coalitional Game** is given by specifying a value for every coalition. 
Formally, the coalitional game consists of a finite set of players N, called the **grand coalition**, 
and a characteristic function v: 2 ^ N -> ℝ from the set of all possible coalitions of players to a set of payments 
that satisfies v(∅)=0.

Two ways for allocating payoffs:
* Shapley value: based on marginal contributions - what does each player contribute to each possible coalition; 
   * "fair" distribution.
 * Core: based on coalitional threats - each coalition must get at least what it can generate alone; 
   * "stable" distribution. 

#### convex Games

A game is **convex** if its characteristic function v is supermodular:


that is, "the incentives for joining a coalition increase as the coalition grows".

**Theorem**
>Every convex game has a nonempty core.
>In every convex game, the Shapley value is in the core.

<p align="right">(<a href="#game-theory-top">back to top</a>)</p>

---

### Dominance

Strategies can *dominate* each other, hence the payoffs for one strategy can be better than others. We use the below definitions as they are relevant for selecting strategies and also for removing them from payoff matrices.

| |x|y|z|
|-|-|-|-|
|1|1,**2**|2,**2**|5,1|
|2|4,1|3,**5**|3,3|
|3|**5**,2|**4**,**4**|**7**,0|
|4|2,3|0,**4**|3,0|

In the above example 3 is a strictly dominant strategy, as it yields the highest payoff regardless what the other player chooses (x, y or z).
In addition y is only a weakly dominant strategy, as in case player 1 chooses 1, x would yield the same payoff as choosing y.

Dominated strategies can be strictly dominated or weakly dominated:

* A strategy is strictly (or strongly) dominated if it leads to worse outcomes than alternative strategies.
* A strategy is weakly dominated if it leads to equal or worse outcomes than alternative strategies.

Dominant strategies can be strictly dominant or weakly dominant:

* A strategy is strictly (or strongly) dominant if it leads to better outcomes than alternative strategies.
* A strategy is weakly dominant if it leads to equal or better outcomes than alternative strategies.


#### Strict Domination

My strategy &alpha; *strictly dominates* my strategy &beta; if my payoff from &alpha; is strictly higher than that from &beta; regardless of others' choices.

A *strictly dominant* strategy for a player yields a strictly higher expected payoff than any other strategy available to the player, regardless of the strategies chosen by everyone else.

#### Weak Domination

My strategy &alpha; *weakly dominates* my strategy &beta; if my payoff from &alpha; is as high as that from &beta; regardless of others' choices, and is strictly higher for at least one such choice.

A strategy that delivers an equal or worse outcome than an alternative strategy.


<p align="right">(<a href="#game-theory-top">back to top</a>)</p>

---

### Equilibrium

#### Nash-Equilibrium

The players are playing a best response to each other. No regrets - no individual can do strictly better by deviating, holding others fixed.

> Theorem (Nash, 1950): Every finite game has a Nash Equilibrium.

#### Pareto Optimum

Definition: An outcome is Pareto optimal if there is no other outcome, which would give both players a higher payoff, or would give one player the same payoff and the other player a higher payoff.

A Nash equilibrium is not necessarily Pareto optimal, and vice versa.

#### Sub-Game Perfect Equilibrium

Nash equilibrium that represents a Nash equilibrium of every subgame in the original game. It's a refinement of the Nash equilibrium that eliminates non-credible threats.

**Non-credible Threat** - a threat made by a player in an extensive form game which would not be in the best interest for the player to carry out. The hope is that the threat is believed in which case there is no need to carry it out. While Nash equilibria may depend on non-credible threats, Backward Induction eliminates them.

**Backward Induction** - identify the equilibria in the bottom-most trees, and adopt these as one moves up the tree.

<p align="right">(<a href="#game-theory-top">back to top</a>)</p>

---

### Strategies

**Tit-for-tat** Start out cooperating. If the opponent defected, defect in the next round. THen go back to cooperation.

**Grim Trigger** Start out cooperating. If the opponent ever defects, defect forever.

### Knowledge

There is a notion of *common* and *mutual* knowledge, but they are not the same. **Common** knowledge is the situation of I know, that you know, that I know, that you know ...

Whereas **mutual** knowledge only holds the information what others know about others.

<p align="right">(<a href="#game-theory-top">back to top</a>)</p>

---
