from datetime import date

date_1 = (14,4,25)
date_2 = (10,4,25)
d1 = date(date_1[2] , date_1[1] , date_1[0])
d2 = date(date_2[2] , date_2[1] , date_2[0])

diff = abs((d2-d1).days)
print(diff)
