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
# On JB's computers...
# setwd('/Users/justinblake/Documents/gpr/');

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


# Store some basic information about size of the decision-making task
num_rdm_trials = 50;
num_rdm_blocks = 4;
number_of_dm_trials_per_person = num_rdm_trials * num_rdm_blocks; # static = 50, dynamic = 120

# Set up variables to hold decision-making data
column_names_dm = c(
  'subjectnumber',
  'trialnumber_overall',
  'trialnumber_block',
  'roundnumber',
  'riskyopt1',
  'riskyopt2',
  'safe',
  'choice',
  'reactiontime', # WE'VE DONE TO HERE
  'outcome',
  'ischecktrial',
  'round_earnings',
  'curr_goal',
  'curr_bonus',
  'cond',
  'dec_epoch_start',
  'dec_epoch_end',
  'otc_epoch_start',
  'otc_epoch_end'
);

data_dm = array(data = NA, dim = c(0, length(column_names_dm)));
colnames(data_dm) <- column_names_dm

# Set up variables to hold working memory data
number_of_wm_trials_per_person = 28; # 14 forward, 14 backward

column_names_rawdata_wm = c(
  'digitsForTrial', #both FS & BS digits
  'textbox.text', #FS response
  'textboxBS.text', #BS response
  'trialNumber', #both trial number
  'digitLoop.thisRepN', #FS number of digits
  'digitLoopBS.thisRepN', #BS number of digits
  'correct' #both FS & BS
);

# this will have trials in rows, these will be col. names
column_names_wm = c(
  'trialnumber',
  'subjectnumber',
  'number_digits',
  'forward1backward0',
  'correct'
);

data_wm = array(data = NA, dim = c(0, length(column_names_wm)));
colnames(data_wm) <- column_names_wm


#### STEP 4: Load and Process Data ####

for(s in 1:number_of_subjects){
  # Load in the data
  tmpdata = read.csv(rdmfn[s]);
  
  # DECISION-MAKING DATA
  dm_data_to_add = array(data = NA, dim = c(number_of_dm_trials_per_person,length(column_names_dm)));
  dm_data_to_add = as.data.frame(dm_data_to_add)
  colnames(dm_data_to_add) <- column_names_dm
  
  dm_data_to_add$subjectnumber = tmpdata$subID
  dm_data_to_add$trialnumber_overall = tmpdata$X
  dm_data_to_add$trialnumber_block = tmpdata$trial+1
  dm_data_to_add$roundnumber = tmpdata$roundRDM
  
  dm_data_to_add$riskyopt1 = tmpdata$riskyGain
  dm_data_to_add$riskyopt2 = tmpdata$riskyLoss
  dm_data_to_add$safe = tmpdata$safe
  dm_data_to_add$choice = tmpdata$choice
  dm_data_to_add$reactiontime = tmpdata$RT
  
  ##### FILL IN THE REMAINING ROWS BETWEEN HERE AND...
  
  
  
  
  ##### ... HERE.
  
  
  
  
  
  ##### TODO: DELETE EVERYTHING BELOW THIS WHEN DONE
  
  tmp_riskyopt1 = c(tmpdata$riskyoption1[dm_index_static],
                    tmpdata$riskyoption1[dm_index_dynamic]);
  tmp_riskyopt2 = c(tmpdata$riskyoption2[dm_index_static],
                    tmpdata$riskyoption2[dm_index_dynamic]);
  tmp_safe = c(tmpdata$safeoption[dm_index_static],
               tmpdata$safeoption[dm_index_dynamic]);
  
  dm_data_to_add[,4:6] = cbind(tmp_riskyopt1,tmp_riskyopt2,tmp_safe) # dollar amounts
  
  dm_data_to_add[,7] = c(tmpdata$choices[dm_index_static],
                         tmpdata$choices[dm_index_dynamic]); # choices
  
  dm_data_to_add[,8] = c(tmpdata$realChoice.rt[dm_index_static],
                         tmpdata$realChoice.rt[dm_index_dynamic]); # RTs
  
  dm_data_to_add[,9] = c(tmpdata$outcomes[dm_index_static],
                         tmpdata$outcomes[dm_index_dynamic]); # outcomes
  
  dm_data_to_add[,10] = c(tmpdata$ischecktrial[dm_index_static],
                          array(data = 0, dim = c(1,num_dynamic_trials))); # is check trial
  
  dm_data_to_add[,11] = c(array(data = 0, dim = c(1,num_static_trials)),
                          array(data = 1, dim = c(1,num_dynamic_trials))); # static 0, dynamic 1
  
  dm_data_to_add[,12] = c(array(data = 0, dim = c(1,num_static_trials)),
                          tmpdata$easy0difficult1[dm_index_dynamic]*-2 + 1); # easy +1, difficult -1
  
  dm_data_to_add[,13] = c(array(data = NA, dim = c(1,num_static_trials)),
                          tmpdata$choiceP[dm_index_dynamic]); # choice probability on easy/diff dynamic trials
  
  dm_data_to_add[,14] = tmpdata$bestRho[is.finite(tmpdata$bestRho)];
  dm_data_to_add[,15] = tmpdata$bestMu[is.finite(tmpdata$bestMu)];
  
  
  
  #### JUST DON'T DELETE THIS LINE! 
  
  # Add this person's DM data to the total DM data.
  data_dm = rbind(data_dm,dm_data_to_add);
  
}