

#### Question
When you roll a pair of dice, a double is when both dice show the same number, e.g. both show '1' or both show '4'. What is the chance of a double when you roll a pair of dice?

##### Answer
Out of all 36 possible rolls of a pair of dice, 6 are doubles.

#### Question
The game Monopoly is played by rolling a pair of dice. If you land in jail, then to get out, you must roll a double on any one of your next three turns, or else pay a fine. What are the chances that you get out of jail without paying a fine?

##### Answer
The probability of rolling at least one double in 3 dice rolls is the same as the probability of not rolling 3 non-doubles in a row, where the probability of rolling a non-double in one roll of a pair of dice is (5/6).

#### Question
3% of all applicants to the Stanford Medical School are admitted. 70% of all applicants have a GPA of 3.6 or above. Of those who are admitted, 95% have a GPA of 3.6 or above.

What are the chances of being admitted for an applicant whose GPA is 3.6 or above?

##### Answer
P(admit|high gpa)=P(admit & high gpa)P(high gpa)=P(high gpa|admit)P(admit)P(high gpa)


#### Question
A multiple choice exam has 10 questions. Each question has 3 possible answers, of which one is correct. A student knows the correct answers to 4 questions and guesses the answers to the other 6 questions.

It turns out that the student answered the first question correctly. What are the chances that the student was merely guessing?

##### Answer
With "g" for "guess", "k" for "know", and "cor" for "correct:

P(g|cor)=P(g & cor)P(cor)=P(cor|g)P(g)P(cor)=P(cor|g)P(g)P(cor|g)P(g)+P(cor|k)P(k)

(The numerical answer is 1/3.)

#### Question
There are three boxes on the table: The first box contains 2 quarters, the second box contains 2 nickels, and the last box contains 1 quarter and 1 nickel. You choose a box at random, then you pick a coin at random from the chosen box.

If the coin you picked is a quarter, what's the chance that the other coin in the box is also a quarter?

##### Answer
With "qq" for "quarter-quater box", "qn" for "quarter-nickel" box, and "q" for "picked a quarter":

P(qq|q)=P(qq & q)P(q)=P(q|qq)P(qq)P(q)=P(q|qq)P(qq)P(q|qq)P(qq)+P(q|qn)P(qn)

Note that the rightmost denominator could also have been written
P(q∣qq)P(qq)+P(q∣qn)P(qn)+P(q∣nn)P(nn)

where "nn" stands for "nickel-nickel box", but then 
P(q∣nn)=0.

(The numerical answer is 2/3.)

