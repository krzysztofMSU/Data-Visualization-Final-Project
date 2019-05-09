import numpy as np
import matplotlib.pyplot as plt

data = open("berkley.txt", "r")
freq = []
admit = []
gender = []
depart = []
admitted_male = []
rejected_male = []
admitted_female = []
rejected_female = []
number = 0
string1 = ""
count = 0
N = 6
ind = np.arange(N)      # the x locations for the groups
width = 0.35            # the width of the bars: can also be len(x) sequence

# Loads data from file to lists
for line in data:
    words = line.split(',')
    data_list = (words[0], words[1], words[2], words[3])
    words[3] = words[3].strip('\n')                         # Removes "\n" from freq list
    admit.append(words[0])
    gender.append(words[1])
    depart.append(words[2])
    # Converts 'frequency' strings to integers
    string1 = words[3]
    if count > 0:
        string1 = int(string1)
    freq.append(string1)                                    # Loads freq integers to freq list
    count = count + 1
data.close()

# Removes first element in each list
freq.remove('Freq')
admit.remove('Admit')
gender.remove('Gender')
depart.remove('Dept')

# # Prints lists to console to check if populates
# print(admit)
# print(gender)
# print(depart)
# print(freq)

for x in range(len(admit)):
    if admit[x] == "Admitted" and gender[x] == "Male":      # Separate admitted male into list
        admitted_male.append(freq[x])
    if admit[x] == "Rejected" and gender[x] == "Male":      # Separate rejected male into list
        rejected_male.append(freq[x])
    if admit[x] == "Admitted" and gender[x] == "Female":    # Separate admitted female into list
        admitted_female.append(freq[x])
    if admit[x] == "Rejected" and gender[x] == "Female":    # Separate rejected female into list
        rejected_female.append(freq[x])

# print("\n")
# # Prints separate lists to console to check if populates
# print(admitted_male)
# print(rejected_male)
# print(admitted_female)
# print(rejected_female)

fig, ax = plt.subplots()
p1 = ax.bar(ind - width/2, admitted_male, width, color='royalblue', label='Admitted Men')
p2 = ax.bar(ind - width/2, rejected_male, width, bottom=admitted_male, color='skyblue', label='Rejected Men')
p3 = ax.bar(ind + width/2, admitted_female, width, color='m', label='Admitted Women')
p4 = ax.bar(ind + width/2, rejected_female, width, bottom=admitted_female, color='orchid', label='Rejected Women')

plt.ylabel('Frequency', fontsize=14)
plt.xlabel('Groups', fontsize=14)
plt.title('Acceptance Frequency by groups and gender', fontsize=14)
plt.xticks(ind, ('A', 'B', 'C', 'D', 'E', 'F'))
# plt.yticks()    # Not needed
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Men Admitted', 'Men Rejected', 'Women Admitted', 'Women Rejected'))
plt.show()
