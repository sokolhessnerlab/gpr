# GPR Data Processing Script
#
# Script to process the eyetracking data collected from the GPR (Goal Pressure
# and Risk-taking) study in 2025-2026.
#

#### STEP 0: CONNECTIONS ####
# - Connect to the server

#### STEP 1: SET YOUR WORKING DIRECTORY! ####
# On PSH's computers...
setwd('/Users/sokolhessner/Documents/gitrepos/gpr/');

#### STEP 2: then run from here on the same ####
config = config::get();

setwd(config$path$data$raw);

#### STEP 3: Get the file names & set variables ####
cat('Identifying data file locations.\n');
rdmfn = dir(pattern = glob2rx('rdmDatasub*_gprRDM_*.csv'),full.names = T, recursive = T);
goalfn = dir(pattern = glob2rx('rdmDatasub*_gprBonusCompensation_*.csv'),full.names = T, recursive = T);
digitspanfn = dir(pattern = glob2rx('*gprDigitSpan*.csv'),full.names = T, recursive = T);
sclfn = dir(pattern = glob2rx('gpr*25_3.txt'),full.names = T, recursive = T);

all_dirs = dir(pattern = glob2rx('gpr*'));
subject_IDs = c();
for (s in 1:length(all_dirs)){
  subject_IDs = c(subject_IDs,as.numeric(substr(all_dirs[s],4,6))) # read subject IDs from directory names
}

number_of_subjects = length(subject_IDs)
