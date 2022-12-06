with open('./Day06/input.txt', 'r') as file:
    dataStream = file.read()


# # part 1
# for i in range(len(dataStream) - 3):
#     if len(set(dataStream[i:i + 4])) == 4:
#         print(i + 4)
#         break

# part 2
for i in range(len(dataStream) - 13):
    if len(set(dataStream[i:i + 14])) == 14:
        print(i + 14)
        break
