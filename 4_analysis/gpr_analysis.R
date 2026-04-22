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
# setwd('/Users/sokolhessner/Documents/gitrepos/gpr/');
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

library(lme4)
library(lmerTest)
library(corrplot)

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

length(best_span_overall) # checking that it's 66 long! 

clean_data_dm$best_span_overall = NA 
clean_data_subjlevel_wide$best_span_overall = NA
clean_data_subjlevel_long$best_span_overall = NA

for (s in 1:length(keep_participants)) {
  subj_id = keep_participants[s]
  wmc_val = best_span_overall[s]
  
  clean_data_dm$best_span_overall[clean_data_dm$subjectnumber == subj_id] = wmc_val
  clean_data_subjlevel_wide$best_span_overall[clean_data_subjlevel_wide$subjectnumber == subj_id] = wmc_val
  clean_data_subjlevel_long$best_span_overall[clean_data_subjlevel_long$subjectnumber == subj_id] = wmc_val
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

### Other Indiv Diffs ----
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

#### BIS-BAS ----

#Correlation for the bas items
bas_cor_items = c('bas_drive',
                  'bas_fun',
                  'bas_reward',
                  'bas_overall',
                  'bis_overall',
                  'bisbas_ratio')

bas_cor_matrix = cor(clean_data_subjlevel_wide[,bas_cor_items])
bas_cor_p = cor.mtest(clean_data_subjlevel_wide[,bas_cor_items], conf.level = 0.95)$p

print(round(bas_cor_matrix, 2))


corrplot(bas_cor_matrix, type = 'lower', col = rev(COL2('RdBu')),
         p.mat = bas_cor_p, sig.level = 0.05, insig='blank',
         addCoef.col ='black', number.cex = 1, diag=FALSE)

plot(clean_data_subjlevel_wide[,bas_cor_items])

# TAKEAWAY: BAS and BIS appear to be largely independent axes. Could be used 
# simultaneously to capture inhibition and activation tendencies, but the RATIO
# (which uses both BAS and BIS overall scores) is well correlated with both and
# can be used as a single metric for ease of analysis. 
#
# TLDR: USE RATIO, and then unpack to BAS or BIS overall if interesting findings or
# motivated by hypothesis. 

#### RRS ----
#Correlation for rrs items
rrs_cor_items = c('rrs_brood',
                  'rrs_reflection',
                  'rrs_overall')

rrs_cor_matrix = cor(clean_data_subjlevel_wide[,rrs_cor_items])
rrs_cor_p = cor.mtest(clean_data_subjlevel_wide[,rrs_cor_items], conf.level = 0.95)$p

print(round(rrs_cor_matrix, 2))


corrplot(rrs_cor_matrix, type = 'lower', col = rev(COL2('RdBu')),
         p.mat = rrs_cor_p, sig.level = 0.05, insig='blank',
         addCoef.col ='black', number.cex = 1, diag=FALSE)

plot(clean_data_subjlevel_wide[,rrs_cor_items])

# TAKEAWAY: Use rrs_overall, as its HIGHLY correlated with subscales.
# Subscales themselves likely not useful. 

#### PSQ Bonus Influence ----
#Correlation for psq_bonus_influence items
bonusinf_cor_items = c('psq_bonus_influence',
                       'psq_bonus_influence_effort',
                       'psq_bonus_influence_speed',
                       'psq_bonus_influence_distract',
                       'psq_bonus_influence_anxiety',
                       'psq_bonus_influence_engage')

bonusinf_cor_matrix = cor(clean_data_subjlevel_wide[,bonusinf_cor_items])
bonusinf_cor_p = cor.mtest(clean_data_subjlevel_wide[,bonusinf_cor_items], conf.level = 0.95)$p

print(round(bonusinf_cor_matrix, 2))


corrplot(bonusinf_cor_matrix, type = 'lower', col = rev(COL2('RdBu')),
         p.mat = bonusinf_cor_p, sig.level = 0.05, insig='blank',
         addCoef.col ='black', number.cex = 1, diag=FALSE)

plot(clean_data_subjlevel_wide[,bonusinf_cor_items])

# TAKEAWAY: The bonus value has a similar influence across people on effort, speed, 
# anxiety, and engagement (so they're all highly correlated), but less consistently
# influences distraction. 
#
# The people who are distracted (high ratings on bonus distraction) have high effort,
# speed, anxiety, and engagement, but the people with low distraction can have
# high or low levels of those 4 things. THUS, lower correlation. Could this be
# a phenotype thing (i.e. about who the high-distraction people are vs. who
# the low-distraction people are). 
#
# TLDR: Could use OVERALL to represent all of speed/engage/anx/effort.
# Distraction might be different (~1/3 is distracted, 1/3 is not).

#### PSQ Goal Influence ----
#Correlation for psq_goal_influence items
goalinf_cor_items = c('psq_goal_influence',
                      'psq_goal_influence_effort',
                      'psq_goal_influence_speed',
                      'psq_goal_influence_distract',
                      'psq_goal_influence_anxiety',
                      'psq_goal_influence_engage')

goalinf_cor_matrix = cor(clean_data_subjlevel_wide[,goalinf_cor_items])
goalinf_cor_p = cor.mtest(clean_data_subjlevel_wide[,goalinf_cor_items], conf.level = 0.95)$p

print(round(goalinf_cor_matrix, 2))


corrplot(goalinf_cor_matrix, type = 'lower', col = rev(COL2('RdBu')),
         p.mat = goalinf_cor_p, sig.level = 0.05, insig='blank',
         addCoef.col ='black', number.cex = 1, diag=FALSE)

plot(clean_data_subjlevel_wide[,goalinf_cor_items])

# Takeaway: relationships between ratings are +ve but much weaker - changes in one don't
# necessarily mean changes in the others. Again, distraction is slightly different 
# from the others (weakest relationships, except w/ anxiety). 
#
# TLDR: Effect of goals on ratings of effort/speed/distraction/anxiety/engagement
# are more heterogeneous (compared to the effect of the bonus). If we see high
# variation in some kind of goal effect behaviorally, could turn to these measures.


#### Anxiety/Stress ----
#Correlation for goal and bonus anxiety with stais/t
anxiety_cor_items = c('stais',
                      'stait',
                      'psq_goal_influence_anxiety',
                      'psq_bonus_influence_anxiety',
                      'psq_stress')

anxiety_cor_matrix = cor(clean_data_subjlevel_wide[,anxiety_cor_items])
anxiety_cor_p = cor.mtest(clean_data_subjlevel_wide[,anxiety_cor_items], conf.level = 0.95)$p

print(round(anxiety_cor_matrix, 2))


corrplot(anxiety_cor_matrix, type = 'lower', col = rev(COL2('RdBu')),
         p.mat = anxiety_cor_p, sig.level = 0.05, insig='blank',
         addCoef.col ='black', number.cex = 1, diag=FALSE)

plot(clean_data_subjlevel_wide[,anxiety_cor_items])
# stress has stronger relationships to pressure than anxiety does! 

# TAKEAWAY: all positive relationships (except goal influence on anxiety w/ stait),
# suggesting that the experience of anxiety in this task is linked to state & 
# trait estimates of anxiety (so it manifests in the task to some degree). 
#
# TLDR: anxiety metrics may be interrelated (and people who experience goal 
# pressure are also likely to experience bonus pressure, and these might be
# related to anxiety [state or trait]). STRESS measure is strongly related to
# task-specific anxiety, and correlated with State Anx, so use that? 


#### Motivation, Aware, Infl ----
#Correlation for psq motivation and goal/bonus awareness and impact
motiv_cor_items = c('psq_motivate',
                    'psq_goal_aware',
                    'psq_goal_influence', 
                    'psq_bonus_aware',
                    'psq_bonus_influence')

motiv_cor_matrix = cor(clean_data_subjlevel_wide[,motiv_cor_items])
motiv_cor_p = cor.mtest(clean_data_subjlevel_wide[,motiv_cor_items], conf.level = 0.95)$p

print(round(motiv_cor_matrix, 2))


corrplot(motiv_cor_matrix, type = 'lower', col = rev(COL2('RdBu')),
         p.mat = motiv_cor_p, sig.level = 0.05, insig='blank',
         addCoef.col ='black', number.cex = 1, diag=FALSE)

plot(clean_data_subjlevel_wide[,motiv_cor_items])

# TAKEAWAY: Goal awareness/influence are highly related (as are bonus awareness/
# influence), but beyond that, relationships are weak (if present at all).


### Main Indiv Diffs ----
overall_cor_items = c('bisbas_ratio', # positive = mostly BIS, negative = mostly BAS
                      'rrs_overall',
                      'psq_stress',
                      'psq_bonus_influence',
                      'best_span_overall',
                      'totalcompensation')

overall_cor_matrix = cor(clean_data_subjlevel_wide[,overall_cor_items])
overall_cor_p = cor.mtest(clean_data_subjlevel_wide[,overall_cor_items], conf.level = 0.95)$p

print(round(overall_cor_matrix, 2))


corrplot(overall_cor_matrix, type = 'lower', col = rev(COL2('RdBu')),
         p.mat = overall_cor_p, sig.level = 0.05, insig='blank',
         addCoef.col ='black', number.cex = 1, diag=FALSE)

# BISBAS Ratio is negatively correlated with RRS; people mostly driven by BAS
# are high in rumination. People high on rumination are low on BIS and high on BAS.

plot(clean_data_subjlevel_wide[,overall_cor_items])

# TAKEAWAY: Very few relationships! Largely independent factors. The only related 
# things are 3: RRS & stress (+ve), bonus influence & stress (+ve), and 
# bisbas ratio & RRS (-ve and strong)
#
# NOTE: NO goal ratings in this corr matrix due to heterogeneity. 
#
# TLDR: We have a bunch of mostly independent factors to use in analysis. Be 
# wary of RRS vs. BISBAS Ratio. 

hist(clean_data_subjlevel_wide$bisbas_ratio,
     col = "red",
     breaks = (seq(from = -0.65, to = 0.1, by = 0.1)),
     xlab = "BIS/BAS Ratio",
     ylab = "Frequency",
     main = "BIS/BAS Ratio",
     ylim = c(0, 25))

hist(clean_data_subjlevel_wide$rrs_overall,
     col = 'blue',
     breaks = (seq(from = 7.5, to = 40, by = 5)),
     xlab = "RRS Score",
     ylab = "Frequency",
     main = "RRS Score",
     xlim = c(6, 40),
     ylim = c(0, 25))

hist(clean_data_subjlevel_wide$psq_stress,
     col = 'black',
     breaks = (seq(from = 0.5, to = 7.5, by = 1)),
     border = "white",
     xlab = "Stress Level",
     ylab = "Frequency",
     main = "Stress Score",
     xlim = c(0.5, 7.5),
     ylim = c(0, 20))

hist(clean_data_subjlevel_wide$psq_bonus_influence,
     col = 'green',
     breaks = (seq(from = 0.5, to = 7.5, by = 1)),
     xlab = "Bonus Influence",
     ylab = "Frequency",
     main = "Bonus Influence",
     xlim = c(0.5, 7.5),
     ylim = c(0, 15))
#The far right boundary cuts off the last histogram bar, couldn't figure out how to change that.

hist(clean_data_subjlevel_wide$best_span_overall,
     col = 'purple',
     breaks = seq(4.5, 11.5, by = 1),
     xlab = "Best Span Overall",
     ylab = "Frequency",
     main = "Best Span Overall",
     xlim = c(4, 12),
     ylim = c(0, 25),
     xaxt = 'n'); axis(1, at = 4:12)


hist(clean_data_subjlevel_wide$totalcompensation,
     col = 'pink',
     breaks = (seq(from = 1450, to = 2250, by = 100)),
     xlab = "Dollars",
     ylab = "Frequency",
     main = "Total Compensation",
     xlim = c(1400, 2200),
     ylim = c(0, 20),
     xaxt = 'n'); axis(1, at = seq(1400, 2200, by = 100))


summary(clean_data_subjlevel_wide$psq_overall_difficult)

hist(clean_data_subjlevel_wide$psq_overall_difficult,
     breaks = (seq(from = 0.5, to = 7.5, by = 1))) # use this to create more effective histogram graphs.
# Mean difficulty was 3.5 from 1-7, indicating moderate
# difficulty in making choices in the task. 


#Summary 1/19/26:
# - RRS items pretty similar, can  just be looked at for its overall score and not sub scores
# - BAS items have a bit of a weaker positive correlation, but still very similar relationships. use
#   BISBAS Overall! 
# - Bonus, just use overall influence (b/c consistent across others)
# - Goal, unclear what to use. Lots of variability/inconsistency. 

# MAIN INDIVIDUAL DIFFERENCE MEASURES:
# - RRS (overall)
# - BISBAS Ratio (can break down if need be)
# - Bonus (psq_bonus_influence)
# - WMC (best_span_overall)
# - Stress (psq_stress) (can break down into state, trait, and stress)




#Description of Age Data for Methods
# summary(clean_data_subjlevel_wide[, c("age", "stait")])
summary(clean_data_subjlevel_wide$age)

mean(clean_data_subjlevel_wide$age, na.rm = TRUE)
sd(clean_data_subjlevel_wide$age, na.rm = TRUE)
median(clean_data_subjlevel_wide$age, na.rm = TRUE)

#Description of Race, Ethnicity, and Gender Data for Methods
#prop.table(table(clean_data_subjlevel_wide$race, clean_data_subjlevel_wide$ethnicity, clean_data_subjlevel_wide$gender)) * 100

#table(clean_data_subjlevel_wide$race, clean_data_subjlevel_wide$ethnicity, clean_data_subjlevel_wide$gender)





## 2. BLOCK-LEVEL ----

# What happened in the different blocks?
clean_data_subjlevel_long$bonusatstakeP1N1 = as.numeric(clean_data_subjlevel_long$bonusatstake == 100) - 
  as.numeric(clean_data_subjlevel_long$bonusatstake == 25)

clean_data_subjlevel_long$goallevelP1N1 = as.numeric(clean_data_subjlevel_long$goallevel == 420.79) - 
  as.numeric(clean_data_subjlevel_long$goallevel == 349.85)

clean_data_subjlevel_long$roundnum0123 = clean_data_subjlevel_long$roundnum - 1


# Earnings By BLock
plot(clean_data_subjlevel_long$earnings, col = clean_data_subjlevel_long$subjectnumber, pch = 16)
hist(clean_data_subjlevel_long$earnings, main = "Blockwise Earnings", xlab = "Dollars")
# variability across people & blocks, all in a similar range of 300-500

model_earnings = lmer(earnings ~ 1 + roundnum0123 * bonusatstakeP1N1 * goallevelP1N1 + (1 | subjectnumber), 
                      data = clean_data_subjlevel_long)
summary(model_earnings)
# Fixed effects:
#                                             Estimate Std. Error       df t value Pr(>|t|)    
# (Intercept)                                 405.7835     4.7788 204.2097  84.914   <2e-16 ***
# roundnum0123                                  1.7617     2.3183 192.0883   0.760   0.4482    
# bonusatstakeP1N1                              3.2498     4.5339 245.7442   0.717   0.4742    
# goallevelP1N1                                 7.7815     4.5399 246.8870   1.714   0.0878 .  
# roundnum0123:bonusatstakeP1N1                -2.1214     2.4802 255.8557  -0.855   0.3932    
# roundnum0123:goallevelP1N1                   -5.4210     2.4851 255.9893  -2.181   0.0301 *  
# bonusatstakeP1N1:goallevelP1N1                1.3067     4.5211 243.1604   0.289   0.7728    
# roundnum0123:bonusatstakeP1N1:goallevelP1N1  -0.5389     2.4699 255.0835  -0.218   0.8275    

# Might be some complex things going on with GOAL LEVELS and BLOCK NUMBERS (TIME).
# Looks like effect of goal is initially positive, but then *flips* by final block.
# Backfiring?? 

# Effect of goal level on earnings as a function of block number:
# 	            1	    2	      3	      4
# low (-1)	-6.0198	1.1629	8.3456	15.5283
# high (+1)	 9.5432	5.8839	2.2246	-1.4347


# PROBLEM: Earnings are variable b/c of high role of chance
# SOLUTION: Use expected earnings (i.e. EV of choice) instead!

# Calculate Expected Earnings

for (sn in 1:number_of_clean_subjects){
  
  tmp_subj_id = keep_participants[sn];
  tmp_dm_data = clean_data_dm[clean_data_dm$subjectnumber == tmp_subj_id,]
  
  for (bn in 1:4){
    
    tmp_blk_data = tmp_dm_data[tmp_dm_data$roundnumber == bn,]
    
    tmp_exp_earnings = sum(tmp_blk_data$safe[tmp_blk_data$choice == 0], na.rm = T) + 
      sum((tmp_blk_data$riskyopt1*.5 + tmp_blk_data$riskyopt2*.5)*tmp_blk_data$choice, na.rm = T)
    
    clean_data_subjlevel_long$expected_earnings[(clean_data_subjlevel_long$subjectnumber == tmp_subj_id) & 
                                                  (clean_data_subjlevel_long$roundnum == bn)] = tmp_exp_earnings
  }
}

# Model it
# REGRESSION GOES HERE, JUSTIN!

expected_earnings = lmer(expected_earnings ~ 1 + roundnum0123 * bonusatstakeP1N1 * goallevelP1N1 + (1 | subjectnumber), 
                      data = clean_data_subjlevel_long)
summary(expected_earnings)
# Fixed effects:
#                                               Estimate Std. Error       df t value Pr(>|t|)    
#   (Intercept)                                 408.6288     1.2633 101.8902 323.471  < 2e-16 ***
#   roundnum0123                                  1.4733     0.3893 190.9292   3.785 0.000206 ***
#   bonusatstakeP1N1                              1.9667     0.8166 210.2679   2.408 0.016893 *  
#   goallevelP1N1                                 0.6853     0.8199 211.0576   0.836 0.404197    
#   roundnum0123:bonusatstakeP1N1                -0.9954     0.4607 217.6368  -2.161 0.031813 *  
#   roundnum0123:goallevelP1N1                   -0.2311     0.4632 218.6150  -0.499 0.618372    
#   bonusatstakeP1N1:goallevelP1N1               -0.9706     0.8100 208.6500  -1.198 0.232137    
#   roundnum0123:bonusatstakeP1N1:goallevelP1N1   0.3052     0.4555 215.6152   0.670 0.503479 

# INTERPRETATION: 
# People may be moving toward risk neutrality on high-bonus blocks vs. low-bonus blocks. Doing so
# (from either risk averse or risk seeking baselines) would produce a higher expected earnings value
# on those blocks. 
#
# NOTE: The effect is strongest in block 1, weaker in block 2, non-existant in block 3, and might reverse 
# in block 4. 
# 
# FOR FUTURE: Verify with block-level averages. 

# STRANGE PATTERN:
# Actual earnings show effects of goals that change across blocks (but not bonuses).
# Expected earnings show effects of bonuses that change across blocks (but not goals).
#
# Resolution: Are these analyses looking at different things (or in a different way?).




model_goalattainment = glmer(bonusreceived01 ~ 1 + roundnum0123 * bonusatstakeP1N1 * goallevelP1N1 + (1 | subjectnumber), 
                      data = clean_data_subjlevel_long, family = 'binomial')
summary(model_goalattainment)

model_goalattainment_ffx = glm(bonusreceived01 ~ 1 + roundnum0123 * bonusatstakeP1N1 * goallevelP1N1, 
                               data = clean_data_subjlevel_long, family = 'binomial')
summary(model_goalattainment_ffx)

anova(model_goalattainment, model_goalattainment_ffx)
# NOTE: The RFX regression does not perform significantly better (p = 0.66) compared to the FFX 
# regression, implying that the RFX are not necessary (though note the pattern of findings
# is the same).


# Expected probabilities were:
# High goal level: 60th percentile of earnings (which means 40% surpass this)
# Low goal level: 10th percentile of earnings (which means 90% surpass this)

#Fixed effects:
#                                             Estimate Std. Error z value Pr(>|z|)    
# (Intercept)                                  0.61652    0.27166   2.269 0.023240 *  
# roundnum0123                                 0.47710    0.22220   2.147 0.031778 *  
# bonusatstakeP1N1                            -0.05945    0.26656  -0.223 0.823517    
# goallevelP1N1                               -0.95801    0.27878  -3.436 0.000589 ***
# roundnum0123:bonusatstakeP1N1                0.12564    0.22347   0.562 0.573950    
# roundnum0123:goallevelP1N1                  -0.50231    0.22330  -2.249 0.024483 *  
# bonusatstakeP1N1:goallevelP1N1              -0.17667    0.26646  -0.663 0.507312    
# roundnum0123:bonusatstakeP1N1:goallevelP1N1 -0.01171    0.22341  -0.052 0.958204    

# Two effects: 
# 1. People are more likely to achieve goals with increasing time in the task
# 2. High goals are harder to reach
# 3. With increasing time, people reach more low goals and fewer high goals
#
# Inspecting the implied betas shows that there is NO CHANGE in high goal level
# attainment, but that low level goals are attained much more frequently with 
# time in the task. 

# LINEAR MODELED PREDICTED PROBABILITIES
# 	                1	        2	          3	          4
# high goal	0.415447584	0.409338658	0.403257592	0.397206114     (EXPECTED ACHIEVEMENT = 40%)
# low goal	0.828428437	0.927837762	0.971621927	0.989150849     (EXPECTED ACHIEVEMENT = 90%)

# Low Level Goal Attainment
# Overall
mean(clean_data_subjlevel_long$bonusreceived01[clean_data_subjlevel_long$goallevel < 400])

# Rounds... 
mean(clean_data_subjlevel_long$bonusreceived01[(clean_data_subjlevel_long$goallevel < 400) & 
                                                 (clean_data_subjlevel_long$roundnum == 1)])
mean(clean_data_subjlevel_long$bonusreceived01[(clean_data_subjlevel_long$goallevel < 400) & 
                                                 (clean_data_subjlevel_long$roundnum == 2)])
mean(clean_data_subjlevel_long$bonusreceived01[(clean_data_subjlevel_long$goallevel < 400) & 
                                                 (clean_data_subjlevel_long$roundnum == 3)])
mean(clean_data_subjlevel_long$bonusreceived01[(clean_data_subjlevel_long$goallevel < 400) & 
                                                 (clean_data_subjlevel_long$roundnum == 4)])
# Data-derived probabilities for LOW:
# .848, .875, .971, 1.0 (!!)

# Rounds... 
mean(clean_data_subjlevel_long$bonusreceived01[(clean_data_subjlevel_long$goallevel > 400) & 
                                                 (clean_data_subjlevel_long$roundnum == 1)])
mean(clean_data_subjlevel_long$bonusreceived01[(clean_data_subjlevel_long$goallevel > 400) & 
                                                 (clean_data_subjlevel_long$roundnum == 2)])
mean(clean_data_subjlevel_long$bonusreceived01[(clean_data_subjlevel_long$goallevel > 400) & 
                                                 (clean_data_subjlevel_long$roundnum == 3)])
mean(clean_data_subjlevel_long$bonusreceived01[(clean_data_subjlevel_long$goallevel > 400) & 
                                                 (clean_data_subjlevel_long$roundnum == 4)])
# Data-derived probabilities for HIGH:
# .45, .41, .29, .47


# Easy goals are met more often with time; hard goals are not affected. Bonuses
# have no effect on goal attainment.

# Plot Earnings as a function of trial

# Approach:
# FIRST, plot the average earnings for high goals
# aggregate(clean_data_dm$round_earnings[clean_data_dm$curr_goal > 400], by = list(clean_data_dm$trialnumber_block[clean_data_dm$curr_goal > 400]), mean)
# Two SETS of nested loops.
# Loop 1: subjects, person by person
# Loop 2 (inside loop 1): round
# - If high goal, then plot earnings for this person & round on the plot
#   use the command lines() and just make it black to start
# OUTSIDE of loop...
# add horizontal line using abline() at the high goal level
# Add that group average again
#
# THEN, do it all over again for low goal

# Average Earnings High Goals

avgearnings_highgoal = aggregate(clean_data_dm$round_earnings[clean_data_dm$curr_goal > 400], by = list(clean_data_dm$trialnumber_block[clean_data_dm$curr_goal > 400]), mean)

colnames(avgearnings_highgoal) = c("trial", "mean_earnings")

plot(avgearnings_highgoal$trial,
     avgearnings_highgoal$mean_earnings,
     type = "l",
     lwd = 3,
     ylim = c(0,520),
     xlab = "Trial Number",
     ylab = "Average Earnings",
     main = "Average Earnings (High Goal)")

for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]
  
  rounds = unique(tmpdata$roundnumber)
  
  for (b in rounds){
    
    round_data = tmpdata[tmpdata$roundnumber == b, ]
  
    if (mean(round_data$curr_goal, na.rm = TRUE) > 400) {
      
      round_data = round_data[order(round_data$trialnumber_block), ]
      
      lines(round_data$trialnumber_block,
            round_data$round_earnings,
            col = rgb(0,0,0,.2))
    }
  }
}

