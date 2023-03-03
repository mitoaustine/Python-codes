class Temperature:
    def __init__(self,celsius,fahrenheit):
        self.celsius=celsius
        self.fahrenheit=fahrenheit
    def covert_fahrenheit(self):
        method1=(self.celsius*9/5)+32
        print("celsius to fahrenheit is:",method1)
    def covert_celsius(self):
        method2=(32*self.fahrenheit-32)*5/9 
        print("fahrenheit to celsius is:",method2)
cel=Temperature(10,32)  
cel.covert_fahrenheit()
cel.covert_celsius()
        
        