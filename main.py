questions = [
    ["Who is shah Rukh Khan?", "WWE Wrestler", "Cleaner", "Actor", "Plumber", 3],
    ["What is capitol of France?", "Rome", "Paris", "London", "Brelin", 2],
    ["Which planet is known as red planet?", "Earth", "Jupiter", "Venus", "Mars", 4],
    ["Which is the larget mammal?", "Blue Whale", "Elephant", "Tiger", "Lion", 1],
    ["Who wrote 'Romio and Juliet'?", "Charles Duckings", "Homer", "Jane Austane", "Willima Shakespere", 4],
    ["What is Square root of 64?", "6", "12", "10", "8", 4],
    ["Which country is known as land of rising sun?", "Japan", "China", "India","South Korea", 1],
    ["Who painted the Mona Lisa?", "Vincent Van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet", 3],
    ["Which is the fasted land animal?", "Lion", "Elephant", "Fox", "Cheetah", 4],
    ["Which ocean is the largest?", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", 1],
    ["Which is the smallest country in the world?", "Vatican city", "San Marino", "Monaco", "Bhutan", 2],
    ["According to Padma Purana, which king had to live as a tiger for a hundered years due to a deer's curse?", "Kshemadhuriti", "Dharmadatta", "Mitadhvaja", "Prabhanjana", 4]
]

prizes = [10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]
i = 0

for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

# check wheather the answer is correct or not

    a = int(input("Enter the answer. 1 for a, 2 for b, 3 for c, 4 for d \n"))

    if(question[5] == a):
        print("Sahi Javab")

    else:
        print(f"Galat Javab...Sahi Javab {question[5]} hai")
        print("Apke sath khel ke achha laga... Thanyavaad Deviyon or Sajjano")
        break
    print(f"Apne jit liye hai pure...{prizes[i]} rupiye\n")

    if(i == 9):
        print("Agla saval 1 core rupiye ke liye ye raha apke screen par...")

    if(i == 10):
        print("1 Core.... Bahut Bahut Shubhkamnaye...\n")
        print("Agla saval 7 core ke liye ye raha apke screen par...\n")

    if(i == 11):
        print("7 core... WAAAA WAAA WAA... Maza a gaya apke sath khel ke\n")
        tp = input("Kya karenge ap itne dhan rashi ka: ")
        print("Apse yahi umeed thi... Bahut Bahut Shubhkamnaye or Thanyavaad khel ne ke liye...")
    i += 1