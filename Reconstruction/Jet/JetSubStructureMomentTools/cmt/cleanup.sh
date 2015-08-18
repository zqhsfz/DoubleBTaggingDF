# echo "cleanup JetSubStructureMomentTools JetSubStructureMomentTools-00-01-21 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet"

if test "${CMTROOT}" = ""; then
  CMTROOT=/cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
cmtJetSubStructureMomentToolstempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if test ! $? = 0 ; then cmtJetSubStructureMomentToolstempfile=/tmp/cmt.$$; fi
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=JetSubStructureMomentTools -version=JetSubStructureMomentTools-00-01-21 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet  $* >${cmtJetSubStructureMomentToolstempfile}
if test $? != 0 ; then
  echo >&2 "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=JetSubStructureMomentTools -version=JetSubStructureMomentTools-00-01-21 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet  $* >${cmtJetSubStructureMomentToolstempfile}"
  cmtcleanupstatus=2
  /bin/rm -f ${cmtJetSubStructureMomentToolstempfile}
  unset cmtJetSubStructureMomentToolstempfile
  return $cmtcleanupstatus
fi
cmtcleanupstatus=0
. ${cmtJetSubStructureMomentToolstempfile}
if test $? != 0 ; then
  cmtcleanupstatus=2
fi
/bin/rm -f ${cmtJetSubStructureMomentToolstempfile}
unset cmtJetSubStructureMomentToolstempfile
return $cmtcleanupstatus

