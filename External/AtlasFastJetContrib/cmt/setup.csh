# echo "setup AtlasFastJetContrib AtlasFastJetContrib-01-14-01 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/External"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131
endif
source ${CMTROOT}/mgr/setup.csh
set cmtAtlasFastJetContribtempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if $status != 0 then
  set cmtAtlasFastJetContribtempfile=/tmp/cmt.$$
endif
${CMTROOT}/${CMTBIN}/cmt.exe setup -csh -pack=AtlasFastJetContrib -version=AtlasFastJetContrib-01-14-01 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/External  -no_cleanup $* >${cmtAtlasFastJetContribtempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/${CMTBIN}/cmt.exe setup -csh -pack=AtlasFastJetContrib -version=AtlasFastJetContrib-01-14-01 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/External  -no_cleanup $* >${cmtAtlasFastJetContribtempfile}"
  set cmtsetupstatus=2
  /bin/rm -f ${cmtAtlasFastJetContribtempfile}
  unset cmtAtlasFastJetContribtempfile
  exit $cmtsetupstatus
endif
set cmtsetupstatus=0
source ${cmtAtlasFastJetContribtempfile}
if ( $status != 0 ) then
  set cmtsetupstatus=2
endif
/bin/rm -f ${cmtAtlasFastJetContribtempfile}
unset cmtAtlasFastJetContribtempfile
exit $cmtsetupstatus

