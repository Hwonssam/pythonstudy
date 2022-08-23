'''import pickle
profile_file = open("profile.pickle","wb")
profile = {"이름" : "박명수", "나이" : 30 ,"취미":["축구","농구","배구"]}
print(profile)
pickle.dump(profile,profile_file)
profile_file.close()'''
"""import pickle
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()"""
'''import pickle
with open("profile.pickle","rb") as profile_file :
    print(pickle.load(profile_file))'''

with open("study.txt", "w", encoding="utf8") as study_file :
    study_file.write("파이썬 열공중")
    
'''
with open("study.txt", "r", encoding="utf8") as study_file :
    print(study_file.read())
'''