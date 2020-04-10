def estimator(data):
    impact = {}
    severeImpact = {}
    impact.currentlyInfected = data.reportedCases * 10
    severeImpact.currentlyInfected = data.reportedCases * 50
    impact.infectionsByRequestedTime = impact.currentlyInfected * 2 ** 9
    severeImpact.infectionsByRequestedTime = severeImpact.currentlyInfected * 2 ** 9

