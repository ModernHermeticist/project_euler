def main():
    num2word = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
                19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
                50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
                90: 'ninety', 100: 'onehundred', 200: 'twohundred', 300: 'threehundred', \
                400: 'fourhundred', 500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred', \
                800: 'eighthundred', 900: 'ninehundred', 1000: 'onethousand'}

    s = []
    for i in range(1, 1001):
        try:
            s.append(num2word[i])
            print(num2word[i])
        except KeyError:
            try:
                if i > 100:
                    s.append(num2word[i-i%10] + "and" + num2word[i%10])
                    print(num2word[i - i % 10] + "and" + num2word[i % 10])
                else:
                    s.append(num2word[i-i%10] + num2word[i%10])
                    print(num2word[i-i%10] + num2word[i%10])
            except:
                try:
                    s.append(num2word[i-i%100] + "and" + num2word[i%100])
                    print(num2word[i-i%100] + "and" + num2word[i%100])
                except:
                    try:
                        s.append(num2word[i-i%100] + "and" + num2word[i%100-i%10] + num2word[i%10])
                        print(num2word[i-i%100] + "and" + num2word[i%100-i%10] + num2word[i%10])
                    except:
                        print("Number out of range")
    l = 0
    for word in s:
        for letter in word:
            l += 1

    print("The sum of the letters used to write out 1-1000 inclusive is: {}".format(l))










main()