abline(h = 420.79, lty = 2, col = 'darkorchid4', lwd = 3)

# Average Earnings Low Goals

avgearnings_lowgoal = aggregate(clean_data_dm$round_earnings[clean_data_dm$curr_goal < 400], by = list(clean_data_dm$trialnumber_block[clean_data_dm$curr_goal > 400]), mean)

colnames(avgearnings_lowgoal) = c("trial", "mean_earnings")

plot(avgearnings_highgoal$trial,
     avgearnings_highgoal$mean_earnings,
     type = "l",
     lwd = 3,
     ylim = c(0,520),
     xlab = "Trial Number",
     ylab = "Average Earnings",
     main = "Average Earnings (Low Goal)")

for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]
  
  rounds = unique(tmpdata$roundnumber)
  
  for (b in rounds){
    
    round_data = tmpdata[tmpdata$roundnumber == b, ]
    
    if (mean(round_data$curr_goal, na.rm = TRUE) < 400) {
      
      round_data = round_data[order(round_data$trialnumber_block), ]
      
      lines(round_data$trialnumber_block,
            round_data$round_earnings,
            col = rgb(0,0,0,.2))
    }
  }
}

abline(h = 349.85, lty = 2, col = 'darkorchid2', lwd = 3)


# TODO:
# 1. Calculate model-free, data-derived mean earnings
# 3. Look at trials-to-goal (when attained)
# 4. somehow..... variance.... ? 




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

# RRS summary data
summary(clean_data_subjlevel_wide$rrs_overall)
mean(clean_data_subjlevel_wide$rrs_overall, na.rm = TRUE)
sd(clean_data_subjlevel_wide$rrs_overall, na.rm = TRUE)

# BIS/BAS ratio summary data
summary(clean_data_subjlevel_wide$bisbas_ratio)
mean(clean_data_subjlevel_wide$bisbas_ratio, na.rm = TRUE)
sd(clean_data_subjlevel_wide$bisbas_ratio, na.rm = TRUE)

# Working memory (best span) summary data
summary(clean_data_subjlevel_wide$best_span_overall)
mean(clean_data_subjlevel_wide$best_span_overall, na.rm = TRUE)
sd(clean_data_subjlevel_wide$best_span_overall, na.rm = TRUE)

# PSQ Overall Difficulty summary data
summary(clean_data_subjlevel_wide$psq_overall_difficult)
mean(clean_data_subjlevel_wide$psq_overall_difficult, na.rm = TRUE)
sd(clean_data_subjlevel_wide$psq_overall_difficult, na.rm = TRUE)

# STAIS summary data
summary(clean_data_subjlevel_wide$stais)
mean(clean_data_subjlevel_wide$stais, na.rm = TRUE)
sd(clean_data_subjlevel_wide$stais, na.rm = TRUE)

# STAIT summary data
summary(clean_data_subjlevel_wide$stait)
mean(clean_data_subjlevel_wide$stait, na.rm = TRUE)
sd(clean_data_subjlevel_wide$stait, na.rm = TRUE)

# Motivate summary data
summary(clean_data_subjlevel_wide$psq_motivate)
mean(clean_data_subjlevel_wide$psq_motivate, na.rm = TRUE)
sd(clean_data_subjlevel_wide$psq_motivate, na.rm = TRUE)

# Goal influence summary data
summary(clean_data_subjlevel_wide$psq_goal_influence)
mean(clean_data_subjlevel_wide$psq_goal_influence, na.rm = TRUE)
sd(clean_data_subjlevel_wide$psq_goal_influence, na.rm = TRUE)

# Bonus influence summary data
summary(clean_data_subjlevel_wide$psq_bonus_influence)
mean(clean_data_subjlevel_wide$psq_bonus_influence, na.rm = TRUE)
sd(clean_data_subjlevel_wide$psq_bonus_influence, na.rm = TRUE)

# Total compensation summary data
summary(clean_data_subjlevel_wide$totalcompensation)
mean(clean_data_subjlevel_wide$totalcompensation, na.rm = TRUE)
sd(clean_data_subjlevel_wide$totalcompensation, na.rm = TRUE)

# ANOVA for block number effect on earnings
anova_model <- aov(earnings ~ roundnum0123 + Error(subjectnumber/roundnum0123),
                   data = clean_data_subjlevel_long)

summary(anova_model)

# Power analysis
# install.packages("pwr")
library(pwr)

pwr.t.test(n = 66,
           power = 0.80,
           sig.level = 0.05,
           type = "paired")


#Total Compensation Scaled
clean_data_subjlevel_wide$total_comp_scaled = clean_data_subjlevel_wide$totalcompensation * 0.009
summary(clean_data_subjlevel_wide$total_comp_scaled)
sd(clean_data_subjlevel_wide$total_comp_scaled, na.rm = TRUE)



## 3. TRIAL-LEVEL ----
# What happened across trials? 
# Why/how did trial events shape block events? 

# Create a Post-Goal variable (1 where their earnings are at or above the goal, 0 elsewhere)
clean_data_dm$postgoal = as.numeric(clean_data_dm$round_earnings >= clean_data_dm$curr_goal)
# NOTE: THIS INCLUDES THE TRIAL ON WHICH THEY REACHED THE GOAL

clean_data_dm$postpostgoal = c(0, clean_data_dm$postgoal[1:(length(clean_data_dm$postgoal)-1)])
clean_data_dm$postpostgoal[clean_data_dm$trialnumber_block == 1] = 0
# NOTE: THIS ONLY INCLUDES TRIALS AFTER THAT ON WHICH THEY MET THE GOAL

### Sub-block analysis (prisky + rt + scl) ----
#### calculation ----
clean_data_subjlevel_long$prisky_overall = NA;
clean_data_subjlevel_long$decisiontime_overall = NA;
nsubblocks = 5 # ENSURE THAT THIS NUMBER DIVIDES EVENLY INTO 50
nsub_divfactor = 50/nsubblocks;
subblocks_colnames = c('subjectnumber',
                       'roundnum',
                       'subblocknum',
                       'prisky',
                       'rt',
                       'scl',
                       'bonusatstakeP1N1',
                       'goallevelP1N1')
subblocks_long = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*4*nsubblocks, length(subblocks_colnames)))); # no. of subj x no. of blocks x subblock
colnames(subblocks_long) = subblocks_colnames

subblocks_long$subjectnumber = rep(keep_participants, each = 4 * nsubblocks)
subblocks_long$roundnum = rep(1:4, each = nsubblocks)
subblocks_long$subblocknum = rep(1:5, number_of_clean_subjects*4)

