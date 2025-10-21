# Input: list of student exam scores
scores = list(map(int, input("Enter student scores separated by space: ").split()))

# Sort the list in descending order
for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[i] < scores[j]:
            # swap values
            scores[i], scores[j] = scores[j], scores[i]

# Pick top 3 scores
top_3 = scores[:3]

print("Top 3 Scores:", top_3)
 
