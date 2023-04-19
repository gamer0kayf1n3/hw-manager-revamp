def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
import re
datematch = r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}"
subjects = [  "Homeroom Guidance",  "Filipino",  "ICT",  "MAPEH",  "ESP",  "Chemistry",  "Research",  "Science",  "English",  "AP",  "Mathematics"]
def check(subject, due, title, description, atype):
    if subject == None:     return "subject is none"
    if due == None:         return "due is none"
    if title == None:       return "title is none"
    if atype == None:       return "type is none"

    #actual verif
    if subject not in subjects:     return "subject not in subject list"
    if not re.match(datematch, due):return "date invalid"
    return 0
