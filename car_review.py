import pickle

class Car:
    def __init__(self):
        self.plate = None
        self.exists = False
        self.year = None
        self.make = None
        self.model = None
        self.smodel = None
        self.bstyle = None
        self.vin = None

    def __str__(self):
        str = ""
        if self.exists:
            if self.year is not None:
                str += "Year: " + self.year + "\n"
            if self.make is not None:
                str += "Make: " + self.make + "\n"
            if self.model is not None:
                str += "Model: " + self.model + "\n"
            if self.smodel is not None:
                str += "Submodel: " + self.smodel + "\n"
            if self.bstyle is not None:
                str += "Body Style: " + self.bstyle + "\n"
            if self.vin is not None:
                str += "VIN: " + self.vin + "\n"
        else:
            str = "Plate: " + self.plate + " has never been registered" + "\n"

        return str


output_cars = "/Users/oscar/Projects/syn/trawler/output_cars.obj"
filehandler = open(output_cars, 'rb')

test = pickle.load(filehandler)

for i in test:
    print(i)