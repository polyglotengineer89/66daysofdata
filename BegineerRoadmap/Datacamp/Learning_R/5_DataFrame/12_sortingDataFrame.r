# planets_df is pre-loaded in your workspace
planets_df

# Use order() to create positions
positions <- order(planets_df$diameter)

# Use positions to sort planets_df
planets_df[positions, ]