class Solution:
    def run(self, N, M):
        self.N = N
        self.M = M

    fizzbuzz = []
    try:
        N = int(input("Enter your starting number: "))
        M = int(input("Enter your ending number: "))
        for num in range(N, M + 1):
            if num % 3 == 0 and num % 5 == 0:
                fizzbuzz.append("FizzBuzz")
                continue
            elif num % 3 == 0:
                fizzbuzz.append("Fizz")
                continue
            elif num % 5 == 0:
                fizzbuzz.append("Buzz")
                continue
            else:
                fizzbuzz.append(str(num))
                continue
    except ValueError:
        print("Not a number, try again")

    print(f" {','.join(fizzbuzz)}")





