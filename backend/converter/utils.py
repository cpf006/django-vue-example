def number_to_words(n):
    if n == 0:
        return "zero"
    if n < 0:
        return "negative " + number_to_words(-n)
    if n < 20:
        return ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][n]
    if n < 100:
        return ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][n // 10] + \
               (" " + number_to_words(n % 10) if n % 10 != 0 else "")
    if n < 1000:
        return number_to_words(n // 100) + " hundred" + \
               (" " + number_to_words(n % 100) if n % 100 != 0 else "")
    for p, w in enumerate(("thousand", "million", "billion", "trillion"), 1):
        if n < 1000 ** (p + 1):
            return number_to_words(n // 1000 ** p) + " " + w + \
                   (" " + number_to_words(n % 1000 ** p) if n % 1000 ** p != 0 else "")
    return "Number too large"
