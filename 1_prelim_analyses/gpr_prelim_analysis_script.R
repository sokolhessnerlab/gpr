# GPR Preliminary Analysis Script
#
# Script to analyze preliminary data from the CGT, CGE, and EDI to determine
# design parameters for the GPR (Goal Pressure & Risk-taking) study to take
# place in 2025. 
#

rm(list=ls()); # Clear the workspace


# Setting Up ###################################

# STEP 1: Set the working directory
# On PSH's computers...
setwd('/Users/sokolhessner/Documents/gitrepos/gpr/');
# On JB's computers...
# setwd('the/path/to/justins/github/repo/for/gpr');

# STEP 2: then run from here on the same
config = config::get()

# Loading Data ########################################

## EDI Data ###########################################
setwd(config$path$edidata$processed)

# Load Decision-Making Data
fn = dir(pattern = glob2rx('edi_processed_decisionmaking*.csv'),full.names = T);
number_of_files = length(fn) # ASSUMES YOU WANT THE MOST-RECENT PROCESSED DATA
edi_data_dm = read.csv(fn[number_of_files]) # decision-making data

number_of_edi_subjects = length(unique(edi_data_dm$subjectnumber));

## CGE Data ###########################################
setwd(config$path$cgedata$processed)

# Load Decision-Making Data
fn = dir(pattern = glob2rx('cge_processed_decisionmaking*.csv'),full.names = T);
number_of_files = length(fn) # ASSUMES YOU WANT THE MOST-RECENT PROCESSED DATA
cge_data_dm = read.csv(fn[number_of_files]) # decision-making data

number_of_cge_subjects = length(unique(cge_data_dm$subjectnumber));

## CGT Data ###########################################
setwd(config$path$cgtdata$processed)

# Load Decision-Making Data
fn = dir(pattern = glob2rx('cgt_processed_decisionmaking*.csv'),full.names = T);
number_of_files = length(fn) # ASSUMES YOU WANT THE MOST-RECENT PROCESSED DATA
cgt_data_dm = read.csv(fn[number_of_files]) # decision-making data

number_of_cgt_subjects = length(unique(cgt_data_dm$subjectnumber));

number_of_gpr_prelim_subjects = number_of_edi_subjects + number_of_cge_subjects + number_of_cgt_subjects;

# Extracting Static Choice Set Data ########################################

# The colnames we want to extract
colnames_to_keep = c('trialnumber',
                     'subjectnumber',
                     'riskyopt1',
                     'riskyopt2',
                     'safe',
                     'choice',
                     'reactiontime',
                     'outcome',
                     'ischecktrial')

# the final column names (including study ID) for the GPR object
all_colnames = c('studyID', colnames_to_keep)

# set up the data object to put the static data into
gpr_prelim_data = array(data = NA, dim = c(0,length(colnames_to_keep)+1))
colnames(gpr_prelim_data) <- all_colnames

# identify the rows we want (static trials only)
edi_ind = edi_data_dm$static0dynamic1 == 0
cge_ind = cge_data_dm$static0dynamic1 == 0
cgt_ind = cgt_data_dm$static0dynamic1 == 0

# Extract the data we want from each study
edi_static_data = cbind(rep(1, sum(edi_ind)), edi_data_dm[edi_ind, colnames_to_keep])
cge_static_data = cbind(rep(2, sum(cge_ind)), cge_data_dm[cge_ind, colnames_to_keep])
cgt_static_data = cbind(rep(3, sum(cgt_ind)), cgt_data_dm[cgt_ind, colnames_to_keep])

# Make column names consistent across studies
colnames(edi_static_data) <- all_colnames
colnames(cge_static_data) <- all_colnames
colnames(cgt_static_data) <- all_colnames

# Deal with duplicate subject IDs by translating IDs to separate ranges
edi_static_data$subjectnumber = edi_static_data$subjectnumber + 100 # EDI subj numbers 100+
cge_static_data$subjectnumber = cge_static_data$subjectnumber + 200 # CGE subj numbers 200+
cgt_static_data$subjectnumber = cgt_static_data$subjectnumber + 300 # CGT subj numbers 300+
# Now every person has a unique subjectnumber value

