#!/bin/tcsh
##########################################################################
# Script to run PhaseIPixelNtuplizer on RECO data on an lxbatch node.
# It runs a cmsRun on a specified file and moves the output to EOS:
# /store/caf/user/<username>/...
# Make sure to modify USERDIR (and OUTDIR, TSBatch.csh does it automatically)
# on the bottom of the script
#
# Default settings:
# INCOMPLETE, SPLIT 1, Nstrip > 0
#
# Usage:
# source jobscript_RECO.csh [CMSSW version] [GlobalTag] [job number] [/store/...] [Nevent = -1]
# example:
# source jobscript_RECO.csh CMSSW_9_2_0_patch2 92X_dataRun2_Express_v2 0001 /store/...
##########################################################################
echo
echo "--------------------------------------------------------------------------------"
echo "--------------------------------------------------------------------------------"
echo "                          Creating JOB ["$3"]"
echo

if [ $?VO_CMS_SW_DIR ]; then
    source ${VO_CMS_SW_DIR}/cmsset_default.csh
fi
setenv SCRAM_ARCH slc7_amd64_gcc700
cmsrel $1
cd $1/src
cmsenv
git clone https://github.com/TizianoBevilacqua/SiPixelTools-PhaseIPixelNtuplizer.git SiPixelTools/PhaseIPixelNtuplizer
cd SiPixelTools/PhaseIPixelNtuplizer

# output file
set output="Ntuple_"$3".root"

echo
echo "--------------------------------------------------------------------------------"
echo "                                JOB ["$3"] ready"
echo "                                  Compiling..."
echo

scram b -j 4

echo
echo "--------------------------------------------------------------------------------"
echo "                                 Compiling ready"
echo "                               Starting JOB ["$3"]"
echo

if [ $#argv > 4 ]; then
    echo "cmsRun test/run_MyTest_PhaseIPixelNtuplizer_Data_2018_106X_cfg.py globalTag=$2 dataTier=ALCARECO inputFileName=$4 outputFileName=$output maxEvents=$5\n"
    cmsRun test/run_MyTest_PhaseIPixelNtuplizer_Data_2018_106X_cfg.py globalTag=$2 outputFileName=$output inputFileName=$4 maxEvents=$5
else
    echo "cmsRun test/run_MyTest_PhaseIPixelNtuplizer_Data_2018_106X_cfg.py globalTag=$2 dataTier=ALCARECO inputFileName=$4 outputFileName=$output maxEvents=-1\n"
    cmsRun test/run_MyTest_PhaseIPixelNtuplizer_Data_2018_106X_cfg.py globalTag=$2 outputFileName=$output inputFileName=$4 maxEvents=-1
endif

echo
echo "--------------------------------------------------------------------------------"
echo "                               JOB ["$3"] Finished"
echo "                            Writing output to EOS..."
echo

# Copy to Eos
set USERDIR = "t/tbevilac"
set OUTDIR = "pixel_out"
mkdir -p /eos/user/$USERDIR/$OUTDIR
cp $output /eos/user/$USERDIR/$OUTDIR/$output

echo
echo "Output: "
ls -l /eos/user/$USERDIR/$OUTDIR/$output

cd ../../../..
rm -rf $1

echo
echo "--------------------------------------------------------------------------------"
echo "                                 JOB ["$3"] DONE"
echo "--------------------------------------------------------------------------------"
echo "--------------------------------------------------------------------------------"

