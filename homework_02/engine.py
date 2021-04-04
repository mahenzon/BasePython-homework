"""
create dataclass `Engine`
"""

class Engine():
    """ defaults """
    volume = None
    pistons = None


    def __init__(self, volume, pistons):

        self.volume = volume
        self.pistons = pistons
