student={
100:{'id': 100, 'name': 'ABC', 'course': 'BCA', 'mark': 140},
101:{'id': 101, 'name': 'CDE', 'course': 'MCA', 'mark': 145},
102:{'id': 102, 'name': 'EGF', 'course': 'BCA', 'mark': 150}

}
def get_student(**kwargs):

    id=kwargs['id']
    if id in student:
     print(student[id]['name'])
     prop=kwargs['property']
     if prop in student[id]:
         print(student[id][prop])
     else:
        print(student[id]['name'],prop,'property not found')
    else:
        print('invalid id')
get_student(id=100,property='course')
print(student[])