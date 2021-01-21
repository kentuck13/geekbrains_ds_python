km_first_day = int(input('Input km first day: '))
wish_km = int(input('Input wish km: '))

day = 1
km = km_first_day

while km < wish_km:
    km += (km / 100) * 10
    day += 1

print('In %d day he will reach result not less than %d km' % (day, km))
