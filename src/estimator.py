import math


def estimator(data):
    # function to calculate the number of currently infected people
    def current_infections():
        return int(data['reportedCases'] * 10)

    # function to calculate 50 * more people infected
    def more_people():
        return int(data['reportedCases'] * 50)

    # infectionsByRequestedTime for impact['currently infected]
    def infections_by_time(days):
        infections = current_infections()
        infectionsByRequestedTime = infections * math.pow(2, math.floor(days / 3))

    # infections for servere impact
    def infections_by_severe_impact(days):
        infections = more_people()
        infectionsByRequestedTime = infections * math.pow(2, math.floor(days / 3))

    return {
        data: {},
        "impact": {
            "currentlyInfected": current_infections()

        },
        "severeImpact": {
            "currentlyInfected": more_people()
        }
    }
