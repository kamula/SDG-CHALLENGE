import math


def estimator(**data):
    # calculate number of days
    def days_months_weeks():
        if data['periodType'] == 'weeks':
            data['timeToElapse'] = data['timeToElapse'] * 7
        elif data['periodType'] == 'months':
            data['timeToElapse'] = data['timeToElapse'] * 30
        else:
            data['timeToElapse'] = data['timeToElapse']
        return data['timeToElapse']

    # calculate power
    def calc_power():
        days = days_months_weeks()
        power_to_raise = math.trunc(days / 3)
        return power_to_raise

    def reported_cases_ten():
        return data['reportedCases'] * 10

    def reported_cases_fifty():
        return data['reportedCases'] * 50

    def impact_severe():
        # trunk = calc_power()
        value = reported_cases_ten()
        return value * math.pow(2, calc_power())

    def severe_impact():
        # trunk = calc_power()
        value2 = reported_cases_fifty()
        return value2 * math.pow(2, calc_power())

    return {
        'impact': {
            'currentlyInfected': reported_cases_ten(),
            'infectionsByRequestedTime': impact_severe()
        },
        'severeImpact': {
            'currentlyInfected': reported_cases_fifty(),
            'infectionsByRequestedTime': severe_impact()
        }

    }
