# Global variable
fuel_level = 100

def fly_ship():
    # Local variable with the same name
    fuel_level = 50
    print(f"Internal fuel level: {fuel_level}")

fly_ship()
print(f"External fuel level: {fuel_level}")