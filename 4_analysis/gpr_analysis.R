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
setwd('/Users/sokolhessner/Documents/gitrepos/gpr/');
# On JB's computers...
# setwd('/Users/justinblake/Documents/GitHub/gpr/');

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

## 3.1: EXCLUSION: RTs ----

mean_rts = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  
  mean_rts[subj] = mean(tmpdata$reactiontime, na.rm = T)
}

keep_dm_rt = mean_rts > 0.85; # excludes 3 people (9, 22, 57)

mean_rts[keep_dm_rt]
hist(mean_rts[keep_dm_rt]) # histogram of mean rts
mean(mean_rts[keep_dm_rt]) # mean rt 1.59362 seconds (4/4/24)

## 3.2: EXCLUSION: % RISKY/SAFE ----
# Non-Check Trials only

mean_risky = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  
  mean_risky[subj] = mean(tmpdata$choice[tmpdata$ischecktrial == 0], na.rm = T)
}

keep_dm_prisky = (mean_risky < 0.95) & (mean_risky > .05); # does not exclude anyone

hist(mean_risky[keep_dm_prisky], xlim = c(0,1), breaks = 15)
mean(mean_risky[keep_dm_prisky])

## 3.3: EXCLUSION: Check Trials ----
# How did subjects do on check trials that they did succcessfully answer

check_trial_failurerate = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  check_trial_index = which((tmpdata$ischecktrial==1) & is.finite(tmpdata$reactiontime));
  correct_answers = (0.5 * tmpdata$riskyopt1[check_trial_index] +
                       0.5 * tmpdata$riskyopt2[check_trial_index]) > tmpdata$safe[check_trial_index];
  check_trial_failurerate[subj] = length(which(!tmpdata$choice[check_trial_index] == correct_answers))/length(check_trial_index);
  
  # Plot the choice data
  plot(tmpdata$riskyopt1[tmpdata$choice == 1],tmpdata$safe[tmpdata$choice == 1], col = 'green',
       xlab = 'Risky Gain $', ylab = 'Safe $', main = paste0('All Subjects; Subj ', subj),
       xlim = c(0,30), ylim = c(0,12))
  points(tmpdata$riskyopt1[tmpdata$choice == 0],tmpdata$safe[tmpdata$choice == 0], col = 'red')
}

check_trial_criterion = 0.2; # The maximum percent of check trials that can be missed
# (there were 40 check trials)
# chance is 0.5, perfect is 0.0.

keep_check_trial = check_trial_failurerate <= check_trial_criterion; # 2 did not meet criteria: 60, 63

## 3.4: EXCLUSION: Qualtrics Attention Check ----

keep_qualAC = data_subjlevel_wide$attn_check_correct == 1

## 3.5: Combine into a single keep_participants variable ----

keep_participants = which(keep_dm_rt & keep_dm_prisky & keep_check_trial & keep_qualAC)


# Create clean data frames for data!
clean_data_dm = data_dm[data_dm$subjectnumber %in% keep_participants,]
clean_data_wm = data_wm[data_wm$subjectnumber %in% keep_participants,]
clean_data_subjlevel_wide = data_subjlevel_wide[data_subjlevel_wide$subjectnumber %in% keep_participants,]
clean_data_subjlevel_long = data_subjlevel_long[data_subjlevel_long$subjectnumber %in% keep_participants,]

number_of_clean_subjects = length(keep_participants);
number_of_clean_subjects # 66 participants

# # Create a re-scaled version of trial number for use in subsequent analyses
clean_data_dm$trialnumber_overallRS = clean_data_dm$trialnumber_overall/max(clean_data_dm$trialnumber_overall)
clean_data_dm$trialnumber_blockRS = clean_data_dm$trialnumber_block/max(clean_data_dm$trialnumber_block)

# Need a separate assessment of whether SCL is "good enough" to be used?
#   Variability in SCL or in change in SCL over time?
#   Mean levels? 


# STEP 4: ANALYZE ----

## 1. PERSON-LEVEL ----
# Who are our subjects? 


### Working Memory Capacity ----

# FS & BS max number_digits/length when correct (BEST SPAN)
# Q: is there a difference in max number of digits correct in FS vs BS (comparing fs max digit length correct to bs)
best_span_FS = array(dim = c(number_of_clean_subjects,1));
best_span_BS = array(dim = c(number_of_clean_subjects,1));

for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_wm[clean_data_wm$subjectnumber == subj_id,]
  best_span_FS[s] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 1) & (tmpdata$correct == 1)], na.rm = T);
  best_span_BS[s] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 0) & (tmpdata$correct == 1)], na.rm = T);
}

