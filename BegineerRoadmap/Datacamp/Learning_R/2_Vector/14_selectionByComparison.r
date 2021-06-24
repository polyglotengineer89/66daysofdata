# Poker and roulette winnings from Monday to Friday:
poker_vector <- c(140, -50, 20, -120, 240)
roulette_vector <- c(-24, -50, 100, -350, 10)
days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
names(poker_vector) <- days_vector
names(roulette_vector) <- days_vector

# Which days did you make money on poker?
# selection_vector <- if(sum(poker_vector) > sum(roulette_vector)){ sum(poker_vector)} else {  sum(roulette_vector)}
selection_vector <- poker_vector > 0
  
# Print out selection_vector
selection_vector