for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]

  for (b in 1:4) {
    clean_data_subjlevel_long$prisky_overall[(clean_data_subjlevel_long$subjectnumber == subj_id) & 
                                               (clean_data_subjlevel_long$roundnum == b)] = mean(tmpdata$choice[tmpdata$roundnumber == b], na.rm = T)
    clean_data_subjlevel_long$decisiontime_overall[(clean_data_subjlevel_long$subjectnumber == subj_id) & 
                                               (clean_data_subjlevel_long$roundnum == b)] = mean(tmpdata$reactiontime[tmpdata$roundnumber == b], na.rm = T)
    subblocks_long$bonusatstakeP1N1[(subblocks_long$subjectnumber == subj_id) & 
                                    (subblocks_long$roundnum == b)] = clean_data_subjlevel_long$bonusatstakeP1N1[(clean_data_subjlevel_long$subjectnumber == subj_id) & 
                                                                                                                 (clean_data_subjlevel_long$roundnum == b)]
    subblocks_long$goallevelP1N1[(subblocks_long$subjectnumber == subj_id) & 
                                 (subblocks_long$roundnum == b)] = clean_data_subjlevel_long$goallevelP1N1[(clean_data_subjlevel_long$subjectnumber == subj_id) & 
                                                                                                           (clean_data_subjlevel_long$roundnum == b)]
    for (sb in 1:nsubblocks){
      tmp_ind = (subblocks_long$subjectnumber == subj_id) & 
                (subblocks_long$roundnum == b) & 
                (subblocks_long$subblocknum == sb)
      subblocks_long$prisky[tmp_ind] = mean(tmpdata$choice[(tmpdata$roundnumber == b) & 
                                                            tmpdata$trialnumber_block == ((sb-1)*nsub_divfactor+1):(sb*nsub_divfactor)], na.rm = T)
      subblocks_long$rt[tmp_ind] = mean(tmpdata$reactiontime[(tmpdata$roundnumber == b) & 
                                                             tmpdata$trialnumber_block == ((sb-1)*nsub_divfactor+1):(sb*nsub_divfactor)], na.rm = T)
      subblocks_long$scl[tmp_ind] = mean(tmpdata$tmeanscl[(tmpdata$roundnumber == b) & 
                                                               tmpdata$trialnumber_block == ((sb-1)*nsub_divfactor+1):(sb*nsub_divfactor)], na.rm = T)
    }
  }
}

subblocks_long$sqrtrt = sqrt(subblocks_long$rt)

# for overall sub-block p(risky)
mean_prisky_subblock = array(data = NA, dim = c(nsubblocks,1))
sem_prisky_subblock = array(data = NA, dim = c(nsubblocks,1))

# subblock prisky by round number
mean_prisky_round_x_subblock = array(data = NA, dim = c(nsubblocks,4))
sem_prisky_round_x_subblock = array(data = NA, dim = c(nsubblocks,4))

# subblock prisky by GOAL LEVEL
mean_prisky_goal_x_subblock = array(data = NA, dim = c(nsubblocks,2))
sem_prisky_goal_x_subblock = array(data = NA, dim = c(nsubblocks,2))

# subblock prisky by BONUS
mean_prisky_bonus_x_subblock = array(data = NA, dim = c(nsubblocks,2))
sem_prisky_bonus_x_subblock = array(data = NA, dim = c(nsubblocks,2))


# For Decision Times
# for overall sub-block rt
mean_rt_subblock = array(data = NA, dim = c(nsubblocks,1))
sem_rt_subblock = array(data = NA, dim = c(nsubblocks,1))

# subblock rt by round number
mean_rt_round_x_subblock = array(data = NA, dim = c(nsubblocks,4))
sem_rt_round_x_subblock = array(data = NA, dim = c(nsubblocks,4))

# subblock rt by GOAL LEVEL
mean_rt_goal_x_subblock = array(data = NA, dim = c(nsubblocks,2))
sem_rt_goal_x_subblock = array(data = NA, dim = c(nsubblocks,2))

# subblock rt by BONUS
mean_rt_bonus_x_subblock = array(data = NA, dim = c(nsubblocks,2))
sem_rt_bonus_x_subblock = array(data = NA, dim = c(nsubblocks,2))


# For SCL
# for overall sub-block rt
mean_scl_subblock = array(data = NA, dim = c(nsubblocks,1))
sem_scl_subblock = array(data = NA, dim = c(nsubblocks,1))

# subblock rt by round number
mean_scl_round_x_subblock = array(data = NA, dim = c(nsubblocks,4))
sem_scl_round_x_subblock = array(data = NA, dim = c(nsubblocks,4))

# subblock rt by GOAL LEVEL
mean_scl_goal_x_subblock = array(data = NA, dim = c(nsubblocks,2))
sem_scl_goal_x_subblock = array(data = NA, dim = c(nsubblocks,2))

# subblock rt by BONUS
mean_scl_bonus_x_subblock = array(data = NA, dim = c(nsubblocks,2))
sem_scl_bonus_x_subblock = array(data = NA, dim = c(nsubblocks,2))


for (sb in 1:nsubblocks){
  # P(Risky) 
  # Overall
  mean_prisky_subblock[sb] = mean(subblocks_long$prisky[subblocks_long$subblocknum == sb])
  sem_prisky_subblock[sb] = sd(subblocks_long$prisky[subblocks_long$subblocknum == sb])/sqrt(number_of_clean_subjects)
  
  # High goal
  mean_prisky_goal_x_subblock[sb,1] = mean(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == 1)])
  sem_prisky_goal_x_subblock[sb,1] = sd(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == 1)])/sqrt(number_of_clean_subjects)
  # Low goal
  mean_prisky_goal_x_subblock[sb,2] = mean(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == -1)])
  sem_prisky_goal_x_subblock[sb,2] = sd(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == -1)])/sqrt(number_of_clean_subjects)
  
  # High Bonus
  mean_prisky_bonus_x_subblock[sb,1] = mean(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == 1)])
  sem_prisky_bonus_x_subblock[sb,1] = sd(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == 1)])/sqrt(number_of_clean_subjects)
  # Low Bonus
  mean_prisky_bonus_x_subblock[sb,2] = mean(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == -1)])
  sem_prisky_bonus_x_subblock[sb,2] = sd(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == -1)])/sqrt(number_of_clean_subjects)
  
  # Summary Data for prisky
  mean_prisky_subblock
  sem_prisky_subblock
  
  # Summary prisky by GOAL (1 is HIGH and 2 is LOW)
  mean_prisky_goal_x_subblock
  sem_prisky_goal_x_subblock
  
  #Summary prisky by BONUS (1 is HIGH and 2 is LOW)
  mean_prisky_bonus_x_subblock
  sem_prisky_bonus_x_subblock
  
  
  # Decision Time
  # Overall
  mean_rt_subblock[sb] = mean(subblocks_long$sqrtrt[subblocks_long$subblocknum == sb])
  sem_rt_subblock[sb] = sd(subblocks_long$sqrtrt[subblocks_long$subblocknum == sb])/sqrt(number_of_clean_subjects)
  
  # High goal
  mean_rt_goal_x_subblock[sb,1] = mean(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == 1)])
  sem_rt_goal_x_subblock[sb,1] = sd(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == 1)])/sqrt(number_of_clean_subjects)
  # Low goal
  mean_rt_goal_x_subblock[sb,2] = mean(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == -1)])
  sem_rt_goal_x_subblock[sb,2] = sd(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == -1)])/sqrt(number_of_clean_subjects)
  
  # High Bonus
  mean_rt_bonus_x_subblock[sb,1] = mean(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == 1)])
  sem_rt_bonus_x_subblock[sb,1] = sd(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == 1)])/sqrt(number_of_clean_subjects)
  # Low Bonus
  mean_rt_bonus_x_subblock[sb,2] = mean(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == -1)])
  sem_rt_bonus_x_subblock[sb,2] = sd(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == -1)])/sqrt(number_of_clean_subjects)
  
  # Summary Data for rt
  mean_rt_subblock
  sem_rt_subblock
  
  # Summary rt by GOAL (1 is HIGH and 2 is LOW)
  mean_rt_goal_x_subblock
  sem_rt_goal_x_subblock
  
  #Summary rt by BONUS (1 is HIGH and 2 is LOW)
  mean_rt_bonus_x_subblock
  sem_rt_bonus_x_subblock
  
  
  # SCL
  # Overall
  mean_scl_subblock[sb] = mean(subblocks_long$scl[subblocks_long$subblocknum == sb])
  sem_scl_subblock[sb] = sd(subblocks_long$scl[subblocks_long$subblocknum == sb])/sqrt(number_of_clean_subjects)
  
  # High goal
  mean_scl_goal_x_subblock[sb,1] = mean(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == 1)])
  sem_scl_goal_x_subblock[sb,1] = sd(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == 1)])/sqrt(number_of_clean_subjects)
  # Low goal
  mean_scl_goal_x_subblock[sb,2] = mean(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == -1)])
  sem_scl_goal_x_subblock[sb,2] = sd(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$goallevelP1N1 == -1)])/sqrt(number_of_clean_subjects)
  
  # High Bonus
  mean_scl_bonus_x_subblock[sb,1] = mean(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == 1)])
  sem_scl_bonus_x_subblock[sb,1] = sd(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == 1)])/sqrt(number_of_clean_subjects)
  # Low Bonus
  mean_scl_bonus_x_subblock[sb,2] = mean(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == -1)])
  sem_scl_bonus_x_subblock[sb,2] = sd(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$bonusatstakeP1N1 == -1)])/sqrt(number_of_clean_subjects)
  
  # Summary Data for rt
  mean_scl_subblock
  sem_scl_subblock
  
  # Summary rt by GOAL (1 is HIGH and 2 is LOW)
  mean_scl_goal_x_subblock
  sem_scl_goal_x_subblock
  
  #Summary rt by BONUS (1 is HIGH and 2 is LOW)
  mean_scl_bonus_x_subblock
  sem_scl_bonus_x_subblock
  
  
   for (b in 1:4){
    # P(risky)
    mean_prisky_round_x_subblock[sb,b] = mean(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$roundnum == b)])
    sem_prisky_round_x_subblock[sb,b] = sd(subblocks_long$prisky[(subblocks_long$subblocknum == sb) & (subblocks_long$roundnum == b)])/sqrt(number_of_clean_subjects)
    # Decision Time
    mean_rt_round_x_subblock[sb,b] = mean(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$roundnum == b)])
    sem_rt_round_x_subblock[sb,b] = sd(subblocks_long$sqrtrt[(subblocks_long$subblocknum == sb) & (subblocks_long$roundnum == b)])/sqrt(number_of_clean_subjects)
    # SCL
    mean_scl_round_x_subblock[sb,b] = mean(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$roundnum == b)])
    sem_scl_round_x_subblock[sb,b] = sd(subblocks_long$scl[(subblocks_long$subblocknum == sb) & (subblocks_long$roundnum == b)])/sqrt(number_of_clean_subjects)
   }
}

#### plotting ----
##### P(risky) ----
plot(mean_prisky_subblock, type = 'l', ylim = c(0.45, 0.6), lwd = 4,
     xlab = 'Sub-block (10 trials)', ylab = 'mean p(risky) +/- SEM',
     main = 'Risky choices as a function of sub-block portion')
arrows(x0 = 1:5, 
       y0 = mean_prisky_subblock - sem_prisky_subblock, 
       y1 = mean_prisky_subblock + sem_prisky_subblock,
       length = 0)

blk_col_vect = c('red','orange','yellow','green')

plot(mean_prisky_round_x_subblock[,1], type = 'l', 
     ylim = c(0.45, 0.6), xlim = c(1,20), lwd = 4, col = blk_col_vect[1],
     xlab = 'block (color) x subblock', ylab = 'mean p(risky) +/- SEM', main = 'Risky choices as a function of block & sub-block portion')
arrows(x0 = 1:5, 
       y0 = mean_prisky_round_x_subblock[,1] - sem_prisky_round_x_subblock[,1], 
       y1 = mean_prisky_round_x_subblock[,1] + sem_prisky_round_x_subblock[,1],
       length = 0)

for (b in 2:4){
  lines(x = (1:5)+(b-1)*5, y = mean_prisky_round_x_subblock[,b], lwd = 4, col = blk_col_vect[b])
  arrows(x0 = (1:5)+(b-1)*5, 
         y0 = mean_prisky_round_x_subblock[,b] - sem_prisky_round_x_subblock[,b], 
         y1 = mean_prisky_round_x_subblock[,b] + sem_prisky_round_x_subblock[,b],
         length = 0)
}
legend("bottomleft",
       legend = c('Block 1','Block 2', 'Block 3', 'Block 4'),
       col = blk_col_vect,
       lty = 1, lwd = 4)


plot(x = (1:5) - 0.05, y = mean_prisky_goal_x_subblock[,1], type = 'l', 
     ylim = c(0.45, 0.6), lwd = 4, col = 'darkorchid4',
     xlab = 'subblock', ylab = 'mean p(risky) +/- SEM', main = 'Risky choices as a function of GOAL level')
arrows(x0 = (1:5) - 0.05, 
       y0 = mean_prisky_goal_x_subblock[,1] - sem_prisky_goal_x_subblock[,1], 
       y1 = mean_prisky_goal_x_subblock[,1] + sem_prisky_goal_x_subblock[,1],
       length = 0)
lines(x = (1:5) + .05, y = mean_prisky_goal_x_subblock[,2], lwd = 4, col = 'darkorchid2')
arrows(x0 = (1:5) + .05, 
       y0 = mean_prisky_goal_x_subblock[,2] - sem_prisky_goal_x_subblock[,2], 
       y1 = mean_prisky_goal_x_subblock[,2] + sem_prisky_goal_x_subblock[,2],
       length = 0)
legend("bottomleft",
       legend = c('High Goal','Low Goal'),
       col = c('darkorchid4','darkorchid2'),
       lty = 1, lwd = 4)


plot(x = (1:5) - 0.05, mean_prisky_bonus_x_subblock[,1], type = 'l', 
     ylim = c(0.45, 0.6), lwd = 4, col = 'blue4',
     xlab = 'subblock', ylab = 'mean p(risky) +/- SEM', main = 'Risky choices as a function of BONUS level')
arrows(x0 = (1:5) - 0.05, 
       y0 = mean_prisky_bonus_x_subblock[,1] - sem_prisky_bonus_x_subblock[,1], 
       y1 = mean_prisky_bonus_x_subblock[,1] + sem_prisky_bonus_x_subblock[,1],
       length = 0)
lines(x = (1:5) + .05, y = mean_prisky_bonus_x_subblock[,2], lwd = 4, col = 'blue2')
arrows(x0 = (1:5) + .05, 
       y0 = mean_prisky_bonus_x_subblock[,2] - sem_prisky_bonus_x_subblock[,2], 
       y1 = mean_prisky_bonus_x_subblock[,2] + sem_prisky_bonus_x_subblock[,2],
       length = 0)
legend("bottomleft",
       legend = c('High Bonus','Low Bonus'),
       col = c('blue4','blue2'),
       lty = 1, lwd = 4)


##### Decision Time ----
plot(mean_rt_subblock, type = 'l', ylim = c(1.05, 1.15), lwd = 4,
     xlab = 'Sub-block (10 trials)', ylab = 'mean sqrt(RT) +/- SEM',
     main = 'Decision Times as a function of sub-block portion')
arrows(x0 = 1:5, 
       y0 = mean_rt_subblock - sem_rt_subblock, 
       y1 = mean_rt_subblock + sem_rt_subblock,
       length = 0)

blk_col_vect = c('red','orange','yellow','green')

plot(mean_rt_round_x_subblock[,1], type = 'l', 
     ylim = c(1, 1.25), xlim = c(1,20), lwd = 4, col = blk_col_vect[1],
     xlab = 'block (color) x subblock', ylab = 'mean sqrt(RT) +/- SEM', main = 'Decision Times as a function of block & sub-block portion')
arrows(x0 = 1:5, 
       y0 = mean_rt_round_x_subblock[,1] - sem_rt_round_x_subblock[,1], 
       y1 = mean_rt_round_x_subblock[,1] + sem_rt_round_x_subblock[,1],
       length = 0)

for (b in 2:4){
  lines(x = (1:5)+(b-1)*5, y = mean_rt_round_x_subblock[,b], lwd = 4, col = blk_col_vect[b])
  arrows(x0 = (1:5)+(b-1)*5, 
         y0 = mean_rt_round_x_subblock[,b] - sem_rt_round_x_subblock[,b], 
         y1 = mean_rt_round_x_subblock[,b] + sem_rt_round_x_subblock[,b],
         length = 0)
}
legend("bottomleft",
       legend = c('Block 1','Block 2', 'Block 3', 'Block 4'),
       col = blk_col_vect,
       lty = 1, lwd = 4)


plot(x = (1:5) - 0.05, y = mean_rt_goal_x_subblock[,1], type = 'l', 
     ylim = c(1, 1.2), lwd = 4, col = 'darkorchid4',
     xlab = 'subblock', ylab = 'mean sqrt(RT) +/- SEM', main = 'Decision Times as a function of GOAL level')
arrows(x0 = (1:5) - 0.05, 
       y0 = mean_rt_goal_x_subblock[,1] - sem_rt_goal_x_subblock[,1], 
       y1 = mean_rt_goal_x_subblock[,1] + sem_rt_goal_x_subblock[,1],
       length = 0)
