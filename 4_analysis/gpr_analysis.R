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

# Effect of goal level as a function of block number:
# 	            1	    2	      3	      4
# low (-1)	-6.0198	1.1629	8.3456	15.5283
# high (+1)	9.5432	5.8839	2.2246	-1.4347





model_goalattainment = glmer(bonusreceived01 ~ 1 + roundnum0123 * bonusatstakeP1N1 * goallevelP1N1 + (1 | subjectnumber), 
                      data = clean_data_subjlevel_long, family = 'binomial')
summary(model_goalattainment)

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
# high goal	0.415447584	0.409338658	0.403257592	0.397206114
# low goal	0.828428437	0.927837762	0.971621927	0.989150849

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


# TODO:
# 1. Check this with EXPECTED EARNINGS instead to eliminate role of chance.
# 3. Look at trials-to-goal (when attained)
# 4. Remove RFX? Do better? Compare to lmer
# 5. somehow..... variance.... ? 
# 6. Calculate model-free, data-derived mean earnings




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

## 3. TRIAL-LEVEL ----
# What happened across trials? 
# Why/how did trial events shape block events? 

