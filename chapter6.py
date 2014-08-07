def coach_data(filename):
        try:
                with open(filename) as f:
                        data = f.readline()
                return(data.strip().split(','))
        except IOError as ioerr:
                print('File error: ' + str(ioerr))
                return(None)

def sanitize(times):
        if '-' in times:
                splitter = '-'
        elif ':' in times:
                splitter = ':'
        else:
                return(times)
        (mins, secs) = times.split(splitter)
        return(mins + '.' + secs)