lines(x = (1:5) + .05, y = mean_rt_goal_x_subblock[,2], lwd = 4, col = 'darkorchid2')
arrows(x0 = (1:5) + .05, 
       y0 = mean_rt_goal_x_subblock[,2] - sem_rt_goal_x_subblock[,2], 
       y1 = mean_rt_goal_x_subblock[,2] + sem_rt_goal_x_subblock[,2],
       length = 0)
legend("bottomleft",
       legend = c('High Goal','Low Goal'),
       col = c('darkorchid4','darkorchid2'),
       lty = 1, lwd = 4)


plot(x = (1:5) - 0.05, y = mean_rt_bonus_x_subblock[,1], type = 'l', 
     ylim = c(1, 1.2), lwd = 4, col = 'blue4',
     xlab = 'subblock', ylab = 'mean sqrt(RT) +/- SEM', main = 'Decision Times as a function of BONUS level')
arrows(x0 = (1:5) - 0.05, 
       y0 = mean_rt_bonus_x_subblock[,1] - sem_rt_bonus_x_subblock[,1], 
       y1 = mean_rt_bonus_x_subblock[,1] + sem_rt_bonus_x_subblock[,1],
       length = 0)
lines(x = (1:5) + .05, y = mean_rt_bonus_x_subblock[,2], lwd = 4, col = 'blue2')
arrows(x0 = (1:5) + .05, 
       y0 = mean_rt_bonus_x_subblock[,2] - sem_rt_bonus_x_subblock[,2], 
       y1 = mean_rt_bonus_x_subblock[,2] + sem_rt_bonus_x_subblock[,2],
       length = 0)
legend("bottomleft",
       legend = c('High Bonus','Low Bonus'),
       col = c('blue4','blue2'),
       lty = 1, lwd = 4)



##### SCL ----
plot(mean_scl_subblock, type = 'l', ylim = c(15, 20), lwd = 4,
     xlab = 'Sub-block (10 trials)', ylab = 'mean SCL +/- SEM',
     main = 'Arousal as a function of sub-block portion')
arrows(x0 = 1:5, 
       y0 = mean_scl_subblock - sem_scl_subblock, 
       y1 = mean_scl_subblock + sem_scl_subblock,
       length = 0)

blk_col_vect = c('red','orange','yellow','green')

plot(mean_scl_round_x_subblock[,1], type = 'l', 
     ylim = c(14.5,20.5), xlim = c(1,20), lwd = 4, col = blk_col_vect[1],
     xlab = 'block (color) x subblock', ylab = 'mean SCL +/- SEM', main = 'Arousal as a function of block & sub-block portion')
arrows(x0 = 1:5, 
       y0 = mean_scl_round_x_subblock[,1] - sem_scl_round_x_subblock[,1], 
       y1 = mean_scl_round_x_subblock[,1] + sem_scl_round_x_subblock[,1],
       length = 0)

for (b in 2:4){
  lines(x = (1:5)+(b-1)*5, y = mean_scl_round_x_subblock[,b], lwd = 4, col = blk_col_vect[b])
  arrows(x0 = (1:5)+(b-1)*5, 
         y0 = mean_scl_round_x_subblock[,b] - sem_scl_round_x_subblock[,b], 
         y1 = mean_scl_round_x_subblock[,b] + sem_scl_round_x_subblock[,b],
         length = 0)
}
legend("topleft",
       legend = c('Block 1','Block 2', 'Block 3', 'Block 4'),
       col = blk_col_vect,
       lty = 1, lwd = 4)


plot(x = (1:5) - 0.05, y = mean_scl_goal_x_subblock[,1], type = 'l', 
     ylim = c(15, 19.5), lwd = 4, col = 'darkorchid4',
     xlab = 'subblock', ylab = 'mean SCL +/- SEM', main = 'Arousal as a function of GOAL level')
arrows(x0 = (1:5) - 0.05, 
       y0 = mean_scl_goal_x_subblock[,1] - sem_scl_goal_x_subblock[,1], 
       y1 = mean_scl_goal_x_subblock[,1] + sem_scl_goal_x_subblock[,1],
       length = 0)
lines(x = (1:5) + .05, y = mean_scl_goal_x_subblock[,2], lwd = 4, col = 'darkorchid2')
arrows(x0 = (1:5) + .05, 
       y0 = mean_scl_goal_x_subblock[,2] - sem_scl_goal_x_subblock[,2], 
       y1 = mean_scl_goal_x_subblock[,2] + sem_scl_goal_x_subblock[,2],
       length = 0)
legend("bottomleft",
       legend = c('High Goal','Low Goal'),
       col = c('darkorchid4','darkorchid2'),
       lty = 1, lwd = 4)


plot(x = (1:5) - 0.05, y = mean_scl_bonus_x_subblock[,1], type = 'l', 
     ylim = c(15, 20), lwd = 4, col = 'blue4',
     xlab = 'subblock', ylab = 'mean SCL +/- SEM', main = 'Arousal as a function of BONUS level')
arrows(x0 = (1:5) - 0.05, 
       y0 = mean_scl_bonus_x_subblock[,1] - sem_scl_bonus_x_subblock[,1], 
       y1 = mean_scl_bonus_x_subblock[,1] + sem_scl_bonus_x_subblock[,1],
       length = 0)
lines(x = (1:5) + .05, y = mean_scl_bonus_x_subblock[,2], lwd = 4, col = 'blue2')
arrows(x0 = (1:5) + .05, 
       y0 = mean_scl_bonus_x_subblock[,2] - sem_scl_bonus_x_subblock[,2], 
       y1 = mean_scl_bonus_x_subblock[,2] + sem_scl_bonus_x_subblock[,2],
       length = 0)
legend("bottomleft",
       legend = c('High Bonus','Low Bonus'),
       col = c('blue4','blue2'),
       lty = 1, lwd = 4)

# INTERPRETATION NOTES HERE

# Could do additional regressions to quantify these findings & explore e.g. interactions? 




### Trials Proximal to Goal Attainment (and not) ----

#### p(Risky) by Goal Proximity ----

##### No-Goal Blocks ----
# First, look at blocks where goals were NOT attained
nfinaltrials = 20 # number of trials at the end of the block to look at

trial_columns_nogoal = c()
for (t in 1:nfinaltrials){
  newt = paste0('trial', t, sep = "")
  trial_columns_nogoal = c(trial_columns_nogoal, newt)
}

other_columns = c('subjectnumber',
                  'roundnum',
                  'bonusatstakeP1N1',
                  'goallevelP1N1')

nogoal_finalchoices = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*4, length(trial_columns_nogoal) + length(other_columns))))
colnames(nogoal_finalchoices) = c(other_columns, trial_columns_nogoal)

nogoal_finalchoices$subjectnumber = rep(keep_participants, each = 4)
nogoal_finalchoices$roundnum = rep(1:4)

mean_nogoal_finalchoices = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects, length(trial_columns_nogoal) + 1)))
colnames(mean_nogoal_finalchoices) = c('subjectnumber', trial_columns_nogoal)

mean_nogoal_finalchoices$subjectnumber = keep_participants

meanbyGL_nogoal_finalchoices = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_nogoal) + 2)))
colnames(meanbyGL_nogoal_finalchoices) = c('subjectnumber', 'goallevelP1N1', trial_columns_nogoal)
meanbyGL_nogoal_finalchoices$subjectnumber = rep(keep_participants, each = 2)
meanbyGL_nogoal_finalchoices$goallevelP1N1 = rep(c(1,-1), number_of_clean_subjects)

meanbyBL_nogoal_finalchoices = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_nogoal) + 2)))
colnames(meanbyBL_nogoal_finalchoices) = c('subjectnumber', 'bonusatstakeP1N1', trial_columns_nogoal)
meanbyBL_nogoal_finalchoices$subjectnumber = rep(keep_participants, each = 2)
meanbyBL_nogoal_finalchoices$bonusatstakeP1N1 = rep(c(1,-1), number_of_clean_subjects)


for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]
  
  for (b in 1:4){
    nogoalInd = (nogoal_finalchoices$subjectnumber == subj_id) & (nogoal_finalchoices$roundnum == b)
    cleanlongInd = (clean_data_subjlevel_long$subjectnumber == subj_id) & (clean_data_subjlevel_long$roundnum == b)
    
    # stores out the goal and bonus level data for each participant
    nogoal_finalchoices$bonusatstakeP1N1[nogoalInd] = clean_data_subjlevel_long$bonusatstakeP1N1[cleanlongInd]
    nogoal_finalchoices$goallevelP1N1[nogoalInd] = clean_data_subjlevel_long$goallevelP1N1[cleanlongInd]
    
    if(clean_data_subjlevel_long$bonusreceived01[cleanlongInd] == 0) { # if they did NOT reach the goal on this round
      # getting nfinaltrials defined as the last 20
      final_trials = tail(tmpdata$choice[tmpdata$roundnum == b], nfinaltrials)
      
      # Storing choices
      nogoal_finalchoices[nogoalInd, trial_columns_nogoal] = final_trials
    }
  }
  
  #Storing the mean choices of the final 20 trials when the goal was NOT reached
  mean_nogoal_finalchoices[s,trial_columns_nogoal] = colMeans(nogoal_finalchoices[nogoal_finalchoices$subjectnumber == subj_id, trial_columns_nogoal], na.rm = TRUE)
  
  # Calculate per-subject averages for final choices on blocks by goal or bonus level
  # Goals
  for (glevel in c(1,-1)){
    meanbyGL_nogoal_finalchoices[(meanbyGL_nogoal_finalchoices$subjectnumber == subj_id) & 
                                   (meanbyGL_nogoal_finalchoices$goallevelP1N1 == glevel), trial_columns_nogoal] = 
      colMeans(nogoal_finalchoices[(nogoal_finalchoices$subjectnumber == subj_id) & 
                                     (nogoal_finalchoices$goallevelP1N1 == glevel), trial_columns_nogoal], na.rm = T)
  }
  
  # Bonuses
  for (blevel in c(1,-1)){
    meanbyBL_nogoal_finalchoices[(meanbyBL_nogoal_finalchoices$subjectnumber == subj_id) & 
                                   (meanbyBL_nogoal_finalchoices$bonusatstakeP1N1 == blevel), trial_columns_nogoal] = 
      colMeans(nogoal_finalchoices[(nogoal_finalchoices$subjectnumber == subj_id) & 
                                     (nogoal_finalchoices$bonusatstakeP1N1 == blevel), trial_columns_nogoal], na.rm = T)
  }
}

m_prisky_nogoal = colMeans(mean_nogoal_finalchoices[,trial_columns_nogoal], na.rm = T)
sem_prisky_nogoal = apply(mean_nogoal_finalchoices[, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(mean_nogoal_finalchoices[, trial_columns_nogoal]*0+1, na.rm = T))


# Goal Levels
m_prisky_nogoal_highGL = colMeans(meanbyGL_nogoal_finalchoices[meanbyGL_nogoal_finalchoices$goallevelP1N1 == 1,trial_columns_nogoal], na.rm = T)
sem_prisky_nogoal_highGL = apply(meanbyGL_nogoal_finalchoices[meanbyGL_nogoal_finalchoices$goallevelP1N1 == 1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_nogoal_finalchoices[meanbyGL_nogoal_finalchoices$goallevelP1N1 == 1, trial_columns_nogoal]*0+1, na.rm = T))

m_prisky_nogoal_lowGL = colMeans(meanbyGL_nogoal_finalchoices[meanbyGL_nogoal_finalchoices$goallevelP1N1 == -1,trial_columns_nogoal], na.rm = T)
sem_prisky_nogoal_lowGL = apply(meanbyGL_nogoal_finalchoices[meanbyGL_nogoal_finalchoices$goallevelP1N1 == -1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_nogoal_finalchoices[meanbyGL_nogoal_finalchoices$goallevelP1N1 == -1, trial_columns_nogoal]*0+1, na.rm = T))

# Bonus Levels
m_prisky_nogoal_highBL = colMeans(meanbyBL_nogoal_finalchoices[meanbyBL_nogoal_finalchoices$bonusatstakeP1N1 == 1,trial_columns_nogoal], na.rm = T)
sem_prisky_nogoal_highBL = apply(meanbyBL_nogoal_finalchoices[meanbyBL_nogoal_finalchoices$bonusatstakeP1N1 == 1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_nogoal_finalchoices[meanbyBL_nogoal_finalchoices$bonusatstakeP1N1 == 1, trial_columns_nogoal]*0+1, na.rm = T))

m_prisky_nogoal_lowBL = colMeans(meanbyBL_nogoal_finalchoices[meanbyBL_nogoal_finalchoices$bonusatstakeP1N1 == -1,trial_columns_nogoal], na.rm = T)
sem_prisky_nogoal_lowBL = apply(meanbyBL_nogoal_finalchoices[meanbyBL_nogoal_finalchoices$bonusatstakeP1N1 == -1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_nogoal_finalchoices[meanbyBL_nogoal_finalchoices$bonusatstakeP1N1 == -1, trial_columns_nogoal]*0+1, na.rm = T))

# Plot it: OVERALL
plot(x = -nfinaltrials:-1, y = m_prisky_nogoal,
     type = 'l', lwd = 3, xlab = 'Trials relative to end of round', ylab = ('p(risky)'),
     ylim = c(0.3, 0.8), main = 'Final risky choices in rounds without goal achievement')
abline(h = 0.5, col = 'black', lwd = 1, lty = 'dashed')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_prisky_nogoal + sem_prisky_nogoal, rev(m_prisky_nogoal - sem_prisky_nogoal)),
        col = rgb(.5, .5, .5, .2))


# HIGH & LOW GOAL:
plot(x = -nfinaltrials:-1, y = m_prisky_nogoal_highGL,
     type = 'l', lwd = 3, xlab = 'Trials relative to end of round', ylab = ('p(risky)'),
     ylim = c(0, 1), main = 'Risky Choices in Unsuccessful Rounds by Goal Level',
     col = 'darkorchid4')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_prisky_nogoal_highGL + sem_prisky_nogoal_highGL, rev(m_prisky_nogoal_highGL - sem_prisky_nogoal_highGL)),
        col = rgb(t(col2rgb('darkorchid4')), alpha = 51, maxColorValue = 255))
lines(x = -nfinaltrials:-1, y = m_prisky_nogoal_lowGL,
      lwd = 3, col = 'darkorchid2')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_prisky_nogoal_lowGL + sem_prisky_nogoal_lowGL, rev(m_prisky_nogoal_lowGL - sem_prisky_nogoal_lowGL)),
        col = rgb(t(col2rgb('darkorchid2')), alpha = 51, maxColorValue = 255))
abline(h = 0.5, col = 'black', lwd = 1, lty = 'dashed')
legend("bottomleft",
       legend = c('High Goal','Low Goal'),
       col = c('darkorchid4','darkorchid2'),
       lty = 1, lwd = 4)


# HIGH & LOW BONUS:
plot(x = -nfinaltrials:-1, y = m_prisky_nogoal_highBL,
     type = 'l', lwd = 3, xlab = 'Trials relative to end of round', ylab = ('p(risky)'),
     ylim = c(0, 1), main = 'Risky Choices in Unsuccessful Rounds by Bonus Level',
     col = 'blue4')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_prisky_nogoal_highBL + sem_prisky_nogoal_highBL, rev(m_prisky_nogoal_highBL - sem_prisky_nogoal_highBL)),
        col = rgb(t(col2rgb('blue4')), alpha = 51, maxColorValue = 255))
lines(x = -nfinaltrials:-1, y = m_prisky_nogoal_lowBL,
      lwd = 3, col = 'blue2')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_prisky_nogoal_lowBL + sem_prisky_nogoal_lowBL, rev(m_prisky_nogoal_lowBL - sem_prisky_nogoal_lowBL)),
        col = rgb(t(col2rgb('blue2')), alpha = 51, maxColorValue = 255))
abline(h = 0.5, col = 'black', lwd = 1, lty = 'dashed')
legend("bottomleft",
       legend = c('High Bonus','Low Bonus'),
       col = c('blue4','blue2'),
       lty = 1, lwd = 4)

# risky decision-making increases as the end of the block approaches, starting around 5-10 trials before the end.


