class printer:
    def __init__(self, model, colour):
        self.model = model 
        self.colour = colour 

    def document_printing(self):
        return f"{self.model} with {self.colour} colour is printing the documents ..."

    def stop(self):
        return f"{self.model} with {self.colour} colour is stop printing the documents ..."


# create the object for the printer class 
printer1 = printer("HP019", "off-white")

print(printer1.model)
print(printer1.colour)

print(printer1.document_printing())

print(printer1.stop())