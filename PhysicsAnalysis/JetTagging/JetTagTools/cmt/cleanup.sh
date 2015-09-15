# echo "cleanup JetTagTools JetTagTools-01-00-54 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging"

if test "${CMTROOT}" = ""; then
  CMTROOT=/cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
cmtJetTagToolstempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if test ! $? = 0 ; then cmtJetTagToolstempfile=/tmp/cmt.$$; fi
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=JetTagTools -version=JetTagTools-01-00-54 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging  $* >${cmtJetTagToolstempfile}
if test $? != 0 ; then
  echo >&2 "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=JetTagTools -version=JetTagTools-01-00-54 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging  $* >${cmtJetTagToolstempfile}"
  cmtcleanupstatus=2
  /bin/rm -f ${cmtJetTagToolstempfile}
  unset cmtJetTagToolstempfile
  return $cmtcleanupstatus
fi
cmtcleanupstatus=0
. ${cmtJetTagToolstempfile}
if test $? != 0 ; then
  cmtcleanupstatus=2
fi
/bin/rm -f ${cmtJetTagToolstempfile}
unset cmtJetTagToolstempfile
return $cmtcleanupstatus

