# Event-Wise-Data-Sorting-For-a-Nuclear-Reaction
For each proton there will be a single or many alpha events. The program sorts them using modified linear search.
Program Explanation:
The program takes in two text files one for proton event and other for alpha event. These are sorted files.FOr each 
proton there is a possibility for multiple alpha events. As the data is sorted in both the files the relevant value with respect to proton will always exist in near proximity of the preceeding values in alpha. Hence, a linear search that remembers the previous value serched and starts from there in it's next search proves to be time saving, compared to binary search.
Test data:
protonn.txt
alphaa.txt
PS:
THe files should be tab and newline delimted.
