print('输入文件名，用英文逗号隔开：', end='')
names = input()
name_li = names.split(',')
import os

def state(s):
    if s == '伪距':
        return 2
    elif s == 'RTK固定解':
        return 4
    elif s == '广域差分':
        return 9
    else:
        return 0



def get_time(day_tim):
    if len(day_tim.split(' ')) == 2:
        tim = day_tim.split(' ')[1]
        hr_min_se = tim.split(':')
        hr = hr_min_se[0]
        min = hr_min_se[1]
        se = hr_min_se[2]
        time = hr + min + se
    else:
        time = day_tim.replace(":", "")
        if time == '0000.0':
            global start_utc
            start_utc += 1
        time = str(start_utc) + time
    return time


def main():
    a1 = os.path.abspath(os.path.dirname((__file__)))
    global name_li
    for name in name_li:
        source = a1+'\\'+name
        target = a1+'\\gga_'+name
        print(target)
        with open(target, 'a', encoding='UTF-8') as inp:
            with open(source, 'r', encoding='ANSI') as file:
                lines = file.readlines()
                del (lines[0])
                for line in lines:

                    name = '$GPGGA'

                    utc_time = get_time(line.split(',')[16])

                    B = eval(line.split(",")[5])
                    L = eval(line.split(",")[6])
                    print(B)
                    B = round(int(B.split(":")[0])*100 + int(B.split(":")[1]) + float((B.split(":")[2]))/60, 7)
                    L = round(int(L.split(":")[0])*100 + int(L.split(":")[1]) + float((L.split(":")[2]))/60, 7)

                    sta = state(line.split(',')[13])
                    num = line.split(',')[20]
                    shuiping = '1.0'
                    tianxian_h = line.split(',')[8]
                    dadi_h = line.split(',')[7]
                    chafen_ = line.split(',')[19]
                    enD = '0007*7F'

                    ST = '{},{},{},N,{},E,{},{},{},{},M,{},M,{},{}\n'.format(name, utc_time, B, L, sta, num, shuiping,
                                                                             tianxian_h, dadi_h, chafen_, enD)
                    inp.write(ST)


if __name__ == '__main__':
    main()
