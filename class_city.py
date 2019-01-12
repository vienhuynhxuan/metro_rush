import collections
from time import time, sleep
import queue as Q

class Station:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.neighbor = []

    def add_neighbor(self, n_info):
        self.neighbor.append(n_info)

    def get_neighbor(self):
        return self.neighbor

    def get_station_info(self):
        return (self.id, self.name)

class Line():
    def __init__(self, color):
        self.line = list()
        self.color = color


    def add_station(self, station_object):
        self.line.append(station_object)


    def get_station(self, name):
        for station in self.line:
            if station.name == name:
                return station
        return None

    def modify_neighbor_station(self, color, neighbor, name_station=None):
        if name_station is None:
            self.line[-1].add_neighbor((color, ) + neighbor.get_station_info())
        else:
            for station in self.line:
                if station.name == name_station:
                    station.add_neighbor((color, ) + neighbor.get_station_info())

class Map:
    def __init__(self):
        self.map = dict()

    def add_line(self, color, line_object):
        self.map[color] = line_object

    def get_line(self, color):
        try:
            return self.map[color]
        except KeyError:
            print("Co' beep dau ma` lay'")

    def get_all_lines(self):
        return self.map.keys()

    def find_station(self, info):
        line = self.map[info[1]]
        return line.get_station(info[3])


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


def add_others_neighbor(line_station, m):
    for station in line_station:
        neighbors = list()
        for line in line_station[station]:
            tmp = m.map[line].get_station(station)
            if tmp is not None:
                neighbors.extend(tmp.get_neighbor())
        neighbors = list(neighbors)

        for line in line_station[station]:
            for neighbor in neighbors:
                tmp = m.map[line].get_station(station)
                if tmp is not None:
                    if neighbor not in tmp.get_neighbor():
                        tmp.add_neighbor(neighbor)


def create_map(file_name):
    line_station = dict()
    # Create map
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
            if len(info) == 4:
                if station.name not in line_station.keys():
                    line_station[station.name] = list()
                if color not in line_station[station.name]:
                    line_station[station.name].append(color)
                if info[3][1:] not in line_station[station.name]:
                    line_station[station.name].append(info[3][1:])

            if last_station == None:
                last_station = station
            else:
                station.add_neighbor((color,) + last_station.get_station_info())
                line.modify_neighbor_station(color, station)
                last_station = station
            line.add_station(station)
        m.add_line(color, line)

    add_others_neighbor(line_station, m)
    # for keys, values in m.map.items():
    #     print(keys)
    #     for station in values.line:
    #         print("--", end = "")
    #         print(station.get_station_info(), end= " co neighbor:\n")
    #         for city in station.get_neighbor():
    #             print("\t", city)
    return m

def remove_element(lst, value):
    print(lst)
    for ele in lst:
        if ele[1:] == value:
            lst.remove(ele)
    return lst


def bfs(requirement, self):
    transper = 0
    path = []
    visited = []
    print(requirement)
    tmp = (0, "Red Line", '15', "Keshav Puram")
    destination = ("Red Line", 12, "Shastri Nagar")
    destination = ('Blue Line', '36', "Mayur Vihar Phase-1")
    #destination = ('Red Line', '14', 'Kanhaiya Nagar')
    queue = Q.PriorityQueue()
    queue.put(tmp)
    count = 0
    while queue.qsize():
        info_station = queue.get()
        path.append(info_station)
        if info_station[1:] == destination:
            count += 1
            path.append(path)
            print("lennn: ", len(visited))
            visited = remove_element(visited, destination)
            print("lennn: ", len(visited))
        station = self.find_station(info_station)
        for ele in station.get_neighbor():
            if ele not in visited:
                print("elelele: ", ele)
                visited.append(ele)
                turn = info_station[0] + 1
                if info_station[1] != ele[0]:
                    transper += 1
                    turn += 1
                queue.put((turn, ) + ele)

    print(transper)
    print(len(path))
    print(count)


m = create_map('file')

bfs(get_requirement('file'), m)
