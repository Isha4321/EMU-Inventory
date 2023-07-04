# Ordered collection of data item
# Contains different types of data items
# indexing is used here
# Can't be changed used to contain multiple values in single variable
# slicing is possible but new tuple will be created 
# if we want to add ,delete or update tuple then we first have to convert it to list because tuples are immutable
tup = (1)
print(type(tup)) # class int

tup = (1,)
print(type(tup))