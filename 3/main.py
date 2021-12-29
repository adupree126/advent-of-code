bytes = [line[:-1]
         for line in open("input").readlines()]  # remove trailing \n
gam = ''
eps = ''
# get gamma and epsilon
for place in range(len(bytes[0])):  # -1 accounts for trailing \n
    digits = [byte[place] for byte in bytes]
    if digits.count('1') > digits.count('0'):
        gam += '1'
        eps += '0'
    else:
        gam += '0'
        eps += '1'
# get oxygen generator rating
o_list = bytes.copy()
for place in range(len(bytes[0])):
    digits = [byte[place] for byte in o_list]
    if len(o_list) == 1:
        break
    if digits.count('1') >= digits.count('0'):
        o_list = list(filter(lambda byte: byte[place] == '1', o_list))
    else:
        o_list = list(filter(lambda byte: byte[place] == '0', o_list))
o_rating = o_list[0]
# get co2 generator rating
co2_list = bytes.copy()
for place in range(len(bytes[0])):
    digits = [byte[place] for byte in co2_list]
    if len(co2_list) == 1:
        break
    if digits.count('1') < digits.count('0'):
        co2_list = list(filter(lambda byte: byte[place] == '1', co2_list))
    else:
        co2_list = list(filter(lambda byte: byte[place] == '0', co2_list))
co2_rating = co2_list[0]

gam_int = int(gam, 2)
eps_int = int(eps, 2)
print("======submarine diagnostics======")
print("gamma:   0b{} ({})".format(gam, gam_int))
print("epsilon: 0b{} ({})".format(eps, eps_int))
print("power: {}".format(gam_int * eps_int))
print("~~~systems~~~")
print("O2 rating: 0b{} ({})".format(o_rating, int(o_rating, 2)))
print("CO2 rating: 0b{} ({})".format(co2_rating, int(co2_rating, 2)))
print("life support: {}".format(int(o_rating, 2) * int(co2_rating, 2)))
