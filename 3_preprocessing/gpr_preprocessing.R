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
# setwd('/Users/justinblake/Documents/GitHub/gpr/');

# STEP 2: then run from here on the same ----
config = config::get();

setwd(config$path$data$raw);

# STEP 3: Get the file names & set variables ----
cat('Identifying data file locations.\n');
rdmfn = dir(pattern = glob2rx('rdmDatasub*_gprRDM_*.csv'),full.names = T, recursive = T);
digitspanfn = dir(pattern = glob2rx('*gprDigitSpan*.csv'),full.names = T, recursive = T);
goalfn = dir(pattern = glob2rx('rdmDatasub*_gprBonusCompensation_*.csv'),full.names = T, recursive = T);
sclfn = dir(pattern = glob2rx('gpr*25_3.txt'),full.names = T, recursive = T);
qualfn = dir(pattern = glob2rx('gprQualtricsData_values_*.csv'),full.names = T, recursive = T);

all_dirs = dir(pattern = glob2rx('gpr???')); # three-numbered item names
subject_IDs = c();
for (s in 1:length(all_dirs)){
  subject_IDs = c(subject_IDs,as.numeric(substr(all_dirs[s],4,6))) # read subject IDs from directory names
}

number_of_subjects = length(subject_IDs)


# Store some basic information about size of the decision-making task
num_rdm_trials = 50;
num_rdm_blocks = 4;
number_of_dm_trials_per_person = num_rdm_trials * num_rdm_blocks;
scl_sampling_rate = 200 # 200 Hz (200 samples/second)

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
  'otc_epoch_end',
  'meanscl'
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
  'totalcompensation', # total $ compensation
  'stais',
  'stait',
  'rrs_brood',
  'rrs_reflection',
  'rrs_overall',
  'bas_drive',
  'bas_fun',
  'bas_reward',
  'bis_overall',
  'bisbas_overall', 
  'age',
  # 'gender', # NOT INCLUDING THESE B/C NO PRIOR HYPOTHESES, AND HARD TO USE AS ANALYSIS VARIABLE
  # 'ethnicity',
  # 'race',
  # 'highest_degree_attained',      
  # 'political_orientation',        
  # 'first_generation',             
  'attn_check_correct',
  'qualtrics_duration'
);

column_names_subjlevel_long = c(
  'subjectnumber',
  'roundnum', # achieved earnings
  'earnings',
  'bonusreceived01', # did they get the bonus (1) or not(0)
  'bonusatstake', # the bonus they were trying to get
  'goallevel', # the goal level
  'stais',
  'stait',
  'rrs_brood',
  'rrs_reflection',
  'rrs_overall',
  'bas_drive',
  'bas_fun',
  'bas_reward',
  'bis_overall',
  'bisbas_overall',
  'age',
  'meanscl', # mean SCL value in this block
  'slopescl', # slope of the SCL across this block
  'changebeforescl' # change of the SCL from 30 seconds before the block begins to onset of first choice, i.e. during instruction
);


data_subjlevel_wide = as.data.frame(array(data = NA, dim = c(number_of_subjects, length(column_names_subjlevel_wide))));
colnames(data_subjlevel_wide) <- column_names_subjlevel_wide

data_subjlevel_long = as.data.frame(array(data = NA, dim = c(number_of_subjects*4, length(column_names_subjlevel_long))));
colnames(data_subjlevel_long) <- column_names_subjlevel_long


# STEP 4: Load and Process Data ----
cat('Loading and processing data.\n');

# Load Qualtrics data (only need to do this once, since all subj are in it)
raw_qualtrics_data <- read.csv(qualfn[length(qualfn)])
raw_qualtrics_data = raw_qualtrics_data[-1:-6,]
num_qualtrics_data = suppressWarnings(as.data.frame(apply(raw_qualtrics_data,2,as.numeric)))
# Warnings suppressed b/c of multiple conversion-to-NA errors

