#!/usr/bin/python2

import random

class FreeTimeRange:
    def __init__(self, day, start, end):
        self.day = day
        self.start = start
        self.end = end
    
    def __repr__(self):
        return "Day %d from %d to %d" % (self.day, self.start, self.end)

class ClassInfo:
    def __init__(self, members_in_team, hours_per_week):
        self.members_in_team = members_in_team
        self.hours_per_week = hours_per_week

class Student:
    def __init__(self, name, free_times):
        self.name = name
        self.free_times = free_times
        self.matched = False
    
    def __repr__(self):
        return self.name + " " + " " + str(self.matched)

def matcher(class_info, students):
    groups = []
    for student in students:
        if student.matched:
            continue
        group = [student]
        for i in xrange(class_info.members_in_team):
            findMatchingStudent(class_info, students, student, group)
        student.matched = True
        groups.append(group)
    return groups

def findMatchingStudent(class_info, students, student, group):
    for otherStudent in students:
        if otherStudent is student:
            continue
        if otherStudent.matched:
            continue
        commonSegments = 0
        for i in xrange(7):
            commonTime = findCommonTime(i, otherStudent, group)
            if commonTime is not None:
                commonSegments += commonTime.end - commonTime.start
        if commonSegments * 30 >= class_info.hours_per_week:
            otherStudent.matched = True
            group.append(otherStudent)
            return

def findCommonTime(i, student, group):
    timeRange = FreeTimeRange(0, student.free_times[i].start, student.free_times[i].end)
    for otherMember in group:
        timeRange.start = max(timeRange.start, otherMember.free_times[i].start)
        timeRange.end = min(timeRange.end, otherMember.free_times[i].end)
    if timeRange.start >= timeRange.end:
        return None
    else:
        return timeRange


class_info = ClassInfo(3, 30)

students = []
for i in xrange(40):
    free_times = []
    for j in xrange(7):
        free_time = FreeTimeRange(j, random.randint(0, 47), 0)
        free_time.end = random.randint(free_time.start + 1, 48)
        free_times.append(free_time)
    students.append(Student("A " + str(i), free_times))

results = matcher(class_info, students)

print(results)
print(len(results))
