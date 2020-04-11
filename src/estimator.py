import math


def estimator(data):
    impact = {}
    severeImpact = {}

    # calculate the number of currently infected people
    impact['currentlyInfected'] = data['reportedCases'] * 10

    # severe impact
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50

    # calculate the number of infections in days, weeks and months
    period = data['timeToElapse']
    if data['periodType'] == 'days':
        impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * (2 ** math.trunc(period / 3))

        severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * (2 ** math.trunc(period / 3))

    elif data['periodType'] == 'weeks':
        period_in_days = period * 7
        impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * math.pow(2, math.trunc(period_in_days / 3))

        # severe impacts
        severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * (
                2 ** math.trunc(period_in_days / 3))

    elif data['periodType'] == 'months':
        month_days = period * 30
        impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * math.pow(2, math.trunc(month_days / 3))

        # severe impact
        severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * (
                2 ** math.trunc(month_days / 3))

    return impact, severeImpact


