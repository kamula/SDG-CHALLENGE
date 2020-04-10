import math


def estimator(data):
    # function to calculate the number of currently infected people
    trunk = math.trunc(data['reportedCases'])

    return {
        data: input(data),
        "impact": {
            "currentlyInfected": data['reportedCases'] * 10,
            'infectionsByRequestedTime': (data['reportedCases'] * 10) * math.pow(2, trunk)

        },
        "severeImpact": {
            "currentlyInfected": data['reportedCases'] * 50,
            'infectionsByRequestedTime': (data['reportedCases'] * 50) * math.pow(2, trunk)
        }
    }
