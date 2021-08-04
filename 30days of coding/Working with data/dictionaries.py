# working with dictionaries

album = (
 	"The Dark Side of the Moon",
 	"Pink Floyd",
 	1973,
 	(
 		"Speak to Me",
 		"Breathe",
 		"On the Run",
 		"Time",
 		"The Great Gig in the Sky",
 		"Money",
 		"Us and Them",
 		"Any Colour You Like",
 		"Brain Damage",
 		"Eclipse"
 	)
 )

# convert the tuple above to a dictionary
album_dict = {}
album_dict["Album Name"] = album[0]
album_dict["Album Artist"] = album[1]
album_dict["Release Year"] = album[2]
album_dict["Track List"] = album[3]

# print the key, value pair in the dictionary
for key, value in album_dict.items():
    print(f"{key} : {value}")

# delete some items in the dictionary
print('\n\n')
del album_dict["Track List"]
del album_dict["Release Year"]

for key, value in album_dict.items():
    print(f"{key} : {value}")


# add a new key to store the date of release
print('\n\n')
album_dict["Year of Album Release"] = "March 1st 1973"
for key, value in album_dict.items():
    print(f"{key} : {value}")


# try retrieving deleted values
print('\n\n')
print(album_dict.get("Track List"))