## Predicting-state-using-markov-chains

In this project we will code a practical example for all of Markov chains.

In this scenario, Jane works late, like if she works over time, what how can we predict what she will be doing the following night?

So the scenario is that, Jane, if she works leads, which is not often, but if she works overtime, she on that night after working late, she either goes to bed early, watches Netflix or goes to the gym.

These are the only three things she ever does on days that she works overtime.

So what we want to do is to figure out that if one night she works late and she decides to sleep early the following night, what are the odds that she would either watch Netflix go to the gym or sleep early?

So each one of these represents a state and whether she goes to the gym.

So if the at the correct state tonight is she went to bed early, this is our current state.

What is the chance that tomorrow, which is our next state, she either goes to the gym or goes or watches Netflix at home.

So we need to predict what she is going to be doing tomorrow night based on what she's doing tonight.

She would possibly either only go to the gym, sleep early or watch Netflix.

We created the probability transition matrix on based on those three states.

So we are going to created a three by three transition matrix using Python.
