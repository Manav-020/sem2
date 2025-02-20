class convertor:
    values={
        "inches": 1,
        "feet": 1 / 12,
        "yards": 1 / 36,
        "miles": 1 / 63360,
        "kilometers": 1 / 39370.1,
        "meters": 1 / 39.3701,
        "centimeters": 1 / 0.393701,
        "millimeters": 1 / 0.0393701
    }
    
    def __init__(self,length,unit):
        self.lenght=length
        self.unit=unit
        self.inches=length/self.values[unit]
    def meters(self):
            return self.lenght*self.values["meters"]
    def yards(self):
            return self.lenght*self.values["yards"]
    def kilometers(self):
            return self.lenght*self.values["kilometers"]
    def millimeters(self):
            return self.lenght*self.values["millimeters"]
    def miles(self):
            return self.lenght*self.values["miles"]
    def centimeters(self):
            return self.lenght*self.values["centimeters"]
    
c=convertor(9,"inches")
print("value in feet is:",c.feet())