def estimator(data):
    impact_current_infections = data['reportedCases'] * 10
    severe_impact_infected = data['reportedCases'] * 50
    impact = {}
    severeImpact = {}
    impact['currentlyInfected'] = impact_current_infections
    impact['currentlyInfected'] = impact_current_infections *512
    severeImpact['currentlyInfected'] = severe_impact_infected
    severeImpact['infectionsByRequestedTime'] = severe_impact_infected * 512

