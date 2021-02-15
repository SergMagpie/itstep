seconds=int(input('ведите количество секунд  '))
days=seconds//(3600*24)
hours=(seconds-days*3600*24)//3600
minutes=(seconds-(days*3600*24+hours*3600))//60
sec=(seconds-(days*3600*24+hours*3600+minutes*60))
print(seconds,' секунд это ',days,':',hours,':',minutes,':',sec,sep='')
