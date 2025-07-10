## Risky decision-making task
This README.md includes information about the files included in this directory.


### Task script: [rcsRDMmodule.py](rcsRDMmodule.py)
- The risky decision-making task is coded in python and uses psychopy to execute the task. 
- This script requires several arguments (e.g. sub id, round 1 condition, round 2 condition, directory name and path, etc) that are passed into it by the rcsPrimary.py script in the directory above. The input arguments are described in the script. 
- This script includes reminder screens about the task instructions, practice trials, additional task instructions (act natural/strategy), both rounds of the decision-making task and the post-round questions. 

Outputs 6 files:
 1. rcsPostQ_sub###_YEARMMDD-HHMMSS: responses to post-round questions
 2. rcsRDM_choiceSet_round0_sub###_YEARMMDD-HHMMSS.csv: choice set generated for first round
 3. rcsRDM_choiceSet_round1_sub001_YEARMMDD-HHMMSS.csv: choice set generated for second round
 4. rcsRDM_sub001_YEARMMDD-HHMMSS.csv: includes choice set, choices, outcomes, reaction time, etc for both rounds of the task
 5. rcsRDMpractice_sub###_YEARMMDD-HHMMSS.csv: includes practice trial information (monetary values, choices, outcomes, etc)
 6. rcsTrialOutcome_sub###_YEARMMDD-HHMMSS.csv: includes outcomes selected at the end of each round (rows 1 and 2) and the outcome that was selected to payment (row 3) and the payment amount (row 4; always half of outcome selected)

### Conditions
Participants were randomly assigned to recieve "act natural" or "strategy" instructions prior to each round of the risky decision-making task and were equally likely to receive either instructions leading to four groups: natural-natural, natural-strategy, strategy-strategy, strategy-natural. 

These conditions were assigned by this [script](rcsConditionAssignment.py) and then later updated during data collection by this [script](rcsConditionUpdateFile.py) (to balance out number of participants in each group on a weekly-ish basis)

Condition files: [original conditions file](rcsConditionsORIGINAL.csv), [fall 2022 updated condition file](rcsConditions.csv) (adjusting for excluded people from the fall), [winter 2023 updated conditions file part 1](rcsConditionsUpdated_Winter_wks1-4.csv) (for evening out groups on a weekly-ish basis and adjusting for excluded condition groups), [winter 2023 updated conditions file part 2](rcsConditionsUpdated_Winter.csv) (for evening out groups on a participant basis (shorter timescale - every 8 people) and adjusting for excluded condition groups)


### Choice set
The [rcsRDMmodule.py](rcsRDMmodule.py) script (this is the script that runs the RDM tasks) calls the choice set function ([here](rcsRDMChoiceSet.py); the thing that actually generates a unique choice set each time its called) prior to starting each round of the task.



### Slider with mouse
Following both rounds of the risky decision-making task, participants respond to two post-round questions using a slider. The [sliderMouse.py script](sliderMouse.py) was used to create and test that slider (and the code is integrated into the rcsRDMmodule.py script)
