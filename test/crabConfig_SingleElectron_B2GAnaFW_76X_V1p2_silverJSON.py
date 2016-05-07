from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SemiLepAnaTrees_SingleElectron_B2GAnaFW_76X_V1p2_silverJSON'
config.General.workArea = 'ZprimeAnaRunIISemiLep'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.inputFiles = ['FrameworkJobReport.xml', 'execute_for_crab.py', 'NtupleReader_fwlite.py', 'leptonic_nu_z_component.py', 'JECs', 'ModMass_2015_09_22.root', 'MistagRateBigBins_JetHT_knash_crab_Run2015D_PromptReco_v3_Sep25_v74x_V7_25ns_All_2015_09_28.root', 'pileup_reweight.root']
config.JobType.outputFiles = ['outplots.root']
config.JobType.scriptExe = 'execute_for_crab_semilep_dataTrigger.sh'

config.section_("Data")
config.Data.inputDataset = '/SingleElectron/srappocc-B2GAnaFW_76X_V1p2-c81ddc7ab49f3e61c4d09f98e2992336/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.ignoreLocality = True
config.Data.publication = False
# This string is used to construct the output dataset name

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.whitelist = ["T2_HU_Budapest"]