##### Yes-Goal Blocks ----
# Second, look at blocks where goals WERE attained
ntrialsprior = 10 # this number DOES NOT include THE TRIAL ON WHICH THE GOAL WAS MET/SURPASSED
ntrialsafter = 10 # starting with the first trial AFTER the goal was met/surpassed
nproximaltrials = ntrialsprior + 1 + ntrialsafter # number of trials to look at

clean_data_subjlevel_long$trialgoalmet = NA

trial_columns_yesgoal = c()
for (t in ntrialsprior:1){
  newt = paste0('trialminus', t, sep = "")
  trial_columns_yesgoal = c(trial_columns_yesgoal, newt)
}

trial_columns_yesgoal = c(trial_columns_yesgoal, 'trial0')

for (t in 1:ntrialsafter){
  newt = paste0('trialplus', t, sep = "")
  trial_columns_yesgoal = c(trial_columns_yesgoal, newt)
}


other_columns = c('subjectnumber',
                  'roundnum',
                  'bonusatstakeP1N1',
                  'goallevelP1N1')

yesgoal_finalchoices = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*4, length(trial_columns_yesgoal) + length(other_columns))))
colnames(yesgoal_finalchoices) = c(other_columns, trial_columns_yesgoal)

yesgoal_finalchoices$subjectnumber = rep(keep_participants, each = 4)
yesgoal_finalchoices$roundnum = rep(1:4)

mean_yesgoal_finalchoices = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects, length(trial_columns_yesgoal) + 1)))
colnames(mean_yesgoal_finalchoices) = c('subjectnumber', trial_columns_yesgoal)

mean_yesgoal_finalchoices$subjectnumber = keep_participants

meanbyGL_yesgoal_finalchoices = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_yesgoal) + 2)))
colnames(meanbyGL_yesgoal_finalchoices) = c('subjectnumber', 'goallevelP1N1', trial_columns_yesgoal)
meanbyGL_yesgoal_finalchoices$subjectnumber = rep(keep_participants, each = 2)
meanbyGL_yesgoal_finalchoices$goallevelP1N1 = rep(c(1,-1), number_of_clean_subjects)

meanbyBL_yesgoal_finalchoices = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_yesgoal) + 2)))
colnames(meanbyBL_yesgoal_finalchoices) = c('subjectnumber', 'bonusatstakeP1N1', trial_columns_yesgoal)
meanbyBL_yesgoal_finalchoices$subjectnumber = rep(keep_participants, each = 2)
meanbyBL_yesgoal_finalchoices$bonusatstakeP1N1 = rep(c(1,-1), number_of_clean_subjects)


for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]
  
  for (b in 1:4){
    # Make the indices we'll use
    yesgoalInd = (yesgoal_finalchoices$subjectnumber == subj_id) & (yesgoal_finalchoices$roundnum == b)
    cleanlongInd = (clean_data_subjlevel_long$subjectnumber == subj_id) & (clean_data_subjlevel_long$roundnum == b)
    
    # If they received the bonus on this round (i.e. attained the goal)
    if(clean_data_subjlevel_long$bonusreceived01[cleanlongInd]){
      # extract that block's data
      tmpblkdata = tmpdata[tmpdata$roundnumber == b,];
      
      # identify trial number where they met/exceeded the goal
      ind_goalmet = min(tmpblkdata$trialnumber_block[tmpblkdata$round_earnings >= unique(tmpblkdata$curr_goal)])
      
      clean_data_subjlevel_long$trialgoalmet[cleanlongInd] = ind_goalmet
      
      # identify the trial numbers to extract from the data
      trials_to_extract = (ind_goalmet - ntrialsprior):min(ind_goalmet + ntrialsafter, 50)
      
      # select the subset of trial column names we'll be using for this person & block
      tmp_trial_columns_yesgoal = trial_columns_yesgoal[1:length(trials_to_extract)]
      
      # do the extraction
      yesgoal_finalchoices[yesgoalInd,tmp_trial_columns_yesgoal] = tmpblkdata$choice[trials_to_extract]
    }
    
    # copy over the goal & bonus info
    yesgoal_finalchoices$bonusatstakeP1N1[yesgoalInd] = clean_data_subjlevel_long$bonusatstakeP1N1[cleanlongInd]
    yesgoal_finalchoices$goallevelP1N1[yesgoalInd] = clean_data_subjlevel_long$goallevelP1N1[cleanlongInd]
  }
  mean_yesgoal_finalchoices[s, trial_columns_yesgoal] = 
    colMeans(yesgoal_finalchoices[yesgoal_finalchoices$subjectnumber == subj_id, trial_columns_yesgoal], na.rm = T)
  
  # Goals
  for (glevel in c(1,-1)){
    meanbyGL_yesgoal_finalchoices[(meanbyGL_yesgoal_finalchoices$subjectnumber == subj_id) & 
                                    (meanbyGL_yesgoal_finalchoices$goallevelP1N1 == glevel), trial_columns_yesgoal] = 
      colMeans(yesgoal_finalchoices[(yesgoal_finalchoices$subjectnumber == subj_id) & 
                                      (yesgoal_finalchoices$goallevelP1N1 == glevel), trial_columns_yesgoal], na.rm = T)
  }
  
  # Bonuses
  for (blevel in c(1,-1)){
    meanbyBL_yesgoal_finalchoices[(meanbyBL_yesgoal_finalchoices$subjectnumber == subj_id) & 
                                    (meanbyBL_yesgoal_finalchoices$bonusatstakeP1N1 == blevel), trial_columns_yesgoal] = 
      colMeans(yesgoal_finalchoices[(yesgoal_finalchoices$subjectnumber == subj_id) & 
                                      (yesgoal_finalchoices$bonusatstakeP1N1 == blevel), trial_columns_yesgoal], na.rm = T)
  }
}

m_prisky_yesgoal = colMeans(mean_yesgoal_finalchoices[,trial_columns_yesgoal], na.rm = T)
sem_prisky_yesgoal = apply(mean_yesgoal_finalchoices[, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(mean_yesgoal_finalchoices[, trial_columns_yesgoal]*0+1, na.rm = T))

# Goal Levels
m_prisky_yesgoal_highGL = colMeans(meanbyGL_yesgoal_finalchoices[meanbyGL_yesgoal_finalchoices$goallevelP1N1 == 1,trial_columns_yesgoal], na.rm = T)
sem_prisky_yesgoal_highGL = apply(meanbyGL_yesgoal_finalchoices[meanbyGL_yesgoal_finalchoices$goallevelP1N1 == 1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_yesgoal_finalchoices[meanbyGL_yesgoal_finalchoices$goallevelP1N1 == 1, trial_columns_yesgoal]*0+1, na.rm = T))

m_prisky_yesgoal_lowGL = colMeans(meanbyGL_yesgoal_finalchoices[meanbyGL_yesgoal_finalchoices$goallevelP1N1 == -1,trial_columns_yesgoal], na.rm = T)
sem_prisky_yesgoal_lowGL = apply(meanbyGL_yesgoal_finalchoices[meanbyGL_yesgoal_finalchoices$goallevelP1N1 == -1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_yesgoal_finalchoices[meanbyGL_yesgoal_finalchoices$goallevelP1N1 == -1, trial_columns_yesgoal]*0+1, na.rm = T))

# Bonus Levels
m_prisky_yesgoal_highBL = colMeans(meanbyBL_yesgoal_finalchoices[meanbyBL_yesgoal_finalchoices$bonusatstakeP1N1 == 1,trial_columns_yesgoal], na.rm = T)
sem_prisky_yesgoal_highBL = apply(meanbyBL_yesgoal_finalchoices[meanbyBL_yesgoal_finalchoices$bonusatstakeP1N1 == 1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_yesgoal_finalchoices[meanbyBL_yesgoal_finalchoices$bonusatstakeP1N1 == 1, trial_columns_yesgoal]*0+1, na.rm = T))

m_prisky_yesgoal_lowBL = colMeans(meanbyBL_yesgoal_finalchoices[meanbyBL_yesgoal_finalchoices$bonusatstakeP1N1 == -1,trial_columns_yesgoal], na.rm = T)
sem_prisky_yesgoal_lowBL = apply(meanbyBL_yesgoal_finalchoices[meanbyBL_yesgoal_finalchoices$bonusatstakeP1N1 == -1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_yesgoal_finalchoices[meanbyBL_yesgoal_finalchoices$bonusatstakeP1N1 == -1, trial_columns_yesgoal]*0+1, na.rm = T))



# Plot it: OVERALL
plot(x = -ntrialsprior:ntrialsafter, y = m_prisky_yesgoal,
     type = 'l', lwd = 3, xlab = 'Trials relative to goal achievement', ylab = ('p(risky)'),
     ylim = c(0.3, 0.7), main = 'Risky Choices by Proximity to Goal Achievement')
abline(v = 0, col = 'black', lwd = 1, lty = 'dashed')
abline(h = 0.5, col = 'black', lwd = 1, lty = 'dashed')
# arrows(x0 = -ntrialsprior:ntrialsafter, 
#        y0 = m_prisky_yesgoal - sem_prisky_yesgoal, 
#        y1 = m_prisky_yesgoal + sem_prisky_yesgoal,
#        length = 0)
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_prisky_yesgoal + sem_prisky_yesgoal, rev(m_prisky_yesgoal - sem_prisky_yesgoal)),
        col = rgb(.5, .5, .5, .2))

# HIGH & LOW GOAL:
plot(x = -ntrialsprior:ntrialsafter, y = m_prisky_yesgoal_highGL,
     type = 'l', lwd = 3, xlab = 'Trials relative to goal achievement', ylab = ('p(risky)'),
     ylim = c(0.2, 1), main = 'Risky Choices by Proximity to Goal Achievement',
     col = 'darkorchid4')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_prisky_yesgoal_highGL + sem_prisky_yesgoal_highGL, rev(m_prisky_yesgoal_highGL - sem_prisky_yesgoal_highGL)),
        col = rgb(t(col2rgb('darkorchid4')), alpha = 51, maxColorValue = 255))
lines(x = -ntrialsprior:ntrialsafter, y = m_prisky_yesgoal_lowGL,
      lwd = 3, col = 'darkorchid2')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_prisky_yesgoal_lowGL + sem_prisky_yesgoal_lowGL, rev(m_prisky_yesgoal_lowGL - sem_prisky_yesgoal_lowGL)),
        col = rgb(t(col2rgb('darkorchid2')), alpha = 51, maxColorValue = 255))
abline(v = 0, col = 'black', lwd = 1, lty = 'dashed')
abline(h = 0.5, col = 'black', lwd = 1, lty = 'dashed')
legend("bottomleft",
       legend = c('High Goal','Low Goal'),
       col = c('darkorchid4','darkorchid2'),
       lty = 1, lwd = 4)



# HIGH & LOW BONUS:
plot(x = -ntrialsprior:ntrialsafter, y = m_prisky_yesgoal_highBL,
     type = 'l', lwd = 3, xlab = 'Trials relative to goal achievement', ylab = ('p(risky)'),
     ylim = c(0.3, 0.8), main = 'Risky Choices by Proximity to Goal Achievement',
     col = 'blue4')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_prisky_yesgoal_highBL + sem_prisky_yesgoal_highBL, rev(m_prisky_yesgoal_highBL - sem_prisky_yesgoal_highBL)),
        col = rgb(t(col2rgb('blue4')), alpha = 51, maxColorValue = 255))
lines(x = -ntrialsprior:ntrialsafter, y = m_prisky_yesgoal_lowBL,
      lwd = 3, col = 'blue2')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_prisky_yesgoal_lowBL + sem_prisky_yesgoal_lowBL, rev(m_prisky_yesgoal_lowBL - sem_prisky_yesgoal_lowBL)),
        col = rgb(t(col2rgb('blue2')), alpha = 51, maxColorValue = 255))
abline(v = 0, col = 'black', lwd = 1, lty = 'dashed')
abline(h = 0.5, col = 'black', lwd = 1, lty = 'dashed')
legend("bottomleft",
       legend = c('High Bonus','Low Bonus'),
       col = c('blue4','blue2'),
       lty = 1, lwd = 4)

# If we want to use regression on this, need to reshape into LONG format, and include a
# new variable "postGoal" that identifies choices made after meeting/exceeding the goal.
# Could also just do that in the clean_data_dm dataframe itself! 

# TAKEAWAY: 
# Risk-taking drops immediately before reaching the goal, and dramatically increases 
# IMMEDIATELY after reaching the goal. This pattern is exacerbated under high vs. low 
# goals. 


###### Supplemental Analysis ----
# looking at trialgoalmet

# Number of goals met
sum(is.finite(clean_data_subjlevel_long$trialgoalmet[clean_data_subjlevel_long$goallevelP1N1 == 1])) # high goal
sum(is.finite(clean_data_subjlevel_long$trialgoalmet[clean_data_subjlevel_long$goallevelP1N1 == -1])) # low goal

# On which trial was the goal met when it was met
mean(clean_data_subjlevel_long$trialgoalmet[clean_data_subjlevel_long$goallevelP1N1 == 1], na.rm = T)
mean(clean_data_subjlevel_long$trialgoalmet[clean_data_subjlevel_long$goallevelP1N1 == -1], na.rm = T)

# On which trial was the goal met when it was met (median)
median(clean_data_subjlevel_long$trialgoalmet[clean_data_subjlevel_long$goallevelP1N1 == 1], na.rm = T)
median(clean_data_subjlevel_long$trialgoalmet[clean_data_subjlevel_long$goallevelP1N1 == -1], na.rm = T)


var(clean_data_subjlevel_long$trialgoalmet[clean_data_subjlevel_long$goallevelP1N1 == 1], na.rm = T)
var(clean_data_subjlevel_long$trialgoalmet[clean_data_subjlevel_long$goallevelP1N1 == -1], na.rm = T)

# People met the goal 54/132 times when goals were high, 122/132 when they were low. 
# They met that goal on trial 47 (high goal) vs. 43 (low goal) WHEN it was met.
# The variance in that number was 8.6 (high goal) vs. 16.4 (low goal) WHEN it was met. 
#   ... this variance calc. might be problematic: closer to boundary (50) might = low var


#### Decision Time by Goal Proximity ----

##### No-Goal Blocks ----
# First, look at blocks where goals were NOT attained
nfinaltrials = 20 # number of trials at the end of the block to look at

trial_columns_nogoal = c()
for (t in 1:nfinaltrials){
  newt = paste0('trial', t, sep = "")
  trial_columns_nogoal = c(trial_columns_nogoal, newt)
}

other_columns = c('subjectnumber',
                  'roundnum',
                  'bonusatstakeP1N1',
                  'goallevelP1N1')

nogoal_finalrts = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*4, length(trial_columns_nogoal) + length(other_columns))))
colnames(nogoal_finalrts) = c(other_columns, trial_columns_nogoal)

nogoal_finalrts$subjectnumber = rep(keep_participants, each = 4)
nogoal_finalrts$roundnum = rep(1:4)

mean_nogoal_finalrts = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects, length(trial_columns_nogoal) + 1)))
colnames(mean_nogoal_finalrts) = c('subjectnumber', trial_columns_nogoal)

mean_nogoal_finalrts$subjectnumber = keep_participants

meanbyGL_nogoal_finalrts = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_nogoal) + 2)))
colnames(meanbyGL_nogoal_finalrts) = c('subjectnumber', 'goallevelP1N1', trial_columns_nogoal)
meanbyGL_nogoal_finalrts$subjectnumber = rep(keep_participants, each = 2)
meanbyGL_nogoal_finalrts$goallevelP1N1 = rep(c(1,-1), number_of_clean_subjects)

meanbyBL_nogoal_finalrts = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_nogoal) + 2)))
colnames(meanbyBL_nogoal_finalrts) = c('subjectnumber', 'bonusatstakeP1N1', trial_columns_nogoal)
meanbyBL_nogoal_finalrts$subjectnumber = rep(keep_participants, each = 2)
meanbyBL_nogoal_finalrts$bonusatstakeP1N1 = rep(c(1,-1), number_of_clean_subjects)

