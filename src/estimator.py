import math


def estimator(data):
    # function to calculate the number of currently infected people
    def current_infections():
        return {
            data: {},
            "impact": {
                "currentlyInfected": data['reportedCases'] * 10,
                'infectionsByRequestedTime': (data['reportedCases'] * 10) * math.pow(2,
                                                                                     math.trunc(data['reportedCases']))

            },
            "severeImpact": {
                "currentlyInfected": data['reportedCases'] * 50,
                'infectionsByRequestedTime': (data['reportedCases'] * 50) * math.pow(2,
                                                                                     math.trunc(data['reportedCases']))
            }
        }
