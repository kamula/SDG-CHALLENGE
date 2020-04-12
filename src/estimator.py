import math


def estimator(data):
    estimate = {
        'impact': {},
        'severeImpact': {}
    }

    # calculate the number of currently infected people
    estimate['impact']['currentlyInfected'] = data['reportedCases'] * 10

    # severe impact
    estimate['severeImpact']['currentlyInfected'] = data['reportedCases'] * 50

    # calculate the number of infections in days, weeks and months
    period = data['timeToElapse']
    if data['periodType'] == 'days':
        estimate['impact']['infectionsByRequestedTime'] = estimate['impact']['currentlyInfected'] * (
                2 ** math.trunc(period / 3))

        estimate['severeImpact']['infectionsByRequestedTime'] = estimate['severeImpact']['currentlyInfected'] * (
                2 ** math.trunc(period / 3))

    elif data['periodType'] == 'weeks':
        period_in_days = period * 7
        estimate['impact']['infectionsByRequestedTime'] = estimate['impact']['currentlyInfected'] * math.pow(2,
                                                                                                             math.trunc(
                                                                                                                 period_in_days / 3))

        # severe impacts in weeks
        estimate['severeImpact']['infectionsByRequestedTime'] = estimate['severeImpact']['currentlyInfected'] * (
                2 ** math.trunc(period_in_days / 3))

    elif data['periodType'] == 'months':
        month_days = period * 30
        estimate['impact']['infectionsByRequestedTime'] = estimate['impact']['currentlyInfected'] * math.pow(2,
                                                                                                             math.trunc(
                                                                                                                 month_days / 3))

        # severe impact in months
        estimate['severeImpact']['infectionsByRequestedTime'] = estimate['severeImpact']['currentlyInfected'] * (
                2 ** math.trunc(month_days / 3))

    # challenge two
    # 15% of infections by request time
    impact_fifteen_percent = 0.15 * estimate['impact']['infectionsByRequestedTime']
    estimate['impact']['severeCasesByRequestedTime'] = impact_fifteen_percent

    # severe cases 15%
    severe_fifteen_percent = estimate['severeImpact']['infectionsByRequestedTime'] * 0.15
    estimate['severeImpact']['severeCasesByRequestedTime'] = severe_fifteen_percent

    # hospital beds by request time
    estimate['impact']['hospitalBedsByRequestedTime'] = math.trunc(data['totalHospitalBeds'] * 0.35) - estimate['impact'][
            'severeCasesByRequestedTime']
    estimate['severeImpact']['hospitalBedsByRequestedTime'] = math.trunc(data['totalHospitalBeds'] * 0.35) - estimate['severeImpact'][
            'severeCasesByRequestedTime']

    return estimate