for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]

  for (b in 1:4){
    nogoalInd = (nogoal_finalrts$subjectnumber == subj_id) & (nogoal_finalrts$roundnum == b)
    cleanlongInd = (clean_data_subjlevel_long$subjectnumber == subj_id) & (clean_data_subjlevel_long$roundnum == b)

    # stores out the goal and bonus level data for each participant
    nogoal_finalrts$bonusatstakeP1N1[nogoalInd] = clean_data_subjlevel_long$bonusatstakeP1N1[cleanlongInd]
    nogoal_finalrts$goallevelP1N1[nogoalInd] = clean_data_subjlevel_long$goallevelP1N1[cleanlongInd]


    if(clean_data_subjlevel_long$bonusreceived01[cleanlongInd] == 0) { # if they did NOT reach the goal on this round
      # getting nfinaltrials defined as the last 20
      final_trials = tail(tmpdata$reactiontime[tmpdata$roundnum == b], nfinaltrials)

      # Storing choices
      nogoal_finalrts[nogoalInd, trial_columns_nogoal] = final_trials
    }
  }

  #Storing the mean choices of the final 20 trials when the goal was NOT reached
  mean_nogoal_finalrts[s,trial_columns_nogoal] = colMeans(nogoal_finalrts[nogoal_finalrts$subjectnumber == subj_id, trial_columns_nogoal], na.rm = TRUE)

  # Calculate per-subject averages for final choices on blocks by goal or bonus level
  # Goals
  for (glevel in c(1,-1)){
    meanbyGL_nogoal_finalrts[(meanbyGL_nogoal_finalrts$subjectnumber == subj_id) &
                                   (meanbyGL_nogoal_finalrts$goallevelP1N1 == glevel), trial_columns_nogoal] =
      colMeans(nogoal_finalrts[(nogoal_finalrts$subjectnumber == subj_id) &
                                     (nogoal_finalrts$goallevelP1N1 == glevel), trial_columns_nogoal], na.rm = T)
  }

  # Bonuses
  for (blevel in c(1,-1)){
    meanbyBL_nogoal_finalrts[(meanbyBL_nogoal_finalrts$subjectnumber == subj_id) &
                                   (meanbyBL_nogoal_finalrts$bonusatstakeP1N1 == blevel), trial_columns_nogoal] =
      colMeans(nogoal_finalrts[(nogoal_finalrts$subjectnumber == subj_id) &
                                     (nogoal_finalrts$bonusatstakeP1N1 == blevel), trial_columns_nogoal], na.rm = T)
  }
}

m_rt_nogoal = colMeans(mean_nogoal_finalrts[,trial_columns_nogoal], na.rm = T)
sem_rt_nogoal = apply(mean_nogoal_finalrts[, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(mean_nogoal_finalrts[, trial_columns_nogoal]*0+1, na.rm = T))


# Goal Levels
m_rt_nogoal_highGL = colMeans(meanbyGL_nogoal_finalrts[meanbyGL_nogoal_finalrts$goallevelP1N1 == 1,trial_columns_nogoal], na.rm = T)
sem_rt_nogoal_highGL = apply(meanbyGL_nogoal_finalrts[meanbyGL_nogoal_finalrts$goallevelP1N1 == 1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_nogoal_finalrts[meanbyGL_nogoal_finalrts$goallevelP1N1 == 1, trial_columns_nogoal]*0+1, na.rm = T))

m_rt_nogoal_lowGL = colMeans(meanbyGL_nogoal_finalrts[meanbyGL_nogoal_finalrts$goallevelP1N1 == -1,trial_columns_nogoal], na.rm = T)
sem_rt_nogoal_lowGL = apply(meanbyGL_nogoal_finalrts[meanbyGL_nogoal_finalrts$goallevelP1N1 == -1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_nogoal_finalrts[meanbyGL_nogoal_finalrts$goallevelP1N1 == -1, trial_columns_nogoal]*0+1, na.rm = T))

# Bonus Levels
m_rt_nogoal_highBL = colMeans(meanbyBL_nogoal_finalrts[meanbyBL_nogoal_finalrts$bonusatstakeP1N1 == 1,trial_columns_nogoal], na.rm = T)
sem_rt_nogoal_highBL = apply(meanbyBL_nogoal_finalrts[meanbyBL_nogoal_finalrts$bonusatstakeP1N1 == 1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_nogoal_finalrts[meanbyBL_nogoal_finalrts$bonusatstakeP1N1 == 1, trial_columns_nogoal]*0+1, na.rm = T))

m_rt_nogoal_lowBL = colMeans(meanbyBL_nogoal_finalrts[meanbyBL_nogoal_finalrts$bonusatstakeP1N1 == -1,trial_columns_nogoal], na.rm = T)
sem_rt_nogoal_lowBL = apply(meanbyBL_nogoal_finalrts[meanbyBL_nogoal_finalrts$bonusatstakeP1N1 == -1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_nogoal_finalrts[meanbyBL_nogoal_finalrts$bonusatstakeP1N1 == -1, trial_columns_nogoal]*0+1, na.rm = T))

print(head(m_rt_nogoal))
print(sum(is.na(m_rt_nogoal)))

print(head(m_rt_nogoal_highGL))
print(head(m_rt_nogoal_lowGL))

# Plot it: OVERALL
plot(x = -nfinaltrials:-1, y = m_rt_nogoal,
     type = 'l', lwd = 3, xlab = 'Trials relative to end of round', ylab = ('decision time (ms)'),
     ylim = c(0.5, 1.6), main = 'Decision times in rounds without goal achievement')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_rt_nogoal + sem_rt_nogoal, rev(m_rt_nogoal - sem_rt_nogoal)),
        col = rgb(.5, .5, .5, .2))


# HIGH & LOW GOAL:
plot(x = -nfinaltrials:-1, y = m_rt_nogoal_highGL,
     type = 'l', lwd = 3, xlab = 'Trials relative to end of round', ylab = ('decision time (ms)'),
     ylim = c(0.5, 1.6), main = 'Decision times in rounds without goal achievement',
     col = 'darkorchid4')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_rt_nogoal_highGL + sem_rt_nogoal_highGL, rev(m_rt_nogoal_highGL - sem_rt_nogoal_highGL)),
        col = rgb(t(col2rgb('darkorchid4')), alpha = 51, maxColorValue = 255))
lines(x = -nfinaltrials:-1, y = m_rt_nogoal_lowGL,
      lwd = 3, col = 'darkorchid2')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_rt_nogoal_lowGL + sem_rt_nogoal_lowGL, rev(m_rt_nogoal_lowGL - sem_rt_nogoal_lowGL)),
        col = rgb(t(col2rgb('darkorchid2')), alpha = 51, maxColorValue = 255))
legend("bottomleft",
       legend = c('High Goal','Low Goal'),
       col = c('darkorchid4','darkorchid2'),
       lty = 1, lwd = 4)


# HIGH & LOW BONUS:
plot(x = -nfinaltrials:-1, y = m_rt_nogoal_highBL,
     type = 'l', lwd = 3, xlab = 'Trials relative to end of round', ylab = ('decision time (ms)'),
     ylim = c(0.5, 1.6), main = 'Decision times in rounds without goal achievement',
     col = 'blue4')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_rt_nogoal_highBL + sem_rt_nogoal_highBL, rev(m_rt_nogoal_highBL - sem_rt_nogoal_highBL)),
        col = rgb(t(col2rgb('blue4')), alpha = 51, maxColorValue = 255))
lines(x = -nfinaltrials:-1, y = m_rt_nogoal_lowBL,
      lwd = 3, col = 'blue2')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_rt_nogoal_lowBL + sem_rt_nogoal_lowBL, rev(m_rt_nogoal_lowBL - sem_rt_nogoal_lowBL)),
        col = rgb(t(col2rgb('blue2')), alpha = 51, maxColorValue = 255))
legend("bottomleft",
       legend = c('High Bonus','Low Bonus'),
       col = c('blue4','blue2'),
       lty = 1, lwd = 4)


##### Yes-Goal Blocks ----
# Second, look at blocks where goals WERE attained
yesgoal_finalrts = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*4, length(trial_columns_yesgoal) + length(other_columns))))
colnames(yesgoal_finalrts) = c(other_columns, trial_columns_yesgoal)

yesgoal_finalrts$subjectnumber = rep(keep_participants, each = 4)
yesgoal_finalrts$roundnum = rep(1:4)

mean_yesgoal_finalrts = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects, length(trial_columns_yesgoal) + 1)))
colnames(mean_yesgoal_finalrts) = c('subjectnumber', trial_columns_yesgoal)

mean_yesgoal_finalrts$subjectnumber = keep_participants

meanbyGL_yesgoal_finalrts = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_yesgoal) + 2)))
colnames(meanbyGL_yesgoal_finalrts) = c('subjectnumber', 'goallevelP1N1', trial_columns_yesgoal)
meanbyGL_yesgoal_finalrts$subjectnumber = rep(keep_participants, each = 2)
meanbyGL_yesgoal_finalrts$goallevelP1N1 = rep(c(1,-1), number_of_clean_subjects)

meanbyBL_yesgoal_finalrts = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_yesgoal) + 2)))
colnames(meanbyBL_yesgoal_finalrts) = c('subjectnumber', 'bonusatstakeP1N1', trial_columns_yesgoal)
meanbyBL_yesgoal_finalrts$subjectnumber = rep(keep_participants, each = 2)
meanbyBL_yesgoal_finalrts$bonusatstakeP1N1 = rep(c(1,-1), number_of_clean_subjects)


for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]
  
  for (b in 1:4){
    # Make the indices we'll use
    yesgoalInd = (yesgoal_finalchoices$subjectnumber == subj_id) & (yesgoal_finalchoices$roundnum == b)
    cleanlongInd = (clean_data_subjlevel_long$subjectnumber == subj_id) & (clean_data_subjlevel_long$roundnum == b)
    
    # If they received the bonus on this round (i.e. attained the goal)
    if(clean_data_subjlevel_long$bonusreceived01[cleanlongInd]){
      # extract that block's data
      tmpblkdata = tmpdata[tmpdata$roundnumber == b,];
      
      # identify trial number where they met/exceeded the goal
      ind_goalmet = min(tmpblkdata$trialnumber_block[tmpblkdata$round_earnings >= unique(tmpblkdata$curr_goal)])
      
      # identify the trial numbers to extract from the data
      trials_to_extract = (ind_goalmet - ntrialsprior):min(ind_goalmet + ntrialsafter, 50)
      
      # select the subset of trial column names we'll be using for this person & block
      tmp_trial_columns_yesgoal = trial_columns_yesgoal[1:length(trials_to_extract)]
      
      # do the extraction
      yesgoal_finalrts[yesgoalInd,tmp_trial_columns_yesgoal] = tmpblkdata$reactiontime[trials_to_extract]
    }
    
    # copy over the goal & bonus info
    yesgoal_finalrts$bonusatstakeP1N1[yesgoalInd] = clean_data_subjlevel_long$bonusatstakeP1N1[cleanlongInd]
    yesgoal_finalrts$goallevelP1N1[yesgoalInd] = clean_data_subjlevel_long$goallevelP1N1[cleanlongInd]
  }
  mean_yesgoal_finalrts[s, trial_columns_yesgoal] = 
    colMeans(yesgoal_finalrts[yesgoal_finalchoices$subjectnumber == subj_id, trial_columns_yesgoal], na.rm = T)
  
  # Goals
  for (glevel in c(1,-1)){
    meanbyGL_yesgoal_finalrts[(meanbyGL_yesgoal_finalrts$subjectnumber == subj_id) & 
                                    (meanbyGL_yesgoal_finalrts$goallevelP1N1 == glevel), trial_columns_yesgoal] = 
      colMeans(yesgoal_finalrts[(yesgoal_finalrts$subjectnumber == subj_id) & 
                                      (yesgoal_finalrts$goallevelP1N1 == glevel), trial_columns_yesgoal], na.rm = T)
  }
  
  # Bonuses
  for (blevel in c(1,-1)){
    meanbyBL_yesgoal_finalrts[(meanbyBL_yesgoal_finalrts$subjectnumber == subj_id) & 
                                    (meanbyBL_yesgoal_finalrts$bonusatstakeP1N1 == blevel), trial_columns_yesgoal] = 
      colMeans(yesgoal_finalrts[(yesgoal_finalrts$subjectnumber == subj_id) & 
                                      (yesgoal_finalrts$bonusatstakeP1N1 == blevel), trial_columns_yesgoal], na.rm = T)
  }
}

m_rt_yesgoal = colMeans(mean_yesgoal_finalrts[,trial_columns_yesgoal], na.rm = T)

sem_rt_yesgoal = apply(mean_yesgoal_finalrts[, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(mean_yesgoal_finalrts[, trial_columns_yesgoal]*0+1, na.rm = T))

# Goal Levels
m_rt_yesgoal_highGL = colMeans(meanbyGL_yesgoal_finalrts[meanbyGL_yesgoal_finalrts$goallevelP1N1 == 1,trial_columns_yesgoal], na.rm = T)
sem_rt_yesgoal_highGL = apply(meanbyGL_yesgoal_finalrts[meanbyGL_yesgoal_finalchoices$goallevelP1N1 == 1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_yesgoal_finalrts[meanbyGL_yesgoal_finalrts$goallevelP1N1 == 1, trial_columns_yesgoal]*0+1, na.rm = T))

m_rt_yesgoal_lowGL = colMeans(meanbyGL_yesgoal_finalrts[meanbyGL_yesgoal_finalrts$goallevelP1N1 == -1,trial_columns_yesgoal], na.rm = T)
sem_rt_yesgoal_lowGL = apply(meanbyGL_yesgoal_finalrts[meanbyGL_yesgoal_finalrts$goallevelP1N1 == -1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_yesgoal_finalrts[meanbyGL_yesgoal_finalrts$goallevelP1N1 == -1, trial_columns_yesgoal]*0+1, na.rm = T))

# Bonus Levels
m_rt_yesgoal_highBL = colMeans(meanbyBL_yesgoal_finalrts[meanbyBL_yesgoal_finalrts$bonusatstakeP1N1 == 1,trial_columns_yesgoal], na.rm = T)
sem_rt_yesgoal_highBL = apply(meanbyBL_yesgoal_finalrts[meanbyBL_yesgoal_finalrts$bonusatstakeP1N1 == 1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_yesgoal_finalrts[meanbyBL_yesgoal_finalrts$bonusatstakeP1N1 == 1, trial_columns_yesgoal]*0+1, na.rm = T))

m_rt_yesgoal_lowBL = colMeans(meanbyBL_yesgoal_finalrts[meanbyBL_yesgoal_finalrts$bonusatstakeP1N1 == -1,trial_columns_yesgoal], na.rm = T)
sem_rt_yesgoal_lowBL = apply(meanbyBL_yesgoal_finalrts[meanbyBL_yesgoal_finalrts$bonusatstakeP1N1 == -1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_yesgoal_finalrts[meanbyBL_yesgoal_finalrts$bonusatstakeP1N1 == -1, trial_columns_yesgoal]*0+1, na.rm = T))


# Plot it
plot(x = -ntrialsprior:ntrialsafter, y = m_rt_yesgoal,
     type = 'l', lwd = 3, xlab = 'Trials relative to goal achievement', ylab = ('decision time (s)'),
     ylim = c(1, 1.3), main = 'Decision Time by Proximity to Goal Achievement')
abline(v = 0, col = 'black', lwd = 1, lty = 'dashed')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_rt_yesgoal + sem_rt_yesgoal, rev(m_rt_yesgoal - sem_rt_yesgoal)),
        col = rgb(.5, .5, .5, .2))
# NOTE: An unequal # of subjects contribute to these points after goal attainment, AND
# an unequal # of blocks/subject. Only the former is accounted for by the SEM calculation.



# HIGH & LOW GOAL:
plot(x = -ntrialsprior:ntrialsafter, y = m_rt_yesgoal_highGL,
     type = 'l', lwd = 3, xlab = 'Trials relative to goal achievement', ylab = ('decision time (s)'),
     ylim = c(0.8,1.4), main = 'Decision Time by Proximity to Goal Achievement',
     col = 'darkorchid4')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_rt_yesgoal_highGL + sem_rt_yesgoal_highGL, rev(m_rt_yesgoal_highGL - sem_rt_yesgoal_highGL)),
        col = rgb(t(col2rgb('darkorchid4')), alpha = 51, maxColorValue = 255))
lines(x = -ntrialsprior:ntrialsafter, y = m_rt_yesgoal_lowGL,
      lwd = 3, col = 'darkorchid2')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_rt_yesgoal_lowGL + sem_rt_yesgoal_lowGL, rev(m_rt_yesgoal_lowGL - sem_rt_yesgoal_lowGL)),
        col = rgb(t(col2rgb('darkorchid2')), alpha = 51, maxColorValue = 255))
