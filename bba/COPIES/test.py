import matplotlib.pyplot as plt

pin = "12345"
print(pin)

pin = list(pin)
print(pin)
print(type(1))
print(type(pin))
print(type(pin[1]))
if type(1) == type(pin[1]):
    print(True)
else:
    print(False)