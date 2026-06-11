class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        for power, coef in enumerate(self.coefficients):
            result += coef * (x ** power)
        return result

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len

        for i in range(max_len):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs[i] = coef1 + coef2

        return Polynomial(new_coeffs)


poly = Polynomial([10, -1])
print(poly(0))  