abline(v = 0, col = 'black', lwd = 1, lty = 'dashed')
legend("bottomleft",
       legend = c('High Goal','Low Goal'),
       col = c('darkorchid4','darkorchid2'),
       lty = 1, lwd = 4)
# Effect of speeding post-goal might be stronger in high goal conditions? Hard to tell. 



# HIGH & LOW BONUS:
plot(x = -ntrialsprior:ntrialsafter, y = m_rt_yesgoal_highBL,
     type = 'l', lwd = 3, xlab = 'Trials relative to goal achievement', ylab = ('decision time (s)'),
     ylim = c(1.0,1.35), main = 'Decision Time by Proximity to Goal Achievement',
     col = 'blue4')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_rt_yesgoal_highBL + sem_rt_yesgoal_highBL, rev(m_rt_yesgoal_highBL - sem_rt_yesgoal_highBL)),
        col = rgb(t(col2rgb('blue4')), alpha = 51, maxColorValue = 255))
lines(x = -ntrialsprior:ntrialsafter, y = m_rt_yesgoal_lowBL,
      lwd = 3, col = 'blue2')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_rt_yesgoal_lowBL + sem_rt_yesgoal_lowBL, rev(m_rt_yesgoal_lowBL - sem_rt_yesgoal_lowBL)),
        col = rgb(t(col2rgb('blue2')), alpha = 51, maxColorValue = 255))
abline(v = 0, col = 'black', lwd = 1, lty = 'dashed')
legend("bottomleft",
       legend = c('High Bonus','Low Bonus'),
       col = c('blue4','blue2'),
       lty = 1, lwd = 4)


# TAKEAWAY: 
# Effort drops after reaching the goal and/or remains consistently low. This effect isn't huge.


#### Arousal by Goal Proximity ----

##### No-Goal Blocks ----
# First, look at blocks where goals were NOT attained
nfinaltrials = 20 # number of trials at the end of the block to look at

trial_columns_nogoal = c()
for (t in 1:nfinaltrials){
  newt = paste0('trial', t, sep = "")
  trial_columns_nogoal = c(trial_columns_nogoal, newt)
}

other_columns = c('subjectnumber',
                  'roundnum',
                  'bonusatstakeP1N1',
                  'goallevelP1N1')

nogoal_finalscl = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*4, length(trial_columns_nogoal) + length(other_columns))))
colnames(nogoal_finalscl) = c(other_columns, trial_columns_nogoal)

nogoal_finalscl$subjectnumber = rep(keep_participants, each = 4)
nogoal_finalscl$roundnum = rep(1:4)

mean_nogoal_finalscl = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects, length(trial_columns_nogoal) + 1)))
colnames(mean_nogoal_finalscl) = c('subjectnumber', trial_columns_nogoal)

mean_nogoal_finalscl$subjectnumber = keep_participants

meanbyGL_nogoal_finalscl = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_nogoal) + 2)))
colnames(meanbyGL_nogoal_finalscl) = c('subjectnumber', 'goallevelP1N1', trial_columns_nogoal)
meanbyGL_nogoal_finalscl$subjectnumber = rep(keep_participants, each = 2)
meanbyGL_nogoal_finalscl$goallevelP1N1 = rep(c(1,-1), number_of_clean_subjects)

meanbyBL_nogoal_finalscl = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_nogoal) + 2)))
colnames(meanbyBL_nogoal_finalscl) = c('subjectnumber', 'bonusatstakeP1N1', trial_columns_nogoal)
meanbyBL_nogoal_finalscl$subjectnumber = rep(keep_participants, each = 2)
meanbyBL_nogoal_finalscl$bonusatstakeP1N1 = rep(c(1,-1), number_of_clean_subjects)

for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]
  
  for (b in 1:4){
    nogoalInd = (nogoal_finalscl$subjectnumber == subj_id) & (nogoal_finalscl$roundnum == b)
    cleanlongInd = (clean_data_subjlevel_long$subjectnumber == subj_id) & (clean_data_subjlevel_long$roundnum == b)
    
    # stores out the goal and bonus level data for each participant
    nogoal_finalscl$bonusatstakeP1N1[nogoalInd] = clean_data_subjlevel_long$bonusatstakeP1N1[cleanlongInd]
    nogoal_finalscl$goallevelP1N1[nogoalInd] = clean_data_subjlevel_long$goallevelP1N1[cleanlongInd]
    
    
    if(clean_data_subjlevel_long$bonusreceived01[cleanlongInd] == 0) { # if they did NOT reach the goal on this round
      # getting nfinaltrials defined as the last 20
      final_trials = tail(tmpdata$tmeanscl[tmpdata$roundnum == b], nfinaltrials)
      
      # Storing choices
      nogoal_finalscl[nogoalInd, trial_columns_nogoal] = final_trials
    }
  }
  
  #Storing the mean choices of the final 20 trials when the goal was NOT reached
  mean_nogoal_finalscl[s,trial_columns_nogoal] = colMeans(nogoal_finalscl[nogoal_finalscl$subjectnumber == subj_id, trial_columns_nogoal], na.rm = TRUE)
  
  # Calculate per-subject averages for final choices on blocks by goal or bonus level
  # Goals
  for (glevel in c(1,-1)){
    meanbyGL_nogoal_finalscl[(meanbyGL_nogoal_finalscl$subjectnumber == subj_id) &
                               (meanbyGL_nogoal_finalscl$goallevelP1N1 == glevel), trial_columns_nogoal] =
      colMeans(nogoal_finalscl[(nogoal_finalscl$subjectnumber == subj_id) &
                                 (nogoal_finalscl$goallevelP1N1 == glevel), trial_columns_nogoal], na.rm = T)
  }
  
  # Bonuses
  for (blevel in c(1,-1)){
    meanbyBL_nogoal_finalscl[(meanbyBL_nogoal_finalscl$subjectnumber == subj_id) &
                               (meanbyBL_nogoal_finalscl$bonusatstakeP1N1 == blevel), trial_columns_nogoal] =
      colMeans(nogoal_finalscl[(nogoal_finalscl$subjectnumber == subj_id) &
                                 (nogoal_finalscl$bonusatstakeP1N1 == blevel), trial_columns_nogoal], na.rm = T)
  }
}

m_scl_nogoal = colMeans(mean_nogoal_finalscl[,trial_columns_nogoal], na.rm = T)
sem_scl_nogoal = apply(mean_nogoal_finalscl[, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(mean_nogoal_finalscl[, trial_columns_nogoal]*0+1, na.rm = T))


# Goal Levels
m_scl_nogoal_highGL = colMeans(meanbyGL_nogoal_finalscl[meanbyGL_nogoal_finalscl$goallevelP1N1 == 1,trial_columns_nogoal], na.rm = T)
sem_scl_nogoal_highGL = apply(meanbyGL_nogoal_finalscl[meanbyGL_nogoal_finalscl$goallevelP1N1 == 1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_nogoal_finalscl[meanbyGL_nogoal_finalscl$goallevelP1N1 == 1, trial_columns_nogoal]*0+1, na.rm = T))

m_scl_nogoal_lowGL = colMeans(meanbyGL_nogoal_finalscl[meanbyGL_nogoal_finalscl$goallevelP1N1 == -1,trial_columns_nogoal], na.rm = T)
sem_scl_nogoal_lowGL = apply(meanbyGL_nogoal_finalscl[meanbyGL_nogoal_finalscl$goallevelP1N1 == -1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_nogoal_finalscl[meanbyGL_nogoal_finalscl$goallevelP1N1 == -1, trial_columns_nogoal]*0+1, na.rm = T))

# Bonus Levels
m_scl_nogoal_highBL = colMeans(meanbyBL_nogoal_finalscl[meanbyBL_nogoal_finalscl$bonusatstakeP1N1 == 1,trial_columns_nogoal], na.rm = T)
sem_scl_nogoal_highBL = apply(meanbyBL_nogoal_finalscl[meanbyBL_nogoal_finalscl$bonusatstakeP1N1 == 1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_nogoal_finalscl[meanbyBL_nogoal_finalscl$bonusatstakeP1N1 == 1, trial_columns_nogoal]*0+1, na.rm = T))

m_scl_nogoal_lowBL = colMeans(meanbyBL_nogoal_finalscl[meanbyBL_nogoal_finalscl$bonusatstakeP1N1 == -1,trial_columns_nogoal], na.rm = T)
sem_scl_nogoal_lowBL = apply(meanbyBL_nogoal_finalscl[meanbyBL_nogoal_finalscl$bonusatstakeP1N1 == -1, trial_columns_nogoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_nogoal_finalscl[meanbyBL_nogoal_finalscl$bonusatstakeP1N1 == -1, trial_columns_nogoal]*0+1, na.rm = T))

print(head(m_scl_nogoal))
print(sum(is.na(m_scl_nogoal)))

print(head(m_scl_nogoal_highGL))
print(head(m_scl_nogoal_lowGL))

# Plot it: OVERALL
plot(x = -nfinaltrials:-1, y = m_scl_nogoal,
     type = 'l', lwd = 3, xlab = 'Trials relative to end of round', ylab = ('SCL (uS)'),
     ylim = c(13,19), main = 'Arousal in rounds without goal achievement')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_scl_nogoal + sem_scl_nogoal, rev(m_scl_nogoal - sem_scl_nogoal)),
        col = rgb(.5, .5, .5, .2))


# HIGH & LOW GOAL:
plot(x = -nfinaltrials:-1, y = m_scl_nogoal_highGL,
     type = 'l', lwd = 3, xlab = 'Trials relative to end of round', ylab = ('SCL (uS)'),
     ylim = c(13, 19), main = 'Arousal in rounds without goal achievement',
     col = 'darkorchid4')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_scl_nogoal_highGL + sem_scl_nogoal_highGL, rev(m_scl_nogoal_highGL - sem_scl_nogoal_highGL)),
        col = rgb(t(col2rgb('darkorchid4')), alpha = 51, maxColorValue = 255))
lines(x = -nfinaltrials:-1, y = m_scl_nogoal_lowGL,
      lwd = 3, col = 'darkorchid2')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_scl_nogoal_lowGL + sem_scl_nogoal_lowGL, rev(m_scl_nogoal_lowGL - sem_scl_nogoal_lowGL)),
        col = rgb(t(col2rgb('darkorchid2')), alpha = 51, maxColorValue = 255))
legend("bottomleft",
       legend = c('High Goal','Low Goal'),
       col = c('darkorchid4','darkorchid2'),
       lty = 1, lwd = 4)


# HIGH & LOW BONUS:
plot(x = -nfinaltrials:-1, y = m_scl_nogoal_highBL,
     type = 'l', lwd = 3, xlab = 'Trials relative to end of round', ylab = ('SCL (uS)'),
     ylim = c(13, 19), main = 'Arousal in rounds without goal achievement',
     col = 'blue4')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_scl_nogoal_highBL + sem_scl_nogoal_highBL, rev(m_scl_nogoal_highBL - sem_scl_nogoal_highBL)),
        col = rgb(t(col2rgb('blue4')), alpha = 51, maxColorValue = 255))
lines(x = -nfinaltrials:-1, y = m_scl_nogoal_lowBL,
      lwd = 3, col = 'blue2')
polygon(x = c(-nfinaltrials:-1, -1:-nfinaltrials),
        y = c(m_scl_nogoal_lowBL + sem_scl_nogoal_lowBL, rev(m_scl_nogoal_lowBL - sem_scl_nogoal_lowBL)),
        col = rgb(t(col2rgb('blue2')), alpha = 51, maxColorValue = 255))
legend("bottomleft",
       legend = c('High Bonus','Low Bonus'),
       col = c('blue4','blue2'),
       lty = 1, lwd = 4)


##### Yes-Goal Blocks ----
# Second, look at blocks where goals WERE attained
yesgoal_finalscl = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*4, length(trial_columns_yesgoal) + length(other_columns))))
colnames(yesgoal_finalscl) = c(other_columns, trial_columns_yesgoal)

yesgoal_finalscl$subjectnumber = rep(keep_participants, each = 4)
yesgoal_finalscl$roundnum = rep(1:4)

mean_yesgoal_finalscl = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects, length(trial_columns_yesgoal) + 1)))
colnames(mean_yesgoal_finalscl) = c('subjectnumber', trial_columns_yesgoal)

mean_yesgoal_finalscl$subjectnumber = keep_participants

meanbyGL_yesgoal_finalscl = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_yesgoal) + 2)))
colnames(meanbyGL_yesgoal_finalscl) = c('subjectnumber', 'goallevelP1N1', trial_columns_yesgoal)
meanbyGL_yesgoal_finalscl$subjectnumber = rep(keep_participants, each = 2)
meanbyGL_yesgoal_finalscl$goallevelP1N1 = rep(c(1,-1), number_of_clean_subjects)

meanbyBL_yesgoal_finalscl = as.data.frame(array(data = NA, dim = c(number_of_clean_subjects*2, length(trial_columns_yesgoal) + 2)))
colnames(meanbyBL_yesgoal_finalscl) = c('subjectnumber', 'bonusatstakeP1N1', trial_columns_yesgoal)
meanbyBL_yesgoal_finalscl$subjectnumber = rep(keep_participants, each = 2)
meanbyBL_yesgoal_finalscl$bonusatstakeP1N1 = rep(c(1,-1), number_of_clean_subjects)


for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]
  
  for (b in 1:4){
    # Make the indices we'll use
    yesgoalInd = (yesgoal_finalchoices$subjectnumber == subj_id) & (yesgoal_finalchoices$roundnum == b)
    cleanlongInd = (clean_data_subjlevel_long$subjectnumber == subj_id) & (clean_data_subjlevel_long$roundnum == b)
    
    # If they received the bonus on this round (i.e. attained the goal)
    if(clean_data_subjlevel_long$bonusreceived01[cleanlongInd]){
      # extract that block's data
      tmpblkdata = tmpdata[tmpdata$roundnumber == b,];
      
      # identify trial number where they met/exceeded the goal
      ind_goalmet = min(tmpblkdata$trialnumber_block[tmpblkdata$round_earnings >= unique(tmpblkdata$curr_goal)])
      
      # identify the trial numbers to extract from the data
      trials_to_extract = (ind_goalmet - ntrialsprior):min(ind_goalmet + ntrialsafter, 50)
      
      # select the subset of trial column names we'll be using for this person & block
      tmp_trial_columns_yesgoal = trial_columns_yesgoal[1:length(trials_to_extract)]
      
      # do the extraction
      yesgoal_finalscl[yesgoalInd,tmp_trial_columns_yesgoal] = tmpblkdata$tmeanscl[trials_to_extract]
    }
    
    # copy over the goal & bonus info
    yesgoal_finalscl$bonusatstakeP1N1[yesgoalInd] = clean_data_subjlevel_long$bonusatstakeP1N1[cleanlongInd]
    yesgoal_finalscl$goallevelP1N1[yesgoalInd] = clean_data_subjlevel_long$goallevelP1N1[cleanlongInd]
  }
  mean_yesgoal_finalscl[s, trial_columns_yesgoal] = 
    colMeans(yesgoal_finalscl[yesgoal_finalchoices$subjectnumber == subj_id, trial_columns_yesgoal], na.rm = T)
  
  # Goals
  for (glevel in c(1,-1)){
    meanbyGL_yesgoal_finalscl[(meanbyGL_yesgoal_finalscl$subjectnumber == subj_id) & 
                                (meanbyGL_yesgoal_finalscl$goallevelP1N1 == glevel), trial_columns_yesgoal] = 
      colMeans(yesgoal_finalscl[(yesgoal_finalscl$subjectnumber == subj_id) & 
                                  (yesgoal_finalscl$goallevelP1N1 == glevel), trial_columns_yesgoal], na.rm = T)
  }
  
  # Bonuses
  for (blevel in c(1,-1)){
    meanbyBL_yesgoal_finalscl[(meanbyBL_yesgoal_finalscl$subjectnumber == subj_id) & 
                                (meanbyBL_yesgoal_finalscl$bonusatstakeP1N1 == blevel), trial_columns_yesgoal] = 
      colMeans(yesgoal_finalscl[(yesgoal_finalscl$subjectnumber == subj_id) & 
                                  (yesgoal_finalscl$bonusatstakeP1N1 == blevel), trial_columns_yesgoal], na.rm = T)
  }
}

