# echo "setup JetSubStructureUtils JetSubStructureUtils-00-02-12 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131
endif
source ${CMTROOT}/mgr/setup.csh
set cmtJetSubStructureUtilstempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if $status != 0 then
  set cmtJetSubStructureUtilstempfile=/tmp/cmt.$$
endif
${CMTROOT}/${CMTBIN}/cmt.exe setup -csh -pack=JetSubStructureUtils -version=JetSubStructureUtils-00-02-12 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet  -no_cleanup $* >${cmtJetSubStructureUtilstempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/${CMTBIN}/cmt.exe setup -csh -pack=JetSubStructureUtils -version=JetSubStructureUtils-00-02-12 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet  -no_cleanup $* >${cmtJetSubStructureUtilstempfile}"
  set cmtsetupstatus=2
  /bin/rm -f ${cmtJetSubStructureUtilstempfile}
  unset cmtJetSubStructureUtilstempfile
  exit $cmtsetupstatus
endif
set cmtsetupstatus=0
source ${cmtJetSubStructureUtilstempfile}
if ( $status != 0 ) then
  set cmtsetupstatus=2
endif
/bin/rm -f ${cmtJetSubStructureUtilstempfile}
unset cmtJetSubStructureUtilstempfile
exit $cmtsetupstatus

