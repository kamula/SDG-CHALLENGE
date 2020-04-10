import math


def estimator(**data):
    impact = {}
    severeImpact = {}

    currentlyInfectedImpact = data['reportedCases'] * 10
    impact['currentlyInfected'] = currentlyInfectedImpact

    currentlyInfectedSevere = data['reportedCases'] * 50
    severeImpact['currentlyInfected'] = currentlyInfectedSevere

    time = data['timeToElapse']

    if data['periodType'] == 'days':
        infected = currentlyInfectedImpact * (2 ** math.trunc(time/3))
        impact['infectionsByRequestedTime'] = infected

        severe_infected = currentlyInfectedSevere * (2 ** math.trunc(time/3))
        severeImpact['infectionsByRequestedTime'] = severe_infected
    elif data['periodType'] == 'weeks':
        weeks_infections_days = time * 7
        week_infections = currentlyInfectedImpact * (2 ** math.trunc(weeks_infections_days/3))
        impact['infectionsByRequestedTime'] = week_infections

        severe_week_infections = currentlyInfectedSevere * (2 ** math.trunc(weeks_infections_days/3))
        severeImpact['infectionsByRequestedTime'] = severe_week_infections

    elif data['periodType'] == 'months':
        month_days = time * 30
        infections_by_month = currentlyInfectedImpact * 2(2**math.trunc(month_days/3))
        impact['infectionsByRequestedTime'] = infections_by_month

        severe_months_infections = currentlyInfectedSevere * 2(2**math.trunc(month_days/3))
        severeImpact['infectionsByRequestedTime'] = severe_months_infections

