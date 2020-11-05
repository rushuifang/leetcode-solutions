class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = defaultdict(list)
        for path in paths:
            cities[path[0]] += [0]
            cities[path[1]] += [1]

        for key in cities:
            if cities[key] == [1]:
                return key


# Faster one:
def destCity(self, paths: List[List[str]]) -> str:
    cityFrequency = dict()
    for cities in paths:
        if cities[0] in cityFrequency:
            cityFrequency[cities[0]] += 1
        else:
            cityFrequency[cities[0]] = 1

        if cities[1] in cityFrequency:
            cityFrequency[cities[1]] += 1
        else:
            cityFrequency[cities[1]] = 1

    for cities in paths:
        if cityFrequency[cities[1]] == 1:
            return cities[1]
