from CSVParser.Helper import Helper
car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
# car_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Car.csv'
motor_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Motorcycle.csv'
bike_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Bicycle.csv'
run_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Run.csv'
walk_path = '/home/phatthanapong/Desktop/City/PyCity/Data/Walk.csv'

data = []
Helper = Helper()
Car = Helper.reader(car_path)
car_speed =[]
speed = []
zero = []
inn = []
temp = None
for car in Car:
    found = 0
    for idx, val in enumerate(car):
        if idx != 0:
            if idx == 206:
                print(val)
            if idx == 207:
                print(val)
            if temp > val['time']:
                print("Del")
                print(idx,temp,val['time'])


        temp = val['time']
    break