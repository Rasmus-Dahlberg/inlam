mpg = float(input('input mgp: '))

lpkm = (1 / (mpg * 1.60934 / 3.78541))*10

print(f'{mpg} mpg is {lpkm:.2f} l/Mil')