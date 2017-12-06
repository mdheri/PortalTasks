from datetime import datetime

class events:
    def __init__(self,event:str, date:list, time1: list,time2:list,abbreviation = True):
        self.event = event
        self.date = date
        self.time1 = time1
        self.time2 = time2
        self.abbreviation = abbreviation

    def __repr__(self):
        dates = {1:"January",2:"Febuary",3:"March", 4:"April",5:"May", 6:"June", 7:"April", 8: "August",9:"September",10:"October",11:"Novemer",12:"December"}
        if(self.abbreviation):
            return "{} {} {}, {} {}:{}{} - {}:{}{}".format(self.event,dates[self.date[0]][:3],self.date[1],self.date[2],self.time1[0],self.time1[1],self.time1[2],self.time2[0],self.time2[1],self.time2[2])
        return "{} {} {}, {} from {}:{}{} to {}:{}{}".format(self.event, dates[self.date[0]][:3], self.date[1], self.date[2],
                                                       self.time1[0], self.time1[1], self.time1[2], self.time2[0],
                                                       self.time2[1], self.time2[2])

    def __eq__(self, other):
        if self.event == other.event:
            return True
        return False

    def convertTime(self):
        if self.time1[0] == 12:
            self.time1[0] = 0
        if self.time1[2] == "PM":
            self.hours1 = self.time1[0]+12
        else:
            self.hours1 = self.time1[0]
        if self.time1 == 00:
            self.hours1 += self.time1[1]/60

        if self.time2[0] == 12:
            self.time2[0] = 0
        if self.time2[2] == "PM":
            self.hours2 = self.time2[0] + 12
        else:
            self.hours2 = self.time2[0]
        if self.time2 != 00:
            self.hours2 += self.time2[1]/60


def checkOverlap(event1,event2):
    event1.convertTime()
    event2.convertTime()
    if event1.date == event2.date:
        if event1.hours1 <= event2.hours1:
            if event1.hours2 >= event2.hours1:
                return True
        if event2.hours1 <= event1.hours1:
            if event2.hours2 >= event1.hours1:
                return True

    return False


if __name__ =="__main__":
    e1 = events("Interview at the Portal:",[2,23,2017],[3,00,"PM"],[4,30,"PM"])
    e2 = events("'Lunch with Cindy' on", [2,23,2017],[12,00,"PM"],[1,00,"PM"], abbreviation= False)
    e3 = events("Dinner with John:", [2,23,2017],[5,00,"PM"],[5,30,"PM"])
    e4 = events("Conference:",[2,24,2017],[11,00,"AM"],[5,30,"PM"])
    e5 = events("Work:",[2,24,2017],[2,00,"PM"],[9,30,"PM"])
    e6 = events("ICS 45C Class:",[2,25,2017],[3,00,"PM"],[4,30,"PM"])
    e7 = events("Project:",[2,26,2017],[3,00,"PM"],[7,30,"PM"])
    e8 = events("Meeting with Ted:",[2,24,2017],[11,00,"AM"],[4,30,"PM"])

    allEvents = [e1,e2,e3,e4,e5,e6,e7,e8]

    print("Your Claender Events are: \n")

    for i in allEvents:
        print(i)
        i.convertTime()
    print("\n\n")

    result = []

    for i in allEvents:
        for j in allEvents:
            if i != j:
                if checkOverlap(i, j):
                    result.append("{} overlaps with {}".format(i,j))


    for i in result:
        print(i)

