def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
subjects = [  "Homeroom Guidance",  "Filipino",  "ICT",  "MAPEH",  "ESP",  "Chemistry",  "Research",  "Science",  "English",  "AP",  "Mathematics"]
def check(subject, due, title, description, atype):
    if subject == None:     return "subject is none"
    if due == None:         return "due is none"
    if title == None:       return "title is none"
    if atype == None:       return "type is none"

    #actual verif
    if subject not in subjects:     return "subject not in subject list"
    if not isfloat(due):            return "due is not a float/int"
    
    return 0
