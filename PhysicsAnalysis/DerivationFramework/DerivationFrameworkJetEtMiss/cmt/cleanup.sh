# echo "cleanup DerivationFrameworkJetEtMiss DerivationFrameworkJetEtMiss-00-02-56 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework"

if test "${CMTROOT}" = ""; then
  CMTROOT=/cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
cmtDerivationFrameworkJetEtMisstempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if test ! $? = 0 ; then cmtDerivationFrameworkJetEtMisstempfile=/tmp/cmt.$$; fi
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=DerivationFrameworkJetEtMiss -version=DerivationFrameworkJetEtMiss-00-02-56 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework  $* >${cmtDerivationFrameworkJetEtMisstempfile}
if test $? != 0 ; then
  echo >&2 "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=DerivationFrameworkJetEtMiss -version=DerivationFrameworkJetEtMiss-00-02-56 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework  $* >${cmtDerivationFrameworkJetEtMisstempfile}"
  cmtcleanupstatus=2
  /bin/rm -f ${cmtDerivationFrameworkJetEtMisstempfile}
  unset cmtDerivationFrameworkJetEtMisstempfile
  return $cmtcleanupstatus
fi
cmtcleanupstatus=0
. ${cmtDerivationFrameworkJetEtMisstempfile}
if test $? != 0 ; then
  cmtcleanupstatus=2
fi
/bin/rm -f ${cmtDerivationFrameworkJetEtMisstempfile}
unset cmtDerivationFrameworkJetEtMisstempfile
return $cmtcleanupstatus

