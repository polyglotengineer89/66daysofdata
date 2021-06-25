# Group the adult dataset by "Sex" and "Above/Below 50k"
gb = adult.groupby(by=['Sex',"Above/Below 50k"])

# Print out how many rows are in each created group
print(gb["Sex", "Above/Below 50k"].size())

# Print out the mean of each group for all columns
print(gb.mean())


# Create a list of user-selected variables
user_list = ["Education","Above/Below 50k"]

# Create a GroupBy object using this list
gb = adult.groupby(by=user_list)

# Find the mean for the variable "Hours/Week" for each group - Be efficient!
print(gb["Hours/Week"].mean())



# Check frequency counts while also printing the NaN count
print(dogs["keep_in"].value_counts(dropna=False))

# Switch to a categorical variable
dogs["keep_in"] = dogs["keep_in"].astype("category")

# Add new categories
new_categories = ["Unknown History", "Open Yard (Countryside)"]
dogs["keep_in"] = dogs["keep_in"].cat.add_categories(new_categories=new_categories)

# Check frequency counts one more time
print(dogs["keep_in"].value_counts(dropna=False))


# Set "maybe" to be "no"
dogs.loc[dogs["likes_children"] == "maybe", "likes_children"] = "no"

# Print out categories
print(dogs["likes_children"].cat.categories)

# Print the frequency table
print(dogs["likes_children"].value_counts())

# Remove the `"maybe" category
dogs["likes_children"] = dogs["likes_children"].cat.remove_categories(removals=["maybe"])
print(dogs["likes_children"].value_counts())

# Print the categories one more time
print(dogs["likes_children"].cat.categories)



# Create the my_changes dictionary
my_changes = {"Maybe?": "Maybe"}

# Rename the categories listed in the my_changes dictionary
dogs["likes_children"] = dogs["likes_children"].cat.rename_categories(my_changes)

# Use a lambda function to convert all categories to uppercase using upper()
dogs["likes_children"] =  dogs["likes_children"].cat.rename_categories(lambda c: c.upper())

# Print the list of categories
print(dogs["likes_children"].cat.categories)