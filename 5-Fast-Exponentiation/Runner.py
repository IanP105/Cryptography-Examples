# Main driver for the program

# Needs to take in values from other files


z = '001001101'
y = int(z, 2)
t = int(0)

print(f'z = {y}')
print(f'z = {z} | {z[-1]}')

end_z = z[-1]
end_t = t[-1]

binaryNumber = '1' + end_z + end_t + '1'
intNumber = int(binaryNumber, 2)

print(f'z = {z} | {end_z}')
print(f't = {t} | {end_t}')
print(binaryNumber)
print(f'my_num_bin = {binaryNumber} = {intNumber}')