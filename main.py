#!/usr/bin/env python

import matplotlib.pyplot as plt
import math
import random

def bet(p, b, stake):
	overvalue = random.random()

	# a lot of bookmakers don't let you bet under £1
	if stake < 1:
		return 0

	if overvalue < p:
		return stake * b

	return -stake

def expected_value(p, b, stake):
	if b < 0:
		return 0

	return stake * (b * p - 1 + p)

def kelly_criterion(p, b):
	if b < 0:
		return 0

	return p - (1 - p) / b

def accumulate_bets(bankroll):
	working_bankroll = bankroll
	this_day = 0
	ev = 0

	probabilities = []
	ratios = []
	stakes = []

	while ev < 90 or this_day < bets_per_day:
		fair_odds = random.uniform(1.05, 2)
		#overvalue = random.uniform(1, 1.1)
		overvalue = 0.2 * math.exp(-this_day) + 1
		#overvalue = 1.2

		odds = fair_odds * overvalue

		p = 1 / fair_odds
		b = odds - 1
		stake = kelly_criterion(p, b) * working_bankroll * 1

		if stake < 1:
			break

		ev =+ expected_value(p, b, stake)

		probabilities.append(p)
		ratios.append(b)
		stakes.append(stake)

		working_bankroll -= stake

		this_day += 1

	for i in range(len(stakes)):
		bankroll += bet(probabilities[i], ratios[i], stakes[i])

	return bankroll, this_day


bankroll = 1000
tolerance = 1000
n = 30
bets_per_day = 20

x = []
y = []

n_bets = 0
bet_list = []

debt = 0

for i in range(n):
	bankroll, this_day = accumulate_bets(bankroll)

	if bankroll < 1000:
		bankroll += 1000 # get some extra help
		debt += 1000

	if bankroll <= 0:
		break

	if i % 30 == 0 and i != 0:
		bankroll -= 1000 + debt # expenses and debt
		debt = 0

	x.append(i)
	y.append(bankroll)
	bet_list.append(this_day)

plt.plot(x, y, c=(1, 0, 0))

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

plt.plot(x, bet_list, c=(0, 1, 0))

plt.xlabel("Step")
plt.ylabel("Number of bets")

plt.title("Graph")

plt.show()
