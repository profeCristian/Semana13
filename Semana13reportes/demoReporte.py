

ventas=[
            ['p004', '23-05-2024', 12712],
            ['p001', '17-05-2024', 15106],
            ['p008', '11-05-2024', 18259],
            ['p007', '03-05-2024', 12936],
            ['p010', '28-05-2024', 17973],
            ['p003', '12-05-2024', 6930],
            ['p007', '16-05-2024', 13292],
            ['p008', '20-05-2024', 6733],
            ['p002', '17-05-2024', 5276],
            ['p006', '07-05-2024', 10002],
            ['p004', '26-05-2024', 8617],
            ['p007', '05-05-2024', 12555],
            ['p005', '14-05-2024', 10540],
            ['p010', '28-05-2024', 18568],
            ['p010', '20-05-2024', 18615],
            ['p007', '11-05-2024', 14414],
            ['p009', '07-05-2024', 7152],
            ['p003', '28-05-2024', 10046],
            ['p002', '14-05-2024', 15188],
            ['p009', '16-05-2024', 11576],
            ['p008', '14-05-2024', 16941],
            ['p003', '05-05-2024', 6145],
            ['p001', '10-05-2024', 5063],
            ['p004', '09-05-2024', 16754],
            ['p007', '06-05-2024', 13776],
            ['p001', '03-05-2024', 6556],
            ['p008', '14-05-2024', 5071],
            ['p008', '30-05-2024', 16142],
            ['p003', '20-05-2024', 12330],
            ['p006', '25-05-2024', 14007],
            ['p004', '30-05-2024', 14332],
            ['p005', '22-05-2024', 14421],
            ['p005', '27-05-2024', 8694],
            ['p002', '25-05-2024', 9179],
            ['p004', '08-05-2024', 10649],
            ['p009', '06-05-2024', 15329],
            ['p006', '14-05-2024', 1935],
            ['p005', '01-05-2024', 15545],
            ['p009', '29-05-2024', 10726],
            ['p003', '15-05-2024', 11341],
            ['p007', '20-05-2024', 18025],
            ['p005', '15-05-2024', 15329],
            ['p010', '05-05-2024', 8772],
            ['p002', '03-05-2024', 5581],
            ['p006', '17-05-2024', 13628],
            ['p009', '21-05-2024', 7893],
            ['p004', '22-05-2024', 10871],
            ['p009', '20-05-2024', 16856],
            ['p002', '15-05-2024', 8952],
            ['p001', '25-05-2024', 12678]
        ]

'''
a=0
for venta in ventas:
    a=a+venta[2]
    print(venta[0]," ",venta[1], "  ", venta[2])
    

print("total= ", a)



01-05-2024      31-05-2024
'''

fecha=input("Ingrese fecha: ")

a=0
for venta in ventas:
   if venta[1] == fecha: 
        a=a+venta[2]
        print(venta[0]," ",venta[1], "  ", venta[2])

print("total= ", a)

# cuánto vendí ese día?

