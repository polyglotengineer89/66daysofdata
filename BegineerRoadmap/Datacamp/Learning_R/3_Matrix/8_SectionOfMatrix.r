# all_wars_matrix is available in your workspace
all_wars_matrix

# Select the non-US revenue for all movies
non_us_all <- all_wars_matrix[,2]
print(non_us_all)
  
# Average non-US revenue
mean(non_us_all)
  
# Select the non-US revenue for first two movies
non_us_some <- all_wars_matrix[1:2, 2]
  
# Average non-US revenue for first two movies
mean(non_us_some)