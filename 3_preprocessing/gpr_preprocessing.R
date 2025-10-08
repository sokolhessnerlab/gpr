# GPR Data Processing Script
#
# Script to process the eyetracking data collected from the GPR (Goal Pressure
# and Risk-taking) study in 2025-2026.
#

# STEP 0: CONNECTIONS ----
# - Connect to the server

# STEP 1: SET YOUR WORKING DIRECTORY! ----
# On PSH's computers...
setwd('/Users/sokolhessner/Documents/gitrepos/gpr/');
# On JB's computers...
# setwd('/Users/justinblake/Documents/gpr/');

# STEP 2: then run from here on the same ----
config = config::get();

setwd(config$path$data$raw);

# STEP 3: Get the file names & set variables ----
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

# Prep object for goalfn information (and other subject-level info
# Set up variables to hold decision-making data

# ONE ROW PER SUBJECT
column_names_subjlevel_wide = c(
  'subjectnumber',
  'round1earnings', # achieved earnings
  'round2earnings',
  'round3earnings',
  'round4earnings',
  'round1bonusreceived01', # did they get the bonus (1) or not(0)
  'round2bonusreceived01',
  'round3bonusreceived01',
  'round4bonusreceived01',
  'round1bonusatstake', # the bonus they were trying to get
  'round2bonusatstake',
  'round3bonusatstake',
  'round4bonusatstake',
  'round1goallevel', # the goal level
  'round2goallevel',
  'round3goallevel',
  'round4goallevel',
  'totalcompensation' # total $ compensation
);

column_names_subjlevel_long = c(
  'subjectnumber',
  'roundnum', # achieved earnings
  'earnings',
  'bonusreceived01', # did they get the bonus (1) or not(0)
  'bonusatstake', # the bonus they were trying to get
  'goallevel' # the goal level
);


data_subjlevel_wide = as.data.frame(array(data = NA, dim = c(number_of_subjects, length(column_names_subjlevel_wide))));
colnames(data_subjlevel_wide) <- column_names_subjlevel_wide

data_subjlevel_long = as.data.frame(array(data = NA, dim = c(number_of_subjects*4, length(column_names_subjlevel_long))));
colnames(data_subjlevel_long) <- column_names_subjlevel_long


# STEP 4: Load and Process Data ----
cat('Loading and processing data.\n');

for(s in 1:number_of_subjects){
  cat(sprintf('GPR%03i: DM',subject_IDs[s]))
  
  
  ## DECISION MAKING PROCESSING ----
  
  # Load in the data
  tmpdata = read.csv(rdmfn[s]);
  
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
  
  
  ## WORKING MEMORY PROCESSING ----
  
  cat(', WM')
  wm_data_to_add = array(data = NA, dim = c(number_of_wm_trials_per_person,length(column_names_wm)));
  wm_data_to_add = as.data.frame(wm_data_to_add)
  colnames(wm_data_to_add) <- column_names_wm
  
  # Load in the data
  tmpdata = read.csv(digitspanfn[s]);
  
  wm_trial_indices = which((!is.na(tmpdata$trialNumber)) & is.finite(tmpdata$correct));
  
  wm_data_to_add[,1] = 1:number_of_wm_trials_per_person; # trial numbers
  wm_data_to_add[,2] = subject_IDs[s]; # subject number

  wm_data_to_add[,3] = nchar(tmpdata$digitsForTrial[wm_trial_indices-1])/3; # number of digits on the trial
  
  wm_data_to_add[1:14,4] = 1; # forward is always first
  wm_data_to_add[15:28,4] = 0; # backward is always second
  
  wm_data_to_add[,5] = tmpdata$correct[wm_trial_indices]; # correct = 1, incorrect = 0
  
  data_wm = rbind(data_wm,wm_data_to_add);
  
  rm(tmpdata) # remove the temporary file
  
  
  ## SUBJECT-LEVEL DATA PROCESSING ----
  
  cat(', subject-level')
  
  # Load in the data
  tmpdata = read.csv(goalfn[s]);
  
  tmpgoals = dm_data_to_add$curr_goal[dm_data_to_add$trialnumber_block == 1]
  tmpbonus = dm_data_to_add$curr_bonus[dm_data_to_add$trialnumber_block == 1]
  
  # WIDE VERSION (1 row per subject)
  data_subjlevel_wide$subjectnumber[s] = subject_IDs[s]
  data_subjlevel_wide$round1earnings[s] = as.numeric(tmpdata$roundearnings[1])
  data_subjlevel_wide$round2earnings[s] = as.numeric(tmpdata$roundearnings[2])
  data_subjlevel_wide$round3earnings[s] = as.numeric(tmpdata$roundearnings[3])
  data_subjlevel_wide$round4earnings[s] = as.numeric(tmpdata$roundearnings[4])
  
  data_subjlevel_wide$round1bonusreceived01[s] = as.numeric(tmpdata$roundbonus[1] > 0)
  data_subjlevel_wide$round2bonusreceived01[s] = as.numeric(tmpdata$roundbonus[2] > 0)
  data_subjlevel_wide$round3bonusreceived01[s] = as.numeric(tmpdata$roundbonus[3] > 0)
  data_subjlevel_wide$round4bonusreceived01[s] = as.numeric(tmpdata$roundbonus[4] > 0)

  data_subjlevel_wide$round1bonusatstake[s] = tmpbonus[1]
  data_subjlevel_wide$round2bonusatstake[s] = tmpbonus[2]
  data_subjlevel_wide$round3bonusatstake[s] = tmpbonus[3]
  data_subjlevel_wide$round4bonusatstake[s] = tmpbonus[4]
  
  data_subjlevel_wide$round1goallevel[s] = tmpgoals[1]
  data_subjlevel_wide$round2goallevel[s] = tmpgoals[2]
  data_subjlevel_wide$round3goallevel[s] = tmpgoals[3]
  data_subjlevel_wide$round4goallevel[s] = tmpgoals[4]
  
  data_subjlevel_wide$totalcompensation = as.numeric(tmpdata$totalcompensation[5])
  
  # "LONG" VERSION (4 rows per subject)
  subj_level_long_ind = ((s-1)*4+1):((s-1)*4+4)
  data_subjlevel_long$subjectnumber[subj_level_long_ind] = subject_IDs[s];
  data_subjlevel_long$roundnum[subj_level_long_ind] = 1:4;
  data_subjlevel_long$earnings[subj_level_long_ind] = as.numeric(tmpdata$roundearnings[1:4])
  data_subjlevel_long$bonusreceived01[subj_level_long_ind] = as.numeric(tmpdata$roundbonus[1:4] > 0)
  data_subjlevel_long$bonusatstake[subj_level_long_ind] = tmpbonus
  data_subjlevel_long$goallevel[subj_level_long_ind] = tmpgoals
  
  cat('. Done.\n')
}

# STEP 5: SAVE OUT PROCESSED DATA FILES ----
cat('Saving data.\n');
setwd(config$path$data$processed);

write.csv(data_dm, file=sprintf('gpr_processed_decisionmaking_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);
write.csv(data_wm, file=sprintf('gpr_processed_workingmemory_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);
write.csv(data_subjlevel_wide, file=sprintf('gpr_processed_subjlevelwide_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);
write.csv(data_subjlevel_long, file=sprintf('gpr_processed_subjlevellong_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);

cat('Finished with preprocessing. Go forth & analyze!\n\n')

