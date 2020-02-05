#Alem Snyder
#1/29/2020
#Fahrenheit Celsius converter
#with errors
#I tip my hat to thoes who can find them
def FandCConverter():
    In_number = ''
    has_units = False
    remainder = False
    decimal = False
    negative = False
    #sigfigs = 0
    numbers = ('0','1','2','3','4','5','6','7','8','9',)
    inp = input("This converter converts from Fahrenheit to Celsius or Celsius to Fahrenheit.\nPlease write the temperature with proper units.\n")
    for letter in inp:
        if letter == "." and not decimal:
            decimal = True
            decimalPosition = len(In_number)
            In_number = In_number+letter
        elif letter == "-" and not negative and len(In_number) == 0:
            negative = True
            In_number = In_number+letter
        elif letter in numbers:
            In_number = In_number+letter
        elif letter.upper() in ("C","F") and not has_units:
            Unite = letter.upper
            has_units = True
        elif letter != "," and letter != " ":
            print("Please don't write gibberish")
            return()
    if not has_units:
        print("What are these, naked numbers?")
        return
    if not decimal:
        decimalPosition = len(In_number)
        
    #how many sigfigs are there?
    if decimal:
        """
        the number of sigfigs will depend
        on if there is a dicemal or not
        and on if the number id negative
        or not"""
        if negative:
            sigfigs = len(In_number) - 2
        """
        this is becasue the total number
        of digits is the length of the
        sting minus 1 if there is a "."
        and one less if there is a "-"
        """
        else:
            sigfigs = len(In_number) - 1
    else:
        if negative:
            for position in range(len(In_number)):
                if In_number[-position-1] != "0":
                    sigfigs = len(In_number) - position - 1
        else:
            for position in range(len(In_number)):
                if In_number[-position-1] != "0":
                    sigfigs = len(In_number) - position
                    break
    if sigfigs < 2:
        sigfigs = 2

    #Calculate the temperature
    
    if Unite == "C":
        outunit = "F"
        Temp = float(In_number)*9/5+32
    if Unite == "F":
        outunit = "C"
        Temp = (float(In_number)-32)*5/9

    Temp = round(Temp, (sigfigs-decimalPosition+1))

    figs = 0
    position= 0
    ended = False
    strTemp = str(Temp)

    out_number = ''
    while(figs < sigfigs and not ended):
        if position < len(strTemp):
            if strTemp[position] == "-":
                out_number = out_number + strTemp[position]
            elif strTemp[position] == ".":
                if figs < sigfigs:
                    out_number = out_number + strTemp[position]
                ended = True
            else:
                out_number = out_number + strTemp[position]
                figs += 1
        else:
            out_number = out_number + "0"
            figs += 1
        position += 1
    
    print(In_number+Unite+" is approximately equal to "+out_number+outunit+".")
while(True):
    FandCConverter()
