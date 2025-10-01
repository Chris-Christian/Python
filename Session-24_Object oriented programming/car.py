class car:                                               
    def __init__(self,model,year,color,for_sale):           #Constructor
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):                                        #methods
        print(f"You drive the {self.color} {self.model}")
    def stop(self):
        print(f"{self.color} {self.model} stopped")
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
