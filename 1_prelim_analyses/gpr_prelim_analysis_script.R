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
