def printstud(**kwargs):
    data=open("student.txt",'r')
    studdata=[]
    if 'id' in kwargs and 'property' in kwargs:
        rol=kwargs['id']
        prop=kwargs['property']
        for stud_deta in data:
            lines=stud_deta.rstrip('\n').split(',')
            # print(lines)
            if rol==int(lines[0]):
                studdata.append(lines[1])
                print(studdata)
                if prop=='total':
                    studdata.append(lines[3])
                    print(studdata)


def mark():
    maxmark=[]
    f=open("student.txt",'r')
    for lines in f:
        total=lines.rstrip("\n").split(",")
        maxmark.append(total[3])
        print(max(maxmark))
        if max(maxmark) == total[3]:

            print("max mark of student:",total[0],total[1],total[2],total[3])


printstud(id=100,property='total')
mark()