t.test(best_span_FS, best_span_BS, paired = T);
#A: yes, significant difference between max digit number/length FS correct compared to BS correct
#   Indicates that people have different capacities FS and BS

cor.test(best_span_BS,best_span_FS)
#A: yes, very correlated (r = 0.76, p = p = 2.0e-13)! 

plot(best_span_BS, best_span_FS, 
     pch = 19, col = rgb(.5, .5, .5, .3), 
     xlim = c(0, 12.5), ylim = c(0, 12.5), cex = 2.5,
     xlab = 'Best Backwards Span', ylab = 'Best Forwards Span', 
     main = 'Forward vs Backwards Capacity')
lines(x = c(0, 12), y = c(0, 12))

# Collapse spans into a single span measure
best_span_overall = rowMeans(cbind(best_span_FS,best_span_BS))
mean(best_span_overall) # 7.45

hist(best_span_overall, breaks = 15)

# JUSTIN:
# 1. INSERT WMC VALUE INTO DM AND SUBJLEVEL ARRAYS
# 2. BUILD CORRELATION MATRIX WITH MAJOR ITEMS FROM SUBJLEVEL_WIDE & START TO INVESTIGATE THAT
# 3. START TO INVESTIGATE BONUS & GOAL AWARENESS & INFLUENCE

length(best_span_overall) # checking that it's 66 long! 

clean_data_dm$best_span_overall = NA 
clean_data_subjlevel_wide$best_span_overall = NA
clean_data_subjlevel_long$best_span_overall = NA

for (s in 1:length(keep_participants)) {
  subj_id = keep_participants[s]
  wmc_val = best_span_overall[s]
  
  clean_data_dm$best_span_overall[clean_data_dm$subjectnumber == subj_id] = wmc_val
  clean_data_subjlevel_wide$best_span_overall[clean_data_subjlevel_wide$subjectnumber == subj_id] = wmc_val
}

#Summary is to see that the above code worked
# summary(clean_data_dm$best_span_overall)
# # summary(clean_data_dm$best_span_overall[clean_data_dm$trialnumber_overall == 1])
# summary(clean_data_subjlevel_wide$best_span_overall)

# major_items = c('stais',
#                 'stait',
#                 'rrs_overall',
#                 'bisbas_overall',
#                 'totalcompensation',
#                 'psq_stress', 
#                 'psq_motivate',
#                 'psq_overall_difficult',
#                 'psq_goal_aware',
#                 'psq_goal_influence', 
#                 'psq_bonus_aware',
#                 'psq_bonus_influence',
#                 'psq_goal_influence_effort',
#                 'psq_goal_influence_speed',
#                 'psq_goal_influence_distract',
#                 'psq_goal_influence_anxiety',
#                 'psq_goal_influence_engage',
#                 'psq_bonus_influence_effort',
#                 'psq_bonus_influence_speed',
#                 'psq_bonus_influence_distract',
#                 'psq_bonus_influence_anxiety',
#                 'psq_bonus_influence_engage')

cor_items = c('totalcompensation',
                 'stais',
                 'stait',
                 'bis_overall',
                 'rrs_overall',
                 'round1earnings',
                 'round2earnings',
                 'round3earnings',
                 'round4earnings',
                 'round1bonusreceived01',
                 'round2bonusreceived01',
                 'round3bonusreceived01',
                 'round4bonusreceived01')
library(corrplot)

cor_matrix = cor(clean_data_subjlevel_wide[,cor_items])
cor_p = cor.mtest(clean_data_subjlevel_wide[,cor_items], conf.level = 0.95)$p

print(round(cor_matrix, 2))


corrplot(cor_matrix, type = 'lower', col = rev(COL2('RdBu')),
         p.mat = cor_p, sig.level = 0.05, insig='blank',
         addCoef.col ='black', number.cex = 1, diag=FALSE)

plot(clean_data_subjlevel_wide[,cor_items])

# SUMMARY: 
# - State, trait, rumination, and behavioral inhibition (-) are all
#   correlated with each other. 
# - Potentially study-level patterns or shifts in behavior. Maybe
#   earnings become more stable/less variable in later rounds?

# TO DO's
# - Histogram earnings across rounds (or density plot?) to examine var
# - test variances in earnings across rounds





