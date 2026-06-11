class Password:
    @staticmethod
    def is_strong(p: str) -> bool:
        if len(p) < 8:
            return False
        has_digit = any(c.isdigit() for c in p)
        has_upper = any(c.isupper() for c in p)
        has_lower = any(c.islower() for c in p)
        return has_digit and has_upper and has_lower


print(Password.is_strong('qwerty'))      
print(Password.is_strong('Qwerty12'))   
print(Password.is_strong('QWERTY12'))   
print(Password.is_strong('Qwerty123'))  
