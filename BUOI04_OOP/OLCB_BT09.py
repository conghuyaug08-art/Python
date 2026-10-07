class NhietDo:
    def __init__(self, celcius = 0.0):
        if celcius < -273.15:
            self.celcius = -273.15
        else:
            self.celcius = celcius
            
    def Farenheit(self):
        return self.celcius * 1.8 + 32
    
    def Kelvin(self):
        return self.celcius + 273.15
    
    def HienThi(self):
        print(f"Celcius: {self.celcius:.2f}")
        print(f"Farenheit: {self.Farenheit():.2f}")
        print(f"Kelvin: {self.Kelvin():.2f}")
        
def main():
    t = NhietDo(40)
    t.HienThi()
    
if __name__ =="__main__":
    main()