import pygal
file = open("Artefact/LoggedData.csv", "r")

# calling the lists
global temperatureList, moistureList, waterLevelList
temperatureList = []
moistureList = []
waterLevelList = []
riskResults = []

# drought risk function
def calculateDroughtRisk(temp, moisture, waterLevel):
    if (temp > 35 or temp < 0) or moisture < 20:
        risk = "High"
    elif (temp > 30 or temp < 5) or moisture < 30 or waterLevel < 50:
        risk = "Medium"
    else:
        risk = "Low"
    return risk

# function to create a graph
def createGraph(fileName):

    riskResults.clear()

    # calculate risk percentage

    for entry in range(len(temperatureList)):
        riskAmount = calculateDroughtRisk(temperatureList[entry], moistureList[entry], waterLevelList[entry])
        riskResults.append(riskAmount)

    high_count = riskResults.count("High")
    medium_count = riskResults.count("Medium")
    low_count = riskResults.count("Low")

    riskPercentage = round(((high_count * 100) + (medium_count * 50)) / (high_count + medium_count + low_count), 2)
    print("Drought risk: " , riskPercentage , "%")

    # create graph using the data from the lists and the risk percentage

    chart = pygal.Line()
    chart.range = (0, 100)
    chart.title = f"Drought Risk: {riskPercentage}%"
    chart.x_labels = map(str, range(1, 25))
    chart.x_title = "Time (Hours)"
    chart.y_title = "Values (Celsius / %)"

    chart.add("temperature", temperatureList)
    chart.add("moisture", moistureList)
    chart.add("water level", waterLevelList)

    chart.render_to_file(f"Artefact/{fileName}.svg")

# create a graph using collected data
for line in file:
    content = line.strip()
    parts = content.split(",")
    temperatureList.append(float(parts[0]))
    moistureList.append(float(parts[1]))
    waterLevelList.append(float(parts[2]))
print("--- Collected Data ---")
createGraph("Collected_Data")

# What if 1
for value in range(len(temperatureList)):
    temperatureList[value] += 10

print("--- What if Temperature Increases? ---")
createGraph("WhatIf1")

# bring back the old lists
for value in range(len(temperatureList)):
    temperatureList[value] -= 10

#  What if 2

moistureList = [70, 68, 66, 64, 61, 57, 52, 45, 38, 32, 29, 58, 55, 51, 47, 43, 39, 35, 31, 28, 26, 24, 22, 20]
waterLevelList = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print("--- What if Water present in the reservoir is low (Moisture renews once) ---")
createGraph("WhatIf2")

file.close() 

