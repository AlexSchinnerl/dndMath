# Helper Functions

def calc_growth(old_value, new_value):
    # returns an array [abulute value, relative value]
    return [new_value-old_value, (new_value-old_value)/old_value]
