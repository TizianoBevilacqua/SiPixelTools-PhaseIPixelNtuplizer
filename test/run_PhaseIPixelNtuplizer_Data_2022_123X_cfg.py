# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: RECO -s RAW2DIGI,L1Reco,RECO --data --scenario pp --conditions auto:run3_data --era Run3 --process RERECO --eventcontent RECO --datatier RECO --filein dummy.root --secondfilein dummy.root --python_filename=test/run_PhaseIPixelNtuplizer_Data_2022_123X_cfg.py --runUnscheduled -n 10 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('RERECO',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
                    '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/903/00000/0ffbbb9b-6ae3-47cb-8988-64080073c929.root',
                    '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/903/00000/6e861dba-8f40-4093-8fc2-7252e67cf785.root',
                    '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/903/00000/7c27fda0-ba93-4666-8c96-9c6da2fdce4a.root',
                    '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/903/00000/7ff5e0b3-8f5d-4a11-9c86-3f531f9577f5.root',
                    '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/903/00000/b212dbfa-ca14-4848-ad2f-7cf7bdb4b3de.root'
    ),
    secondaryFileNames = cms.untracked.vstring('dummy.root')
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('RECO nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('RECO_RAW2DIGI_L1Reco_RECO.root'),
    outputCommands = process.RECOEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)



















# begin inserting configs
#------------------------------------------
#  Options - can be given from command line
#------------------------------------------
import FWCore.ParameterSet.VarParsing as opts

opt = opts.VarParsing ('analysis')

opt.register('globalTag',          '',
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
	     'Global Tag, Default="" which uses auto:run2_data')

opt.register('dataTier',           'RECO',
             opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
             'Input file data tier')

