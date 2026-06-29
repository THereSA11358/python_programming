def plusOne(digits):
        l=digits.pop()+1
        
        if l>=10:
            return digits.extend(list(l))
        else:
            return digits.append(l)
plusOne([9])
        