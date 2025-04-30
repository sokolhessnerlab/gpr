## Symmetry Span

- Details about this task and the contents of this directory are described here: [symSpanOutline.md](symSpanOutline.md)

### [Symspan task script](symSpanTaskModule.py)
- This script runs the symspan task and takes several input arguments that are passed in from the rcsPrimary.py script. These arguments include subject ID, whether the task is real or for testing (0=testing; 1= real) and directory information which is set by the rcsPrimary.py script depending on the computer being used.

Outputs 4 files:
1. rcsSYMSPANsquarePractice_sub###_YYYYMMDD-HHMMSS.csv: output from red square practice (e.g. set size, location of red square, response, etc)
2. rcsSYMSPANsymmetryPractice_sub###_YYYYMMDD-HHMMSS.csv: output from symmetry practice (e.g. set size, images shown, response, etc)
3. rcsSYMSPANbothPractice_sub###_YYYYMMDD-HHMMSS.csv: output from the symmetry-square practice (all information listed above and more)
4. rcsSYMSPANbothReal_sub###_YYYYMMDD-HHMMSS.csv: same as practice but for the real task
