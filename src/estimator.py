def estimator(data):
    impact_current_infections = data['reportedCases'] * 10
    severe_impact_infected = data['reportedCases'] * 50
    return {
        'impact': {
            'currentlyInfected': impact_current_infections,
            'infectionsByRequestedTime': impact_current_infections * 512
        },
        'severeImpact': {
            'currentlyInfected': severe_impact_infected,
            'infectionsByRequestedTime': severe_impact_infected * 512

        }
    }
