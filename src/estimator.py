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
    number_of_days = 0
    if data['periodType'] == 'days':
        number_of_days = period
        estimate['impact']['infectionsByRequestedTime'] = estimate['impact']['currentlyInfected'] * (
                2 ** math.trunc(period / 3))

        estimate['severeImpact']['infectionsByRequestedTime'] = estimate['severeImpact']['currentlyInfected'] * (
                2 ** math.trunc(period / 3))

    elif data['periodType'] == 'weeks':
        period_in_days = period * 7
        number_of_days = period_in_days
        estimate['impact']['infectionsByRequestedTime'] = estimate['impact']['currentlyInfected'] * math.pow(2,
                                                                                                             math.trunc(
                                                                                                                 period_in_days / 3))

        # severe impacts in weeks
        estimate['severeImpact']['infectionsByRequestedTime'] = estimate['severeImpact']['currentlyInfected'] * (
                2 ** math.trunc(period_in_days / 3))

    elif data['periodType'] == 'months':
        month_days = period * 30
        number_of_days = month_days
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
    estimate['impact']['hospitalBedsByRequestedTime'] = math.trunc(
        data['totalHospitalBeds'] * 0.35 - estimate['impact'][
            'severeCasesByRequestedTime'])
    estimate['severeImpact']['hospitalBedsByRequestedTime'] = math.trunc(
        data['totalHospitalBeds'] * 0.35 - estimate['severeImpact'][
            'severeCasesByRequestedTime'])

    # challenge 3
    # 5% of infections by requested time
    estimate['impact']['casesForICUByRequestedTime'] = math.trunc(0.05 * estimate['impact'][
        'infectionsByRequestedTime'])

    estimate['severeImpact']['casesForICUByRequestedTime'] = math.trunc(0.05 * estimate['severeImpact'][
        'infectionsByRequestedTime'])

    # 2% of infectionsByRequestedTime
    estimate['impact']['casesForVentilatorsByRequestedTime'] = math.trunc(0.02 * estimate['impact'][
        'infectionsByRequestedTime'])

    estimate['severeImpact']['casesForVentilatorsByRequestedTime'] = math.trunc(0.02 * estimate['severeImpact'][
        'infectionsByRequestedTime'])
    # dollars in flight

    dollars = math.trunc(estimate['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data[
        'region']['avgDailyIncomeInUSD'] * number_of_days)
    estimate['impact']['dollarsInFlight'] = dollars

    dollars_severe = math.trunc(estimate['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data[
        'region']['avgDailyIncomeInUSD'] * number_of_days)
    estimate['severeImpact']['dollarsInFlight'] = dollars_severe

    return estimate
