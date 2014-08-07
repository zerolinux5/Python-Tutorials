class AthleteList(list):
        def __init__(self, a_name, a_dob=None, a_times=[]):
                list.__init__([])
                self.name = a_name
                self.dob = a_dob
                self.extend(a_times)
        def top3(self):
                return(sorted(set([sanitize(t) for t in self]))[0:3])

def sanitize(times):
        if '-' in times:
                splitter = '-'
        elif ':' in times:
                splitter = ':'
        else:
                return(times)
        (mins, secs) = times.split(splitter)
        return(mins + '.' + secs)
