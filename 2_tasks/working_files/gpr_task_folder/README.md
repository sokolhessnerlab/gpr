# Study overview
- This study includes two rounds of a risky decision-making task ([python script](./rdmTask/rcsRDMmodule.py)), and two complex span tasks ([operation span script](./ospan/ospanTaskModule.py) and [symmetry span script](./symspan/symSpanTaskModule.py)). 
- Participants were randomly assigned to receive "act natural" or "strategy" instructions prior to each round of the risky decision-making task resulting in four possible groups: natural-natural, natural-strategy, strategy-natural, strategy-strategy. The conditions are listed [here](./rdmTask/rcsConditionsUpdated_Winter.csv) and were determined using these scripts ([older](./rdmTask/rcsConditionAssignment.py), [newer](./rdmTask/rcsConditionUpdateFile.py)). 
- Each round of the risky decision-making task was marked with green (coded as 0) or purple (coded as 1; randomly assigned to each round). This information is also included in the [conditions file](./rdmTask/rcsConditionsUpdated_Winter.csv).
- Each task is in its own directory and the study is run using a primary script that calls the functions for each task.
- Following the computerized task, participants complete post-task questionnaires and this data is currently located on the lab's shared drive (as of 01/11/23 - subject to change upon publication)


### [Primary script](./rcsPrimary.py)
Takes 4 input arguments: 
1. subject ID ("001")
2. isReal (0 = testing; 1 = real)
3. computer (1 = HB macbook, 2= mahimahi, 3 = tofu, 4 = goulash)
4. tasks (1= do all tasks; 2 = do just complex span tasks; 3 = do just symspan task)

Then it pulls condition and color information from the conditions file and passes that information on to the risky decision-making script and the complex span task scripts.

Data is saved by each individual task script (and NOT by the primary script). For example, following the risky decision-making task, the python script saves the RDM data prior to the complex span tasks being called by the primary script. 
  
### [rdmTask directory](./rdmTask/)
- contains materials to run the risky decision-making task including conditions files, choice set generation files, psychopy scripts
### [ospan directory](./ospan/)
- contains materials to run the operation span task including spreadsheets for the math problems and psychopy scripts
### [symspan directory](./symspan)
- contains materials to run the symmetry span task including symmetry images and psychopy scripts

