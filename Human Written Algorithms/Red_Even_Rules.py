

def find_output(example_list):
    odd = True
    prime = True
    even = True
    red = True
    black = True

    average_adder = 1
    for element in example_list:
        num = element[0]
        suit = element[1]

        if num%2 == 0:
            odd = False
            if not num == 2:
                prime = False
        if num%2 == 1:
            even = False
            if num == 9:
                prime = False

        if suit ==1 or suit ==3:
            black = False
        else:
            red = False
        counter = 0
        check = [odd,prime,even,red,black]
  

        for element in check:
            if element == True:
                counter+= 1
        if check[2] == True and check[3] == True and check[0] == False and check[1]== False and check[4] == False:
            check.append(average_adder)
    
            return(check)
        average_adder+=1

average = 0
for i in range(100):
    import random
    example_list = []
    for i in range (100):
        example_list.extend([((random.randint(1,6)*2, (random.randint(1,2)*2-1)))])

    output = find_output(example_list)
    average += output[-1]
    output.pop(-1)

  
# print(player_list_compare)
# if (compare(output,player_list_compare)) == 5:
#     print ("Success")
# else:
#     print("No match")
# ##is the card good to play??

print(average/100)

  
