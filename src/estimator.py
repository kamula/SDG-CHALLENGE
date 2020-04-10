import math


def estimator(**data):
    def reported_cases_ten():
        return data['reportedCases'] * 10

    def reported_cases_fifty():
        return data['reportedCases'] * 50

    def impact_severe():
        value = reported_cases_ten()
        return value * math.pow(2, 9)

    def severe_impact():
        value2 = reported_cases_fifty()
        return value2 * math.pow(2, 9)

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
