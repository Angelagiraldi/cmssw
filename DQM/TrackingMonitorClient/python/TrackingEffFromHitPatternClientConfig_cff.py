import FWCore.ParameterSet.Config as cms

trackingEffFromHitPattern = cms.EDAnalyzer("DQMGenericClient",
                                           subDirs = cms.untracked.vstring(
        "Tracking/TrackParameters/generalTracks/HitEffFromHitPattern*",
        "Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitEffFromHitPattern*",
                                           ),
                                           efficiency = cms.vstring(
        "effic_vs_PU_PXB1 'PXB Layer1 Efficiency vs GoodNumVertices' Hits_valid_PXB_Subdet1 Hits_total_PXB_Subdet1",
        "effic_vs_PU_PXB2 'PXB Layer2 Efficiency vs GoodNumVertices' Hits_valid_PXB_Subdet2 Hits_total_PXB_Subdet2",
        "effic_vs_PU_PXB3 'PXB Layer3 Efficiency vs GoodNumVertices' Hits_valid_PXB_Subdet3 Hits_total_PXB_Subdet3",
        "effic_vs_PU_PXF1 'PXF Layer1 Efficiency vs GoodNumVertices' Hits_valid_PXF_Subdet1 Hits_total_PXF_Subdet1",
        "effic_vs_PU_PXF2 'PXF Layer2 Efficiency vs GoodNumVertices' Hits_valid_PXF_Subdet2 Hits_total_PXF_Subdet2",
        "effic_vs_PU_TIB1 'TIB Layer1 Efficiency vs GoodNumVertices' Hits_valid_TIB_Subdet1 Hits_total_TIB_Subdet1",
        "effic_vs_PU_TIB2 'TIB Layer2 Efficiency vs GoodNumVertices' Hits_valid_TIB_Subdet2 Hits_total_TIB_Subdet2",
        "effic_vs_PU_TIB3 'TIB Layer3 Efficiency vs GoodNumVertices' Hits_valid_TIB_Subdet3 Hits_total_TIB_Subdet3",
        "effic_vs_PU_TIB4 'TIB Layer4 Efficiency vs GoodNumVertices' Hits_valid_TIB_Subdet4 Hits_total_TIB_Subdet4",
        "effic_vs_PU_TOB1 'TOB Layer1 Efficiency vs GoodNumVertices' Hits_valid_TOB_Subdet1 Hits_total_TOB_Subdet1",
        "effic_vs_PU_TOB2 'TOB Layer2 Efficiency vs GoodNumVertices' Hits_valid_TOB_Subdet2 Hits_total_TOB_Subdet2",
        "effic_vs_PU_TOB3 'TOB Layer3 Efficiency vs GoodNumVertices' Hits_valid_TOB_Subdet3 Hits_total_TOB_Subdet3",
        "effic_vs_PU_TOB4 'TOB Layer4 Efficiency vs GoodNumVertices' Hits_valid_TOB_Subdet4 Hits_total_TOB_Subdet4",
        "effic_vs_PU_TOB5 'TOB Layer5 Efficiency vs GoodNumVertices' Hits_valid_TOB_Subdet5 Hits_total_TOB_Subdet5",
        "effic_vs_PU_TOB6 'TOB Layer6 Efficiency vs GoodNumVertices' Hits_valid_TOB_Subdet6 Hits_total_TOB_Subdet6",
        "effic_vs_PU_TID1 'TID Layer1 Efficiency vs GoodNumVertices' Hits_valid_TID_Subdet1 Hits_total_TID_Subdet1",
        "effic_vs_PU_TID2 'TID Layer2 Efficiency vs GoodNumVertices' Hits_valid_TID_Subdet2 Hits_total_TID_Subdet2",
        "effic_vs_PU_TID3 'TID Layer3 Efficiency vs GoodNumVertices' Hits_valid_TID_Subdet3 Hits_total_TID_Subdet3",
        "effic_vs_PU_TEC1 'TEC Layer1 Efficiency vs GoodNumVertices' Hits_valid_TEC_Subdet1 Hits_total_TEC_Subdet1",
        "effic_vs_PU_TEC2 'TEC Layer2 Efficiency vs GoodNumVertices' Hits_valid_TEC_Subdet2 Hits_total_TEC_Subdet2",
        "effic_vs_PU_TEC3 'TEC Layer3 Efficiency vs GoodNumVertices' Hits_valid_TEC_Subdet3 Hits_total_TEC_Subdet3",
        "effic_vs_PU_TEC4 'TEC Layer4 Efficiency vs GoodNumVertices' Hits_valid_TEC_Subdet4 Hits_total_TEC_Subdet4",
        "effic_vs_PU_TEC5 'TEC Layer5 Efficiency vs GoodNumVertices' Hits_valid_TEC_Subdet5 Hits_total_TEC_Subdet5",
        "effic_vs_PU_TEC6 'TEC Layer6 Efficiency vs GoodNumVertices' Hits_valid_TEC_Subdet6 Hits_total_TEC_Subdet6",
        "effic_vs_PU_TEC7 'TEC Layer7 Efficiency vs GoodNumVertices' Hits_valid_TEC_Subdet7 Hits_total_TEC_Subdet7",
        "effic_vs_PU_TEC8 'TEC Layer8 Efficiency vs GoodNumVertices' Hits_valid_TEC_Subdet8 Hits_total_TEC_Subdet8",
        "effic_vs_PU_TEC9 'TEC Layer9 Efficiency vs GoodNumVertices' Hits_valid_TEC_Subdet9 Hits_total_TEC_Subdet9",
        "effic_vs_BX_PXB1 'PXB Layer1 Efficiency vs BX' HitsVsBX_valid_PXB_Subdet1 HitsVsBX_total_PXB_Subdet1",
        "effic_vs_BX_PXB2 'PXB Layer2 Efficiency vs BX' HitsVsBX_valid_PXB_Subdet2 HitsVsBX_total_PXB_Subdet2",
        "effic_vs_BX_PXB3 'PXB Layer3 Efficiency vs BX' HitsVsBX_valid_PXB_Subdet3 HitsVsBX_total_PXB_Subdet3",
        "effic_vs_BX_PXF1 'PXF Layer1 Efficiency vs BX' HitsVsBX_valid_PXF_Subdet1 HitsVsBX_total_PXF_Subdet1",
        "effic_vs_BX_PXF2 'PXF Layer2 Efficiency vs BX' HitsVsBX_valid_PXF_Subdet2 HitsVsBX_total_PXF_Subdet2",
        "effic_vs_BX_TIB1 'TIB Layer1 Efficiency vs BX' HitsVsBX_valid_TIB_Subdet1 HitsVsBX_total_TIB_Subdet1",
        "effic_vs_BX_TIB2 'TIB Layer2 Efficiency vs BX' HitsVsBX_valid_TIB_Subdet2 HitsVsBX_total_TIB_Subdet2",
        "effic_vs_BX_TIB3 'TIB Layer3 Efficiency vs BX' HitsVsBX_valid_TIB_Subdet3 HitsVsBX_total_TIB_Subdet3",
        "effic_vs_BX_TIB4 'TIB Layer4 Efficiency vs BX' HitsVsBX_valid_TIB_Subdet4 HitsVsBX_total_TIB_Subdet4",
        "effic_vs_BX_TOB1 'TOB Layer1 Efficiency vs BX' HitsVsBX_valid_TOB_Subdet1 HitsVsBX_total_TOB_Subdet1",
        "effic_vs_BX_TOB2 'TOB Layer2 Efficiency vs BX' HitsVsBX_valid_TOB_Subdet2 HitsVsBX_total_TOB_Subdet2",
        "effic_vs_BX_TOB3 'TOB Layer3 Efficiency vs BX' HitsVsBX_valid_TOB_Subdet3 HitsVsBX_total_TOB_Subdet3",
        "effic_vs_BX_TOB4 'TOB Layer4 Efficiency vs BX' HitsVsBX_valid_TOB_Subdet4 HitsVsBX_total_TOB_Subdet4",
        "effic_vs_BX_TOB5 'TOB Layer5 Efficiency vs BX' HitsVsBX_valid_TOB_Subdet5 HitsVsBX_total_TOB_Subdet5",
        "effic_vs_BX_TOB6 'TOB Layer6 Efficiency vs BX' HitsVsBX_valid_TOB_Subdet6 HitsVsBX_total_TOB_Subdet6",
        "effic_vs_BX_TID1 'TID Layer1 Efficiency vs BX' HitsVsBX_valid_TID_Subdet1 HitsVsBX_total_TID_Subdet1",
        "effic_vs_BX_TID2 'TID Layer2 Efficiency vs BX' HitsVsBX_valid_TID_Subdet2 HitsVsBX_total_TID_Subdet2",
        "effic_vs_BX_TID3 'TID Layer3 Efficiency vs BX' HitsVsBX_valid_TID_Subdet3 HitsVsBX_total_TID_Subdet3",
        "effic_vs_BX_TEC1 'TEC Layer1 Efficiency vs BX' HitsVsBX_valid_TEC_Subdet1 HitsVsBX_total_TEC_Subdet1",
        "effic_vs_BX_TEC2 'TEC Layer2 Efficiency vs BX' HitsVsBX_valid_TEC_Subdet2 HitsVsBX_total_TEC_Subdet2",
        "effic_vs_BX_TEC3 'TEC Layer3 Efficiency vs BX' HitsVsBX_valid_TEC_Subdet3 HitsVsBX_total_TEC_Subdet3",
        "effic_vs_BX_TEC4 'TEC Layer4 Efficiency vs BX' HitsVsBX_valid_TEC_Subdet4 HitsVsBX_total_TEC_Subdet4",
        "effic_vs_BX_TEC5 'TEC Layer5 Efficiency vs BX' HitsVsBX_valid_TEC_Subdet5 HitsVsBX_total_TEC_Subdet5",
        "effic_vs_BX_TEC6 'TEC Layer6 Efficiency vs BX' HitsVsBX_valid_TEC_Subdet6 HitsVsBX_total_TEC_Subdet6",
        "effic_vs_BX_TEC7 'TEC Layer7 Efficiency vs BX' HitsVsBX_valid_TEC_Subdet7 HitsVsBX_total_TEC_Subdet7",
        "effic_vs_BX_TEC8 'TEC Layer8 Efficiency vs BX' HitsVsBX_valid_TEC_Subdet8 HitsVsBX_total_TEC_Subdet8",
        "effic_vs_BX_TEC9 'TEC Layer9 Efficiency vs BX' HitsVsBX_valid_TEC_Subdet9 HitsVsBX_total_TEC_Subdet9",
        "effic_vs_LUMI_PXB1 'PXB Layer1 Efficiency vs LUMI' HitsVsLUMI_valid_PXB_Subdet1 HitsVsLUMI_total_PXB_Subdet1",
        "effic_vs_LUMI_PXB2 'PXB Layer2 Efficiency vs LUMI' HitsVsLUMI_valid_PXB_Subdet2 HitsVsLUMI_total_PXB_Subdet2",
        "effic_vs_LUMI_PXB3 'PXB Layer3 Efficiency vs LUMI' HitsVsLUMI_valid_PXB_Subdet3 HitsVsLUMI_total_PXB_Subdet3",
        "effic_vs_LUMI_PXF1 'PXF Layer1 Efficiency vs LUMI' HitsVsLUMI_valid_PXF_Subdet1 HitsVsLUMI_total_PXF_Subdet1",
        "effic_vs_LUMI_PXF2 'PXF Layer2 Efficiency vs LUMI' HitsVsLUMI_valid_PXF_Subdet2 HitsVsLUMI_total_PXF_Subdet2",
        "effic_vs_LUMI_TIB1 'TIB Layer1 Efficiency vs LUMI' HitsVsLUMI_valid_TIB_Subdet1 HitsVsLUMI_total_TIB_Subdet1",
        "effic_vs_LUMI_TIB2 'TIB Layer2 Efficiency vs LUMI' HitsVsLUMI_valid_TIB_Subdet2 HitsVsLUMI_total_TIB_Subdet2",
        "effic_vs_LUMI_TIB3 'TIB Layer3 Efficiency vs LUMI' HitsVsLUMI_valid_TIB_Subdet3 HitsVsLUMI_total_TIB_Subdet3",
        "effic_vs_LUMI_TIB4 'TIB Layer4 Efficiency vs LUMI' HitsVsLUMI_valid_TIB_Subdet4 HitsVsLUMI_total_TIB_Subdet4",
        "effic_vs_LUMI_TOB1 'TOB Layer1 Efficiency vs LUMI' HitsVsLUMI_valid_TOB_Subdet1 HitsVsLUMI_total_TOB_Subdet1",
        "effic_vs_LUMI_TOB2 'TOB Layer2 Efficiency vs LUMI' HitsVsLUMI_valid_TOB_Subdet2 HitsVsLUMI_total_TOB_Subdet2",
        "effic_vs_LUMI_TOB3 'TOB Layer3 Efficiency vs LUMI' HitsVsLUMI_valid_TOB_Subdet3 HitsVsLUMI_total_TOB_Subdet3",
        "effic_vs_LUMI_TOB4 'TOB Layer4 Efficiency vs LUMI' HitsVsLUMI_valid_TOB_Subdet4 HitsVsLUMI_total_TOB_Subdet4",
        "effic_vs_LUMI_TOB5 'TOB Layer5 Efficiency vs LUMI' HitsVsLUMI_valid_TOB_Subdet5 HitsVsLUMI_total_TOB_Subdet5",
        "effic_vs_LUMI_TOB6 'TOB Layer6 Efficiency vs LUMI' HitsVsLUMI_valid_TOB_Subdet6 HitsVsLUMI_total_TOB_Subdet6",
        "effic_vs_LUMI_TID1 'TID Layer1 Efficiency vs LUMI' HitsVsLUMI_valid_TID_Subdet1 HitsVsLUMI_total_TID_Subdet1",
        "effic_vs_LUMI_TID2 'TID Layer2 Efficiency vs LUMI' HitsVsLUMI_valid_TID_Subdet2 HitsVsLUMI_total_TID_Subdet2",
        "effic_vs_LUMI_TID3 'TID Layer3 Efficiency vs LUMI' HitsVsLUMI_valid_TID_Subdet3 HitsVsLUMI_total_TID_Subdet3",
        "effic_vs_LUMI_TEC1 'TEC Layer1 Efficiency vs LUMI' HitsVsLUMI_valid_TEC_Subdet1 HitsVsLUMI_total_TEC_Subdet1",
        "effic_vs_LUMI_TEC2 'TEC Layer2 Efficiency vs LUMI' HitsVsLUMI_valid_TEC_Subdet2 HitsVsLUMI_total_TEC_Subdet2",
        "effic_vs_LUMI_TEC3 'TEC Layer3 Efficiency vs LUMI' HitsVsLUMI_valid_TEC_Subdet3 HitsVsLUMI_total_TEC_Subdet3",
        "effic_vs_LUMI_TEC4 'TEC Layer4 Efficiency vs LUMI' HitsVsLUMI_valid_TEC_Subdet4 HitsVsLUMI_total_TEC_Subdet4",
        "effic_vs_LUMI_TEC5 'TEC Layer5 Efficiency vs LUMI' HitsVsLUMI_valid_TEC_Subdet5 HitsVsLUMI_total_TEC_Subdet5",
        "effic_vs_LUMI_TEC6 'TEC Layer6 Efficiency vs LUMI' HitsVsLUMI_valid_TEC_Subdet6 HitsVsLUMI_total_TEC_Subdet6",
        "effic_vs_LUMI_TEC7 'TEC Layer7 Efficiency vs LUMI' HitsVsLUMI_valid_TEC_Subdet7 HitsVsLUMI_total_TEC_Subdet7",
        "effic_vs_LUMI_TEC8 'TEC Layer8 Efficiency vs LUMI' HitsVsLUMI_valid_TEC_Subdet8 HitsVsLUMI_total_TEC_Subdet8",
        "effic_vs_LUMI_TEC9 'TEC Layer9 Efficiency vs LUMI' HitsVsLUMI_valid_TEC_Subdet9 HitsVsLUMI_total_TEC_Subdet9"
        ),
                                           resolution = cms.vstring(),
                                           verbose = cms.untracked.uint32(5),
                                           outputFileName = cms.untracked.string(""),
                                           )
def __extendEfficiencyForPixels(dets):
    """Inject the efficiency computation for the additional layers in the
    PhaseI detectors wrt Run2. The input list is cloned and modified
    rather than updated in place. The substitution add another layer
    by replacing flat '3' -> '4' for the barrel case and '2' -> '3'
    for the forward case.
    """
    from re import match
    ret = []
    for d in dets:
        ret.append(d)
        if match('.*PXB3.*', d):
            ret.append(d.replace('3', '4'))
        elif match('.*PXF2.*', d):
            ret.append(d.replace('2', '3'))
    return ret


# Use additional pixel layers in PhaseI geometry.
from Configuration.Eras.Modifier_trackingPhase1_cff import trackingPhase1
trackingPhase1.toModify(trackingEffFromHitPattern, efficiency = __extendEfficiencyForPixels(trackingEffFromHitPattern.efficiency))
