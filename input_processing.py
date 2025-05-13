# input_processing.py
# <YOUR NAME>, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:


    def __init__(self):
        
        # initialze with default values from specs
        self.light_colour = "green"
        self.ped_status = "no"
        self.vehicle_status = "no"

    def update_status(self, status_type, status_change): # You may decide how to implement the arguments for this function
        if status_type == "1":
            self.light_colour = status_change
        elif status_type == "2":
            self.ped_status = status_change
        elif status_type == "3":
            self.vehicle_status = status_change
        else:
            print("Error: invalid arguments")



# This function takes a Sensor object as input, prints the Action, followed 
# by the current status of traffic light, pedestrian, and vehicle.
def print_message(sensor):
    if (sensor.light_colour == "red") or (sensor.ped_status == "yes") or (sensor.vehicle_status == "yes"):
        print("STOP", "\n")

    elif (sensor.light_colour == "yellow") and (sensor.ped_status == "no") and (sensor.vehicle_status == "no"):
        print("CAUTION", "\n")
    
    else:
        print("PROCEED", "\n")
        
    print("Light = ", sensor.light_colour, " , Pedestrian = ", sensor.ped_status, " , Vehicle = ", sensor.vehicle_status, " .")


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    # initialize an instance of Sensor
    sensor = Sensor()

    # get user input for the change type (1, 2, 3, or 0)
    # input_type = None

    while True:

        input_type = input("Are any changes detected in the vision input? Enter '1' for traffic light, '2' for pedestrian, '3' for vehicle, or '0' to exit program: ")
        
        # end the program
        if input_type == "0":
            break 

        # change traffic light colour
        elif input_type == "1":

            valid_colours = ["red", "yellow", "green"]

            # get valid input for traffic light status 
            while True:
                input_colour_status = input("What change has been identified? ")
                if input_colour_status not in valid_colours:
                    print("Invalid vision change")
                    continue
                else:
                    break

            sensor.update_status(input_type, input_colour_status)
            print_message(sensor)

        # change pedestrian status    
        elif input_type == "2":

            valid_ped_status = ["yes", "no"]
            input_ped_status = None

            # get valid input for pedestrian status
            while True:
                input_ped_status = input("What change has been identified? ")
                if input_ped_status not in valid_ped_status:
                    print("Invalid vision change")
                    continue
                else:
                    break

            sensor.update_status(input_type, input_ped_status)
            print_message(sensor)

        # change vehicle status
        elif input_type == "3":
            
            valid_vehicle_status = ["yes", "no"]

            # get valid input for vehicle status
            while True:
                input_vehicle_status = input("What change has been identified? ")                   
                if input_vehicle_status not in valid_vehicle_status:
                    print("Invalid vision change")
                    continue
                else:
                    break
            

            sensor.update_status(input_type, input_vehicle_status)
            print_message(sensor)
        else:
            print("You must select either 1, 2, 3, or 0")


    
    print("Closing Vision Detection Program")    
    
    





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

