/********************* 
 * Gprdigitspan Test *
 *********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'gprDigitSpan';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from code
psychoJS.start({
  expName,
  expInfo,
  resources: [
    // relative path to index.html
    { name: 'digitSpanTrialNumber.xlsx', path: 'digitSpanTrialNumber.xlsx' },
    { name: 'CGT-choice-set.csv', path: 'CGT-choice-set.csv' },
    { name: 'cgtRDMPractice.xlsx', path: 'cgtRDMPractice.xlsx' },
    { name: 'continue.png', path: 'continue.png' },
    { name: 'digitSpanPractice.xlsx', path: 'digitSpanPractice.xlsx' },
    // absolute path:
    //{ name: 'trialTypes_B.xls', path: 'http://a.website.org/a.path/trialTypes_B.xls' }
  ]
});
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(settingUpRoutineBegin());
flowScheduler.add(settingUpRoutineEachFrame());
flowScheduler.add(settingUpRoutineEnd());
flowScheduler.add(SpanGeneralInstructionsRoutineBegin());
flowScheduler.add(SpanGeneralInstructionsRoutineEachFrame());
flowScheduler.add(SpanGeneralInstructionsRoutineEnd());
flowScheduler.add(SpanReminder1RoutineBegin());
flowScheduler.add(SpanReminder1RoutineEachFrame());
flowScheduler.add(SpanReminder1RoutineEnd());
flowScheduler.add(SpanReminder2RoutineBegin());
flowScheduler.add(SpanReminder2RoutineEachFrame());
flowScheduler.add(SpanReminder2RoutineEnd());
flowScheduler.add(FSInstructionsRoutineBegin());
flowScheduler.add(FSInstructionsRoutineEachFrame());
flowScheduler.add(FSInstructionsRoutineEnd());
const trialFSPracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialFSPracticeLoopBegin(trialFSPracticeLoopScheduler));
flowScheduler.add(trialFSPracticeLoopScheduler);
flowScheduler.add(trialFSPracticeLoopEnd);
flowScheduler.add(StartRealFSRoutineBegin());
flowScheduler.add(StartRealFSRoutineEachFrame());
flowScheduler.add(StartRealFSRoutineEnd());
const trialsFSLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsFSLoopBegin(trialsFSLoopScheduler));
flowScheduler.add(trialsFSLoopScheduler);
flowScheduler.add(trialsFSLoopEnd);
flowScheduler.add(FStoBStransitionRoutineBegin());
flowScheduler.add(FStoBStransitionRoutineEachFrame());
flowScheduler.add(FStoBStransitionRoutineEnd());
flowScheduler.add(InstructionsBSRoutineBegin());
flowScheduler.add(InstructionsBSRoutineEachFrame());
flowScheduler.add(InstructionsBSRoutineEnd());
const trialsPracticeBSLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeBSLoopBegin(trialsPracticeBSLoopScheduler));
flowScheduler.add(trialsPracticeBSLoopScheduler);
flowScheduler.add(trialsPracticeBSLoopEnd);
flowScheduler.add(startRealBSRoutineBegin());
flowScheduler.add(startRealBSRoutineEachFrame());
flowScheduler.add(startRealBSRoutineEnd());
const trialsBSLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsBSLoopBegin(trialsBSLoopScheduler));
flowScheduler.add(trialsBSLoopScheduler);
flowScheduler.add(trialsBSLoopEnd);
flowScheduler.add(ENDRoutineBegin());
flowScheduler.add(ENDRoutineEachFrame());
flowScheduler.add(ENDRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'digitSpanTrialNumber.xlsx', 'path': 'digitSpanTrialNumber.xlsx'},
    {'name': 'continue.png', 'path': 'continue.png'},
    {'name': 'digitSpanPractice.xlsx', 'path': 'digitSpanPractice.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.1';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls(('https://udenver.qualtrics.com/jfe/form/SV_a4qaGzutOwOjcPk?id=' + expInfo['participant']), 'https://du.sona-systems.com');

  return Scheduler.Event.NEXT;
}


var settingUpClock;
var instructionsTextHeight;
var lettersTextHeight;
var wrap;
var SpanGeneralInstructionsClock;
var letterTextHeight;
var GenInsText;
var movealong;
var SpanReminder1Clock;
var Reminder1;
var movealong2;
var SpanReminder2Clock;
var Reminder2;
var movealong3;
var FSInstructionsClock;
var FSGenInsText;
var startPractice;
var ShowNumbersPracticeClock;
var fixation_2;
var pres_text_practice;
var RecallPracticeClock;
var recall_txtPractice;
var textboxPractice;
var cont_buttonPractice;
var mousePractice;
var FeedbackPracticeClock;
var feedbac_textPractice;
var StartRealFSClock;
var praccomplete;
var startFSreal;
var selectNumbersClock;
var ShowNumbersClock;
var fixation;
var presentation_text;
var RecallClock;
var recall_txt;
var textbox;
var cont_button;
var mouse_3;
var FeedbackClock;
var feedback_text;
var FStoBStransitionClock;
var roundTransition;
var moveToBS;
var InstructionsBSClock;
var BSGenInsText;
var startBSprac;
var showNumbersPracticeBSClock;
var fixation_3;
var pres_text_practice_2;
var recallPracticeBSClock;
var recall_txtPractice_2;
var textboxPractice_2;
var cont_buttonPractice_2;
var mousePractice_2;
var feedbackPracticeBSClock;
var feedbac_textPractice_2;
var startRealBSClock;
var praccompleteBS;
var startBSreal;
var selectNumbersBSClock;
var showNumbersBSClock;
var fixationBS;
var presentation_textBS;
var RecallBSClock;
var recall_txtBS;
var textboxBS;
var cont_buttonBS;
var mouseBS;
var FeedbackBSClock;
var feedback_textBS;
var ENDClock;
var ThankYou;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "settingUp"
  settingUpClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  instructionsTextHeight = 0.05;
  lettersTextHeight = 0.1;
  wrap = 1.5;
  
  
  var initITIstatic
  var initITIdynamic
  
  
  
  // Initialize components for Routine "SpanGeneralInstructions"
  SpanGeneralInstructionsClock = new util.Clock();
  // Run 'Begin Experiment' code from setUpTextFormatting_2
  instructionsTextHeight = 0.04;
  letterTextHeight = 0.1;
  wrap = 1.6;
  
  GenInsText = new visual.TextStim({
    win: psychoJS.window,
    name: 'GenInsText',
    text: "In this task you will be asked to memorize a series of numbers and recall them. \n\nYou will do this twice, once recalling the numbers in the order as presented on the screen and once recalling the numbers in the reverse order as presented on the screen. \n\nThere are 14 trials in each direction for a total of 28 trials. \n\nYou will complete 2 practice sets prior to starting each round of this task.\n\nPress 'enter' to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  movealong = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SpanReminder1"
  SpanReminder1Clock = new util.Clock();
  Reminder1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Reminder1',
    text: "Your performance on this task does not affect your compensation. \n\nThis task is supposed to be challenging - you are not expected to nor do you need to remember everything or get everything correct! \n\nPress 'enter' to continue. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  movealong2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SpanReminder2"
  SpanReminder2Clock = new util.Clock();
  Reminder2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Reminder2',
    text: "We are interested in how many digits you can reliably and truthfully recall. \n\nPlease do your best, and do not cheat (e.g. write down or photograph digits). Thank you for completing this task honestly!\n\nPress 'enter' to continue. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  movealong3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FSInstructions"
  FSInstructionsClock = new util.Clock();
  FSGenInsText = new visual.TextStim({
    win: psychoJS.window,
    name: 'FSGenInsText',
    text: 'The practice for the forwards section of this task is up next.\n\nYou will complete two practice trials, each with a list of 3 numbers. \n\nType out your answer when "Recall" appears on the screen using the numbers at the top of the keyboard to type out the numbers in the order they were presented on the screen. \n\nDO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nFor example, if the numbers displayed on the screen are 5 then 7, the correct response is 57.\n\nIf you make a mistake you can use backspace to correct it.  \n\nFeedback will be provided.\n\nPress \'enter\' to begin the practice.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  startPractice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ShowNumbersPractice"
  ShowNumbersPracticeClock = new util.Clock();
  fixation_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  pres_text_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'pres_text_practice',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: letterTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "RecallPractice"
  RecallPracticeClock = new util.Clock();
  recall_txtPractice = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txtPractice',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  textboxPractice = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxPractice',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: letterTextHeight,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  cont_buttonPractice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cont_buttonPractice', units : undefined, 
    image : 'continue.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.4)], size : [0.3, 0.07],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mousePractice = new core.Mouse({
    win: psychoJS.window,
  });
  mousePractice.mouseClock = new util.Clock();
  // Initialize components for Routine "FeedbackPractice"
  FeedbackPracticeClock = new util.Clock();
  feedbac_textPractice = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbac_textPractice',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "StartRealFS"
  StartRealFSClock = new util.Clock();
  praccomplete = new visual.TextStim({
    win: psychoJS.window,
    name: 'praccomplete',
    text: "Practice complete! \n\nYou are about to begin the forwards section of this task. \n\nYou will start with a list of 3 numbers. If you are able to correctly recall the list of numbers, you will continue to larger lists. \n\nDO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nPress 'enter' to start the task.\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  startFSreal = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "selectNumbers"
  selectNumbersClock = new util.Clock();
  // Run 'Begin Experiment' code from selectNumbersFS
  var digitSpan, digitsForTrial, nTrialsFS, correctCount, incorrectCount;
  
  //nTrialsFS = 0;
  // Initialize components for Routine "ShowNumbers"
  ShowNumbersClock = new util.Clock();
  fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  presentation_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'presentation_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: letterTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Recall"
  RecallClock = new util.Clock();
  recall_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txt',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: letterTextHeight,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  cont_button = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cont_button', units : undefined, 
    image : 'continue.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.4)], size : [0.3, 0.07],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "FStoBStransition"
  FStoBStransitionClock = new util.Clock();
  roundTransition = new visual.TextStim({
    win: psychoJS.window,
    name: 'roundTransition',
    text: 'The first round of the letter task is complete!\n\nPress "enter" to continue to the last round.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  moveToBS = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "InstructionsBS"
  InstructionsBSClock = new util.Clock();
  BSGenInsText = new visual.TextStim({
    win: psychoJS.window,
    name: 'BSGenInsText',
    text: 'The practice for the backwards section of this task is up next.\n\nYou will complete two practice trials, each with a list of 2 numbers. \n\nType out your answer when "Recall" appears on the screen using the numbers at the top of the keyboard to type out the numbers in the REVERSE order they were presented on the screen. \n\nFor example, if the numbers presented are 6 then 2, your response should be 26.\n\nPlease DO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nIf you make a mistake you can use backspace to correct it.  \n\nFeedback will be provided.\n\nPress \'enter\' to begin the practice.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  startBSprac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "showNumbersPracticeBS"
  showNumbersPracticeBSClock = new util.Clock();
  fixation_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  pres_text_practice_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'pres_text_practice_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: letterTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "recallPracticeBS"
  recallPracticeBSClock = new util.Clock();
  recall_txtPractice_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txtPractice_2',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  textboxPractice_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxPractice_2',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: letterTextHeight,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  cont_buttonPractice_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cont_buttonPractice_2', units : undefined, 
    image : 'continue.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.4)], size : [0.3, 0.07],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mousePractice_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mousePractice_2.mouseClock = new util.Clock();
  // Initialize components for Routine "feedbackPracticeBS"
  feedbackPracticeBSClock = new util.Clock();
  feedbac_textPractice_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbac_textPractice_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "startRealBS"
  startRealBSClock = new util.Clock();
  praccompleteBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'praccompleteBS',
    text: "Practice complete!\n\nYou are about to begin the backwards section of this task. \n\nYou will start with a list of 2 numbers. If you are able to correctly recall the list of numbers, you will continue to larger lists. \n\nDO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nPress 'enter' to start the task.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  startBSreal = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "selectNumbersBS"
  selectNumbersBSClock = new util.Clock();
  // Run 'Begin Experiment' code from selectNumbersBScode
  var nTrialsBS
  
  //nTrialsBS = 0;
  // Initialize components for Routine "showNumbersBS"
  showNumbersBSClock = new util.Clock();
  fixationBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationBS',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  presentation_textBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'presentation_textBS',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: letterTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "RecallBS"
  RecallBSClock = new util.Clock();
  recall_txtBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txtBS',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  textboxBS = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxBS',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: letterTextHeight,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  cont_buttonBS = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cont_buttonBS', units : undefined, 
    image : 'continue.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.4)], size : [0.3, 0.07],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mouseBS = new core.Mouse({
    win: psychoJS.window,
  });
  mouseBS.mouseClock = new util.Clock();
  // Initialize components for Routine "FeedbackBS"
  FeedbackBSClock = new util.Clock();
  feedback_textBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_textBS',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "END"
  ENDClock = new util.Clock();
  ThankYou = new visual.TextStim({
    win: psychoJS.window,
    name: 'ThankYou',
    text: 'Thank you! You have sucessfully completed the second portion of this study.\n\nYou will now be automatically redirected to Qualtrics.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var settingUpComponents;
function settingUpRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'settingUp' ---
    t = 0;
    settingUpClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    settingUpComponents = [];
    
    for (const thisComponent of settingUpComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function settingUpRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'settingUp' ---
    // get current time
    t = settingUpClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of settingUpComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var initITIstatic;
var initITIdynamic;
function settingUpRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'settingUp' ---
    for (const thisComponent of settingUpComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    function shuffle(array) {
      let currentIndex = array.length,  randomIndex;
    
      // While there remain elements to shuffle.
      while (currentIndex != 0) {
    
        // Pick a remaining element.
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
    
        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
          array[randomIndex], array[currentIndex]];
      }
    
      return array;
    }
    
    // initialize ITIs
    initITIstatic = Array(25).fill([1, 1.5]).flat();
    initITIdynamic = Array(60).fill([1, 1.5]).flat();
    
    // shuffle the ITIs using the function above
    initITIstatic = shuffle(initITIstatic);
    initITIdynamic = shuffle(initITIdynamic);
    
    // save the ITIs
    psychoJS.experiment.addData('initITIstatic', initITIstatic)
    psychoJS.experiment.addData('initITIdynamic', initITIdynamic)
    
    // the Routine "settingUp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _movealong_allKeys;
var SpanGeneralInstructionsComponents;
function SpanGeneralInstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SpanGeneralInstructions' ---
    t = 0;
    SpanGeneralInstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    movealong.keys = undefined;
    movealong.rt = undefined;
    _movealong_allKeys = [];
    // keep track of which components have finished
    SpanGeneralInstructionsComponents = [];
    SpanGeneralInstructionsComponents.push(GenInsText);
    SpanGeneralInstructionsComponents.push(movealong);
    
    for (const thisComponent of SpanGeneralInstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SpanGeneralInstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SpanGeneralInstructions' ---
    // get current time
    t = SpanGeneralInstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *GenInsText* updates
    if (t >= 0.0 && GenInsText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GenInsText.tStart = t;  // (not accounting for frame time here)
      GenInsText.frameNStart = frameN;  // exact frame index
      
      GenInsText.setAutoDraw(true);
    }

    
    // *movealong* updates
    if (t >= 0.0 && movealong.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movealong.tStart = t;  // (not accounting for frame time here)
      movealong.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { movealong.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { movealong.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { movealong.clearEvents(); });
    }

    if (movealong.status === PsychoJS.Status.STARTED) {
      let theseKeys = movealong.getKeys({keyList: ['return'], waitRelease: false});
      _movealong_allKeys = _movealong_allKeys.concat(theseKeys);
      if (_movealong_allKeys.length > 0) {
        movealong.keys = _movealong_allKeys[_movealong_allKeys.length - 1].name;  // just the last key pressed
        movealong.rt = _movealong_allKeys[_movealong_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SpanGeneralInstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SpanGeneralInstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SpanGeneralInstructions' ---
    for (const thisComponent of SpanGeneralInstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(movealong.corr, level);
    }
    psychoJS.experiment.addData('movealong.keys', movealong.keys);
    if (typeof movealong.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('movealong.rt', movealong.rt);
        routineTimer.reset();
        }
    
    movealong.stop();
    // the Routine "SpanGeneralInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _movealong2_allKeys;
var SpanReminder1Components;
function SpanReminder1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SpanReminder1' ---
    t = 0;
    SpanReminder1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    movealong2.keys = undefined;
    movealong2.rt = undefined;
    _movealong2_allKeys = [];
    // keep track of which components have finished
    SpanReminder1Components = [];
    SpanReminder1Components.push(Reminder1);
    SpanReminder1Components.push(movealong2);
    
    for (const thisComponent of SpanReminder1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SpanReminder1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SpanReminder1' ---
    // get current time
    t = SpanReminder1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Reminder1* updates
    if (t >= 0.0 && Reminder1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Reminder1.tStart = t;  // (not accounting for frame time here)
      Reminder1.frameNStart = frameN;  // exact frame index
      
      Reminder1.setAutoDraw(true);
    }

    
    // *movealong2* updates
    if (t >= 0.0 && movealong2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movealong2.tStart = t;  // (not accounting for frame time here)
      movealong2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { movealong2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { movealong2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { movealong2.clearEvents(); });
    }

    if (movealong2.status === PsychoJS.Status.STARTED) {
      let theseKeys = movealong2.getKeys({keyList: ['return'], waitRelease: false});
      _movealong2_allKeys = _movealong2_allKeys.concat(theseKeys);
      if (_movealong2_allKeys.length > 0) {
        movealong2.keys = _movealong2_allKeys[_movealong2_allKeys.length - 1].name;  // just the last key pressed
        movealong2.rt = _movealong2_allKeys[_movealong2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SpanReminder1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SpanReminder1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SpanReminder1' ---
    for (const thisComponent of SpanReminder1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(movealong2.corr, level);
    }
    psychoJS.experiment.addData('movealong2.keys', movealong2.keys);
    if (typeof movealong2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('movealong2.rt', movealong2.rt);
        routineTimer.reset();
        }
    
    movealong2.stop();
    // the Routine "SpanReminder1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _movealong3_allKeys;
var SpanReminder2Components;
function SpanReminder2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SpanReminder2' ---
    t = 0;
    SpanReminder2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    movealong3.keys = undefined;
    movealong3.rt = undefined;
    _movealong3_allKeys = [];
    // keep track of which components have finished
    SpanReminder2Components = [];
    SpanReminder2Components.push(Reminder2);
    SpanReminder2Components.push(movealong3);
    
    for (const thisComponent of SpanReminder2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SpanReminder2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SpanReminder2' ---
    // get current time
    t = SpanReminder2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Reminder2* updates
    if (t >= 0.0 && Reminder2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Reminder2.tStart = t;  // (not accounting for frame time here)
      Reminder2.frameNStart = frameN;  // exact frame index
      
      Reminder2.setAutoDraw(true);
    }

    
    // *movealong3* updates
    if (t >= 0.0 && movealong3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movealong3.tStart = t;  // (not accounting for frame time here)
      movealong3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { movealong3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { movealong3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { movealong3.clearEvents(); });
    }

    if (movealong3.status === PsychoJS.Status.STARTED) {
      let theseKeys = movealong3.getKeys({keyList: ['return'], waitRelease: false});
      _movealong3_allKeys = _movealong3_allKeys.concat(theseKeys);
      if (_movealong3_allKeys.length > 0) {
        movealong3.keys = _movealong3_allKeys[_movealong3_allKeys.length - 1].name;  // just the last key pressed
        movealong3.rt = _movealong3_allKeys[_movealong3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SpanReminder2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SpanReminder2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SpanReminder2' ---
    for (const thisComponent of SpanReminder2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(movealong3.corr, level);
    }
    psychoJS.experiment.addData('movealong3.keys', movealong3.keys);
    if (typeof movealong3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('movealong3.rt', movealong3.rt);
        routineTimer.reset();
        }
    
    movealong3.stop();
    // the Routine "SpanReminder2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startPractice_allKeys;
var FSInstructionsComponents;
function FSInstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FSInstructions' ---
    t = 0;
    FSInstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startPractice.keys = undefined;
    startPractice.rt = undefined;
    _startPractice_allKeys = [];
    // keep track of which components have finished
    FSInstructionsComponents = [];
    FSInstructionsComponents.push(FSGenInsText);
    FSInstructionsComponents.push(startPractice);
    
    for (const thisComponent of FSInstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FSInstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FSInstructions' ---
    // get current time
    t = FSInstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *FSGenInsText* updates
    if (t >= 0.0 && FSGenInsText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FSGenInsText.tStart = t;  // (not accounting for frame time here)
      FSGenInsText.frameNStart = frameN;  // exact frame index
      
      FSGenInsText.setAutoDraw(true);
    }

    
    // *startPractice* updates
    if (t >= 0.0 && startPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startPractice.tStart = t;  // (not accounting for frame time here)
      startPractice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startPractice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startPractice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startPractice.clearEvents(); });
    }

    if (startPractice.status === PsychoJS.Status.STARTED) {
      let theseKeys = startPractice.getKeys({keyList: ['return'], waitRelease: false});
      _startPractice_allKeys = _startPractice_allKeys.concat(theseKeys);
      if (_startPractice_allKeys.length > 0) {
        startPractice.keys = _startPractice_allKeys[_startPractice_allKeys.length - 1].name;  // just the last key pressed
        startPractice.rt = _startPractice_allKeys[_startPractice_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FSInstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FSInstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FSInstructions' ---
    for (const thisComponent of FSInstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startPractice.corr, level);
    }
    psychoJS.experiment.addData('startPractice.keys', startPractice.keys);
    if (typeof startPractice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startPractice.rt', startPractice.rt);
        routineTimer.reset();
        }
    
    startPractice.stop();
    // the Routine "FSInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialFSPractice;
function trialFSPracticeLoopBegin(trialFSPracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialFSPractice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'digitSpanPractice.xlsx',
      seed: undefined, name: 'trialFSPractice'
    });
    psychoJS.experiment.addLoop(trialFSPractice); // add the loop to the experiment
    currentLoop = trialFSPractice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialFSPractice of trialFSPractice) {
      snapshot = trialFSPractice.getSnapshot();
      trialFSPracticeLoopScheduler.add(importConditions(snapshot));
      const DigitLoopPracticeLoopScheduler = new Scheduler(psychoJS);
      trialFSPracticeLoopScheduler.add(DigitLoopPracticeLoopBegin(DigitLoopPracticeLoopScheduler, snapshot));
      trialFSPracticeLoopScheduler.add(DigitLoopPracticeLoopScheduler);
      trialFSPracticeLoopScheduler.add(DigitLoopPracticeLoopEnd);
      trialFSPracticeLoopScheduler.add(RecallPracticeRoutineBegin(snapshot));
      trialFSPracticeLoopScheduler.add(RecallPracticeRoutineEachFrame());
      trialFSPracticeLoopScheduler.add(RecallPracticeRoutineEnd(snapshot));
      trialFSPracticeLoopScheduler.add(FeedbackPracticeRoutineBegin(snapshot));
      trialFSPracticeLoopScheduler.add(FeedbackPracticeRoutineEachFrame());
      trialFSPracticeLoopScheduler.add(FeedbackPracticeRoutineEnd(snapshot));
      trialFSPracticeLoopScheduler.add(trialFSPracticeLoopEndIteration(trialFSPracticeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var DigitLoopPractice;
function DigitLoopPracticeLoopBegin(DigitLoopPracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    DigitLoopPractice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'DigitLoopPractice'
    });
    psychoJS.experiment.addLoop(DigitLoopPractice); // add the loop to the experiment
    currentLoop = DigitLoopPractice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoopPractice of DigitLoopPractice) {
      snapshot = DigitLoopPractice.getSnapshot();
      DigitLoopPracticeLoopScheduler.add(importConditions(snapshot));
      DigitLoopPracticeLoopScheduler.add(ShowNumbersPracticeRoutineBegin(snapshot));
      DigitLoopPracticeLoopScheduler.add(ShowNumbersPracticeRoutineEachFrame());
      DigitLoopPracticeLoopScheduler.add(ShowNumbersPracticeRoutineEnd(snapshot));
      DigitLoopPracticeLoopScheduler.add(DigitLoopPracticeLoopEndIteration(DigitLoopPracticeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function DigitLoopPracticeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(DigitLoopPractice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function DigitLoopPracticeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialFSPracticeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialFSPractice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialFSPracticeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialsFS;
function trialsFSLoopBegin(trialsFSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsFS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'digitSpanTrialNumber.xlsx',
      seed: undefined, name: 'trialsFS'
    });
    psychoJS.experiment.addLoop(trialsFS); // add the loop to the experiment
    currentLoop = trialsFS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsFS of trialsFS) {
      snapshot = trialsFS.getSnapshot();
      trialsFSLoopScheduler.add(importConditions(snapshot));
      trialsFSLoopScheduler.add(selectNumbersRoutineBegin(snapshot));
      trialsFSLoopScheduler.add(selectNumbersRoutineEachFrame());
      trialsFSLoopScheduler.add(selectNumbersRoutineEnd(snapshot));
      const digitLoopLoopScheduler = new Scheduler(psychoJS);
      trialsFSLoopScheduler.add(digitLoopLoopBegin(digitLoopLoopScheduler, snapshot));
      trialsFSLoopScheduler.add(digitLoopLoopScheduler);
      trialsFSLoopScheduler.add(digitLoopLoopEnd);
      trialsFSLoopScheduler.add(RecallRoutineBegin(snapshot));
      trialsFSLoopScheduler.add(RecallRoutineEachFrame());
      trialsFSLoopScheduler.add(RecallRoutineEnd(snapshot));
      trialsFSLoopScheduler.add(FeedbackRoutineBegin(snapshot));
      trialsFSLoopScheduler.add(FeedbackRoutineEachFrame());
      trialsFSLoopScheduler.add(FeedbackRoutineEnd(snapshot));
      trialsFSLoopScheduler.add(trialsFSLoopEndIteration(trialsFSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var digitLoop;
function digitLoopLoopBegin(digitLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    digitLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'digitLoop'
    });
    psychoJS.experiment.addLoop(digitLoop); // add the loop to the experiment
    currentLoop = digitLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoop of digitLoop) {
      snapshot = digitLoop.getSnapshot();
      digitLoopLoopScheduler.add(importConditions(snapshot));
      digitLoopLoopScheduler.add(ShowNumbersRoutineBegin(snapshot));
      digitLoopLoopScheduler.add(ShowNumbersRoutineEachFrame());
      digitLoopLoopScheduler.add(ShowNumbersRoutineEnd(snapshot));
      digitLoopLoopScheduler.add(digitLoopLoopEndIteration(digitLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function digitLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(digitLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function digitLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsFSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsFS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsFSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialsPracticeBS;
function trialsPracticeBSLoopBegin(trialsPracticeBSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsPracticeBS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'digitSpanPractice.xlsx',
      seed: undefined, name: 'trialsPracticeBS'
    });
    psychoJS.experiment.addLoop(trialsPracticeBS); // add the loop to the experiment
    currentLoop = trialsPracticeBS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsPracticeBS of trialsPracticeBS) {
      snapshot = trialsPracticeBS.getSnapshot();
      trialsPracticeBSLoopScheduler.add(importConditions(snapshot));
      const digitLoopPracticeBSLoopScheduler = new Scheduler(psychoJS);
      trialsPracticeBSLoopScheduler.add(digitLoopPracticeBSLoopBegin(digitLoopPracticeBSLoopScheduler, snapshot));
      trialsPracticeBSLoopScheduler.add(digitLoopPracticeBSLoopScheduler);
      trialsPracticeBSLoopScheduler.add(digitLoopPracticeBSLoopEnd);
      trialsPracticeBSLoopScheduler.add(recallPracticeBSRoutineBegin(snapshot));
      trialsPracticeBSLoopScheduler.add(recallPracticeBSRoutineEachFrame());
      trialsPracticeBSLoopScheduler.add(recallPracticeBSRoutineEnd(snapshot));
      trialsPracticeBSLoopScheduler.add(feedbackPracticeBSRoutineBegin(snapshot));
      trialsPracticeBSLoopScheduler.add(feedbackPracticeBSRoutineEachFrame());
      trialsPracticeBSLoopScheduler.add(feedbackPracticeBSRoutineEnd(snapshot));
      trialsPracticeBSLoopScheduler.add(trialsPracticeBSLoopEndIteration(trialsPracticeBSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var digitLoopPracticeBS;
function digitLoopPracticeBSLoopBegin(digitLoopPracticeBSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    digitLoopPracticeBS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'digitLoopPracticeBS'
    });
    psychoJS.experiment.addLoop(digitLoopPracticeBS); // add the loop to the experiment
    currentLoop = digitLoopPracticeBS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoopPracticeBS of digitLoopPracticeBS) {
      snapshot = digitLoopPracticeBS.getSnapshot();
      digitLoopPracticeBSLoopScheduler.add(importConditions(snapshot));
      digitLoopPracticeBSLoopScheduler.add(showNumbersPracticeBSRoutineBegin(snapshot));
      digitLoopPracticeBSLoopScheduler.add(showNumbersPracticeBSRoutineEachFrame());
      digitLoopPracticeBSLoopScheduler.add(showNumbersPracticeBSRoutineEnd(snapshot));
      digitLoopPracticeBSLoopScheduler.add(digitLoopPracticeBSLoopEndIteration(digitLoopPracticeBSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function digitLoopPracticeBSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(digitLoopPracticeBS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function digitLoopPracticeBSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsPracticeBSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsPracticeBS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsPracticeBSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialsBS;
function trialsBSLoopBegin(trialsBSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsBS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'digitSpanTrialNumber.xlsx',
      seed: undefined, name: 'trialsBS'
    });
    psychoJS.experiment.addLoop(trialsBS); // add the loop to the experiment
    currentLoop = trialsBS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsBS of trialsBS) {
      snapshot = trialsBS.getSnapshot();
      trialsBSLoopScheduler.add(importConditions(snapshot));
      trialsBSLoopScheduler.add(selectNumbersBSRoutineBegin(snapshot));
      trialsBSLoopScheduler.add(selectNumbersBSRoutineEachFrame());
      trialsBSLoopScheduler.add(selectNumbersBSRoutineEnd(snapshot));
      const digitLoopBSLoopScheduler = new Scheduler(psychoJS);
      trialsBSLoopScheduler.add(digitLoopBSLoopBegin(digitLoopBSLoopScheduler, snapshot));
      trialsBSLoopScheduler.add(digitLoopBSLoopScheduler);
      trialsBSLoopScheduler.add(digitLoopBSLoopEnd);
      trialsBSLoopScheduler.add(RecallBSRoutineBegin(snapshot));
      trialsBSLoopScheduler.add(RecallBSRoutineEachFrame());
      trialsBSLoopScheduler.add(RecallBSRoutineEnd(snapshot));
      trialsBSLoopScheduler.add(FeedbackBSRoutineBegin(snapshot));
      trialsBSLoopScheduler.add(FeedbackBSRoutineEachFrame());
      trialsBSLoopScheduler.add(FeedbackBSRoutineEnd(snapshot));
      trialsBSLoopScheduler.add(trialsBSLoopEndIteration(trialsBSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var digitLoopBS;
function digitLoopBSLoopBegin(digitLoopBSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    digitLoopBS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'digitLoopBS'
    });
    psychoJS.experiment.addLoop(digitLoopBS); // add the loop to the experiment
    currentLoop = digitLoopBS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoopBS of digitLoopBS) {
      snapshot = digitLoopBS.getSnapshot();
      digitLoopBSLoopScheduler.add(importConditions(snapshot));
      digitLoopBSLoopScheduler.add(showNumbersBSRoutineBegin(snapshot));
      digitLoopBSLoopScheduler.add(showNumbersBSRoutineEachFrame());
      digitLoopBSLoopScheduler.add(showNumbersBSRoutineEnd(snapshot));
      digitLoopBSLoopScheduler.add(digitLoopBSLoopEndIteration(digitLoopBSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function digitLoopBSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(digitLoopBS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function digitLoopBSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsBSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsBS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsBSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var ShowNumbersPracticeComponents;
function ShowNumbersPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ShowNumbersPractice' ---
    t = 0;
    ShowNumbersPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    //console.log(digits)
    
    pres_text_practice.setText(digits.toString()[DigitLoopPractice.thisN]);
    // keep track of which components have finished
    ShowNumbersPracticeComponents = [];
    ShowNumbersPracticeComponents.push(fixation_2);
    ShowNumbersPracticeComponents.push(pres_text_practice);
    
    for (const thisComponent of ShowNumbersPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ShowNumbersPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ShowNumbersPractice' ---
    // get current time
    t = ShowNumbersPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_2* updates
    if (t >= 0.0 && fixation_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_2.tStart = t;  // (not accounting for frame time here)
      fixation_2.frameNStart = frameN;  // exact frame index
      
      fixation_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_2.setAutoDraw(false);
    }
    
    // *pres_text_practice* updates
    if (t >= 1 && pres_text_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pres_text_practice.tStart = t;  // (not accounting for frame time here)
      pres_text_practice.frameNStart = frameN;  // exact frame index
      
      pres_text_practice.setAutoDraw(true);
    }

    frameRemains = 1 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pres_text_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pres_text_practice.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ShowNumbersPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ShowNumbersPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ShowNumbersPractice' ---
    for (const thisComponent of ShowNumbersPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var gotValidClick;
var RecallPracticeComponents;
function RecallPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RecallPractice' ---
    t = 0;
    RecallPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textboxPractice.setText('');
    textboxPractice.refresh();
    // Run 'Begin Routine' code from code_3practice
    new psychoJS.eventManager.Mouse({"visible": true});
    
    // setup some python lists for storing info about the mousePractice
    mousePractice.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from JScodePractice
    // this is a temporary fix to allow editable textbox to be used on several trials
    textboxPractice.refresh()
    // keep track of which components have finished
    RecallPracticeComponents = [];
    RecallPracticeComponents.push(recall_txtPractice);
    RecallPracticeComponents.push(textboxPractice);
    RecallPracticeComponents.push(cont_buttonPractice);
    RecallPracticeComponents.push(mousePractice);
    
    for (const thisComponent of RecallPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function RecallPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RecallPractice' ---
    // get current time
    t = RecallPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txtPractice* updates
    if (t >= 0 && recall_txtPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txtPractice.tStart = t;  // (not accounting for frame time here)
      recall_txtPractice.frameNStart = frameN;  // exact frame index
      
      recall_txtPractice.setAutoDraw(true);
    }

    
    // *textboxPractice* updates
    if (t >= 0 && textboxPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxPractice.tStart = t;  // (not accounting for frame time here)
      textboxPractice.frameNStart = frameN;  // exact frame index
      
      textboxPractice.setAutoDraw(true);
    }

    
    // *cont_buttonPractice* updates
    if (t >= 0 && cont_buttonPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_buttonPractice.tStart = t;  // (not accounting for frame time here)
      cont_buttonPractice.frameNStart = frameN;  // exact frame index
      
      cont_buttonPractice.setAutoDraw(true);
    }

    // *mousePractice* updates
    if (t >= 0 && mousePractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mousePractice.tStart = t;  // (not accounting for frame time here)
      mousePractice.frameNStart = frameN;  // exact frame index
      
      mousePractice.status = PsychoJS.Status.STARTED;
      mousePractice.mouseClock.reset();
      prevButtonState = mousePractice.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mousePractice.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mousePractice.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_buttonPractice]) {
            if (obj.contains(mousePractice)) {
              gotValidClick = true;
              mousePractice.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RecallPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correct;
var fbTxt;
var _mouseXYs;
function RecallPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RecallPractice' ---
    for (const thisComponent of RecallPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textboxPractice.text',textboxPractice.text)
    // Run 'End Routine' code from code_3practice
    if ((textboxPractice.text === digits.toString())) {
        correct = 1;
        fbTxt = "Correct!";
    } else {
        correct = 0;
        fbTxt = "Incorrect";
    }
    psychoJS.experiment.addData("correct", correct);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mousePractice.getPos();
    _mouseButtons = mousePractice.getPressed();
    psychoJS.experiment.addData('mousePractice.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mousePractice.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mousePractice.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mousePractice.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mousePractice.rightButton', _mouseButtons[2]);
    if (mousePractice.clicked_name.length > 0) {
      psychoJS.experiment.addData('mousePractice.clicked_name', mousePractice.clicked_name[0]);}
    // the Routine "RecallPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FeedbackPracticeComponents;
function FeedbackPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FeedbackPractice' ---
    t = 0;
    FeedbackPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedbac_textPractice.setText(fbTxt);
    // keep track of which components have finished
    FeedbackPracticeComponents = [];
    FeedbackPracticeComponents.push(feedbac_textPractice);
    
    for (const thisComponent of FeedbackPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FeedbackPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FeedbackPractice' ---
    // get current time
    t = FeedbackPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedbac_textPractice* updates
    if (t >= 0.0 && feedbac_textPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbac_textPractice.tStart = t;  // (not accounting for frame time here)
      feedbac_textPractice.frameNStart = frameN;  // exact frame index
      
      feedbac_textPractice.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedbac_textPractice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbac_textPractice.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FeedbackPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FeedbackPractice' ---
    for (const thisComponent of FeedbackPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startFSreal_allKeys;
var StartRealFSComponents;
function StartRealFSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'StartRealFS' ---
    t = 0;
    StartRealFSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startFSreal.keys = undefined;
    startFSreal.rt = undefined;
    _startFSreal_allKeys = [];
    // keep track of which components have finished
    StartRealFSComponents = [];
    StartRealFSComponents.push(praccomplete);
    StartRealFSComponents.push(startFSreal);
    
    for (const thisComponent of StartRealFSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function StartRealFSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'StartRealFS' ---
    // get current time
    t = StartRealFSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *praccomplete* updates
    if (t >= 0.0 && praccomplete.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      praccomplete.tStart = t;  // (not accounting for frame time here)
      praccomplete.frameNStart = frameN;  // exact frame index
      
      praccomplete.setAutoDraw(true);
    }

    
    // *startFSreal* updates
    if (t >= 0.0 && startFSreal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startFSreal.tStart = t;  // (not accounting for frame time here)
      startFSreal.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startFSreal.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startFSreal.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startFSreal.clearEvents(); });
    }

    if (startFSreal.status === PsychoJS.Status.STARTED) {
      let theseKeys = startFSreal.getKeys({keyList: ['return'], waitRelease: false});
      _startFSreal_allKeys = _startFSreal_allKeys.concat(theseKeys);
      if (_startFSreal_allKeys.length > 0) {
        startFSreal.keys = _startFSreal_allKeys[_startFSreal_allKeys.length - 1].name;  // just the last key pressed
        startFSreal.rt = _startFSreal_allKeys[_startFSreal_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StartRealFSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StartRealFSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'StartRealFS' ---
    for (const thisComponent of StartRealFSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startFSreal.corr, level);
    }
    psychoJS.experiment.addData('startFSreal.keys', startFSreal.keys);
    if (typeof startFSreal.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startFSreal.rt', startFSreal.rt);
        routineTimer.reset();
        }
    
    startFSreal.stop();
    // the Routine "StartRealFS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var numbersToChoose;
var minDigitFS;
var maxDigitFS;
var nTrialsFS;
var incorrectCount;
var digitSpan;
var digitsForTrial;
var checkingNumbers;
var startN;
var endN;
var selectNumbersComponents;
function selectNumbersRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'selectNumbers' ---
    t = 0;
    selectNumbersClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from selectNumbersFS
    //import * as random from 'random';
    var checkingNumbers, endN, singleNumber, startN, tmpFirst, tmpSecond, numbersToChoose, minDigitFS, maxDigitFS;
    
    numbersToChoose = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    minDigitFS = 3;
    maxDigitFS = 16;
    //correctCount = [];
    //incorrectCount = 0;
    
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    //nTrialsFS += 1;
    //nTrialsFS = nTrialsFS+1;
    
    nTrialsFS = trialsFS.thisN
    //console.log("nTrialsFS:", nTrialsFS)
    
    // make incorrect count 0 on the first trial
    if (nTrialsFS === 0){
        incorrectCount = 0;
    }
    
    if (correctCount === 0) {
        incorrectCount = incorrectCount + 1;
    }
    
    //if ((nTrialsFS === 1)) {
    if (nTrialsFS === 0) {
        digitSpan = minDigitFS;
    } else if (nTrialsFS !== 0) {
        if (correctCount ===1) {
            digitSpan = (digitSpan +1)
            incorrectCount = 0;
        } else if (correctCount === 0 && incorrectCount < 2){
            digitSpan = digitSpan
        } else if (correctCount === 0 && incorrectCount === 2){
            digitSpan = (digitSpan - 1);
            incorrectCount = 0;
        }      
    }
    
    /*
    console.log("digit span:",digitSpan)
    console.log("correct count:", correctCount)
    console.log("incorrectCount:", incorrectCount)
    */
    
    if ((digitSpan < minDigitFS)) {
        digitSpan = minDigitFS;
    }
    
    digitsForTrial = [];
    while ((digitsForTrial.length < digitSpan)) {
        if ((digitSpan <= 9)) {
            singleNumber = random_item(numbersToChoose);
            if ((util.count(digitsForTrial, singleNumber) < 1)) {
                digitsForTrial.push(singleNumber);
            }
        } else {
            if ((digitSpan > 9)) {
                singleNumber = random_item(numbersToChoose);
                if (((digitsForTrial.length < 9) && (util.count(digitsForTrial, singleNumber) === 0))) {
                    digitsForTrial.push(singleNumber);
                }
                if (((digitsForTrial.length >= 9) && (util.count(digitsForTrial, singleNumber) < 2))) {
                    digitsForTrial.push(singleNumber);
                }
            }
        }
    }
    checkingNumbers = true;
    startN = 1;
    endN = (digitsForTrial.length - 1);
    while (checkingNumbers) {
        for (var n, _pj_c = 0, _pj_a = util.range(startN, endN), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            n = _pj_a[_pj_c];
            if (((digitsForTrial[n] === (digitsForTrial[(n - 1)] + 1)) && (digitsForTrial[n] === (digitsForTrial[(n + 1)] - 1)))) {
                tmpFirst = digitsForTrial[n];
                tmpSecond = digitsForTrial[(n - 1)];
                digitsForTrial[n] = tmpSecond;
                digitsForTrial[(n - 1)] = tmpFirst;
            }
            if (((digitsForTrial[n] === (digitsForTrial[(n - 1)] - 1)) && (digitsForTrial[n] === (digitsForTrial[(n + 1)] + 1)))) {
                tmpFirst = digitsForTrial[n];
                tmpSecond = digitsForTrial[(n - 1)];
                digitsForTrial[n] = tmpSecond;
                digitsForTrial[(n - 1)] = tmpFirst;
            }
        }
        checkingNumbers = false;
    }
    
    //console.log(digitSpan)
    //console.log(digitsForTrial)
    // keep track of which components have finished
    selectNumbersComponents = [];
    
    for (const thisComponent of selectNumbersComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function selectNumbersRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'selectNumbers' ---
    // get current time
    t = selectNumbersClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of selectNumbersComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function selectNumbersRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'selectNumbers' ---
    for (const thisComponent of selectNumbersComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "selectNumbers" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var tmpNumber;
var ShowNumbersComponents;
function ShowNumbersRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ShowNumbers' ---
    t = 0;
    ShowNumbersClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from getTmpNumberCodeFS
    var tmpNumber
    tmpNumber = digitsForTrial[digitLoop.thisN];
    
    presentation_text.setText(tmpNumber);
    // keep track of which components have finished
    ShowNumbersComponents = [];
    ShowNumbersComponents.push(fixation);
    ShowNumbersComponents.push(presentation_text);
    
    for (const thisComponent of ShowNumbersComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ShowNumbersRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ShowNumbers' ---
    // get current time
    t = ShowNumbersClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // *presentation_text* updates
    if (t >= 1 && presentation_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presentation_text.tStart = t;  // (not accounting for frame time here)
      presentation_text.frameNStart = frameN;  // exact frame index
      
      presentation_text.setAutoDraw(true);
    }

    frameRemains = 1 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (presentation_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      presentation_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ShowNumbersComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ShowNumbersRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ShowNumbers' ---
    for (const thisComponent of ShowNumbersComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from getTmpNumberCodeFS
    psychoJS.experiment.addData("digitsForTrial", digitsForTrial);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RecallComponents;
function RecallRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Recall' ---
    t = 0;
    RecallClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textbox.setText('');
    textbox.refresh();
    // setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from JScode
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    RecallComponents = [];
    RecallComponents.push(recall_txt);
    RecallComponents.push(textbox);
    RecallComponents.push(cont_button);
    RecallComponents.push(mouse_3);
    
    for (const thisComponent of RecallComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RecallRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Recall' ---
    // get current time
    t = RecallClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txt* updates
    if (t >= 0 && recall_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txt.tStart = t;  // (not accounting for frame time here)
      recall_txt.frameNStart = frameN;  // exact frame index
      
      recall_txt.setAutoDraw(true);
    }

    
    // *textbox* updates
    if (t >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }

    
    // *cont_button* updates
    if (t >= 0.0 && cont_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_button.tStart = t;  // (not accounting for frame time here)
      cont_button.frameNStart = frameN;  // exact frame index
      
      cont_button.setAutoDraw(true);
    }

    // *mouse_3* updates
    if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      mouse_3.mouseClock.reset();
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_button]) {
            if (obj.contains(mouse_3)) {
              gotValidClick = true;
              mouse_3.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RecallComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correctCount;
function RecallRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Recall' ---
    for (const thisComponent of RecallComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textbox.text',textbox.text)
    // Run 'End Routine' code from code_3
    for (var r, _pj_c = 0, _pj_a = util.range(digitsForTrial.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        r = _pj_a[_pj_c];
        digitsForTrial[r] = digitsForTrial[r].toString();
    }
    digitsForTrial = digitsForTrial.join("");
    if ((textbox.text === digitsForTrial.toString())) {
        correctCount = 1;
        fbTxt = "Correct!";
    } else {
        correctCount = 0;
        fbTxt = "Incorrect";
    }
    psychoJS.experiment.addData("correct", correctCount);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_3.getPos();
    _mouseButtons = mouse_3.getPressed();
    psychoJS.experiment.addData('mouse_3.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_3.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_3.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_3.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_3.rightButton', _mouseButtons[2]);
    if (mouse_3.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name[0]);}
    // the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FeedbackComponents;
function FeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Feedback' ---
    t = 0;
    FeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedback_text.setText(fbTxt);
    // keep track of which components have finished
    FeedbackComponents = [];
    FeedbackComponents.push(feedback_text);
    
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Feedback' ---
    // get current time
    t = FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text* updates
    if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Feedback' ---
    for (const thisComponent of FeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _moveToBS_allKeys;
var FStoBStransitionComponents;
function FStoBStransitionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FStoBStransition' ---
    t = 0;
    FStoBStransitionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    moveToBS.keys = undefined;
    moveToBS.rt = undefined;
    _moveToBS_allKeys = [];
    // keep track of which components have finished
    FStoBStransitionComponents = [];
    FStoBStransitionComponents.push(roundTransition);
    FStoBStransitionComponents.push(moveToBS);
    
    for (const thisComponent of FStoBStransitionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FStoBStransitionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FStoBStransition' ---
    // get current time
    t = FStoBStransitionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *roundTransition* updates
    if (t >= 0.0 && roundTransition.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      roundTransition.tStart = t;  // (not accounting for frame time here)
      roundTransition.frameNStart = frameN;  // exact frame index
      
      roundTransition.setAutoDraw(true);
    }

    
    // *moveToBS* updates
    if (t >= 0.0 && moveToBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      moveToBS.tStart = t;  // (not accounting for frame time here)
      moveToBS.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { moveToBS.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { moveToBS.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { moveToBS.clearEvents(); });
    }

    if (moveToBS.status === PsychoJS.Status.STARTED) {
      let theseKeys = moveToBS.getKeys({keyList: ['return'], waitRelease: false});
      _moveToBS_allKeys = _moveToBS_allKeys.concat(theseKeys);
      if (_moveToBS_allKeys.length > 0) {
        moveToBS.keys = _moveToBS_allKeys[_moveToBS_allKeys.length - 1].name;  // just the last key pressed
        moveToBS.rt = _moveToBS_allKeys[_moveToBS_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FStoBStransitionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FStoBStransitionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FStoBStransition' ---
    for (const thisComponent of FStoBStransitionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(moveToBS.corr, level);
    }
    psychoJS.experiment.addData('moveToBS.keys', moveToBS.keys);
    if (typeof moveToBS.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('moveToBS.rt', moveToBS.rt);
        routineTimer.reset();
        }
    
    moveToBS.stop();
    // the Routine "FStoBStransition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startBSprac_allKeys;
var InstructionsBSComponents;
function InstructionsBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'InstructionsBS' ---
    t = 0;
    InstructionsBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startBSprac.keys = undefined;
    startBSprac.rt = undefined;
    _startBSprac_allKeys = [];
    // keep track of which components have finished
    InstructionsBSComponents = [];
    InstructionsBSComponents.push(BSGenInsText);
    InstructionsBSComponents.push(startBSprac);
    
    for (const thisComponent of InstructionsBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionsBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstructionsBS' ---
    // get current time
    t = InstructionsBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BSGenInsText* updates
    if (t >= 0.0 && BSGenInsText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BSGenInsText.tStart = t;  // (not accounting for frame time here)
      BSGenInsText.frameNStart = frameN;  // exact frame index
      
      BSGenInsText.setAutoDraw(true);
    }

    
    // *startBSprac* updates
    if (t >= 0.0 && startBSprac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startBSprac.tStart = t;  // (not accounting for frame time here)
      startBSprac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startBSprac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startBSprac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startBSprac.clearEvents(); });
    }

    if (startBSprac.status === PsychoJS.Status.STARTED) {
      let theseKeys = startBSprac.getKeys({keyList: ['return'], waitRelease: false});
      _startBSprac_allKeys = _startBSprac_allKeys.concat(theseKeys);
      if (_startBSprac_allKeys.length > 0) {
        startBSprac.keys = _startBSprac_allKeys[_startBSprac_allKeys.length - 1].name;  // just the last key pressed
        startBSprac.rt = _startBSprac_allKeys[_startBSprac_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstructionsBS' ---
    for (const thisComponent of InstructionsBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startBSprac.corr, level);
    }
    psychoJS.experiment.addData('startBSprac.keys', startBSprac.keys);
    if (typeof startBSprac.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startBSprac.rt', startBSprac.rt);
        routineTimer.reset();
        }
    
    startBSprac.stop();
    // the Routine "InstructionsBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var showNumbersPracticeBSComponents;
function showNumbersPracticeBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'showNumbersPracticeBS' ---
    t = 0;
    showNumbersPracticeBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    pres_text_practice_2.setText(digitsReverse.toString()[digitLoopPracticeBS.thisN]);
    // keep track of which components have finished
    showNumbersPracticeBSComponents = [];
    showNumbersPracticeBSComponents.push(fixation_3);
    showNumbersPracticeBSComponents.push(pres_text_practice_2);
    
    for (const thisComponent of showNumbersPracticeBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function showNumbersPracticeBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'showNumbersPracticeBS' ---
    // get current time
    t = showNumbersPracticeBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_3* updates
    if (t >= 0.0 && fixation_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_3.tStart = t;  // (not accounting for frame time here)
      fixation_3.frameNStart = frameN;  // exact frame index
      
      fixation_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_3.setAutoDraw(false);
    }
    
    // *pres_text_practice_2* updates
    if (t >= 1 && pres_text_practice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pres_text_practice_2.tStart = t;  // (not accounting for frame time here)
      pres_text_practice_2.frameNStart = frameN;  // exact frame index
      
      pres_text_practice_2.setAutoDraw(true);
    }

    frameRemains = 1 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pres_text_practice_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pres_text_practice_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of showNumbersPracticeBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function showNumbersPracticeBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'showNumbersPracticeBS' ---
    for (const thisComponent of showNumbersPracticeBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var recallPracticeBSComponents;
function recallPracticeBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'recallPracticeBS' ---
    t = 0;
    recallPracticeBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textboxPractice_2.setText('');
    textboxPractice_2.refresh();
    // setup some python lists for storing info about the mousePractice_2
    mousePractice_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from JScodePractice_2
    // this is a temporary fix to allow editable textbox to be used on several trials
    textboxPractice_2.refresh()
    // keep track of which components have finished
    recallPracticeBSComponents = [];
    recallPracticeBSComponents.push(recall_txtPractice_2);
    recallPracticeBSComponents.push(textboxPractice_2);
    recallPracticeBSComponents.push(cont_buttonPractice_2);
    recallPracticeBSComponents.push(mousePractice_2);
    
    for (const thisComponent of recallPracticeBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function recallPracticeBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'recallPracticeBS' ---
    // get current time
    t = recallPracticeBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txtPractice_2* updates
    if (t >= 0 && recall_txtPractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txtPractice_2.tStart = t;  // (not accounting for frame time here)
      recall_txtPractice_2.frameNStart = frameN;  // exact frame index
      
      recall_txtPractice_2.setAutoDraw(true);
    }

    
    // *textboxPractice_2* updates
    if (t >= 0.0 && textboxPractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxPractice_2.tStart = t;  // (not accounting for frame time here)
      textboxPractice_2.frameNStart = frameN;  // exact frame index
      
      textboxPractice_2.setAutoDraw(true);
    }

    
    // *cont_buttonPractice_2* updates
    if (t >= 0.0 && cont_buttonPractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_buttonPractice_2.tStart = t;  // (not accounting for frame time here)
      cont_buttonPractice_2.frameNStart = frameN;  // exact frame index
      
      cont_buttonPractice_2.setAutoDraw(true);
    }

    // *mousePractice_2* updates
    if (t >= 0.0 && mousePractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mousePractice_2.tStart = t;  // (not accounting for frame time here)
      mousePractice_2.frameNStart = frameN;  // exact frame index
      
      mousePractice_2.status = PsychoJS.Status.STARTED;
      mousePractice_2.mouseClock.reset();
      prevButtonState = mousePractice_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mousePractice_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mousePractice_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_buttonPractice_2]) {
            if (obj.contains(mousePractice_2)) {
              gotValidClick = true;
              mousePractice_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of recallPracticeBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function recallPracticeBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'recallPracticeBS' ---
    for (const thisComponent of recallPracticeBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textboxPractice_2.text',textboxPractice_2.text)
    // Run 'End Routine' code from code_3practice_2
    if ((textboxPractice_2.text === digitsReverseCorrAnswer.toString())) {
        correct = 1;
        fbTxt = "Correct!";
    } else {
        correct = 0;
        fbTxt = "Incorrect";
    }
    psychoJS.experiment.addData("correct", correct);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mousePractice_2.getPos();
    _mouseButtons = mousePractice_2.getPressed();
    psychoJS.experiment.addData('mousePractice_2.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mousePractice_2.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mousePractice_2.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mousePractice_2.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mousePractice_2.rightButton', _mouseButtons[2]);
    if (mousePractice_2.clicked_name.length > 0) {
      psychoJS.experiment.addData('mousePractice_2.clicked_name', mousePractice_2.clicked_name[0]);}
    // the Routine "recallPracticeBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbackPracticeBSComponents;
function feedbackPracticeBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedbackPracticeBS' ---
    t = 0;
    feedbackPracticeBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedbac_textPractice_2.setText(fbTxt);
    // keep track of which components have finished
    feedbackPracticeBSComponents = [];
    feedbackPracticeBSComponents.push(feedbac_textPractice_2);
    
    for (const thisComponent of feedbackPracticeBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackPracticeBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedbackPracticeBS' ---
    // get current time
    t = feedbackPracticeBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedbac_textPractice_2* updates
    if (t >= 0.0 && feedbac_textPractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbac_textPractice_2.tStart = t;  // (not accounting for frame time here)
      feedbac_textPractice_2.frameNStart = frameN;  // exact frame index
      
      feedbac_textPractice_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedbac_textPractice_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbac_textPractice_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackPracticeBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackPracticeBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedbackPracticeBS' ---
    for (const thisComponent of feedbackPracticeBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startBSreal_allKeys;
var startRealBSComponents;
function startRealBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'startRealBS' ---
    t = 0;
    startRealBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startBSreal.keys = undefined;
    startBSreal.rt = undefined;
    _startBSreal_allKeys = [];
    // keep track of which components have finished
    startRealBSComponents = [];
    startRealBSComponents.push(praccompleteBS);
    startRealBSComponents.push(startBSreal);
    
    for (const thisComponent of startRealBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function startRealBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'startRealBS' ---
    // get current time
    t = startRealBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *praccompleteBS* updates
    if (t >= 0.0 && praccompleteBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      praccompleteBS.tStart = t;  // (not accounting for frame time here)
      praccompleteBS.frameNStart = frameN;  // exact frame index
      
      praccompleteBS.setAutoDraw(true);
    }

    
    // *startBSreal* updates
    if (t >= 0.0 && startBSreal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startBSreal.tStart = t;  // (not accounting for frame time here)
      startBSreal.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startBSreal.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startBSreal.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startBSreal.clearEvents(); });
    }

    if (startBSreal.status === PsychoJS.Status.STARTED) {
      let theseKeys = startBSreal.getKeys({keyList: ['return'], waitRelease: false});
      _startBSreal_allKeys = _startBSreal_allKeys.concat(theseKeys);
      if (_startBSreal_allKeys.length > 0) {
        startBSreal.keys = _startBSreal_allKeys[_startBSreal_allKeys.length - 1].name;  // just the last key pressed
        startBSreal.rt = _startBSreal_allKeys[_startBSreal_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of startRealBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startRealBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'startRealBS' ---
    for (const thisComponent of startRealBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startBSreal.corr, level);
    }
    psychoJS.experiment.addData('startBSreal.keys', startBSreal.keys);
    if (typeof startBSreal.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startBSreal.rt', startBSreal.rt);
        routineTimer.reset();
        }
    
    startBSreal.stop();
    // the Routine "startRealBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var minDigitBS;
var maxDigitBS;
var nTrialsBS;
var selectNumbersBSComponents;
function selectNumbersBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'selectNumbersBS' ---
    t = 0;
    selectNumbersBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from selectNumbersBScode
    //import * as random from 'random';
    var checkingNumbers,endN, singleNumber, startN, tmpFirst, tmpSecond, numbersToChoose, minDigitBS, maxDigitBS
    
    numbersToChoose = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    minDigitBS = 2;
    maxDigitBS = 15;
    //correct = [];
    //incorrectCount = 0;
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    
    
    //nTrialsBS += 1;
    nTrialsBS = trialsBS.thisN
    //console.log("nTrialsBS:", nTrialsBS)
    
    // reset incorrect count on the first trial
    if (nTrialsBS ===0) {
        incorrectCount = 0
        correctCount = Math.nan
    }
    
    if (correctCount === 0) {
        incorrectCount = incorrectCount + 1;
    }
    
    if (nTrialsBS === 0) {
        //correctCount = 0;
        digitSpan = minDigitBS;
    } else if (nTrialsBS !==0){
        if (correctCount ===1){
            digitSpan = (digitSpan + 1);
            incorrectCount = 0;
        } else if (correctCount === 0 && incorrectCount < 2) {
            digitSpan = digitSpan;
        } else if (correctCount === 0 && incorrectCount === 2) {
            digitSpan = (digitSpan - 1);
            incorrectCount = 0;
        }
    }
    
    /*
    console.log("digit span:",digitSpan)
    console.log("correct count:", correctCount)
    console.log("incorrectCount:", incorrectCount)
    */
    
    if (digitSpan < minDigitBS) {
        digitSpan = minDigitBS;
    }
    
    digitsForTrial = [];
    while ((digitsForTrial.length < digitSpan)) {
        if ((digitSpan <= 9)) {
            singleNumber = random_item(numbersToChoose);
            if ((util.count(digitsForTrial, singleNumber) < 1)) {
                digitsForTrial.push(singleNumber);
            }
        } else {
            if ((digitSpan > 9)) {
                singleNumber = random_item(numbersToChoose);
                if (((digitsForTrial.length < 9) && (util.count(digitsForTrial, singleNumber) === 0))) {
                    digitsForTrial.push(singleNumber);
                }
                if (((digitsForTrial.length >= 9) && (util.count(digitsForTrial, singleNumber) < 2))) {
                    digitsForTrial.push(singleNumber);
                }
            }
        }
    }
    checkingNumbers = true;
    startN = 1;
    endN = (digitsForTrial.length - 1);
    while (checkingNumbers) {
        for (var n, _pj_c = 0, _pj_a = util.range(startN, endN), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            n = _pj_a[_pj_c];
            if (((digitsForTrial[n] === (digitsForTrial[(n - 1)] + 1)) && (digitsForTrial[n] === (digitsForTrial[(n + 1)] - 1)))) {
                tmpFirst = digitsForTrial[n];
                tmpSecond = digitsForTrial[(n - 1)];
                digitsForTrial[n] = tmpSecond;
                digitsForTrial[(n - 1)] = tmpFirst;
            }
            if (((digitsForTrial[n] === (digitsForTrial[(n - 1)] - 1)) && (digitsForTrial[n] === (digitsForTrial[(n + 1)] + 1)))) {
                tmpFirst = digitsForTrial[n];
                tmpSecond = digitsForTrial[(n - 1)];
                digitsForTrial[n] = tmpSecond;
                digitsForTrial[(n - 1)] = tmpFirst;
            }
        }
        checkingNumbers = false;
    }
    
    //console.log("digitSpan:", digitSpan)
    //console.log("digitSpan:", digitsForTrial)
    // keep track of which components have finished
    selectNumbersBSComponents = [];
    
    for (const thisComponent of selectNumbersBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function selectNumbersBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'selectNumbersBS' ---
    // get current time
    t = selectNumbersBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of selectNumbersBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function selectNumbersBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'selectNumbersBS' ---
    for (const thisComponent of selectNumbersBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "selectNumbersBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var showNumbersBSComponents;
function showNumbersBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'showNumbersBS' ---
    t = 0;
    showNumbersBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from getTmpNumberCodeBS
    tmpNumber = digitsForTrial[digitLoopBS.thisN];
    
    presentation_textBS.setText(tmpNumber);
    // keep track of which components have finished
    showNumbersBSComponents = [];
    showNumbersBSComponents.push(fixationBS);
    showNumbersBSComponents.push(presentation_textBS);
    
    for (const thisComponent of showNumbersBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function showNumbersBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'showNumbersBS' ---
    // get current time
    t = showNumbersBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixationBS* updates
    if (t >= 0.0 && fixationBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationBS.tStart = t;  // (not accounting for frame time here)
      fixationBS.frameNStart = frameN;  // exact frame index
      
      fixationBS.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixationBS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationBS.setAutoDraw(false);
    }
    
    // *presentation_textBS* updates
    if (t >= 1 && presentation_textBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presentation_textBS.tStart = t;  // (not accounting for frame time here)
      presentation_textBS.frameNStart = frameN;  // exact frame index
      
      presentation_textBS.setAutoDraw(true);
    }

    frameRemains = 1 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (presentation_textBS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      presentation_textBS.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of showNumbersBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function showNumbersBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'showNumbersBS' ---
    for (const thisComponent of showNumbersBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from getTmpNumberCodeBS
    psychoJS.experiment.addData("digitsForTrial", digitsForTrial);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RecallBSComponents;
function RecallBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RecallBS' ---
    t = 0;
    RecallBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textboxBS.setText('');
    textboxBS.refresh();
    // setup some python lists for storing info about the mouseBS
    mouseBS.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from JScode_BS
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    RecallBSComponents = [];
    RecallBSComponents.push(recall_txtBS);
    RecallBSComponents.push(textboxBS);
    RecallBSComponents.push(cont_buttonBS);
    RecallBSComponents.push(mouseBS);
    
    for (const thisComponent of RecallBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RecallBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RecallBS' ---
    // get current time
    t = RecallBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txtBS* updates
    if (t >= 0 && recall_txtBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txtBS.tStart = t;  // (not accounting for frame time here)
      recall_txtBS.frameNStart = frameN;  // exact frame index
      
      recall_txtBS.setAutoDraw(true);
    }

    
    // *textboxBS* updates
    if (t >= 0.0 && textboxBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxBS.tStart = t;  // (not accounting for frame time here)
      textboxBS.frameNStart = frameN;  // exact frame index
      
      textboxBS.setAutoDraw(true);
    }

    
    // *cont_buttonBS* updates
    if (t >= 0.0 && cont_buttonBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_buttonBS.tStart = t;  // (not accounting for frame time here)
      cont_buttonBS.frameNStart = frameN;  // exact frame index
      
      cont_buttonBS.setAutoDraw(true);
    }

    // *mouseBS* updates
    if (t >= 0.0 && mouseBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseBS.tStart = t;  // (not accounting for frame time here)
      mouseBS.frameNStart = frameN;  // exact frame index
      
      mouseBS.status = PsychoJS.Status.STARTED;
      mouseBS.mouseClock.reset();
      prevButtonState = mouseBS.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseBS.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseBS.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_buttonBS]) {
            if (obj.contains(mouseBS)) {
              gotValidClick = true;
              mouseBS.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RecallBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RecallBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RecallBS' ---
    for (const thisComponent of RecallBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textboxBS.text',textboxBS.text)
    // Run 'End Routine' code from code_3BS
    function reversed(x) {
        var revList;
        revList = [];
        for (var i = 0, _pj_a = x.length; (i < _pj_a); i += 1) {
            revList.push(x[((x.length - 1) - i)]);
        }
        return revList;
    }
    
    digitsForTrial = reversed(digitsForTrial)
    //console.log("reversed digits:", digitsForTrial)
    
    for (var r, _pj_c = 0, _pj_a = util.range(digitsForTrial.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        r = _pj_a[_pj_c];
        digitsForTrial[r] = digitsForTrial[r].toString();
    }
    digitsForTrial = digitsForTrial.join("");
    if ((textboxBS.text === digitsForTrial.toString())) {
        correctCount = 1;
        fbTxt = "Correct!";
    } else {
        correctCount = 0;
        fbTxt = "Incorrect";
    }
    psychoJS.experiment.addData("correct", correctCount);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouseBS.getPos();
    _mouseButtons = mouseBS.getPressed();
    psychoJS.experiment.addData('mouseBS.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouseBS.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouseBS.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouseBS.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouseBS.rightButton', _mouseButtons[2]);
    if (mouseBS.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouseBS.clicked_name', mouseBS.clicked_name[0]);}
    // the Routine "RecallBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FeedbackBSComponents;
function FeedbackBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FeedbackBS' ---
    t = 0;
    FeedbackBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedback_textBS.setText(fbTxt);
    // keep track of which components have finished
    FeedbackBSComponents = [];
    FeedbackBSComponents.push(feedback_textBS);
    
    for (const thisComponent of FeedbackBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FeedbackBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FeedbackBS' ---
    // get current time
    t = FeedbackBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_textBS* updates
    if (t >= 0.0 && feedback_textBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_textBS.tStart = t;  // (not accounting for frame time here)
      feedback_textBS.frameNStart = frameN;  // exact frame index
      
      feedback_textBS.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_textBS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_textBS.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FeedbackBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FeedbackBS' ---
    for (const thisComponent of FeedbackBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ENDComponents;
function ENDRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'END' ---
    t = 0;
    ENDClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ENDComponents = [];
    ENDComponents.push(ThankYou);
    
    for (const thisComponent of ENDComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ENDRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'END' ---
    // get current time
    t = ENDClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ThankYou* updates
    if (t >= 0.0 && ThankYou.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ThankYou.tStart = t;  // (not accounting for frame time here)
      ThankYou.frameNStart = frameN;  // exact frame index
      
      ThankYou.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ThankYou.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ThankYou.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ENDComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ENDRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'END' ---
    for (const thisComponent of ENDComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  // Run 'End Experiment' code from codeFeedbackReal_dynamic
  psychoJS.experiment.addData("outcomes", outcomes);
  psychoJS.experiment.addData("choices", choices);
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
