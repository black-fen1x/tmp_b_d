import json
import codecs
import re
from datetime import datetime 

def findTeacher(teacher="", day="", time="",schedule={}): 
    lessons = schedule[teacher][day]
    if (len(lessons) == 0):
        return None
    needTime = datetime.strptime(time, "%H:%M").time()
    for lesson in lessons:
        lessonTime = datetime.strptime(lesson["time"], "%H:%M").time()
        if (needTime <= lessonTime):
            return lesson
    return None

def findTeacherOnAllDay(teacher="", day="", schedule={}):
    lessons = schedule[teacher][day]
    if (len(lessons) == 0):
        return None
    return lessons

def lessonToString(lesson={}):
    nameOfLesson = lesson.get("nameOfLesson")
    groups = lesson.get("groups")
    office = lesson.get("office")
    typesOfLesson = lesson.get("type")
    timeOfLesson = lesson.get("time")
    strGroups = ""
    for group in groups:
        strGroups += f"{group}; "
    strGroups = strGroups[0:len(strGroups) - 2]
    strTypeOfLesson = ""
    for lessonType in typesOfLesson:
        strTypeOfLesson += f"{lessonType}\n"
    strTypeOfLesson = strTypeOfLesson[0:len(strTypeOfLesson) - 1]
    return f"{nameOfLesson}\nКабинет: {office}\nВремя: {timeOfLesson}\nГруппы: {strGroups}\nВид занятия:\n{strTypeOfLesson}"

def findGroup(group="", day="", time="", schedule={}):
    teachers = schedule.keys()
    needTime = datetime.strptime(time, "%H:%M").time()
    for teacher in teachers:
        lessons = schedule.get(teacher).get(day)
        if (lessons != None):
            for lesson in lessons:
                groups = lesson["groups"]
                lessonTime = lessonTime = datetime.strptime(lesson["time"], "%H:%M").time()
                for grp in groups:
                    if grp in group and needTime <= lessonTime:
                        return lesson
    return None

def getSchedule():
    fileObj = codecs.open( "test.json", "r", "utf_8_sig" )
    schedule: dict = json.load(fileObj)
    return schedule

def getAvailableGroups():
    schedule = getSchedule()
    groups = set()
    regExps = []
    regExps.append(re.compile("\d\d[а-яА-Я]{2,}"))
    regExps.append(re.compile("\d\d-[а-яА-Я]{2,}"))
    for teacherKey in schedule.keys():
        teacherSchedule = schedule.get(teacherKey)
        for dayKey in teacherSchedule.keys():
            lessons = teacherSchedule.get(dayKey)
            for lesson in lessons:
                lessonGroups = lesson.get("groups")
                for group in lessonGroups:
                    match = None
                    for regEx in regExps:
                        match = regEx.search(group)
                        if (match != None):
                            break
                    if match != None:
                        groupSplited = group.split(",")
                        for grSpl in groupSplited:
                            for regEx in regExps:
                                match = regEx.search(grSpl)
                                if match!= None:
                                    groups.add(re.sub("нч|чн|\.", "", grSpl))
    return sorted(list(groups))

def main():
    fileObj = codecs.open( "test.json", "r", "utf_8_sig" )
    schedule: dict = getSchedule()
    # print(findTeacher('Бухнин Алексей Викторович', "Понедельник", "13:10", schedule))
    # print(findGroup('20СБК', 'Понедельник', '10:50', schedule))
    print(getAvailableGroups())

if __name__ == "__main__":
    main()