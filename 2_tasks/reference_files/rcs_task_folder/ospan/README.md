## Operation Span

- Details about this task and the contents of this directory are described here: [operationSpanOutline.md](operationSpanOutline.md)

[Ospan task script](ospanTaskModule.py)
- This script runs the ospan task and takes several input arguments that are passed in from the rcsPrimary.py script. These arguments include subject ID, whether the task is real or for testing (0=testing; 1= real) and directory information which is set by the rcsPrimary.py script depending on the computer being used. 

Outputs 4 files:
1. rcsOSPANletterPractice_ssub###_YYYYMMDD-HHMMSS.csv: output from letter practice (e.g. set size, letters shown, letters recalled, etc)
2. rcsOSPANmathPractice_sub###_YYYYMMDD-HHMMSS.csv: output from math practice (e.g. set size, problems shown, solutions, suggested solutions, etc)
3. rcsOSPANbothPractice_sub###_YYYYMMDD-HHMMSS.csv: output from the letter-math practice (all information listed above and more)
4. rcsOSPANbothReal_sub###_YYYYMMDD-HHMMSS.csv: same as practice but for the real task

