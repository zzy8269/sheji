import time
choose=int(input('输入1自动获取当前年份\n输入2手动输入当前年份\n您的选择是：'))
if choose==1:
    x=int(input('请输入出生年：'))
    y=int(input('请输入出生月：'))
    z=int(input('请输入出生日：'))
    yea=int(time.strftime("%Y", time.localtime()))
    mon=int(time.strftime("%m", time.localtime()))
    day=int(time.strftime("%d", time.localtime()))
    if yea>x:
        if mon>y:
            i=yea-x
            print('周岁是%d' % (i))
        elif mon==y:
            if day>=z:
                i=yea-x
                print('周岁是%d' % (i))
            else :
                i=yea-x-1
                print('周岁是%d' % (i))
        else :
            i=yea-x-1
            print('周岁是%d' % (i))
    else :
        print('出生不到一年')
elif choose==2:
    x=int(input('请输入出生年：'))
    y=int(input('请输入出生月：'))
    z=int(input('请输入出生日：'))
    a=int(input('请输入现在年：'))
    b=int(input('请输入现在月：'))
    c=int(input('请输入现在日：'))
    if a>x:
        if b>y:
            i=a-x
            print('周岁是%d' % (i))
        elif b==y:
            if c>=z:
                i=a-x
                print('周岁是%d' % (i))
            else :
                i=a-x-1
                print('周岁是%d' % (i))
        else :
            i=a-x-1
            print('周岁是%d' % (i))
    else :
        print('出生不到一年')
else :
    print('输入数字有误，请重新输入')
