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
setwd(config$path$data$processed)

# Load Decision-Making Data
fn = dir(pattern = glob2rx('edi_processed_decisionmaking*.csv'),full.names = T);
number_of_files = length(fn) # ASSUMES YOU WANT THE MOST-RECENT PROCESSED DATA
data_dm = read.csv(fn[number_of_files]) # decision-making data

number_of_subjects = length(unique(data_dm$subjectnumber));

