import matplotlib.pyplot as plt

arr = ['King','Sockeye','Silver','Chum','Humpback']
arr1 = [15,8,12,15,5]

plt.bar(arr,arr1)
plt.xlabel("Salmon Species")
plt.ylabel("Average Weight (lbs)")
plt.title("Size of pacific Salmon for 1 year")
plt.show()