# Combine data
gpr_prelim_data = rbind(gpr_prelim_data,
                        edi_static_data,
                        cge_static_data,
                        cgt_static_data)

gpr_prelim_subjnumbers = unique(gpr_prelim_data$subjectnumber)


# Actual Earnings ################################################
# Calculate actual earnings & percentiles related to them. 

final_earnings_actual = as.data.frame(array(data = NA, dim = c(number_of_gpr_prelim_subjects, 2)))
colnames(final_earnings_actual) <- c('subjectnumber',
                                     'actualearnings')

for (s in 1:number_of_gpr_prelim_subjects){
  final_earnings_actual$subjectnumber[s] = gpr_prelim_subjnumbers[s];
  final_earnings_actual$actualearnings[s] = sum(gpr_prelim_data$outcome[gpr_prelim_data$subjectnumber == gpr_prelim_subjnumbers[s]], na.rm = T)
}

# Plot the results
hist(final_earnings_actual$actualearnings, 
     breaks = 20,
     xlab = 'Earnings ($)', ylab = 'Number of Subjects', 
     main = sprintf('Actual Final Earnings in CGT, CGE, and EDI studies (N = %i)',number_of_gpr_prelim_subjects))
abline(v = quantile(probs = 0.5, final_earnings_actual$actualearnings), col = 'black', lty = 'dashed', lwd = 5) # 50% (median)
abline(v = quantile(probs = 0.1, final_earnings_actual$actualearnings), col = rgb(1,0,0), lwd = 5) 
abline(v = quantile(probs = 0.2, final_earnings_actual$actualearnings), col = rgb(.8,0,0), lwd = 5)
abline(v = quantile(probs = 0.3, final_earnings_actual$actualearnings), col = rgb(.6,0,0), lwd = 5)
abline(v = quantile(probs = 0.7, final_earnings_actual$actualearnings), col = rgb(0,0,.6), lwd = 5)
abline(v = quantile(probs = 0.8, final_earnings_actual$actualearnings), col = rgb(0,0,.8), lwd = 5)
abline(v = quantile(probs = 0.9, final_earnings_actual$actualearnings), col = rgb(0,0,1), lwd = 5)

prcntles = c(0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9)
gpr_possible_percentiles = cbind(prcntles,quantile(probs = prcntles,final_earnings_actual$actualearnings))


# Simulate Earnings ################################################
# Calculate possible earnings & percentiles related to them. 
# The approach here relies on brute force simulation of new random outcomes, given
# the exact same set of choices as occurred in real life. That is, these are simulations
# of earnings given choices, not simulations of choices. 
#
# An alternate approach would simply calculate expected value of each person's choices
# which would produce a similar graph. 

nSim = 10000; # number of simulations to do per person

final_earnings_simulated = as.data.frame(array(data = NA, dim = c(number_of_gpr_prelim_subjects * nSim, 2)))
colnames(final_earnings_simulated) <- c('subjectnumber',
                                        'simearnings')

preposttrial_counts_simulated = as.data.frame(array(data = NA, 
                                                    dim = c(number_of_gpr_prelim_subjects * nSim, 3)))
colnames(preposttrial_counts_simulated) <- c('subjectnumber',
                                        'pretrials',
                                        'posttrials')
# sim_goal = 448.07; # 80th percentile as simulated 3/10/2025
# sim_goal = 384.49; # 30th percentile as simulated 3/10/2025
sim_goal = 349.90; # 10th percentile as simulated 3/10/2025