opt.register('useTemplates',       True,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Only for On-track clusters! True: use Template reco, False: use Generic reco')

opt.register('saveRECO',           False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Option to keep GEN-SIM-RECO')

opt.register('RECOFileName',  '',
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
	     'Name of the RECO output file in case saveRECO was used')

opt.register('inputFileName',   '',
             opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
             'Name of the input root file')

opt.register('secondaryInputFileName',   '',
             opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
             'Name of the RAW (parent) input root file')

opt.register('outputFileName',   'Ntuple.root',
             opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
             'Name of the histograms file')

opt.register('noMagField',         False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test LA (SIM) conditions locally (prep/prod database or sqlite file')

opt.register('useLocalQuality',    False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test Quality conditions locally (prep/prod database or sqlite file')

opt.register('useLocalLA',         False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test LA (RECO) conditions locally (prep/prod database or sqlite file')

opt.register('useLocalGain',       False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test Gain conditions locally (prep/prod database or sqlite file')

opt.register('useLocalGenErr',     False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test GenError conditions locally (prep/prod database or sqlite file')

opt.register('useLocalTemplates',  False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test Template conditions locally (prep/prod database or sqlite file')

opt.register('prescale',           1,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.int,
	     'Save only 1/nth of the events (to conserve disk space for long runs)')

opt.register('loadTagsFromPrep',   '',
             opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
             'Load and use condition(s) from Prep automatically (can specify more if separated by commas, useful for quick validation)')

### Events to process: 'maxEvents' is already registered by the framework
opt.setDefault('maxEvents', 100)

# Proceed with settings from command line
opt.parseArguments()

process.maxEvents.input = opt.maxEvents
process.MessageLogger.cerr.FwkReport.reportEvery = 10

# Switch off magnetic field if needed
if opt.noMagField:
	process.load('Configuration.StandardSequences.MagneticField_0T_cff')

# Set some default options based on others
if opt.RECOFileName == '': opt.RECOFileName = 'file:RECO_'+str(opt.maxEvents)+'.root'
# Input file
if opt.inputFileName == '':
    if opt.dataTier == 'RAW':
        process.source = cms.Source("PoolSource",
                                    fileNames = cms.untracked.vstring(
                                        'file:/data/store/data/Run2016B/ZeroBias/RAW/v2/000/273/158/00000/C62669DA-7418-E611-A8FB-02163E01377A.root' #273158 RAW
                                        )
                                    )
    elif opt.dataTier == 'AOD':
        process.source = cms.Source("PoolSource",
                                    fileNames = cms.untracked.vstring('/store/data/Run2016D/ZeroBias/AOD/PromptReco-v2/000/276/317/00000/12A3F60B-1145-E611-83B1-02163E01431C.root'),
                                    secondaryFileNames = cms.untracked.vstring('/store/data/Run2016D/ZeroBias/RAW/v2/000/276/317/00000/46CDE349-0842-E611-A1F4-02163E012067.root')
                                    )
    else:
        process.source = cms.Source("PoolSource",
                                    fileNames = cms.untracked.vstring(
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/2de686ea-bfd4-4a49-87bc-86434ae4a731.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/3ec20bd7-b98a-42cb-89b7-8b52caeea346.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/61c344df-fa20-4c52-a95d-6ff65e7d384d.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/68711ddd-b556-4211-8f1f-fe1748d983b4.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/718a10e1-075f-4675-82bf-b3870b61d0bf.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/9031a9d9-11ad-490e-bac0-5515b2724f8e.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/97a48c59-c1e8-4325-8904-dc667b51a8b5.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/a09fc8ee-f38e-47cf-9a89-c2304cdf77ff.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/bcb55467-063f-4e79-bce7-67e21d5e4578.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/d2deae3c-34a2-4545-8b83-c06f9200d862.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/d76b29d0-1051-42b0-8c99-1d0f1d24a4b8.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/f3e43475-e461-4416-8621-bda201fc6da7.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/f9422c0a-f0ac-455d-af8f-7d43b5d4fd31.root',
                                        '/store/express/Run2022A/StreamExpress/ALCARECO/SiPixelCalSingleMuon-Express-v1/000/352/909/00000/fe4b96d6-46d4-4af4-892d-2b69dc16ff2e.root',
                                        )
                                    )
else:
    if opt.secondaryInputFileName == '':
        process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring(opt.inputFileName))
    else:
        process.source = cms.Source("PoolSource",
                                    fileNames = cms.untracked.vstring(opt.inputFileName),
                                    secondaryFileNames = cms.untracked.vstring(opt.secondaryInputFileName)
                                    )

# Fix problem with default config
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound'), wantSummary = cms.untracked.bool(True)
)

#________________________________________________________________________
#                        Main Analysis Module

# Refitter
process.load("RecoTracker.MeasurementDet.MeasurementTrackerEventProducer_cfi")
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

# Specify inputs/outputs
if opt.useTemplates:
	process.TrackRefitter.TTRHBuilder = 'WithAngleAndTemplate'
	if opt.outputFileName == '': opt.outputFileName = 'Ntuple_'+str(opt.maxEvents)+'.root'
else:
	process.TrackRefitter.TTRHBuilder = 'WithTrackAngle'
	if opt.outputFileName == '': opt.outputFileName = 'Ntuple_GenericReco_'+str(opt.maxEvents)+'.root'

# Load and confiugre the plugin you want to use
#---------------------------
#  PhaseIPixelNtuplizer
#---------------------------
process.PhaseINtuplizerPlugin = cms.EDAnalyzer("PhaseIPixelNtuplizer",
    trajectoryInput = cms.InputTag('TrackRefitter'),
    outputFileName = cms.untracked.string(opt.outputFileName),
    # Global muon collection
    muonCollection                 = cms.InputTag("muons"),
    keepAllGlobalMuons             = cms.untracked.bool(True),
    keepAllTrackerMuons            = cms.untracked.bool(True),
    # information to save
    eventSaveDownscaleFactor       = cms.untracked.int32(opt.prescale),
    trackSaveDownscaleFactor       = cms.untracked.int32(1),
    clusterSaveDownscaleFactor     = cms.untracked.int32(1),
    saveDigiTree                   = cms.untracked.bool(False),
    saveTrackTree                  = cms.untracked.bool(True),
    saveNonPropagatedExtraTrajTree = cms.untracked.bool(False),
    clusterCollection              = cms.InputTag("siPixelClusters"),
    )

# Switch ALCARECO collections
if opt.dataTier == 'ALCARECO':
    process.MeasurementTrackerEvent.pixelClusterProducer = 'ALCARECOSiPixelCalSingleMuon'
    process.MeasurementTrackerEvent.stripClusterProducer = 'ALCARECOSiPixelCalSingleMuon'
    process.MeasurementTrackerEvent.inactivePixelDetectorLabels = cms.VInputTag()
    process.MeasurementTrackerEvent.inactiveStripDetectorLabels = cms.VInputTag()
    process.TrackRefitter.src = 'ALCARECOSiPixelCalSingleMuon'
    process.TrackRefitter.TrajectoryInEvent = True
    process.PhaseINtuplizerPlugin.clusterCollection = cms.InputTag("ALCARECOSiPixelCalSingleMuon")

# myAnalyzer Path
process.TrackRefitter_step = cms.Path(process.offlineBeamSpot*process.MeasurementTrackerEvent*process.TrackRefitter)
process.PhaseIPixelNtuplizer_step = cms.Path(process.PhaseINtuplizerPlugin)

#________________________________________________________________________
#                        DataBase Stuff

# Print settings
print("Using options: ")
if opt.globalTag == '':
    print("  globalTag (auto:run2_data) = ", str(process.GlobalTag.globaltag))
else:
    if "auto:" in opt.globalTag:
        process.GlobalTag = GlobalTag(process.GlobalTag, opt.globalTag, '')
        print("  globalTag (", opt.globalTag, ") = ",str(process.GlobalTag.globaltag))
    else:
        process.GlobalTag.globaltag = opt.globalTag
        print("  globalTag (manually chosen)            = ",str(process.GlobalTag.globaltag))
print("  dataTier                               = ", str(opt.dataTier))
print("  useTemplates                           = ", str(opt.useTemplates))
print("  saveRECO                               = ", str(opt.saveRECO))
print("  RECOFileName                           = ", str(opt.RECOFileName))
print("  inputFileName                          = ", str(opt.inputFileName))
print("  secondaryInputFileName                 = ", str(opt.secondaryInputFileName))
print("  outputFileName                         = ", str(opt.outputFileName))
print("  noMagField                             = ", str(opt.noMagField))
print("  maxEvents                              = ", str(opt.maxEvents))
print("  useLocalQuality                        = ", str(opt.useLocalQuality))
print("  useLocalLA                             = ", str(opt.useLocalLA))
print("  useLocalGain                           = ", str(opt.useLocalGain))
print("  useLocalGenErr                         = ", str(opt.useLocalGenErr))
print("  useLocalTemplates                      = ", str(opt.useLocalTemplates))
print("  prescale                               = ", str(opt.prescale))

if opt.loadTagsFromPrep != '':
    Rcds = {
        "SiPixelQuality":		   "SiPixelQualityFromDbRcd",
        "SiPixelLorentzAngle":		   "SiPixelLorentzAngleRcd",
        "SiPixelGainCalibration":          "SiPixelGainCalibrationOfflineRcd",
        "SiPixelGenErrorDBObject":	   "SiPixelGenErrorDBObjectRcd",
        "SiPixelTemplateDBObject":	   "SiPixelTemplateDBObjectRcd"
    }
    for cond in str(opt.loadTagsFromPrep).split(','):
        print("Loading condition: ", cond)
        if opt.noMagField and "Template" in cond:
            process.GlobalTag.toGet.append(cms.PSet(
				connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS'),
				record = cms.string(Rcds[cond.split("_")[0]]),
				tag = cms.string(cond),
				label = cms.untracked.string('0T'))
            )
        else:
            process.GlobalTag.toGet.append(cms.PSet(
				connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS'),
				record = cms.string(Rcds[cond.split("_")[0]]),
				tag = cms.string(cond))
            )
else:
    dir   = 'sqlite_file:/afs/cern.ch/user/j/jkarancs/public/DB/Phase1/'
    Danek = 'sqlite_file:/afs/cern.ch/user/d/dkotlins/public/CMSSW/DB/phase1/'
	
        # Test Local DB conditions
        # Quality
        #Qua_db          = 'frontier://FrontierProd/CMS_CONDITIONS'
    Qua_db='frontier://FrontierPrep/CMS_CONDITIONS'
        #Qua_tag         = 'SiPixelQuality_phase1_2017_v1_hltvalidation'
    Qua_tag         = 'SiPixelQuality_phase1_2017_v2' # 2017 May 18 version from Tamas
        
        # Gains
        #Gain_db         = 'frontier://FrontierProd/CMS_CONDITIONS'
    Gain_db         = 'frontier://FrontierPrep/CMS_CONDITIONS'
        #Gain_db         = dir + '2017_05_17/SiPixelGainCalibration_2017_v1_offline.db'
        #Gain_tag        = 'SiPixelGainCalibration_2017_v1_hltvalidation'
    Gain_tag        = 'SiPixelGainCalibration_2017_v4'
        
        # LA (RECO)
        #LA_db           = 'frontier://FrontierProd/CMS_CONDITIONS'
    LA_db           = 'frontier://FrontierPrep/CMS_CONDITIONS'
        # MC
        #LA_db           = dir+'2017_02_13/SiPixelLorentzAngle_phase1_mc_v2.db'
        #LA_tag          = 'SiPixelLorentzAngle_phase1_mc_v2'
        # Data
        #LA_db           = dir+'2017_04_05/SiPixelLorentzAngle_phase1_2017_v1.db'
    LA_tag          = 'SiPixelLorentzAngle_phase1_2017_v4'
        
        # LA (Width)
        #LA_Width_db     = 'frontier://FrontierProd/CMS_CONDITIONS'
        #LA_Width_db     = 'frontier://FrontierPrep/CMS_CONDITIONS'
    LA_Width_db     = dir+'2017_02_13/SiPixelLorentzAngle_forWidth_phase1_mc_v2.db'
    LA_Width_tag    = 'SiPixelLorentzAngle_forWidth_phase1_mc_v2'
        
        # GenErrors
    if opt.noMagField:
        	# 0T GenErrors
        	#GenErr_db       = 'frontier://FrontierProd/CMS_CONDITIONS'
        	#GenErr_db       = 'frontier://FrontierPrep/CMS_CONDITIONS'
        	# MC
        	GenErr_db       = dir+'2017_04_05/SiPixelGenErrorDBObject_phase1_00T_mc_v2.db'
        	GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_00T_mc_v2'
        	# Data
        	#GenErr_db       = dir+'2017_03_20/SiPixelGenErrorDBObject_phase1_00T_2017_v1.db'
        	#GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_00T_2017_v1'
        	
        	# 0T Templates
        	#Templates_db       = 'frontier://FrontierProd/CMS_CONDITIONS'
        	#Templates_db       = 'frontier://FrontierPrep/CMS_CONDITIONS'
        	# MC
        	Templates_db       = dir+'2017_04_05/SiPixelTemplateDBObject_phase1_00T_mc_v2.db'
        	Templates_tag      = 'SiPixelTemplateDBObject_phase1_00T_mc_v2'
        	# Data
        	#Templates_db       = dir+'2017_03_20/SiPixelTemplateDBObject_phase1_00T_2017_v1.db'
        	#Templates_tag      = 'SiPixelTemplateDBObject_phase1_00T_2017_v1'
    else:
        	# 3.8T GenErrors
        	#GenErr_db       = 'frontier://FrontierProd/CMS_CONDITIONS'
        	GenErr_db       = 'frontier://FrontierPrep/CMS_CONDITIONS'
        	# MC
        	#GenErr_db       = dir+'2017_02_13/SiPixelGenErrorDBObject_phase1_38T_mc_v2.db'
        	#GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_38T_mc_v2'
        	# Data
        	#GenErr_db       = dir+'2017_04_05/SiPixelGenErrorDBObject_phase1_38T_2017_v1.db'
        	#GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_38T_2017_v1'
        	#GenErr_db       = dir+'2017_07_06/SiPixelGenErrorDBObject_phase1_38T_2017_v4_bugfix.db'
        	#GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_38T_2017_v4_bugfix'
        	GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_38T_2017_v8'
        	
        	# 3.8T Templates
        	#Templates_db       = 'frontier://FrontierProd/CMS_CONDITIONS'
        	Templates_db       = 'frontier://FrontierPrep/CMS_CONDITIONS'
        	# MC
        	#Templates_db       = dir+'2017_02_13/SiPixelTemplateDBObject_phase1_38T_mc_v2.db'
        	#Templates_tag      = 'SiPixelTemplateDBObject_phase1_38T_mc_v2'
        	# Data
        	#Templates_db       = dir+'2017_04_05/SiPixelTemplateDBObject_phase1_38T_2017_v1.db'
        	#Templates_tag      = 'SiPixelTemplateDBObject_phase1_38T_2017_v1'
        	#Templates_db       = dir+'2017_07_06/SiPixelTemplateDBObject_phase1_38T_2017_v4_bugfix.db'
        	#Templates_tag      = 'SiPixelTemplateDBObject_phase1_38T_2017_v4_bugfix'
        	Templates_tag      = 'SiPixelTemplateDBObject_phase1_38T_2017_v8'
    
    # Quality
    if opt.useLocalQuality :
    	process.QualityReader = cms.ESSource("PoolDBESSource",
    		DBParameters = cms.PSet(
    			messageLevel = cms.untracked.int32(0),
    			authenticationPath = cms.untracked.string('')),
    		toGet = cms.VPSet(cms.PSet(
    			record = cms.string('SiPixelQualityFromDbRcd'),
    			tag = cms.string(Qua_tag))),
    		connect = cms.string(Qua_db))
    	process.es_prefer_QualityReader = cms.ESPrefer("PoolDBESSource","QualityReader")
    
    # for reco
    # LA 
    if opt.useLocalLA :
    	process.LAReader = cms.ESSource("PoolDBESSource",
    		DBParameters = cms.PSet(
    			messageLevel = cms.untracked.int32(0),
    			authenticationPath = cms.untracked.string('')),
    		toGet = cms.VPSet(cms.PSet(
    			record = cms.string("SiPixelLorentzAngleRcd"),
    			tag = cms.string(LA_tag))),
    		connect = cms.string(LA_db))
    	process.LAprefer = cms.ESPrefer("PoolDBESSource","LAReader")
    	# now the forWidth LA
    	process.LAWidthReader = cms.ESSource("PoolDBESSource",
    		DBParameters = cms.PSet(
    			messageLevel = cms.untracked.int32(0),
    			authenticationPath = cms.untracked.string('')),
    		toGet = cms.VPSet(cms.PSet(
    			record = cms.string("SiPixelLorentzAngleRcd"),
    			label = cms.untracked.string("forWidth"),
    			tag = cms.string(LA_Width_tag))),
    		connect = cms.string(LA_Width_db))
    	process.LAWidthprefer = cms.ESPrefer("PoolDBESSource","LAWidthReader")
    
    # Gain 
    if opt.useLocalGain :
    	process.GainsReader = cms.ESSource("PoolDBESSource",
    		DBParameters = cms.PSet(
    			messageLevel = cms.untracked.int32(0),
    			authenticationPath = cms.untracked.string('')),
    		toGet = cms.VPSet(cms.PSet(
    			record = cms.string('SiPixelGainCalibrationOfflineRcd'),
    			tag = cms.string(Gain_tag))),
    		connect = cms.string(Gain_db))
    	process.Gainprefer = cms.ESPrefer("PoolDBESSource","GainsReader")
    
    # GenError
    if opt.useLocalGenErr :
    	process.GenErrReader = cms.ESSource("PoolDBESSource",
    		DBParameters = cms.PSet(
    			messageLevel = cms.untracked.int32(0),
    			authenticationPath = cms.untracked.string('')),
    		toGet = cms.VPSet(cms.PSet(
    			record = cms.string('SiPixelGenErrorDBObjectRcd'),
    			tag = cms.string(GenErr_tag))),
    		connect = cms.string(GenErr_db))
    	process.generrprefer = cms.ESPrefer("PoolDBESSource","GenErrReader")
    
    # Templates
    if opt.useLocalTemplates :
    	process.TemplatesReader = cms.ESSource("PoolDBESSource",
    		DBParameters = cms.PSet(
    			messageLevel = cms.untracked.int32(0),
    			authenticationPath = cms.untracked.string('')),
    		toGet = cms.VPSet(cms.PSet(
    			record = cms.string('SiPixelTemplateDBObjectRcd'),
    			tag = cms.string(Templates_tag))),
    		connect = cms.string(Templates_db))
    	if opt.noMagField:
    		process.TemplatesReader.toGet = cms.VPSet(
    			cms.PSet(
    				label = cms.untracked.string('0T'),
    				record = cms.string('SiPixelTemplateDBObjectRcd'),
    				tag = cms.string(Templates_tag)
    				)
    			)
    	process.templateprefer = cms.ESPrefer("PoolDBESSource","TemplatesReader")

#---------------------------
#  Schedule
#---------------------------

# Modify Schedule
if opt.dataTier == 'RECO' or opt.dataTier == 'FEVT' or opt.dataTier == 'ALCARECO':
    #process.schedule = cms.Schedule(process.myAnalyzer_step)
    process.schedule = cms.Schedule(
	process.TrackRefitter_step,
	process.PhaseIPixelNtuplizer_step,
	process.endjob_step
	)
else:
    if not opt.saveRECO:
        process.schedule.remove(process.RECOoutput_step)
    else:
        process.RECOoutput.fileName = opt.RECOFileName
    # Remove unnecessary steps and add Analyzer in the end of the chain
    process.schedule.remove(process.endjob_step)
    process.schedule.append(process.TrackRefitter_step)
    process.schedule.append(process.PhaseIPixelNtuplizer_step)
    process.schedule.append(process.endjob_step)
# End of inserted code


























# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