m_scl_yesgoal = colMeans(mean_yesgoal_finalscl[,trial_columns_yesgoal], na.rm = T)

sem_scl_yesgoal = apply(mean_yesgoal_finalscl[, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(mean_yesgoal_finalscl[, trial_columns_yesgoal]*0+1, na.rm = T))

# Goal Levels
m_scl_yesgoal_highGL = colMeans(meanbyGL_yesgoal_finalscl[meanbyGL_yesgoal_finalscl$goallevelP1N1 == 1,trial_columns_yesgoal], na.rm = T)
sem_scl_yesgoal_highGL = apply(meanbyGL_yesgoal_finalscl[meanbyGL_yesgoal_finalchoices$goallevelP1N1 == 1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_yesgoal_finalscl[meanbyGL_yesgoal_finalscl$goallevelP1N1 == 1, trial_columns_yesgoal]*0+1, na.rm = T))

m_scl_yesgoal_lowGL = colMeans(meanbyGL_yesgoal_finalscl[meanbyGL_yesgoal_finalscl$goallevelP1N1 == -1,trial_columns_yesgoal], na.rm = T)
sem_scl_yesgoal_lowGL = apply(meanbyGL_yesgoal_finalscl[meanbyGL_yesgoal_finalscl$goallevelP1N1 == -1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyGL_yesgoal_finalscl[meanbyGL_yesgoal_finalscl$goallevelP1N1 == -1, trial_columns_yesgoal]*0+1, na.rm = T))

# Bonus Levels
m_scl_yesgoal_highBL = colMeans(meanbyBL_yesgoal_finalscl[meanbyBL_yesgoal_finalscl$bonusatstakeP1N1 == 1,trial_columns_yesgoal], na.rm = T)
sem_scl_yesgoal_highBL = apply(meanbyBL_yesgoal_finalscl[meanbyBL_yesgoal_finalscl$bonusatstakeP1N1 == 1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_yesgoal_finalscl[meanbyBL_yesgoal_finalscl$bonusatstakeP1N1 == 1, trial_columns_yesgoal]*0+1, na.rm = T))

m_scl_yesgoal_lowBL = colMeans(meanbyBL_yesgoal_finalscl[meanbyBL_yesgoal_finalscl$bonusatstakeP1N1 == -1,trial_columns_yesgoal], na.rm = T)
sem_scl_yesgoal_lowBL = apply(meanbyBL_yesgoal_finalscl[meanbyBL_yesgoal_finalscl$bonusatstakeP1N1 == -1, trial_columns_yesgoal], 2, sd, na.rm = T)/
  sqrt(colSums(meanbyBL_yesgoal_finalscl[meanbyBL_yesgoal_finalscl$bonusatstakeP1N1 == -1, trial_columns_yesgoal]*0+1, na.rm = T))


# Plot it
# OVERALL
plot(x = -ntrialsprior:ntrialsafter, y = m_scl_yesgoal,
     type = 'l', lwd = 3, xlab = 'Trials relative to goal achievement', ylab = ('SCL (uS)'),
     ylim = c(12, 19), main = 'Arousal by Proximity to Goal Achievement')
abline(v = 0, col = 'black', lwd = 1, lty = 'dashed')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_scl_yesgoal + sem_scl_yesgoal, rev(m_scl_yesgoal - sem_scl_yesgoal)),
        col = rgb(.5, .5, .5, .2))


# HIGH & LOW GOAL:
plot(x = -ntrialsprior:ntrialsafter, y = m_scl_yesgoal_highGL,
     type = 'l', lwd = 3, xlab = 'Trials relative to goal achievement', ylab = ('SCL (uS)'),
     ylim = c(9, 21), main = 'Arousal by Proximity to Goal Achievement',
     col = 'darkorchid4')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_scl_yesgoal_highGL + sem_scl_yesgoal_highGL, rev(m_scl_yesgoal_highGL - sem_scl_yesgoal_highGL)),
        col = rgb(t(col2rgb('darkorchid4')), alpha = 51, maxColorValue = 255))
lines(x = -ntrialsprior:ntrialsafter, y = m_scl_yesgoal_lowGL,
      lwd = 3, col = 'darkorchid2')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_scl_yesgoal_lowGL + sem_scl_yesgoal_lowGL, rev(m_scl_yesgoal_lowGL - sem_scl_yesgoal_lowGL)),
        col = rgb(t(col2rgb('darkorchid2')), alpha = 51, maxColorValue = 255))
abline(v = 0, col = 'black', lwd = 1, lty = 'dashed')
legend("bottomleft",
       legend = c('High Goal','Low Goal'),
       col = c('darkorchid4','darkorchid2'),
       lty = 1, lwd = 4)
# Effect of speeding post-goal might be stronger in high goal conditions? Hard to tell. 



# HIGH & LOW BONUS:
plot(x = -ntrialsprior:ntrialsafter, y = m_scl_yesgoal_highBL,
     type = 'l', lwd = 3, xlab = 'Trials relative to goal achievement', ylab = ('SCL (uS)'),
     ylim = c(9, 21), main = 'Arousal by Proximity to Goal Achievement',
     col = 'blue4')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_scl_yesgoal_highBL + sem_scl_yesgoal_highBL, rev(m_scl_yesgoal_highBL - sem_scl_yesgoal_highBL)),
        col = rgb(t(col2rgb('blue4')), alpha = 51, maxColorValue = 255))
lines(x = -ntrialsprior:ntrialsafter, y = m_scl_yesgoal_lowBL,
      lwd = 3, col = 'blue2')
polygon(x = c(-ntrialsprior:ntrialsafter, ntrialsafter:-ntrialsprior),
        y = c(m_scl_yesgoal_lowBL + sem_scl_yesgoal_lowBL, rev(m_scl_yesgoal_lowBL - sem_scl_yesgoal_lowBL)),
        col = rgb(t(col2rgb('blue2')), alpha = 51, maxColorValue = 255))
abline(v = 0, col = 'black', lwd = 1, lty = 'dashed')
abline(h = 0.5, col = 'black', lwd = 1, lty = 'dashed')
legend("bottomleft",
       legend = c('High Bonus','Low Bonus'),
       col = c('blue4','blue2'),
       lty = 1, lwd = 4)





## 4. RHO ESTIMATES ----
# What are the computational model estimates of behavior?
# Can modified models capture some of what we see behaviorally? 

### Function Definitions ----
# Function to calculate choice probabilities
choice_probability <- function(parameters, choiceset) {
  # A function to calculate the probability of taking a risky option
  # using a prospect theory model.
  # Assumes parameters are [rho, mu] as used in S-H 2009, 2013, 2015, etc.
  # Assumes choiceset has columns riskyoption1, riskyoption2, and safeoption
  #
  # PSH 2026
  
  # extract  parameters
  rho = as.double(parameters[1]); # risk attitudes
  mu = as.double(parameters[2]); # choice consistency
  
  # Correct parameter bounds
  if(rho <= 0){
    rho = .Machine$double.eps;
  }
  
  if(mu < 0){
    mu = 0;
  }
  
  # calculate utility of the two options
  utility_risky_option = 0.5 * choiceset$riskyoption1^rho +
    0.5 * choiceset$riskyoption2^rho;
  utility_safe_option = choiceset$safeoption^rho;
  
  # normalize values using this term
  div <- max(choiceset[,1:3])^rho; # decorrelates rho & mu
  
  # calculate the probability of selecting the risky option
  p = 1/(1+exp(-mu/div*(utility_risky_option - utility_safe_option)));
  
  return(p)
}

# Likelihood function
negLLprospect_gpr_basic <- function(parameters,choiceset,choices) {
  # A negative log likelihood function for a prospect-theory estimation.
  # Assumes parameters are [rho, mu] as used in S-H 2009, 2013, 2015, etc.
  # Assumes choiceset has columns riskyoption1, riskyoption2, and safeoption
  # Assumes choices are binary/logical, with 1 = risky, 0 = safe.
  #
  # Peter Sokol-Hessner
  # July 2026
  
  choiceP = choice_probability(parameters, choiceset);
  
  likelihood = choices * choiceP + (1 - choices) * (1-choiceP);
  likelihood[likelihood == 0] = 0.000000000000001; # 1e-15, i.e. 14 zeros followed by a 1
  
  nll <- -sum(log(likelihood));
  return(nll)
}


### Optimization ----
eps = .Machine$double.eps;
lower_bounds = c(eps, 0); # R, M
upper_bounds = c(2,80);
number_of_parameters = length(lower_bounds);

# Create placeholders for parameters, errors, NLL (and anything else you want)
number_of_iterations = 200; # 100 or more
estimated_parameters = array(dim = c(number_of_clean_subjects, 2, 4));
estimated_parameter_errors = array(dim = c(number_of_clean_subjects, 2, 4));
NLLs = array(dim = c(number_of_clean_subjects,4));

clean_data_dm$all_choiceP = NA;
clean_data_subjlevel_long$rho = NA;
clean_data_subjlevel_long$mu = NA;
clean_data_subjlevel_long$rhoSE = NA;
clean_data_subjlevel_long$muSE = NA;
clean_data_subjlevel_long$nll = NA;

cat('Beginning Optimization\n')

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  cat(paste0('\nSubject ',subj_id,', round 0'))
  
  for (b in 1:4){
    cat(paste0('\b',b))
    
    all_choice_ind = (clean_data_dm$subjectnumber == subj_id) & 
                     (clean_data_dm$roundnumber == b) & 
                     is.finite(clean_data_dm$choice)
    
    tmpdata = clean_data_dm[all_choice_ind,]; # defines this person's data for this block
    
    temp_parameters = array(dim = c(number_of_iterations,number_of_parameters));
    temp_hessians = array(dim = c(number_of_iterations,number_of_parameters,number_of_parameters));
    temp_NLLs = array(dim = c(number_of_iterations,1));
    
    choiceset = as.data.frame(cbind(tmpdata$riskyopt1, tmpdata$riskyopt2, tmpdata$safe));
    colnames(choiceset) <- c('riskyoption1', 'riskyoption2', 'safeoption');
    
    # tic() # start the timer
    
    for(iter in 1:number_of_iterations){
      # Randomly set initial values within supported values
      # using uniformly-distributed values. Many ways to do this!
      
      initial_values = runif(number_of_parameters, min = lower_bounds, max = upper_bounds)
      
      temp_output = optim(initial_values, negLLprospect_gpr_basic,
                          choiceset = choiceset,
                          choices = tmpdata$choice,
                          lower = lower_bounds,
                          upper = upper_bounds,
                          method = "L-BFGS-B",
                          hessian = T)
      
      # Store the output we need access to later
      temp_parameters[iter,] = temp_output$par; # parameter values
      temp_hessians[iter,,] = temp_output$hessian; # SEs
      temp_NLLs[iter,] = temp_output$value; # the NLLs
    }
    
    # Compare output; select the best one
    NLLs[subj, b] = min(temp_NLLs); # the best NLL for this person
    best_ind = which(temp_NLLs == NLLs[subj, b])[1]; # the index of that NLL
    
    estimated_parameters[subj,,b] = temp_parameters[best_ind,] # the parameters
    estimated_parameter_errors[subj,,b] = sqrt(diag(solve(temp_hessians[best_ind,,]))); # the SEs
    
    clean_data_subjlevel_long$rho[(clean_data_subjlevel_long$subjectnumber == subj_id) & 
                                  (clean_data_subjlevel_long$roundnum == b)] = estimated_parameters[subj,1,b]
    clean_data_subjlevel_long$mu[(clean_data_subjlevel_long$subjectnumber == subj_id) & 
                                 (clean_data_subjlevel_long$roundnum == b)] = estimated_parameters[subj,2,b]

    clean_data_subjlevel_long$rhoSE[(clean_data_subjlevel_long$subjectnumber == subj_id) & 
                                    (clean_data_subjlevel_long$roundnum == b)] = estimated_parameter_errors[subj,1,b]
    clean_data_subjlevel_long$muSE[(clean_data_subjlevel_long$subjectnumber == subj_id) & 
                                   (clean_data_subjlevel_long$roundnum == b)] = estimated_parameter_errors[subj,2,b]
    
    clean_data_subjlevel_long$nll[(clean_data_subjlevel_long$subjectnumber == subj_id) & 
                                  (clean_data_subjlevel_long$roundnum == b)] = NLLs[subj, b]
    
    # Calculating all choice probabilities for this participant, given best-fit parameters
    clean_data_dm$all_choiceP[all_choice_ind] = choice_probability(temp_parameters[best_ind,],choiceset);
  }
}
cat('\nDone.\n')

# Vary by condition?
boxplot(rho ~ goallevelP1N1 * bonusatstakeP1N1, data = clean_data_subjlevel_long)
# Looks like low vs. high goals may have a weak effect (higher rho w/ higher goals)?
rho_lmer = lmer(rho ~ 1 + goallevelP1N1 * bonusatstakeP1N1 + (1 | subjectnumber), 
                data = clean_data_subjlevel_long )
summary(rho_lmer)
rho_lm = lm(rho ~ 1 + goallevelP1N1 * bonusatstakeP1N1, 
                data = clean_data_subjlevel_long )
summary(rho_lm)

AIC(rho_lmer) # LOWER/BETTER
AIC(rho_lm)
# Neither model finds any significant effect of goal, bonus, or their interaction
# THOUGH the RFX model finds a trending goal x bonus interaction, p = 0.06
# The interaction would indicate that high goal & bonus pressure raises risk-seeking
# more than either alone would predict. 
#
# POSSIBLE ROLE FOR AN INDIV-DIFF COVARIATE? 

# MAIN INDIVIDUAL DIFFERENCE MEASURES:
# - RRS (overall)
# - BISBAS Ratio (can break down if need be)
# - Bonus (psq_bonus_influence)
# - WMC (best_span_overall)
# - Stress (psq_stress) (can break down into state, trait, and stress)

rho_lm_rrs = lm(rho ~ 1 + goallevelP1N1 * bonusatstakeP1N1 * rrs_overall, 
            data = clean_data_subjlevel_long )
summary(rho_lm_rrs)
# nothing

rho_lm_bisbas_ratio = lm(rho ~ 1 + goallevelP1N1 * bonusatstakeP1N1 * bisbas_ratio, 
                data = clean_data_subjlevel_long )
summary(rho_lm_bisbas_ratio)
# BIS-BAS ratio positively predicts rho

rho_lm_span = lm(rho ~ 1 + goallevelP1N1 * bonusatstakeP1N1 * best_span_overall, 
                data = clean_data_subjlevel_long )
summary(rho_lm_span)
# nothing

rho_lm_stress = lm(rho ~ 1 + goallevelP1N1 * bonusatstakeP1N1 * psq_stress, 
                 data = clean_data_subjlevel_long )
summary(rho_lm_stress)
# nothing

rho_lm_influence = lm(rho ~ 1 + goallevelP1N1 * psq_goal_influence +
                        bonusatstakeP1N1 * psq_bonus_influence, 
                   data = clean_data_subjlevel_long )
summary(rho_lm_influence)
# Bonus influence alone predicts higher rho

rho_lm_round = lm(rho ~ 1 + goallevelP1N1 * bonusatstakeP1N1 * roundnum0123, 
                      data = clean_data_subjlevel_long )
summary(rho_lm_round)
# Round number has a trending (!) neg. effect on rho values. 

# TAKEAWAYS: No individual difference terms interact with goal or bonus levels to change rho.
# There might be weak effects of a) round number, BIS-BAS ratio, or self-reported bonus
# influence (though this as a main effect doesn't make sense...)

# Next step options:
# 1. Modify the model to capture changes in risk attitudes. Changes...
#   ... within round
#   ... across rounds
#   ... after goal attainment (and interactions here w/ goal level?)





# Things We Could Analyze
# 1. proportion risky choices (overall; separate windows; sliding window; with respect to goal attainment)
#      could do with respect to choices before/after goal or dollars before/after goal
# 2. decision times (same as p(risky choices))
# 3. context effects (effect of previous outcomes on subsequent choices)
# 
# Deeper options:
#   - calculate rho on a per block or sub-block level
#   - with rhos, calculate subjective difficulty, and do CGT/CGE/EDI analyses

