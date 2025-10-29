# GPR Analysis Script
#
# Script to process the data collected from the GPR (Goal Pressure
# and Risk-taking) study in 2025-2026.
#

# STEP 0: CONNECTIONS ----
# - Connect to the server
rm(list = ls())

# STEP 1: SET YOUR WORKING DIRECTORY! ----
# On PSH's computers...
#setwd('/Users/sokolhessner/Documents/gitrepos/gpr/');
# On JB's computers...
setwd('/Users/justinblake/Documents/GitHub/gpr/');

# STEP 2: Load pre-processed data files ----
config = config::get();

setwd(config$path$data$processed)

dmfn = dir(pattern = glob2rx('gpr_processed_decisionmaking_data_*.csv'),full.names = T, recursive = T);
wmfn = dir(pattern = glob2rx('gpr_processed_workingmemory_data_*.csv'),full.names = T, recursive = T);
subjlevelwidefn = dir(pattern = glob2rx('gpr_processed_subjlevelwide_data_*.csv'),full.names = T, recursive = T);
subjlevellongfn = dir(pattern = glob2rx('gpr_processed_subjlevellong_data_*.csv'),full.names = T, recursive = T);

data_dm = read.csv(dmfn[length(dmfn)])
data_wm = read.csv(wmfn[length(wmfn)])
data_subjlevel_wide = read.csv(subjlevelwidefn[length(subjlevelwidefn)])
data_subjlevel_long = read.csv(subjlevellongfn[length(subjlevellongfn)])

num_rdm_trials = 50;
num_rdm_blocks = 4;
number_of_dm_trials_per_person = num_rdm_trials * num_rdm_blocks; # static = 200

subject_IDs = unique(data_dm$subjectnumber)
number_of_subjects = length(subject_IDs)

# STEP 3: Quality Assurance ----

# Use...
# - percent risky/safe choices
# - RTs (too fast)
# - qualtrics attention check
# - button press (e.g. all left; or all alternating)

# Need a separate assessment of whether SCL is "good enough" to be used?
#   Variability in SCL or in change in SCL over time?
#   Mean levels? 


# STEP 4: ANALYZE ----

## 1. PERSON-LEVEL ----
# Who are our subjects? 

# Working Memory
# FS & BS max number_digits/length when correct (BEST SPAN)
# Q: is there a difference in max number of digits correct in FS vs BS (comparing fs max digit length correct to bs)
best_span_FS = array(dim = c(number_of_subjects,1));
best_span_BS = array(dim = c(number_of_subjects,1));

for (s in 1:number_of_subjects){
  # subj_id = keep_participants[subj]
  # tmpdata = data_wm[data_wm$subjectnumber == subj_id,]
  # best_span_FS[subj] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 1) & (tmpdata$correct == 1)], na.rm = T);
  # best_span_BS[subj] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 0) & (tmpdata$correct == 1)], na.rm = T);
  subj_id = subject_IDs[s]
  tmpdata = data_wm[data_wm$subjectnumber == subj_id,]
  best_span_FS[s] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 1) & (tmpdata$correct == 1)], na.rm = T);
  best_span_BS[s] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 0) & (tmpdata$correct == 1)], na.rm = T);
}

t.test(best_span_FS, best_span_BS, paired = T);
#A: yes, significant difference between max digit number/length FS correct compared to BS correct (10/8/25)!
#   Indicates that people have different capcities FS and BS

cor.test(best_span_BS,best_span_FS)
#A: yes, very correlated (r = 0.77, p = 4.5e-10)! 
plot(best_span_BS, best_span_FS, 
     pch = 19, col = rgb(.5, .5, .5, .3), 
     xlim = c(0, 12.5), ylim = c(0, 12.5), cex = 2.5,
     xlab = 'Best Backwards Span', ylab = 'Best Forwards Span', 
     main = 'Forward vs Backwards Capacity')
lines(x = c(0, 12), y = c(0, 12))

# Collapse spans into a single span measure
best_span_overall = rowMeans(cbind(best_span_FS,best_span_BS))

hist(best_span_overall)


## 2. BLOCK-LEVEL ----
# What happened in the different blocks?


## 3. TRIAL-LEVEL ----
# What happened across trials? 
# Why/how did trial events shape block events? 