cat(sprintf('Progress: 000%%'))
for (s in 1:number_of_gpr_prelim_subjects){
  # Extract this participant's data
  tmp_data = gpr_prelim_data[gpr_prelim_data$subjectnumber == gpr_prelim_subjnumbers[s],];
  
  # Set up the sim_earnings object to be empty & ready
  sim_earnings = array(data = NA, dim = c(nSim,2));
  sim_earnings[,1] = gpr_prelim_subjnumbers[s];
  
  # Set up the trial counts object to be empty and ready
  sim_counts = array(data = NA, dim = c(nSim, 3));
  sim_counts[,1] = gpr_prelim_subjnumbers[s];
  
  # Loop
  for (i in 1:nSim){ # for each simulation... 
    sim_otcs = array(data = NA, dim = 50); # Create empty outcome vector
    rand_otcs = runif(50) > 0.5; # Randomly simulate wins/losses (T = win, F = lose)
    risky_wins = is.finite(tmp_data$choice) & (tmp_data$choice == 1) & rand_otcs # indices of risky wins
    risky_losses = is.finite(tmp_data$choice) & (tmp_data$choice == 1) & !rand_otcs # indices of risky losses
    
    # Fill in the outcome vector
    sim_otcs = tmp_data$safe; # Assume safe choices
    sim_otcs[risky_wins] = tmp_data$riskyopt1[risky_wins]        # If risky and WON
    sim_otcs[risky_losses] = tmp_data$riskyopt2[risky_losses]    # If risky and LOST

    # Calculate cumulative earnings, given outcomes
    sim_earnings[i,2] = sum(sim_otcs, na.rm = T)
    
    # calculate trial counts
    sim_counts[i,2] = sum(cumsum(sim_otcs[is.finite(sim_otcs)]) < sim_goal) # trials BEFORE the goal
    sim_counts[i,3] = sum(cumsum(sim_otcs[is.finite(sim_otcs)]) >= sim_goal) # trials AT and AFTER the goal
  }
  
  final_sim_row_ind = ((s-1)*nSim + 1):(s*nSim) # Get the right indices for this person's simulations
  final_earnings_simulated[final_sim_row_ind,] = sim_earnings; # chuck 'em in
  
  preposttrial_counts_simulated[final_sim_row_ind,] = sim_counts; # chuck in the trial counts
  
  cat(sprintf('\b\b\b\b%03.f%%',s/number_of_gpr_prelim_subjects*100))
}
cat(sprintf('\n'))

# Plot the earnings results
hist(final_earnings_simulated$simearnings, 
     breaks = 20,
     xlab = 'Earnings ($)', ylab = 'Number of Subjects', 
     main = sprintf('Simulated Final Earnings in CGT, CGE, and EDI studies (N = %i)',number_of_gpr_prelim_subjects * nSim))
abline(v = quantile(probs = 0.5, final_earnings_simulated$simearnings), col = 'black', lty = 'dashed', lwd = 5) # 50% (median)
abline(v = quantile(probs = 0.1, final_earnings_simulated$simearnings), col = rgb(1,0,0), lwd = 5) 
abline(v = quantile(probs = 0.2, final_earnings_simulated$simearnings), col = rgb(.8,0,0), lwd = 5)
abline(v = quantile(probs = 0.3, final_earnings_simulated$simearnings), col = rgb(.6,0,0), lwd = 5)
abline(v = quantile(probs = 0.7, final_earnings_simulated$simearnings), col = rgb(0,0,.6), lwd = 5)
abline(v = quantile(probs = 0.8, final_earnings_simulated$simearnings), col = rgb(0,0,.8), lwd = 5)
abline(v = quantile(probs = 0.9, final_earnings_simulated$simearnings), col = rgb(0,0,1), lwd = 5)

prcntles = c(0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9)
gpr_possible_percentiles = cbind(prcntles,quantile(probs = prcntles,final_earnings_simulated$simearnings))


hist(preposttrial_counts_simulated$pretrials,
     xlab = 'Number of trials', ylab = 'Simulated participants',
     main = sprintf('Trials BEFORE the goal (Med = %i; p(>5) = %.1f)',
                    median(preposttrial_counts_simulated$pretrials),
                    sum(preposttrial_counts_simulated$pretrials > 5)/(length(preposttrial_counts_simulated$pretrials))))

hist(preposttrial_counts_simulated$posttrials,
     xlab = 'Number of trials', ylab = 'Simulated participants',
     main = sprintf('Trials AFTER the goal (Med = %i; p(>5) = %.2f)',
                    median(preposttrial_counts_simulated$posttrials),
                    sum(preposttrial_counts_simulated$posttrials > 5)/(length(preposttrial_counts_simulated$posttrials))))

