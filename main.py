#!/usr/bin/env python

import matplotlib.pyplot as plt
import math
import random

def bet(stake, p, b):
	rng = random.random()

	# a lot of bookmakers don't let you bet under £1
	# if stake < 1:
	# 	return 0

	if rng < p:
		return stake * b

	return -stake

def kelly_criterion(p, b):
	if b < 0:
		return 0

	return p - (1 - p) / b

bankroll = 1000
n = 10000

x = []
y = []

# uses gambling odds
for i in range(n):
	fair_odds = random.uniform(1, 10)
	rng = random.uniform(1 - fair_odds, 1)

	rng = math.copysign(1, rng) * abs(rng)**2

	random_odds = fair_odds + rng

	p = 1 / fair_odds
	b = random_odds - 1
	stake = kelly_criterion(p, b) * bankroll

	if stake > 0:
		bankroll += bet(stake, p, b)

	if bankroll <= 0:
		break

	x.append(i)
	y.append(bankroll)

plt.plot(x, y)

plt.xlabel("Step")
plt.ylabel("Bankroll")

plt.title("Graph")

plt.show()

plt.plot(x, y)

plt.xlabel("Step")
plt.ylabel("Bankroll")

plt.title("Graph")

plt.yscale("log")
plt.show()
