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

    def get_station_info(self):
        return (self.id, self.name)


class Line:
    def __init__(self, color):
        self.line = list()
        self.color = color

    def add_station(self, station_object):
        self.line.append(station_object)

    def get_station(self, ind=None):
        if ind:
            return self.line[ind]
        else:
            return self.line

    def set_station(self, station):
        self.line[-1].add_neighbor(station.get_station_info())


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
    # for color in m.get_all_lines():
    #     for line_color in m.get_line(color):
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
get_requirement('file')
exit()

# START=Red Line:15
# END=Blue Line:36
# TRAINS=30
start = 0
end = 0
m = Map()
f = open('file','r')
lines = f.read()
lines = lines.split('\n')

for i in lines:
    if i.startswith('#'):
        try:
            m.append_line(train)
        except:
            pass
        train = Line(i[1:])
    elif i[:1].isdigit():
        if ":Conn:" not in i:
            id, name = i.split(":", 1)
            station = Station(id,name.strip(),None)
            train.line.append(station)
        else:
            id, name, _, connect = i.split(":")
            station = Station(id,name.strip(), connect.strip())
            train.line.append(station)
    elif "=" in i:
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

station_names = {}
for i in range(len(lines)):
    if lines[i][:1].isdigit():
        info = lines[i].split(":")
        if len(info) == 2:
            id, name = info[0], info[1]
        elif len(info) == 4:
            id, name, _, connect = info[0], info[1], info[2], info[3]
        try:
            if lines[i-1][:1].isdigit():
                station_names[name].append(lines[i-1][lines[i-1].find(":")+1:])
            if lines[i+1][:1].isdigit():
                station_names[name].append(lines[i+1][lines[i+1].find(":")+1:])
        except IndexError:
            continue
        except KeyError:
            station_names[name] = []
            if lines[i-1][:1].isdigit():
                station_names[name].append(lines[i-1][lines[i-1].find(":")+1:])
            if lines[i+1][:1].isdigit():
                station_names[name].append(lines[i+1][lines[i+1].find(":")+1:])


for i in range(len(m.map)):
    # print(m.map[i].name)
    # print(m.map[i].name)
    for j in range(len(m.map[i].line)):
        # print(m.map[i].line[j].connect)
        # print(m.map[i])
        if color_start in m.map[i].name and m.map[i].line[j].id == position_start:
            start = m.map[i].line[j]
            print( m.map[i].line[j].name)
        if color_end in m.map[i].name and m.map[i].line[j].id == position_end:
            end = m.map[i].line[j]
            print( m.map[i].line[j].name)


# print(color_start, position_start)
# print("-------------------------")
# print(color_end, position_end)
# print("-------------------------")
# print(leng_trains)


def beautiful_dict(_dict):
    for keys, values in _dict.items():
        for i in range(len(values)):
            tmp = _dict[keys][i].split(":")[0]
            _dict[keys][i] = tmp
    return _dict


def bfs(m, color_start, start, color_end, end):
    queue = collections.deque([[start]])
    # print(start.id, start.name, start.connect)
    seen = [start]
    station_names = beautiful_dict(station_names)
    while queue:
        # tmp = queue.popleft()
        # if color_start == color_end:
        path = queue.popleft()
        x = path[-1]
        if x.id == end.id:
            return path
        for nearby in station_names[x]:
            queue.append()
        # for i in range(len(m.map)):
        #     for j in range(len(m.map[i].line)):
        #         if x
        #         # print(m.map[i].name)
        #         if color_start in m.map[i].name and m.map[i].line[j].name not in station_names[]:
        #             print(path + [m.map[i].line[j]])
        #             sleep(1)
        #             queue.append(path + [m.map[i].line[j]])
        #             seen.append(m.map[i].line[j])

print(bfs(m, color_start, start, color_end, end))

# for i in path:
#     print(i.name)
    # around = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    # path = [start]
    # for i, j in around:
    #     x = start[0] + i
    #     y = start[1] + j
    #     if grid[x][y] != "#" and grid[x][y] not in aphal:
    #         path.append([x, y])
    # return path
