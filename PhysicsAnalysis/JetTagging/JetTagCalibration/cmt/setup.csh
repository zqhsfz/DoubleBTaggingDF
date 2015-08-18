# echo "setup JetTagCalibration JetTagCalibration-00-02-28 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131
endif
source ${CMTROOT}/mgr/setup.csh
set cmtJetTagCalibrationtempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if $status != 0 then
  set cmtJetTagCalibrationtempfile=/tmp/cmt.$$
endif
${CMTROOT}/${CMTBIN}/cmt.exe setup -csh -pack=JetTagCalibration -version=JetTagCalibration-00-02-28 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging  -no_cleanup $* >${cmtJetTagCalibrationtempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/${CMTBIN}/cmt.exe setup -csh -pack=JetTagCalibration -version=JetTagCalibration-00-02-28 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging  -no_cleanup $* >${cmtJetTagCalibrationtempfile}"
  set cmtsetupstatus=2
  /bin/rm -f ${cmtJetTagCalibrationtempfile}
  unset cmtJetTagCalibrationtempfile
  exit $cmtsetupstatus
endif
set cmtsetupstatus=0
source ${cmtJetTagCalibrationtempfile}
if ( $status != 0 ) then
  set cmtsetupstatus=2
endif
/bin/rm -f ${cmtJetTagCalibrationtempfile}
unset cmtJetTagCalibrationtempfile
exit $cmtsetupstatus

