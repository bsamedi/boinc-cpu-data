import re

def parse_cpu_description(desc):
    g = re.match('(?:(\S+)? (.+?)?(?: @ ([0-9.]+[MGTP]Hz))? \[Family (\S+)? Model (\S+)? Stepping (\S+)?\])?', desc)
    #                 Make   Name        Frequency
    return {
        'Make': g.group(1),
        'Name': g.group(2),
        'Frequency': g.group(3),
        'Family': g.group(4),
        'Model': g.group(5),
        'Steppping': g.group(6),
        'original_text': desc
    }
