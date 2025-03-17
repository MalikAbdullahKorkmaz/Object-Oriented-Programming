# Vehicles - Demonstrating Polymorphism
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "The car is driving on the road."

class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is pedaling on the path."

class Boat(Vehicle):
    def move(self):
        return "The boat is sailing on the water."

# Demonstrating polymorphism
vehicles = [Car(), Bicycle(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())


# User Authentication - Demonstrating Polymorphism
class UserAuthentication:
    def login(self):
        pass

class EmailPasswordAuth(UserAuthentication):
    def login(self):
        return "Logging in with email and password."

class GoogleAuth(UserAuthentication):
    def login(self):
        return "Logging in with Google authentication."

class FingerprintAuth(UserAuthentication):
    def login(self):
        return "Logging in with fingerprint authentication."

# Demonstrating polymorphism
auth_methods = [EmailPasswordAuth(), GoogleAuth(), FingerprintAuth()]
for auth in auth_methods:
    print(auth.login())
