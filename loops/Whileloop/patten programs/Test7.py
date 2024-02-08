class MyPatterns:
    def A_method(self):
        n = 5
        for i in range(n):
            for j in range(n):
                if j == 0 or i == 0 or i == 2 or j == 4:
                    print('*', end='  ')
                else:
                    print(end='   ')
            print()
    def B_method(self):
        for a in range(5):
            for b in range(5):
                if b == 0 or a == 0 or a == 2 or b == 4 or a == 4:
                    print('*', end='  ')
                else:
                    print(end='   ')
            print()
        
            
            
# Create an instance of the class
patterns = MyPatterns()

# Call the A_method
patterns.A_method()
patterns.B_method()