# Do big correlation matrix of major individual difference terms? 
# plot(cbind(clean_data_survey[,c('stais','stait','SNS','PSS')],clean_data_complexspan['compositeSpanScore']));
# 
# library(corrplot)
# cor_matrix = cor(cbind(clean_data_survey[,c('NCS','IUS','SNS','PSS')],clean_data_complexspan['compositeSpanScore']),
#                  use = 'complete.obs');
# corrplot(cor_matrix, type = 'lower')


## 2. BLOCK-LEVEL ----
# What happened in the different blocks?


# Previous success or failure effects on next round earnings
library(dplyr)
library(tidyr)

round_data <- clean_data_subjlevel_wide %>%
  select(subjectnumber,
         round1bonusreceived01, round2bonusreceived01,
         round3bonusreceived01, round4bonusreceived01,
         round1earnings, round2earnings,
         round3earnings, round4earnings) %>%
  pivot_longer(
    cols = starts_with("round"),
    names_to = c("round", ".value"),
    names_pattern = "(round[1-4])(.*)"
  )

round_data <- round_data %>%
  arrange(subjectnumber, round) %>%
  group_by(subjectnumber) %>%
  mutate(previous_success = lag(bonusreceived01))

round_data %>%
  group_by(previous_success) %>%
  summarize(mean_earnings = mean(earnings, na.rm = TRUE),
            sd_earnings = sd(earnings, na.rm = TRUE),
            n = n())

t.test(earnings ~ previous_success, data = round_data)

boxplot(earnings ~ previous_success, data = round_data,
        names = c("Failed previous round", "Succeeded previous round"),
        ylab = "Earnings on current round")

# Correlation between total compensation and best span overall / working memory
cor.test(clean_data_subjlevel_wide$best_span_overall,
         clean_data_subjlevel_wide$totalcompensation)

plot(clean_data_subjlevel_wide$best_span_overall,
     clean_data_subjlevel_wide$totalcompensation,
     pch = 19, col = rgb(0,0,0,0.4),
     xlab = "Working Memory: Best Span",
     ylab = "Total Compensation",
     main = "Correlation Between Best Span and Earnings")
abline(lm(totalcompensation ~ best_span_overall,
          data = clean_data_subjlevel_wide),
       lwd = 2)

# Correlation between total compensation and bonus awareness
cor.test(clean_data_subjlevel_wide$psq_bonus_aware,
         clean_data_subjlevel_wide$totalcompensation)

plot(clean_data_subjlevel_wide$psq_bonus_aware,
     clean_data_subjlevel_wide$totalcompensation,
     pch = 19, col = rgb(0,0,0,0.4),
     xlab = "Bonus Awareness",
     ylab = "Total Compensation",
     main = "Correlation Between Bonus Awareness and Earnings")
abline(lm(totalcompensation ~ psq_bonus_aware,
          data = clean_data_subjlevel_wide),
       lwd = 2)

# Correlation between total compensation and goal awareness
cor.test(clean_data_subjlevel_wide$psq_goal_aware,
         clean_data_subjlevel_wide$totalcompensation)

plot(clean_data_subjlevel_wide$psq_goal_aware,
     clean_data_subjlevel_wide$totalcompensation,
     pch = 19, col = rgb(0,0,0,0.4),
     xlab = "Goal Awareness",
     ylab = "Total Compensation",
     main = "Correlation Between Goal Awareness and Earnings")
abline(lm(totalcompensation ~ psq_goal_aware,
          data = clean_data_subjlevel_wide),
       lwd = 2)

#Risky Choices vs. Goal and Bonus Levels
library(dplyr)

risk_by_condition <- clean_data_dm %>%
  filter(ischecktrial == 0) %>%  
  group_by(subjectnumber, curr_goal, curr_bonus) %>%
  summarize(
    prop_risky = mean(choice, na.rm = TRUE),
    n_trials   = n(),
    .groups = "drop"
  )

risk_summary <- risk_by_condition %>%
  group_by(curr_goal, curr_bonus) %>%
  summarize(
    mean_prop_risky = mean(prop_risky, na.rm = TRUE),
    se = sd(prop_risky, na.rm = TRUE) / sqrt(n()),
    .groups = "drop"
  )

with(risk_summary,
     interaction.plot(
       x.factor = curr_goal,
       trace.factor = curr_bonus,
       response = mean_prop_risky,
       ylab = "Proportion Risky Choices",
       xlab = "Goal Level",
       trace.label = "Bonus Level",
       col = 1:4,
       lwd = 2
     ))




## 3. TRIAL-LEVEL ----
# What happened across trials? 
# Why/how did trial events shape block events? 

