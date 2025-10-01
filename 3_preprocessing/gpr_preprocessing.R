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
digitspanfn = dir(pattern = glob2rx('*gprDigitSpan*.csv'),full.names = T, recursive = T);
goalfn = dir(pattern = glob2rx('rdmDatasub*_gprBonusCompensation_*.csv'),full.names = T, recursive = T);
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
cat('Loading and processing data.\n');

for(s in 1:number_of_subjects){
  ##### DECISION MAKING PROCESSING ##############
  
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
  dm_data_to_add$outcome = tmpdata$outcome
  dm_data_to_add$ischecktrial = tmpdata$ischecktrial
  dm_data_to_add$round_earnings = tmpdata$round_earnings
  dm_data_to_add$curr_goal = tmpdata$curr_goal
  dm_data_to_add$curr_bonus = tmpdata$curr_bonus
  dm_data_to_add$cond = tmpdata$cond
  dm_data_to_add$dec_epoch_start = tmpdata$stimDispStart
  dm_data_to_add$dec_epoch_end = tmpdata$isiStart
  dm_data_to_add$otc_epoch_start = tmpdata$outcomeDispStart
  dm_data_to_add$otc_epoch_end = tmpdata$itiStart
  
  # Add this person's DM data to the total DM data.
  data_dm = rbind(data_dm,dm_data_to_add);
  
  
  rm(tmpdata) # remove the temporary file
  
  ##### WORKING MEMORY PROCESSING ##############
  wm_data_to_add = array(data = NA, dim = c(number_of_wm_trials_per_person,length(column_names_wm)));
  wm_data_to_add = as.data.frame(wm_data_to_add)
  colnames(wm_data_to_add) <- column_names_wm
  
  # Load in the data
  tmpdata = read.csv(digitspanfn[s]);
  
  wm_trial_indices = which((!is.na(tmpdata$trialNumber)) & is.finite(tmpdata$correct));
  
  wm_data_to_add[,1] = 1:number_of_wm_trials_per_person; # trial numbers
  wm_data_to_add[,2] = s; # subject number

  wm_data_to_add[,3] = nchar(tmpdata$digitsForTrial[wm_trial_indices-1])/3; # number of digits on the trial
  
  wm_data_to_add[1:14,4] = 1; # forward is always first
  wm_data_to_add[15:28,4] = 0; # backward is always second
  
  wm_data_to_add[,5] = tmpdata$correct[wm_trial_indices]; # correct = 1, incorrect = 0
  
  data_wm = rbind(data_wm,wm_data_to_add);
}

setwd(config$path$data$processed);

write.csv(data_dm, file=sprintf('gpr_processed_decisionmaking_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);
write.csv(data_wm, file=sprintf('gpr_processed_workingmemory_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);
