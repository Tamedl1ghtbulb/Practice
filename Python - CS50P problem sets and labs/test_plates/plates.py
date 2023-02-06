def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2<= len(s)<=6:
        if not s[0].isalpha():
            return False
        if not s[1].isalpha():
            return False
        if s.isalnum():
            for i in s:
                if i.isdigit():
                    b=s.index(i)
                    l = i
                    break
            else:
                return True
            if l == '0':
                return False
            preost = (len(s))-b
            for k in range(preost):
                if  s[k+b].isdigit():
                    if k+1+b==len(s):
                        return True
                    continue
                else:
                    return False
                return True
        else:
            return False
    else:
        return False
if __name__ == '__main_':
    main()