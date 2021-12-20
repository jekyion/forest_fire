import csv
import matplotlib.pyplot as plt
import os
import glob

from .agents import *

class Csv_writer:
    iterator = 0

    def __init__(self, firefighters):
        # self.file = open('simulation_data.csv', 'w', encoding='utf-8', newline='')
        self.file2 = open('simulation_individuality_1.csv', 'w', encoding='utf-8', newline='')
        self.file3 = open('simulation_individuality_2.csv', 'w', encoding='utf-8', newline='')
        self.file4 = open('simulation_activity.csv', 'w', encoding='utf-8', newline='')
        self.file5 = open('simulation_activity_locations.csv', 'w', encoding='utf-8', newline='')
        self.indiv_1_data = list()
        self.indiv_2_data = list()
        self.sectors_types = list()
        self.graph_indiv_1_data = list()
        self.graph_indiv_2_data = list()

        for x in range(20):
            self.sectors_types.append([])

        # print(self.sectors_types)
        for x in range(800):
            self.indiv_1_data.append([[], [], [], [], []])
            self.graph_indiv_1_data.append([[], [], [], [], [], []])
            self.indiv_2_data.append([[], [], [], []])
            self.graph_indiv_2_data.append([[], [], [], [], []])

        self.firefighters_limit = firefighters
        self.firefighters_list = list()

        for x in range(self.firefighters_limit):
            self.firefighters_list.append([])


    def save_indiv_1_graphs(self):
        files = glob.glob('.\graphs\indiv_1\*')
        for f in files:
            os.remove(f)
        iteracje = [x for x in range(1, Csv_writer.iterator+1)]

        title = ''
        i = 0

        for sectors in self.graph_indiv_1_data:
            if sectors[5][0] is not None:

                print(sectors[1][0])
                print(((sum(sectors[1])) / len(sectors[1])))
                if abs(((sum(sectors[1])) / len(sectors[1])) - sectors[1][0])>1:
                    figure = plt.figure()
                    plt.plot(iteracje, sectors[1])
                    plt.plot(iteracje, sectors[2])
                    plt.plot(iteracje, sectors[3])
                    plt.plot(iteracje, sectors[4])
                    title = sectors[0][0]
                    i += 1

                    plt.title('Idividualtiy_1 for sector ' + title)
                    plt.legend(['Temperatura', 'Wilgotność Powietrza', 'Wilgotność Ściółki', 'Prędkość Wiatru'])
                    plt.savefig('.\graphs\indiv_1\sector_' + title)
                    plt.close(figure)




    def write_indiv_1(self, sectors_data):
        i = 0

        for key, values in sectors_data.items():
            if Csv_writer.iterator == 0:
                self.indiv_1_data[i][0].append('Sektor: ' + str(key))
                self.indiv_1_data[i][1].append('Temperatura')
                self.indiv_1_data[i][2].append('Wilgotność powietrza')
                self.indiv_1_data[i][3].append('Wilgotność Ściółki')
                self.indiv_1_data[i][4].append('Prędkość Wiatru')
                self.graph_indiv_1_data[i][0].append(str(key))

            self.indiv_1_data[i][1].append(values['temperature'])
            self.indiv_1_data[i][2].append(values['air_humidity'])
            self.indiv_1_data[i][3].append(values['litter_moisture'])
            self.indiv_1_data[i][4].append(values['wind_speed'])

            self.graph_indiv_1_data[i][1].append(values['temperature'])
            self.graph_indiv_1_data[i][2].append(values['air_humidity'])
            self.graph_indiv_1_data[i][3].append(values['litter_moisture'])
            self.graph_indiv_1_data[i][4].append(values['wind_speed'])
            self.graph_indiv_1_data[i][5].append(values['sector_state'])
            i += 1

    def write_indiv_2(self, sectors_data):
        i = 0
        for key, values in sectors_data.items():
            if Csv_writer.iterator == 0:
                self.indiv_2_data[i][0].append('Sektor: ' + str(key))
                self.indiv_2_data[i][1].append('Prędkość Wiatru')
                self.indiv_2_data[i][2].append('Stężenie CO2')
                self.indiv_2_data[i][3].append('Stężenie PM2.5')

            self.indiv_2_data[i][1].append(values['wind_speed'])
            self.indiv_2_data[i][2].append(values['co2'])
            self.indiv_2_data[i][3].append(values['pm25'])
            i += 1

    def write_activity(self, firefighter_locations):
        i = 0
        if Csv_writer.iterator == 0:
            for x in self.firefighters_list:
                x.append('Wóż strażacki nr: ' + str(i+1))
                i += 1

        i2 = 0
        for y in range(self.firefighters_limit):
            if i2 < len(firefighter_locations):
                self.firefighters_list[i2].append(firefighter_locations[i2])
            else:
                self.firefighters_list[i2].append('')
            i2 += 1

        # print(firefighter_locations)

    def write_activity_locations(self, sectors_data):
        if Csv_writer.iterator == 0:
            i = 0
            keys = sectors_data.keys()
            # print(keys)
            for x in self.sectors_types:

                for y in range(40):
                    if i in keys:
                        x.append(sectors_data[i]['forest_type'])
                    else:
                        x.append('0')
                    i += 1




    def save_extinguished_fires(self):
        csvwriter = csv.writer(self.file4)
        csvwriter.writerow(['Pożary ugaszone przez wozy strażackie: '])
        csvwriter.writerow([])



        i = 1
        for values in Firefighter.ugaszono.values():
            out1 = ['Wóz strażacki nr: ', i]
            out2 = ['Sektory: ']
            for x in values:
                out2.append(x)
            i += 1
            csvwriter.writerow(out1)
            csvwriter.writerow(out2)




    def save_to_file(self):

        csvwriter = csv.writer(self.file2)
        csvwriter_2 = csv.writer(self.file3)
        csvwriter_3 = csv.writer(self.file4)
        csvwriter_4 = csv.writer(self.file5)

        header = list()
        header.append('Nr iteracji')

        for i in range(Csv_writer.iterator):
            header.append(i + 1)

        csvwriter.writerow(header)
        csvwriter_2.writerow(header)
        csvwriter_3.writerow(header)


        for x in self.indiv_1_data:
            csvwriter.writerows(x)

        for x in self.indiv_2_data:
            csvwriter_2.writerows(x)

        csvwriter_3.writerows(self.firefighters_list)
        csvwriter_3.writerows([[],[],[]])
        csvwriter_4.writerows(self.sectors_types)

        location_descriptions = [['Rodzaje lasu: '], ['Brak lasu', '0'], ['Las liściasty', '1'], ['Las mieszany','2'], ['Las iglasty','3']]

        csvwriter_4.writerows(location_descriptions)

    def close_file(self):
        # self.file.close()
        self.save_extinguished_fires()
        self.file2.close()
        self.file3.close()
        self.file4.close()
        self.file5.close()
        print("Liczba iteracji: " + str(Csv_writer.iterator))

        Csv_writer.iterator = 0


