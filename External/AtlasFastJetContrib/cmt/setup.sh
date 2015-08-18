# echo "setup AtlasFastJetContrib AtlasFastJetContrib-01-14-01 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/External"

if test "${CMTROOT}" = ""; then
  CMTROOT=/cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
cmtAtlasFastJetContribtempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if test ! $? = 0 ; then cmtAtlasFastJetContribtempfile=/tmp/cmt.$$; fi
${CMTROOT}/${CMTBIN}/cmt.exe setup -sh -pack=AtlasFastJetContrib -version=AtlasFastJetContrib-01-14-01 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/External  -no_cleanup $* >${cmtAtlasFastJetContribtempfile}
if test $? != 0 ; then
  echo >&2 "${CMTROOT}/${CMTBIN}/cmt.exe setup -sh -pack=AtlasFastJetContrib -version=AtlasFastJetContrib-01-14-01 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/External  -no_cleanup $* >${cmtAtlasFastJetContribtempfile}"
  cmtsetupstatus=2
  /bin/rm -f ${cmtAtlasFastJetContribtempfile}
  unset cmtAtlasFastJetContribtempfile
  return $cmtsetupstatus
fi
cmtsetupstatus=0
. ${cmtAtlasFastJetContribtempfile}
if test $? != 0 ; then
  cmtsetupstatus=2
fi
/bin/rm -f ${cmtAtlasFastJetContribtempfile}
unset cmtAtlasFastJetContribtempfile
return $cmtsetupstatus