number_of_qualtrics_subjects = nrow(num_qualtrics_data)

if (number_of_subjects != number_of_qualtrics_subjects){
  warning(sprintf('Numbers of subjects do not match! Behavioral N = %i; Qualtrics N = %i.',
                  number_of_subjects, number_of_qualtrics_subjects))
}

for(s in 1:number_of_subjects){
  cat(sprintf('GPR%03i: DM',subject_IDs[s]))
  
  
  ## DECISION-MAKING PROCESSING ----
  
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
  
  data_subjlevel_wide$totalcompensation[s] = as.numeric(tmpdata$totalcompensation[5])
  
  # "LONG" VERSION (4 rows per subject)
  subj_level_long_ind = ((s-1)*4+1):((s-1)*4+4)
  data_subjlevel_long$subjectnumber[subj_level_long_ind] = subject_IDs[s];
  data_subjlevel_long$roundnum[subj_level_long_ind] = 1:4;
  data_subjlevel_long$earnings[subj_level_long_ind] = as.numeric(tmpdata$roundearnings[1:4])
  data_subjlevel_long$bonusreceived01[subj_level_long_ind] = as.numeric(tmpdata$roundbonus[1:4] > 0)
  data_subjlevel_long$bonusatstake[subj_level_long_ind] = tmpbonus
  data_subjlevel_long$goallevel[subj_level_long_ind] = tmpgoals
  
  
  if(subject_IDs[s] %in% num_qualtrics_data$EI_2){
    
    # First, identify which row of the qualtrics import we're using
    qual_rowInd = which(subject_IDs[s] == num_qualtrics_data$EI_2)
    
    # Process the QUALTRICS Data and include in subject-level dfs
    # Do WIDE first
    data_subjlevel_wide$stais[s] =  5 - num_qualtrics_data$GPR.STAI.S_1[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.S_2[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_3[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_4[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.S_5[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_6[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_7[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.S_8[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_9[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.S_10[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.S_11[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_12[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_13[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_14[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.S_15[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.S_16[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_17[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.S_18[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.S_19[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.S_20[qual_rowInd];
    
    data_subjlevel_wide$stait[s] =  5 - num_qualtrics_data$GPR.STAI.T_1[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_2[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.T_3[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_4[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_5[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.T_6[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.T_7[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_8[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_9[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.T_10[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_11[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_12[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.T_13[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.T_14[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_15[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.T_16[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_17[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_18[qual_rowInd] +
                                    5 - num_qualtrics_data$GPR.STAI.T_19[qual_rowInd] +
                                    num_qualtrics_data$GPR.STAI.T_20[qual_rowInd];
    
    
    data_subjlevel_wide$attn_check_correct[s] = as.numeric(num_qualtrics_data$Attention.Check[qual_rowInd] == 3);

    data_subjlevel_wide$age[s] = num_qualtrics_data$Age[qual_rowInd];

    data_subjlevel_wide$rrs_brood[s] =  num_qualtrics_data$GPR.RRS.10_1[qual_rowInd] +
                                        num_qualtrics_data$GPR.RRS.10_3[qual_rowInd] +
                                        num_qualtrics_data$GPR.RRS.10_6[qual_rowInd] +
                                        num_qualtrics_data$GPR.RRS.10_7[qual_rowInd] +
                                        num_qualtrics_data$GPR.RRS.10_8[qual_rowInd];

    data_subjlevel_wide$rrs_reflection[s] = num_qualtrics_data$GPR.RRS.10_2[qual_rowInd] +
                                            num_qualtrics_data$GPR.RRS.10_4[qual_rowInd] +
                                            num_qualtrics_data$GPR.RRS.10_5[qual_rowInd] +
                                            num_qualtrics_data$GPR.RRS.10_9[qual_rowInd] +
                                            num_qualtrics_data$GPR.RRS.10_10[qual_rowInd];

    data_subjlevel_wide$rrs_overall[s] = data_subjlevel_wide$rrs_brood[s] + data_subjlevel_wide$rrs_reflection[s]


    data_subjlevel_wide$bas_drive[s] =  num_qualtrics_data$GPR.BIS.BAS_3[qual_rowInd] +
                                        num_qualtrics_data$GPR.BIS.BAS_9[qual_rowInd] +
                                        num_qualtrics_data$GPR.BIS.BAS_12[qual_rowInd]
                                        num_qualtrics_data$GPR.BIS.BAS_21[qual_rowInd];
    
    
    data_subjlevel_wide$bas_fun[s] =  num_qualtrics_data$GPR.BIS.BAS_5[qual_rowInd] +
                                      num_qualtrics_data$GPR.BIS.BAS_10[qual_rowInd] +
                                      num_qualtrics_data$GPR.BIS.BAS_15[qual_rowInd] +
                                      num_qualtrics_data$GPR.BIS.BAS_20[qual_rowInd];

    data_subjlevel_wide$bas_reward[s] = 5 - num_qualtrics_data$GPR.BIS.BAS_4[qual_rowInd] +
                                            num_qualtrics_data$GPR.BIS.BAS_7[qual_rowInd] +
                                            num_qualtrics_data$GPR.BIS.BAS_14[qual_rowInd] +
                                            num_qualtrics_data$GPR.BIS.BAS_18[qual_rowInd] +
                                            num_qualtrics_data$GPR.BIS.BAS_23[qual_rowInd];
                                  
     
    data_subjlevel_wide$bis_overall[s] =  5 - num_qualtrics_data$GPR.BIS.BAS_2[qual_rowInd] +
                                              num_qualtrics_data$GPR.BIS.BAS_8[qual_rowInd] +
                                              num_qualtrics_data$GPR.BIS.BAS_13[qual_rowInd] +
                                              num_qualtrics_data$GPR.BIS.BAS_16[qual_rowInd] +
                                              num_qualtrics_data$GPR.BIS.BAS_19[qual_rowInd] +
                                              num_qualtrics_data$GPR.BIS.BAS_22[qual_rowInd] +
                                              num_qualtrics_data$GPR.BIS.BAS_24[qual_rowInd];
    
    data_subjlevel_wide$bisbas_overall[s] = data_subjlevel_wide$bis_overall[s] + data_subjlevel_wide$bas_drive[s] + data_subjlevel_wide$bas_fun[s] + data_subjlevel_wide$bas_reward[s]
                                        
    data_subjlevel_wide$qualtrics_duration[s] = num_qualtrics_data$Duration..in.seconds.[qual_rowInd]
  }
  
  
  ## SCL DATA PROCESSING ----
  
  cat(', SCL')
  
  # Load the data
  tmp_scl = read.delim(sclfn[s], sep = "\t", header = F)
  tmp_scl = tmp_scl[,-5] # remove an empty data column
  
  colnames(tmp_scl) <- c('scl_raw', 'scl_filt', 'scl_filt_sm', 'ttl')
  # Columns:
  # 1. Raw SCL (microsiemens)
  # 2. SCL filtered (Low pass filter, freq. cutoff of 25, coefficients = 16, type = Blackman)
  # 3. SCL filtered & smoothed (kernel of 3, mean)
  # 4. TTL (values of 0 or 5 corresponding to off or on)
  #     Pattern is:
  #     ON: ITI ends / Decision window begins
  #     OFF: Response entered & decision window ends / ISI begins
  #     ON: ISI ends / Outcome begins
  #     OFF: Outcome ends / ITI begins
  #
  # N.B.: in practice, filtering is the most impactful thing. Smoothing does 
  # relatively little after the filtering. 
  
  
  ### PER-TRIAL MEANS ----
  
  # Identify sample indices of the start and end of each trial
  diff_ttl = diff(tmp_scl$ttl) # identify where the TTL changes from 0-5 and 5-0
  
  ttl_onsets_ind = which(diff_ttl == 5) + 1 # FIRST +5 value
  ttl_offsets_ind = which(diff_ttl == -5) # LAST +5 value
  
  # Check that assumptions are correct!
  # With 5 practice trials + 50 trials/block for 4 blocks, expect 205 trials,
  # each of which should have two onsets and two offsets (see above), so length
  # of both of these indices should be 410. 
  if(length(ttl_onsets_ind) != 410){
    warning(sprintf('Incorrect number of ONSETS found (expecting %i, found %i)!',
                    length(ttl_onsets_ind), 410))
  }
  
  if(length(ttl_offsets_ind) != 410){
    warning(sprintf('Incorrect number of OFFSETS found (expecting %i, found %i)!',
                    length(ttl_offsets_ind), 410))
  }
  
  # Onset of the decision period (odd indices of the onsets, skipping prac.)
  trial_start_ind = ttl_onsets_ind[seq(from = 11, by = 2, to = 410)]
  
  # Offset of the outcome period (even indices of the offsets, skipping prac.)
  trial_end_ind = ttl_offsets_ind[seq(from = 12, by = 2, to = 410)]
  
  # Calculate means on a per-trial basis
  for (t in 1:number_of_dm_trials_per_person){
    tmp_ind_vals = trial_start_ind[t]:trial_end_ind[t] # the indices
    dm_data_to_add$meanscl[t] = mean(tmp_scl$scl_filt_sm[tmp_ind_vals]) # calc the mean
  }
  
  ### PER-BLOCK MEANS ----
  # meanscl
  data_subjlevel_long$meanscl[subj_level_long_ind] = c(
    mean(tmp_scl$scl_filt_sm[trial_start_ind[1]:trial_end_ind[50]]),
    mean(tmp_scl$scl_filt_sm[trial_start_ind[51]:trial_end_ind[100]]),
    mean(tmp_scl$scl_filt_sm[trial_start_ind[101]:trial_end_ind[150]]),
    mean(tmp_scl$scl_filt_sm[trial_start_ind[151]:trial_end_ind[200]])
  )
  
  # slopescl
  data_subjlevel_long$slopescl[subj_level_long_ind] = c(
    tmp_scl$scl_filt_sm[trial_end_ind[50]] - tmp_scl$scl_filt_sm[trial_start_ind[1]],
    tmp_scl$scl_filt_sm[trial_end_ind[100]] - tmp_scl$scl_filt_sm[trial_start_ind[51]],
    tmp_scl$scl_filt_sm[trial_end_ind[150]] - tmp_scl$scl_filt_sm[trial_start_ind[101]],
    tmp_scl$scl_filt_sm[trial_end_ind[200]] - tmp_scl$scl_filt_sm[trial_start_ind[151]]
  )
  
  # changebeforescl
  lengthback = 30 # seconds back
  nsamplesback = lengthback * scl_sampling_rate
  data_subjlevel_long$changebeforescl[subj_level_long_ind] = c(
    tmp_scl$scl_filt_sm[trial_start_ind[1]] - tmp_scl$scl_filt_sm[trial_start_ind[1] - nsamplesback],
    tmp_scl$scl_filt_sm[trial_start_ind[51]] - tmp_scl$scl_filt_sm[trial_start_ind[51] - nsamplesback],
    tmp_scl$scl_filt_sm[trial_start_ind[101]] - tmp_scl$scl_filt_sm[trial_start_ind[101] - nsamplesback],
    tmp_scl$scl_filt_sm[trial_start_ind[151]] - tmp_scl$scl_filt_sm[trial_start_ind[151] - nsamplesback]
  )
  
  
  # Bind all the data
  # Add this person's DM and WM data to the total data structures. 
  data_dm = rbind(data_dm,dm_data_to_add);
  data_wm = rbind(data_wm,wm_data_to_add);
  
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

