# GPR Data Processing Script
#
# Script to process the eyetracking data collected from the GPR (Goal Pressure
# and Risk-taking) study in 2025-2026.
#

# STEP 0: CONNECTIONS ----
# - Connect to the server

# STEP 1: SET YOUR WORKING DIRECTORY! ----
# On PSH's computers...
#setwd('/Users/sokolhessner/Documents/gitrepos/gpr/');
# On JB's computers...
setwd('/Users/justinblake/Documents/GitHub/gpr/');

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
  
  # End of Task Qualtrics Data
  raw_qualtrics_data <- read.csv("gprQualtricsData_values_20251011.csv")
  raw_qualtrics_data = raw_qualtrics_data[-1,]
  
  column_names_qualtrics = c(
    'subID',          #gprXXX
    'stai_s_1',       #state anxiety - Just put the overall score? - 1, 2, 5, 8, 10, 11, 15, 16, 19, 20 reverse scored (might be already from XM)
    'stai_s_2',
    'stai_s_3',
    'stai_s_4',
    'stai_s_5',
    'stai_s_6',
    'stai_s_7',
    'stai_s_8',
    'stai_s_9',
    'stai_s_10',
    'stai_s_11',
    'stai_s_12',
    'stai_s_13',
    'stai_s_14',
    'stai_s_15',
    'stai_s_16',
    'stai_s_17',
    'stai_s_18',
    'stai_s_19',
    'stai_s_20',
    'stai_s_overall',
    'stai_t_1',       #trait anxiety - Just put the overall score? - 1, 3, 6, 7, 10, 13, 14, 16, 19 reverse scored (might be already from XM)
    'stai_t_2',
    'stai_t_3',
    'stai_t_4',
    'stai_t_5',
    'stai_t_6',
    'stai_t_7',
    'stai_t_8',
    'stai_t_9',
    'stai_t_10',
    'stai_t_11',
    'stai_t_12',
    'stai_t_13',
    'stai_t_14',
    'stai_t_15',
    'stai_t_16',
    'stai_t_17',
    'stai_t_18',
    'stai_t_19',
    'stai_t_20',
    'stai_t_overall',
    'rrs_1',          #rumination - Just put the overall score?
    'rrs_2',
    'rrs_3',
    'rrs_4',
    'rrs_5',
    'rrs_6',
    'rrs_7',
    'rrs_8',
    'rrs_9',
    'rrs_10',
    'rrs_brood',
    'rrs_reflect',
    'rrs_overall',
    'bis_bas_1',      #BIS/BAS - Just put the overall score? - 1, 6, 11, and 17 are fillers (won't calculate them)
    'bis_bas_2',
    'bis_bas_3',
    'bis_bas_4',
    'bis_bas_5',
    'bis_bas_6',
    'bis_bas_7',
    'bis_bas_8',
    'bis_bas_9',
    'bis_bas_10',
    'bis_bas_11',
    'bis_bas_12',
    'bis_bas_13',
    'bis_bas_14',
    'bis_bas_15',
    'bis_bas_16',
    'bis_bas_17',
    'bis_bas_18',
    'bis_bas_19',
    'bis_bas_20',
    'bis_bas_21',
    'bis_bas_22',
    'bis_bas_23',
    'bis_bas_24',
    'bis_bas_overall',
    'age',
    'gender',                       
    'ethnicity',                    
    'race',                         
    'highest_degree_attained',      
    'political_orientation',        
    'first_generation',             
    'fraction_attn_check_correct'
  );
  
  number_of_qualtrics_subjects = dim(raw_qualtrics_data)
  
  data_qualtrics = array(data = NA, dim = c(number_of_qualtrics_subjects, length(column_names_qualtrics)));
  colnames(data_qualtrics) <- column_names_qualtrics
  data_qualtrics = as.data.frame(data_qualtrics) ### THIS IS WHERE I GOT STUCK - I don't know what's wrong exactly, but I think that it might be that the above names don't match what is in the qualtrics csv file? ###
  
  data_qualtrics$attn_check_correct = (as.numeric(raw_qualtrics_data$attentionCheck1) +
                                         as.numeric(raw_qualtrics_data$attentionCheck2) +
                                         as.numeric(raw_qualtrics_data$attentionCheck3))/3;
  
  
  data_qualtrics$subID = as.numeric(raw_qualtrics_data$subID);
  
  data_qualtrics$age = as.numeric(raw_qualtrics_data$Age);
  
  data_qualtrics$ethnicity = as.numeric(raw_qualtrics_data$Ethnicity);
  # 1-Hispanic/Latinx, 2-Not Hispanic/Latinx, 3-Prefer not to say
  
  data_qualtrics$race = as.numeric(raw_qualtrics_data$Race);
  # 1-American/Alaskan Native, 2-Black/African-American, 3-East Asian, 4-Native Hawaiian/Pacific Islander, 5-South Asian, 6-White, 7-Bi-racial, 8-Other, 9-Prefer not to say
  
  data_qualtrics$highest_degree_attained = as.numeric(raw_qualtrics_data$Education_Level)
  # 1-No school, 2-Nursery to 8th, 3-High school-no diploma, 4-High school diploma, 5-trade school, 6-associates degree, 7-bachelors degree, 8-masters degree, 9-professional degree, 10-doctorate
  
  data_qualtrics$gender = as.numeric(raw_qualtrics_data$Gender)
  # 1-Man, 2-Woman, 3-Non-Binary, 4-Genderqueer, 5-Gender Expansive, 6-Two-Spirited, 7-Third Gender, 8-Agender, 9-Not Sure, 10-Other, 11-Prefer not to say
  
  data_qualtrics$political_orientation = as.numeric(raw_qualtrics_data$Politics)
  # 1-Extremely conservative, 5-centrist, 9-Extremely liberal
  
  data_qualtrics$first_generation = as.numeric(raw_qualtrics_data$First_Generation)
  # 1-Yes, 2-No, 3-Unsure
  
  data_qualtrics$stai_s_overall = (5 - as.numeric(raw_qualtrics_data$stai_s_1)) +
                                     5 - as.numeric(raw_qualtrics_data$stai_s_2) +
                                     as.numeric(raw_qualtrics_data$stai_s_3) +
                                     as.numeric(raw_qualtrics_data$stai_s_4) +
                                     5 - as.numeric(raw_qualtrics_data$stai_s_5) +
                                     as.numeric(raw_qualtrics_data$stai_s_6) +
                                     as.numeric(raw_qualtrics_data$stai_s_7) +
                                     5 - as.numeric(raw_qualtrics_data$stai_s_8) +
                                     as.numeric(raw_qualtrics_data$stai_s_9) +
                                     5 - as.numeric(raw_qualtrics_data$stai_s_10) +
                                     5 - as.numeric(raw_qualtrics_data$stai_s_11) +
                                     as.numeric(raw_qualtrics_data$stai_s_12) +
                                     as.numeric(raw_qualtrics_data$stai_s_13) +
                                     as.numeric(raw_qualtrics_data$stai_s_14) +
                                     5 - as.numeric(raw_qualtrics_data$stai_s_15) +
                                     5 - as.numeric(raw_qualtrics_data$stai_s_16) +
                                     as.numeric(raw_qualtrics_data$stai_s_17) +
                                     as.numeric(raw_qualtrics_data$stai_s_18) +
                                     5 - as.numeric(raw_qualtrics_data$stai_s_19) +
                                     5 - as.numeric(raw_qualtrics_data$stai_s_20);
  
  data_qualtrics$stai_t_overall = (5 - as.numeric(raw_qualtrics_data$stai_t_1)) +
                                     as.numeric(raw_qualtrics_data$stai_t_2) +
                                     5 - as.numeric(raw_qualtrics_data$stai_t_3) +
                                     as.numeric(raw_qualtrics_data$stai_t_4) +
                                     as.numeric(raw_qualtrics_data$stai_t_5) +
                                     5 - as.numeric(raw_qualtrics_data$stai_t_6) +
                                     5 - as.numeric(raw_qualtrics_data$stai_t_7) +
                                     as.numeric(raw_qualtrics_data$stai_t_8) +
                                     as.numeric(raw_qualtrics_data$stai_t_9) +
                                     5 - as.numeric(raw_qualtrics_data$stai_t_10) +
                                     as.numeric(raw_qualtrics_data$stai_t_11) +
                                     as.numeric(raw_qualtrics_data$stai_t_12) +
                                     5 - as.numeric(raw_qualtrics_data$stai_t_13) +
                                     5 - as.numeric(raw_qualtrics_data$stai_t_14) +
                                     as.numeric(raw_qualtrics_data$stai_t_15) +
                                     5 - as.numeric(raw_qualtrics_data$stai_t_16) +
                                     as.numeric(raw_qualtrics_data$stai_t_17) +
                                     as.numeric(raw_qualtrics_data$stai_t_18) +
                                     5 - as.numeric(raw_qualtrics_data$stai_t_19) +
                                     as.numeric(raw_qualtrics_data$stai_t_20);
  
  data_qualtrics$rrs_brood = (as.numeric(raw_qualtrics_data$rrs_1)) +
                                as.numeric(raw_qualtrics_data$rrs_3) +
                                as.numeric(raw_qualtrics_data$rrs_6) +
                                as.numeric(raw_qualtrics_data$rrs_7) +
                                as.numeric(raw_qualtrics_data$rrs_8);
                                 
  data_qualtrics$rrs_reflect = (as.numeric(raw_qualtrics_data$rrs_2)) +
                                  as.numeric(raw_qualtrics_data$rrs_4) +
                                  as.numeric(raw_qualtrics_data$rrs_5) +
                                  as.numeric(raw_qualtrics_data$rrs_9) +
                                  as.numeric(raw_qualtrics_data$rrs_10);
                                
  data_qualtrics$rrs_overall = (rrs_brood + rrs_reflect)
  
                                
  data_qualtrics$bas_drive = (as.numeric(raw_qualtrics_data$bis_bas_3)) +
                                      as.numeric(raw_qualtrics_data$bis_bas_9) +
                                      as.numeric(raw_qualtrics_data$bis_bas_12) +
                                      as.numeric(raw_qualtrics_data$bis_bas_21);
  
  data_qualtrics$bas_fun = (as.numeric(raw_qualtrics_data$bis_bas_5)) +
                                      5 - as.numeric(raw_qualtrics_data$bis_bas_10) +
                                      as.numeric(raw_qualtrics_data$bis_bas_15) +
                                      as.numeric(raw_qualtrics_data$bis_bas_20);
  
  data_qualtrics$bas_reward = (5 - as.numeric(raw_qualtrics_data$bis_bas_4)) +
                                      as.numeric(raw_qualtrics_data$bis_bas_7) +
                                      as.numeric(raw_qualtrics_data$bis_bas_14) +
                                      as.numeric(raw_qualtrics_data$bis_bas_18) +
                                      as.numeric(raw_qualtrics_data$bis_bas_23);
  
  data_qualtrics$bis_overall = (5 - as.numeric(raw_qualtrics_data$bis_bas_2)) +
                                      5 - as.numeric(raw_qualtrics_data$bis_bas_8) +
                                      5 - as.numeric(raw_qualtrics_data$bis_bas_13) +
                                      as.numeric(raw_qualtrics_data$bis_bas_16) +
                                      as.numeric(raw_qualtrics_data$bis_bas_19) +
                                      as.numeric(raw_qualtrics_data$bis_bas_22) +
                                      as.numeric(raw_qualtrics_data$bis_bas_24);
  
  data_qualtrics$bis_bas_overall = (bis_overall + bas_drive + bas_fun + bas_reward)
  
  
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

