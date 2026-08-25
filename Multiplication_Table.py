##Program to generate multiplication table up to 10 for number 1 to 5
print("MULTILICATION TABLES")
start_number=1
end_number=5
table_limit=10
for number in range(start_number, end_number+1):
    print()
    print("Multiplication table of", number)
    for multiplier in range(1,table_limit+1):
        product=number*multiplier
        frist_value=number
        second_value=multiplier
        result=product
        print(frist_value,"x",second_value,"=",result)
    print()
print("All Multiplication Table from 1 to 5")
print("are generated successfully")
