FOLDER = "swimdata/"
import statistics

def read_swim_data(filename):

    """ Return swim data from a file.
    
    Given the name of a swimmer's file (in filename), extract all the required data,
    then return it to the caller as a tuple."""
    
    swimmer, age, distance, stroke = filename.removesuffix('.txt').split('-')

    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip().split(',')

    converts = []
    for t in times:
        # not all the times include a 'minutes' value  so need to handle both cases
        if ':' in t:
            minutes, rest = t.split(":")
            seconds, hundredths = rest.split(".")
        else:
            seconds, hundredths = t.split(".")
            minutes = 0
        converts.append((int(minutes) * 60*100) + (int(seconds)*100) + int(hundredths))


    average = statistics.mean(converts)
    mins_secs, hundredths = str(round(average / 100,2)).split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes*60
    average = str(minutes) + ":" + str(seconds) + "." + hundredths

    return swimmer, age, distance, stroke, times, average # returned as a tuple
