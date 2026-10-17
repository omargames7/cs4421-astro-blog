import serial

ser = serial.Serial("COM5", 115200)

while True:
    # get the values from the microbit
    line = ser.readline().decode("utf-8").strip()

    parts = line.split(",")

    temp = parts[0]
    moisture = parts[1]
    waterLevel = parts[2]

    # write the data into the csv file
    file = open("Artefact/LoggedData.csv", "a+")
    file.write(f"{temp},{moisture},{waterLevel}\n")
    file.close()

