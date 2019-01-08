import collections
from time import time, sleep


class Station:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.neighbor = []

    def add_neighbor(self, n_info):
        self.neighbor.append(n_info)

    def get_neighbor(self):
        return self.neighbor

    def add_color(color):
        self.color.append(color)


    def get_station_info(self):
        return (self.id, self.name)


class Line:
    def __init__(self, color):
        self.line = list()
        self.color = color

    def __getitem__(self, key):
         return self.line[key]

    def add_station(self, station_object):
        self.line.append(station_object)

    def get_station(self, ind=None):
        if ind:
            return self.line[ind]
        else:
            return self.line

    def set_station(self, station):
        self.line[-1].add_neighbor(station.get_station_info())

    def edit_station(self, station, neighbor):
        pass

class Map:
    def __init__(self):
        self.map = dict()

    def add_station(self, color, station):
        if color not in self.map.keys():
            self.map[color] = list()
        self.map[color].append(station)

    def add_line(self, color, line_object):
        self.map[color] = line_object

    def get_line(self, color):
        try:
            return self.map[color]
        except KeyError:
            print("Co' beep dau ma` lay'")

    def get_all_lines(self):
        return self.map.keys()


def read_file(file_name, choice):
    with open(file_name, 'r') as f:
        content = f.read()
    if choice == 'create_map':
        return content
    if choice == 'get_requirement':
        content = content.split('\n')
        return content[-4:]


def get_requirement(file_name):
    requirement = read_file(file_name, 'get_requirement')
    for i in requirement:
        if "=" in i:
            if "START" in i:
                line_start, position = i.split()
                _, color_start = line_start.split("=")
                _, position_start = position.split(":")
            elif  "END" in i:
                line_end, position = i.split()
                _, color_end = line_end.split("=")
                _, position_end = position.split(":")
            else:
                _, leng_trains = i.split("=")
    return (color_start, position_start, color_end, position_end, leng_trains)


def create_map(file_name):
    # Create map
    line_station = dict()
    #key = (red, blue) or (blue, red); values= [], values[0] =(id_red, name_red), values[1] = (id_blue, name_blue)
    m = Map()
    content = read_file(file_name, 'create_map')
    color_section = content.split("#")[1:]
    for section in color_section:
        tmp = section.split('\n')[:-1]
        color = tmp[0]
        line = Line(color)
        if section == color_section[-1]:
            tmp = section.split('\n')[:-5]
        last_station = None
        for i in range(1, len(tmp)):
            info = tmp[i].split(':')
            station = Station(info[0], info[1])
            if(len(info) == 4):
                if tuple(sorted([color, info[3][1:]])) not in line_station.keys():
                    line_station[tuple(sorted([color, info[3][1:]]))] = list()
                # if(station not in line_station[tuple(sorted([color, info[3][1:]]))]):
                line_station[tuple(sorted([color, info[3][1:]]))].append(station)

            if last_station == None:
                last_station = station
            else:
                station.add_neighbor(last_station.get_station_info())
                line.set_station(station)
                # print(line.get_station(-1).get_station_info())
                # print(line.get_station(-1).get_neighbor())
                last_station = station
            line.add_station(station)
        m.add_line(color, line)

    # add neighbor of station which in many line
    print("........................")
    for keys, values in line_station.items():
        if(len(values) == 4):
            print(keys)
            for i in values:
                print(i.get_station_info())
        # if 3 == len(values):
        # for i in range(len(keys)):
        #     print(i)


    # for color in m.get_all_lines():
    #     for line_color in m.get_line(color):
    # print(line_station)
    print("........................")
    return
    for line in m.map:
        for keys, values in m.map.items():
            for station in values.line:
                if station.get_station_info()[1] == 'Kashmere Gate':
                    print(station.neighbor)
                # print(station.get_station_info())
                # print ("co neighbor la: ")
                # print(station.neighbor)
                # print("------------------")
    return m

create_map('file')
get_requirement('delhi')
exit()

# START=Red Line:15
# END=Blue Line:36
# TRAINS=30
