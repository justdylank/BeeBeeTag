@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ef_emblem_NT.DIG', '')
        Unknown23015(5)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-1, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 80)

@State
def EMB_NT_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ef_emblem_NT', '')
        Unknown23015(5)
    sprite('null', 8)
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 8)
    Unknown3025(-8342273, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 80)

@State
def EMB_NT_AH():

    def upon_IMMEDIATE():
        Unknown1096(1400)
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('ef_emblem_NT', '')
        Unknown23015(5)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-65536, 10)
    sprite('null', 10)
    Unknown3025(-55256, 10)
    sprite('null', 10)
    Unknown3025(-19276, 10)
    sprite('null', 10)
    Unknown3025(-65536, 10)
    sprite('null', 80)

@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('rgef_mc.DIG', 'rgef_mc_motion_000.mmot')
        Unknown4015()
        Unknown21004(224)
        Unknown2054(1)
    sprite('null', 74)

@State
def BackThrow_DashStop():

    def upon_IMMEDIATE():
        Unknown2006()
    sprite('null', 20)
    Unknown8010(100, 1, 1)

@State
def ntef_340():

    def upon_IMMEDIATE():
        Unknown4003('ntef340_wind.DIG', '')
        Unknown3032()
        Unknown2054(1)
        Unknown21010(1)
        teleportRelativeX(150000)
        Unknown1007(-42500)
        physicsXImpulse(-3000)
        Unknown1057(350)
        Unknown3001(130)
    sprite('vr_nt340_00', 4)
    GFX_1('ntef_340_gsmoke', 0)
    GFX_1('ntef_340_gsmoke', 1)
    GFX_1('ntef_340_add', 2)
    sprite('vr_nt340_01', 8)
    sprite('vr_nt340_02', 4)
    GFX_1('ntef_340_gsmoke', 0)
    GFX_1('ntef_340_gsmoke', 1)
    sprite('vr_nt340_03', 4)
    Unknown3004(-7)
    sprite('vr_nt340_04', 4)
    sprite('vr_nt340_05', 4)

@State
def ntef_340_pt():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown21010(1)

@State
def ntef_400_aura():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown1097(200)
        Unknown4011(3)
    sprite('vr_nt400_00', 3)
    sprite('vr_nt400_01', 3)
    sprite('vr_nt400_02', 3)
    sprite('vr_nt400_03', 3)
    Unknown3004(-20)
    sprite('vr_nt400_04', 2)
    sprite('vr_nt400_05', 2)

@State
def ntef_401_aura1():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('vr_nt401_00', 32767)

@State
def ntef_401_aura2():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown1097(350)
        teleportRelativeX(-75000)
        Unknown4011(3)
    sprite('vr_nt401_01', 4)
    sprite('vr_nt401_02', 4)
    sprite('vr_nt401_03', 2)
    GFX_1('ntef_402_aura2_pos', 0)
    GFX_1('ntef_402_aura3_pos', 1)
    sprite('vr_nt401_04', 2)

@State
def ntef_402():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown21010(1)
    sprite('vr_nt402_00', 3)
    sprite('vr_nt402_01', 3)
    Unknown1097(500)
    Unknown1007(-150000)
    teleportRelativeX(-150000)
    sprite('vr_nt402_02', 2)
    GFX_1('ntef_402_aura', 2)
    GFX_1('ntef_402_aura', 3)
    GFX_1('ntef_402_aura', 4)
    sprite('vr_nt402_03', 2)
    Unknown21010(0)
    sprite('vr_nt402_04', 2)
    GFX_1('ntef_402_aura2_pos', 0)
    GFX_1('ntef_402_aura3_pos', 1)
    GFX_1('ntef_402_aura4', 2)
    sprite('vr_nt402_05', 2)

@State
def ntef_403():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown1097(500)
        Unknown1007(-75000)
    sprite('vr_nt403_00', 3)
    sprite('vr_nt403_01', 3)
    sprite('vr_nt403_02', 3)
    sprite('vr_nt403_03', 2)
    sprite('vr_nt403_04', 2)
    GFX_1('ntef_403_aura', 0)
    GFX_1('ntef_403_aura', 1)
    GFX_1('ntef_403_aura', 2)
    GFX_1('ntef_403_aura3', 3)
    GFX_1('ntef_403_aura2', 4)
    sprite('vr_nt403_05', 2)

@State
def ntef_405Weak():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown1007(300000)
        teleportRelativeX(100000)
        Unknown1072(15000)
        Unknown3001(210)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 2)
    sprite('vr_nt405_20', 32767)
    GFX_0('ntef_405WeakSub', -1)
    GFX_0('ntef_405WeakSmoke', -1)
    Unknown1096(750)
    label(0)
    sprite('vr_nt405_20', 2)
    Unknown21012('ntef_405WeakSub', 32)
    Unknown1007(100000)
    teleportRelativeX(50000)
    Unknown1096(1200)
    label(1)
    sprite('vr_nt405_21', 2)
    sprite('vr_nt405_22', 2)
    sprite('vr_nt405_20', 2)
    gotoLabel(1)
    label(2)
    sprite('null', 14)
    GFX_0('ntef_405WeakEnd', -1)
    Unknown26('ntef_405WeakSub')

@State
def ntef_405WeakSub():

    def upon_IMMEDIATE():
        Unknown3035()
        Unknown4061(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown23015(11)
        sendToLabelUpon(32, 1)
        Unknown3001(210)
    sprite('vr_nt405_30', 32767)
    label(1)
    sprite('vr_nt405_31', 2)
    sprite('vr_nt405_32', 2)
    sprite('vr_nt405_30', 2)
    gotoLabel(1)

@State
def ntef_405WeakEnd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(3)
        Unknown4007(2)
        Unknown4003('ntef405_syoryu01', '')
    sprite('null', 13)
    Unknown1096(600)
    Unknown1099(-15)
    Unknown3004(-15)
    teleportRelativeX(-160000)

@State
def ntef_405WeakAir():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown1007(300000)
        teleportRelativeX(100000)
        Unknown1096(650)
        Unknown3001(210)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 2)
    sprite('vr_nt405_20', 32767)
    GFX_0('ntef_405WeakSub', -1)
    label(0)
    sprite('vr_nt405_20', 2)
    Unknown21012('ntef_405WeakSub', 32)
    Unknown1007(100000)
    teleportRelativeX(50000)
    Unknown1096(800)
    label(1)
    sprite('vr_nt405_21', 2)
    Unknown1096(1200)
    sprite('vr_nt405_22', 2)
    sprite('vr_nt405_20', 2)
    gotoLabel(1)
    label(2)
    sprite('null', 14)
    Unknown26('ntef_405WeakSub')
    GFX_0('ntef_405WeakEnd', -1)

@State
def ntef_405WeakSmoke():

    def upon_IMMEDIATE():
        GFX_2('ntef_405_smoke')
        Unknown4009(3)
        Unknown4010(2)
        teleportRelativeY(0)
        Unknown1096(1100)
    sprite('null', 30)

@State
def ntef_405Test():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('ntef405_Bloodsyoryu00', '')
        Unknown1073(10000)
        teleportRelativeX(50000)
        Unknown1096(1300)

        def upon_43():
            if (SLOT_48 == 1004):
                sendToLabel(1)
    sprite('null', 3)
    GFX_0('ntef_405Sub', -1)
    GFX_1('ntef_405_nokosi', -1)
    sprite('null', 1)
    Unknown1096(1300)
    Unknown1007(80000)
    teleportRelativeX(60000)
    GFX_1('ntef_405_nokosi', -1)
    Unknown4009(0)
    label(0)
    sprite('null', 3)
    GFX_1('ntef_405_nokosi', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 4)
    Unknown4010(0)
    Unknown4007(0)
    GFX_1('ntef_405_nokosi', -1)
    teleportRelativeX(-60000)
    Unknown1007(-140000)
    Unknown1073(-10000)
    Unknown4003('ntef405_Bloodsyoryu01', '')
    sprite('null', 4)
    GFX_1('ntef_405_nokosi', -1)
    sprite('null', 4)
    GFX_1('ntef_405_nokosi', -1)
    sprite('null', 5)
    GFX_1('ntef_405_nokosi', -1)

@State
def ntef_405():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        sendToLabelUpon(32, 1)
        Unknown4054(12)
        Unknown23067('tef_405_back')
    sprite('vr_nt405_00', 1)
    GFX_0('ntef_405Sub', -1)
    Unknown1096(950)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    sprite('vr_nt405_01', 2)
    sprite('vr_nt405_00', 2)
    Unknown1007(80000)
    teleportRelativeX(40000)
    Unknown4009(0)
    sprite('vr_nt405_01', 2)
    label(0)
    sprite('vr_nt405_00', 2)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    sprite('vr_nt405_01', 2)
    sprite('vr_nt405_00', 2)
    sprite('vr_nt405_01', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_0('ntef_405end', -1)

@State
def ntef_405end():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown1096(1100)
    sprite('vr_nt405_01', 2)
    sprite('vr_nt405_02', 4)
    sprite('vr_nt405_03', 4)
    sprite('vr_nt405_04', 4)
    sprite('vr_nt405_05', 4)

@State
def ntef_405Sub():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        teleportRelativeY(0)
        Unknown1007(-15000)
        teleportRelativeX(40000)
        Unknown1096(1000)
        Unknown23015(6)
    sprite('vr_nt405_10', 6)
    Unknown4009(2)
    sprite('vr_nt405_11', 6)
    sprite('vr_nt405_12', 4)
    Unknown4009(0)
    sprite('vr_nt405_13', 4)
    sprite('vr_nt405_14', 4)
    sprite('vr_nt405_15', 4)
    sprite('vr_nt405_16', 4)

@State
def ntef_405AirTest():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('ntef405_Bloodsyoryu00', '')
        Unknown1073(10000)
        teleportRelativeX(50000)
        Unknown1096(1300)

        def upon_43():
            if (SLOT_48 == 1005):
                sendToLabel(1)
    sprite('null', 3)
    GFX_1('ntef_405_nokosi', -1)
    sprite('null', 1)
    Unknown1096(1300)
    Unknown1007(80000)
    teleportRelativeX(60000)
    GFX_1('ntef_405_nokosi', -1)
    Unknown4009(0)
    label(0)
    sprite('null', 3)
    GFX_1('ntef_405_nokosi', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 4)
    Unknown4010(0)
    Unknown4007(0)
    GFX_1('ntef_405_nokosi', -1)
    teleportRelativeX(-60000)
    Unknown1007(-140000)
    Unknown1073(-10000)
    Unknown4003('ntef405_Bloodsyoryu01', '')
    sprite('null', 4)
    GFX_1('ntef_405_nokosi', -1)
    sprite('null', 4)
    GFX_1('ntef_405_nokosi', -1)
    sprite('null', 5)
    GFX_1('ntef_405_nokosi', -1)

@State
def ntef_405Air():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4054(12)
        Unknown23067('tef_405_back')
        sendToLabelUpon(32, 1)
    sprite('vr_nt405_00', 1)
    sprite('vr_nt405_01', 2)
    sprite('vr_nt405_00', 2)
    Unknown1007(80000)
    teleportRelativeX(40000)
    Unknown4009(0)
    Unknown3029(1)
    sprite('vr_nt405_01', 2)
    label(0)
    sprite('vr_nt405_00', 2)
    Unknown1096(800)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    sprite('vr_nt405_01', 2)
    Unknown1096(1000)
    sprite('vr_nt405_00', 2)
    Unknown1096(800)
    sprite('vr_nt405_01', 2)
    Unknown1096(1000)
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    GFX_0('ntef_405end', -1)

@State
def ntef_409():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef409_strike00', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown1007(400000)
        Unknown1096(1700)
    sprite('null', 14)

@State
def ntef_410():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef409_strike01', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown1007(300000)
        teleportRelativeX(50000)
        Unknown1096(1500)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    sprite('null', 9)
    Unknown4003('ntef409_strike02', '')
    physicsYImpulse(-15000)

@State
def ntef_430_bloodMatome():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1007(180000)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(3)
    sprite('null', 6)
    GFX_0('ntef_430_blood2', -1)
    GFX_0('ntef_430_blood', -1)
    Unknown36(1)
    Unknown1073(35000)
    Unknown35()
    GFX_0('ntef_430_aura00', -1)
    sprite('null', 6)
    GFX_0('ntef_430_blood', -1)
    Unknown36(1)
    Unknown1073(-35000)
    Unknown35()
    sprite('null', 6)
    GFX_0('ntef_430_blood2', -1)

@State
def ntef_430_blood():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef430_aura00', '')
        Unknown2054(1)
        Unknown4011(3)
    sprite('null', 24)
    Unknown1099(-5)

@State
def ntef_430_blood2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef430_aura01', '')
        Unknown4011(3)
        Unknown2054(1)
        Unknown1007(-200000)
    sprite('null', 7)
    Unknown1059(37)
    Unknown1067(37)
    sprite('null', 7)
    Unknown1059(75)
    Unknown1067(75)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ntef_430_aura00():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4011(3)
        Unknown1007(-130000)
        Unknown3038(1)
        Unknown2055(20)
    sprite('vr_nt430aurapos', 6)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 0)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 1)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 4)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 5)
    Unknown4045('tef_430_auranml', 0)
    Unknown4045('tef_430_auranml', 1)
    Unknown4045('tef_430_auranml', 4)
    Unknown4045('tef_430_auranml', 5)
    sprite('vr_nt430aurapos', 6)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 0)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 1)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 4)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 5)
    Unknown4045('tef_430_auranml', 0)
    Unknown4045('tef_430_auranml', 1)
    Unknown4045('tef_430_auranml', 4)
    Unknown4045('tef_430_auranml', 5)
    sprite('vr_nt430aurapos', 6)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 0)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 1)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 4)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 5)
    Unknown4045('tef_430_auranml', 0)
    Unknown4045('tef_430_auranml', 1)
    Unknown4045('tef_430_auranml', 4)
    Unknown4045('tef_430_auranml', 5)
    sprite('vr_nt430aurapos', 6)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 0)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 1)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 4)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 5)
    Unknown4045('tef_430_auranml', 0)
    Unknown4045('tef_430_auranml', 1)
    Unknown4045('tef_430_auranml', 4)
    Unknown4045('tef_430_auranml', 5)
    sprite('vr_nt430aurapos', 6)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 0)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 1)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 4)
    Unknown4054(11)
    Unknown4045('tef_430_aura', 5)
    Unknown4045('tef_430_auranml', 0)
    Unknown4045('tef_430_auranml', 1)
    Unknown4045('tef_430_auranml', 4)
    Unknown4045('tef_430_auranml', 5)

@State
def ntef_430atk():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown3032()
        Unknown3001(230)

        def upon_43():
            if (SLOT_48 == 2001):
                sendToLabel(1)
            if (SLOT_48 == 2002):
                sendToLabel(3)
    label(0)
    sprite('vr_nt430_00', 2)
    sprite('vr_nt430_01', 2)
    gotoLabel(0)
    label(1)
    sprite('vr_nt430_02', 4)
    Unknown21010(1)
    sprite('vr_nt430_03', 4)
    sprite('vr_nt430_04', 4)
    sprite('vr_nt430_05', 4)
    sprite('vr_nt430_06', 4)
    sprite('vr_nt430_07', 6)
    sprite('vr_nt430_08', 3)
    sprite('vr_nt430_09', 3)
    sprite('vr_nt430_10', 2)
    sprite('vr_nt430_20', 2)
    GFX_0('ntef_430blood_3d', -1)
    Unknown1096(1150)
    Unknown3001(200)
    Unknown1007(220000)
    teleportRelativeX(290000)
    Unknown23015(11)
    Unknown4009(2)
    Unknown21010(0)
    GFX_0('ntef_atksub', -1)
    label(2)
    sprite('vr_nt430_21', 3)
    sprite('vr_nt430_20', 3)
    gotoLabel(2)
    label(3)
    sprite('vr_nt430_21', 2)
    Unknown4010(0)
    Unknown21012('ntef_atksub', 32)
    sprite('vr_nt430_22', 4)
    Unknown23015(0)
    Unknown4007(0)
    Unknown21012('ntef_430blood_3d', 32)
    sprite('vr_nt430_23', 2)
    sprite('vr_nt430_23', 2)
    GFX_1('ntef_430_sibuki', 1)
    GFX_1('ntef_430_sibuki', 3)
    GFX_1('ntef_430_sibuki', 5)
    GFX_1('ntef_430_sibuki', 0)
    GFX_1('ntef_430_sibuki', 2)
    GFX_1('ntef_430_sibuki', 4)
    sprite('vr_nt430_24', 4)
    sprite('vr_nt430_25', 3)
    GFX_1('tef_430_last', 0)
    GFX_1('tef_430_last', 1)
    GFX_1('tef_430_last', 2)
    GFX_1('tef_430_last', 3)

@State
def ntef_atksub():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('tef_430_core')
        Unknown3038(1)
        sendToLabelUpon(32, 1)
        Unknown4006(2)
    label(0)
    sprite('vr_nt430_22', 7)
    GFX_1('tef_430_tossin_00', 0)
    GFX_1('tef_430_tossin_00', 1)
    GFX_1('tef_430_tossin_00', 2)
    GFX_1('tef_430_tossin_00', 3)
    GFX_1('tef_430_tossin_00', 4)
    gotoLabel(0)
    label(1)
    sprite('vr_nt430_22', 7)
    Unknown3004(-51)
    GFX_1('tef_430_tossin_00', 0)
    GFX_1('tef_430_tossin_00', 1)
    GFX_1('tef_430_tossin_00', 2)
    GFX_1('tef_430_tossin_00', 3)
    GFX_1('tef_430_tossin_00', 4)

@State
def ntef_430blood_3d():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4006(2)
        Unknown4003('ntef430_blood.DIG', '')
        Unknown3032()
        Unknown4025(2)
        Unknown23015(11)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 15)
    Unknown23015(0)
    Unknown4003('ntef430_blood2.DIG', '')

@State
def ntef_Air430atk():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown3032()
        Unknown4061(1)
        Unknown3001(230)
        Unknown1007(80000)
        teleportRelativeX(20000)

        def upon_43():
            if (SLOT_48 == 2004):
                sendToLabel(1)
            if (SLOT_48 == 2005):
                sendToLabel(3)
    label(0)
    sprite('vr_nt430_00', 2)
    sprite('vr_nt430_01', 2)
    gotoLabel(0)
    label(1)
    sprite('vr_nt430_30', 6)
    Unknown21010(1)
    Unknown1007(-80000)
    teleportRelativeX(-20000)
    sprite('vr_nt430_31', 8)
    sprite('vr_nt430_32', 6)
    sprite('vr_nt430_33', 6)
    sprite('vr_nt430_34', 4)
    Unknown23015(11)
    sprite('vr_nt430_20', 2)
    GFX_0('ntef_430blood_3d', -1)
    Unknown1096(1150)
    Unknown1007(-50000)
    teleportRelativeX(290000)
    Unknown3001(250)
    Unknown4009(2)
    Unknown21010(0)
    GFX_0('ntef_atksub', -1)
    Unknown1072(45000)
    label(2)
    sprite('vr_nt430_21', 3)
    sprite('vr_nt430_20', 3)
    gotoLabel(2)
    label(3)
    sprite('vr_nt430_21', 2)
    Unknown4010(0)
    Unknown21012('ntef_atksub', 32)
    Unknown1000(290000)
    teleportRelativeY(-50000)
    Unknown1072(45000)
    sprite('vr_nt430_22', 3)
    Unknown21012('ntef_430blood_3d', 32)
    Unknown23015(0)
    Unknown4007(0)
    sprite('vr_nt430_23', 3)
    sprite('vr_nt430_24', 3)
    sprite('vr_nt430_25', 3)
    GFX_1('tef_430_last', 0)
    GFX_1('tef_430_last', 1)
    GFX_1('tef_430_last', 2)
    GFX_1('tef_430_last', 3)

@State
def ntef_430_AirbloodMatome():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1007(180000)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(3)
    sprite('null', 6)
    GFX_0('ntef_430_blood', -1)
    Unknown36(1)
    Unknown1073(35000)
    Unknown1099(-30)
    Unknown1097(300)
    Unknown35()
    GFX_0('ntef_430_aura00', -1)
    sprite('null', 6)
    GFX_0('ntef_430_blood', -1)
    Unknown36(1)
    Unknown1073(-35000)
    Unknown1099(-15)
    Unknown1097(100)
    Unknown35()
    sprite('null', 6)

@State
def ntef_430atkOD():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4010(2)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(1)
        teleportRelativeY(0)
        Unknown1007(-30000)
        teleportRelativeX(-55000)
        Unknown3007(255)
        Unknown3019(223)
        Unknown3013(223)
    sprite('vr_nt430_40', 6)
    GFX_0('ntef_430atkODsub', -1)
    GFX_1('tef_430a_tossin_00', 0)
    GFX_1('tef_430a_tossin_00', 1)
    GFX_1('tef_430a_tossin_00', 2)
    GFX_1('tef_430a_tossin_00', 3)
    GFX_1('tef_430a_tossin_00', 4)
    sprite('vr_nt430_41', 6)
    Unknown4009(2)
    GFX_0('ntef_430atkODsub', -1)
    GFX_1('tef_430a_tossin_00', 0)
    GFX_1('tef_430a_tossin_00', 1)
    GFX_1('tef_430a_tossin_00', 2)
    GFX_1('tef_430a_tossin_00', 3)
    GFX_1('tef_430a_tossin_00', 4)
    sprite('vr_nt430_42', 5)
    sprite('vr_nt430_43', 4)
    sprite('vr_nt430_44', 4)

@State
def ntef_430atkODsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1500)
        Unknown3001(200)
        Unknown4003('ntef430a_moya2', '')
        Unknown4010(2)
        Unknown2005()
    sprite('null', 17)
    Unknown1099(75)

@State
def ntef_430_moya():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1500)
        teleportRelativeX(300000)
        Unknown1007(75000)
        GFX_2('tef_430a_yotyou')
        Unknown4010(2)
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 2003):
                sendToLabel(0)
    sprite('null', 15)
    sprite('null', 32767)
    GFX_0('ntef_430_moyaa', -1)
    Unknown4007(0)
    label(0)
    sprite('null', 1)

@State
def ntef_430_moyaa():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('ntef430a_moya', '')
        Unknown4010(2)
        Unknown1097(500)
        Unknown3001(200)
        Unknown1007(-100000)
    sprite('null', 20)
    Unknown3001(0)
    Unknown3004(15)
    sprite('null', 21)
    Unknown3004(0)

@State
def ntef_431():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(3)
        Damage(2300)
        AttackP2(60)
        Unknown11092(1)
        Hitstop(3)
        Unknown11001(1, 1, 1)
        blockstun(13)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(36000)
        AirUntechableTime(60)
        Unknown4009(2)
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 3001):
                clearUponHandler(56)
                Unknown2003(1)
                Unknown4007(0)
            if (SLOT_48 == 3003):
                Damage(2400)

        def upon_56():
            Unknown4007(0)
        Unknown3032()
        Unknown1097(50)
        teleportRelativeX(100000)
        Unknown1007(-30000)
    sprite('vr_nt431_00', 3)
    GFX_0('ntef_431_3d', -1)
    physicsXImpulse(24000)
    ScreenShake(10000, 10000)
    GFX_0('ntef_431Sub', 2)
    sprite('vr_nt431_00', 3)
    Unknown1097(300)
    physicsXImpulse(6000)
    sprite('vr_nt431_01', 3)
    Unknown4009(0)
    physicsXImpulse(4000)
    sprite('vr_nt431_01', 3)
    RefreshMultihit()
    Unknown1097(300)
    physicsXImpulse(3000)
    GFX_0('ntef_431OdLastSub', -1)
    Unknown36(1)
    Unknown1056(1500)
    Unknown1064(1000)
    Unknown1007(30000)
    teleportRelativeX(-250000)
    Unknown35()
    sprite('vr_nt431_02', 6)
    RefreshMultihit()
    physicsXImpulse(0)
    sprite('vr_nt431_03', 4)
    sprite('vr_nt431_04', 4)
    Unknown21012('ntef_431_3d', 32)
    Unknown21012('ntef_431Sub', 32)
    sprite('vr_nt431_05', 4)
    GFX_1('tef_430a_tossin_00', 0)
    GFX_1('tef_430a_tossin_00', 1)
    GFX_1('tef_430a_tossin_00', 2)
    GFX_1('tef_430a_tossin_00', 3)
    GFX_1('tef_430a_tossin_00', 4)
    GFX_1('tef_430a_tossin_00', 5)

@State
def ntef_431_3d():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('ntef431_upper.DIG', '')
        Unknown3032()
        Unknown4025(2)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
        Unknown1096(1200)
        Unknown1007(-16000)
        teleportRelativeX(32000)
    sprite('null', 3)
    sprite('null', 3)
    Unknown1097(120)
    sprite('null', 3)
    sprite('null', 3)
    Unknown1097(180)
    sprite('null', 2)
    sprite('null', 4)
    Unknown3001(225)
    sprite('null', 4)
    Unknown3001(200)
    label(0)
    sprite('null', 4)
    Unknown4003('ntef431_upper2.DIG', '')
    Unknown3001(175)
    sprite('null', 4)

@State
def ntef_431_OD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(3)
        Damage(2600)
        AttackP2(60)
        Unknown11092(1)
        Hitstop(3)
        Unknown11001(1, 1, 1)
        blockstun(13)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(36000)
        AirUntechableTime(60)
        Unknown4009(2)
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 3002):
                clearUponHandler(56)
                Unknown2003(1)
                Unknown4007(0)
            if (SLOT_48 == 3004):
                Damage(2700)

        def upon_56():
            Unknown4007(0)
        Unknown3032()
        Unknown1096(1050)
        teleportRelativeX(100000)
        Unknown1007(-30000)
    sprite('vr_nt431_00', 3)
    GFX_0('ntef_431_3d', -1)
    physicsXImpulse(24000)
    ScreenShake(10000, 10000)
    GFX_0('ntef_431Sub', 2)
    sprite('vr_nt431_00', 3)
    Unknown1097(300)
    physicsXImpulse(6000)
    sprite('vr_nt431_01', 3)
    Unknown4009(0)
    physicsXImpulse(4000)
    sprite('vr_nt431_01', 3)
    RefreshMultihit()
    Unknown1097(300)
    physicsXImpulse(3000)
    GFX_0('ntef_431OdLastSub', -1)
    Unknown36(1)
    Unknown1056(1500)
    Unknown1064(1000)
    Unknown1007(30000)
    teleportRelativeX(-250000)
    Unknown35()
    sprite('vr_nt431_02', 6)
    RefreshMultihit()
    physicsXImpulse(0)
    sprite('vr_nt431_03', 4)
    sprite('vr_nt431_04', 4)
    Unknown21012('ntef_431_3d', 32)
    Unknown21012('ntef_431Sub', 32)
    sprite('vr_nt431_05', 4)
    GFX_1('tef_430a_tossin_00', 0)
    GFX_1('tef_430a_tossin_00', 1)
    GFX_1('tef_430a_tossin_00', 2)
    GFX_1('tef_430a_tossin_00', 3)
    GFX_1('tef_430a_tossin_00', 4)
    GFX_1('tef_430a_tossin_00', 5)

@State
def ntef_431AddAtk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef431_addslash00', '')
        Unknown4010(2)
        Unknown1007(185000)
        Unknown1096(2000)
    sprite('null', 2)
    GFX_1('ntef_431_speed', -1)
    GFX_0('ntef_431shockwave', -1)
    sprite('null', 2)
    Unknown1065(1600)
    sprite('null', 2)
    Unknown1065(-1600)
    sprite('null', 2)
    Unknown1065(1600)
    sprite('null', 2)
    Unknown1065(-1600)
    sprite('null', 5)
    sprite('null', 10)
    Unknown1067(-200)

@State
def ntef_431shockwave():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef431_saddslash01', '')
        Unknown4010(2)
        Unknown1096(150)
    sprite('null', 8)
    sprite('null', 5)
    physicsXImpulse(10000)
    Unknown1099(50)
    sprite('null', 5)
    Unknown1099(100)

@State
def ntef_431Sub():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('tef_431_ground')
        Unknown4010(2)
        Unknown1096(850)
        teleportRelativeX(75000)
        Unknown2005()
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    Unknown3004(-51)
    loopRest()

@State
def ntef_431OD():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4061(1)
    sprite('vr_nt431_10', 4)
    teleportRelativeX(-20000)
    sprite('vr_nt431_11', 4)
    sprite('vr_nt431_12', 4)
    teleportRelativeX(-30100)
    sprite('vr_nt431_13', 4)
    teleportRelativeX(50100)
    sprite('vr_nt431_14', 4)
    sprite('vr_nt431_15', 2)
    sprite('vr_nt431_16', 2)
    sprite('vr_nt431_17', 2)
    teleportRelativeX(-50100)
    GFX_0('ntef_431OdSub', 0)
    sprite('vr_nt431_18', 5)
    GFX_0('ntef_431OdLastAtk', -1)
    sprite('vr_nt431_19', 4)
    sprite('vr_nt431_20', 6)
    sprite('vr_nt431_21', 6)
    sprite('vr_nt431_22', 6)

@State
def ntef_431OdSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef431_slash00', '')
        Unknown4009(2)
        Unknown1056(1600)
        Unknown1064(1000)
        Unknown1007(-20000)
        Unknown20003(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
    sprite('null', 12)
    GFX_0('ntef_431OdShake', -1)
    Unknown20000(2)
    Unknown20009(900)

@State
def ntef_431OdShake():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        GFX_2('tef_431od_tame')
    label(0)
    sprite('null', 4)
    ScreenShake(10000, 10000)
    gotoLabel(0)

@State
def ntef_431OdLastAtk():

    def upon_IMMEDIATE():
        GFX_2('tef_431_ground_00')
        teleportRelativeX(600000)
        Unknown2005()
        Unknown1096(1200)
    sprite('null', 120)
    ScreenShake(20000, 20000)

@State
def ntef_431OdLastSubMato():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(4700)
        MinimumDamagePct(20)
        AttackP1(48)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(45000)
        AirPushbackY(20000)
        AirUntechableTime(100)
        Unknown9202(25)
        Unknown11023(1)
        Unknown9016(1)
        Unknown11108(3)
        Unknown4010(2)
        Unknown3038(1)

        def upon_12():
            Unknown21012('UltimateEdgeAssault_Exe_OD', 32)
    sprite('vr_nt431_atk', 4)
    GFX_0('ntef_431OdLastSub', 0)
    sprite('vr_nt431_atk', 4)
    GFX_0('ntef_431OdLastSub', 2)
    sprite('vr_nt431_atk', 4)
    GFX_0('ntef_431OdLastSub', 3)
    sprite('vr_nt431_atk', 4)
    GFX_0('ntef_431OdLastSub', 1)
    sprite('null', 6)
    sprite('vr_nt431_atk', 4)
    GFX_0('ntef_431OdLastSub', 0)
    sprite('vr_nt431_atk', 4)
    GFX_0('ntef_431OdLastSub', 2)
    sprite('vr_nt431_atk', 4)
    GFX_0('ntef_431OdLastSub', 3)
    sprite('vr_nt431_atk', 4)
    GFX_0('ntef_431OdLastSub', 1)

@State
def ntef_431OdLastSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef_cmnblood00', '')
        Unknown1096(2500)
        Unknown1102(-300, 300)
    sprite('null', 23)

@State
def ntef_440Axe():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    sprite('vr_nt440_06', 3)
    GFX_0('ntef_440Last', -1)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown1065(1000)
    Unknown1057(600)
    Unknown35()
    sprite('vr_nt440_06', 3)
    Unknown3038(1)
    GFX_0('ntef_440Last', -1)
    Unknown36(1)
    teleportRelativeX(400000)
    Unknown1097(400)
    Unknown35()
    sprite('vr_nt440_06', 3)
    Unknown3038(1)
    GFX_0('ntef_440Last', -1)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown1057(1200)
    Unknown1065(0)
    Unknown35()
    GFX_1('ntef_611_end', 0)
    GFX_1('ntef_611_end', 1)
    GFX_1('ntef_611_end', 2)
    GFX_1('ntef_611_end', 3)
    GFX_1('ntef_611_end', 4)

@State
def ntef_440Last():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef_cmnblood00', '')
        Unknown1096(1000)
    sprite('null', 23)

@State
def ntef_440LastEx():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2005()
        GFX_2('tef_431_ground_00')
        Unknown1096(1200)
        teleportRelativeX(-400000)
        Unknown1007(100000)
    sprite('null', 40)
    ScreenShake(40000, 40000)
    sprite('null', 30)
    Unknown3004(-8)

@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20003(1)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4008(3)
        teleportRelativeX(200000)
    sprite('null', 32767)

@State
def ntef_451aura():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef451_aura00', '')
        Unknown2054(1)
        Unknown1096(300)
    sprite('null', 24)
    Unknown1099(65)

@State
def ntef_451():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('vr_nt451_02', 5)
    sprite('vr_nt451_02', 5)
    Unknown3004(-51)
    GFX_1('tef_451_tame00', 0)
    GFX_1('tef_451_tame00', 1)
    GFX_1('tef_451_tame00', 2)
    GFX_1('tef_451_tame00', 3)
    GFX_1('tef_451_tame00', 4)
    GFX_1('tef_451_tame00', 5)
    GFX_1('tef_451_tame00', 6)
    ExitState()

@State
def ntef_451_hit():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('vr_nt451_02', 15)
    sprite('vr_nt451_02', 10)
    Unknown3004(-25)
    GFX_1('tef_451_tame00', 0)
    GFX_1('tef_451_tame00', 1)
    GFX_1('tef_451_tame00', 2)
    GFX_1('tef_451_tame00', 3)
    GFX_1('tef_451_tame00', 4)
    GFX_1('tef_451_tame00', 5)
    GFX_1('tef_451_tame00', 6)

@State
def ntef_451_2():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown4010(2)
        Unknown4009(2)

        def upon_43():
            if (SLOT_48 == 4001):
                sendToLabel(10)
            if (SLOT_48 == 4002):
                sendToLabel(1)
            if (SLOT_48 == 4003):
                sendToLabel(3)
    sprite('vr_nt451_04', 2)
    label(0)
    sprite('vr_nt451_05', 2)
    GFX_1('tef_451_tame00', 0)
    GFX_1('tef_451_tame00', 1)
    GFX_1('tef_451_tame00', 2)
    GFX_1('tef_451_tame00', 3)
    GFX_1('tef_451_tame00', 4)
    GFX_1('tef_451_tame00', 5)
    GFX_1('tef_451_tame00', 6)
    ScreenShake(2000, 2000)
    sprite('vr_nt451_05a', 2)
    sprite('vr_nt451_05b', 2)
    sprite('vr_nt451_05c', 2)
    sprite('vr_nt451_05d', 2)
    sprite('vr_nt451_05e', 2)
    gotoLabel(0)
    label(10)
    sprite('null', 32767)
    label(1)
    sprite('vr_nt451_28', 3)
    GFX_0('ntef_451slash_kyushu', 0)
    Unknown23015(11)
    label(2)
    sprite('vr_nt451_29', 3)
    sprite('vr_nt451_28', 3)
    gotoLabel(2)
    label(3)
    sprite('vr_nt451_31', 15)
    Unknown23015(0)
    GFX_0('ntef_451slash3', 0)
    sprite('vr_nt451_32', 3)
    sprite('vr_nt451_33', 3)
    sprite('vr_nt451_34', 3)

@State
def ntef_451slash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4003('ntef451_slash00', '')
        Unknown1096(1400)
    sprite('null', 21)

@State
def ntef_451slash2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4003('ntef451_slash01', '')
        Unknown1096(1400)
    sprite('null', 21)

@State
def ntef_451slash3():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4003('ntef451_slash02', '')
        Unknown1096(1300)
        teleportRelativeX(-150000)
    sprite('null', 4)
    ScreenShake(20000, 20000)
    sprite('null', 4)
    ScreenShake(15000, 20000)
    sprite('null', 4)
    ScreenShake(20000, 20000)
    sprite('null', 4)
    ScreenShake(20000, 20000)
    sprite('null', 4)
    ScreenShake(20000, 20000)
    sprite('null', 2)

@State
def ntef_451SubMato():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown2005()
        teleportRelativeX(-600000)
    sprite('nt431_23', 4)
    GFX_0('ntef_431OdLastSub', 0)
    Unknown36(1)
    Unknown1097(600)
    Unknown35()
    sprite('nt431_23', 4)
    GFX_0('ntef_431OdLastSub', 2)
    Unknown36(1)
    Unknown1097(600)
    Unknown35()
    sprite('nt431_23', 4)
    GFX_0('ntef_431OdLastSub', 3)
    Unknown36(1)
    Unknown1097(600)
    Unknown35()
    sprite('nt431_23', 4)
    GFX_0('ntef_431OdLastSub', 1)
    Unknown36(1)
    Unknown1097(600)
    Unknown35()
    sprite('null', 6)
    sprite('nt431_23', 4)
    GFX_0('ntef_431OdLastSub', 0)
    Unknown36(1)
    Unknown1097(600)
    Unknown35()
    sprite('nt431_23', 4)
    GFX_0('ntef_431OdLastSub', 2)
    Unknown36(1)
    Unknown1097(600)
    Unknown35()
    sprite('nt431_23', 4)
    GFX_0('ntef_431OdLastSub', 3)
    Unknown36(1)
    Unknown1097(600)
    Unknown35()
    sprite('nt431_23', 4)
    GFX_0('ntef_431OdLastSub', 1)
    Unknown36(1)
    Unknown1097(600)
    Unknown35()

@State
def ntef_451slash_kyushu():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1000)
        Unknown1075(20)
        GFX_2('tef_451_core')

        def upon_43():
            if (SLOT_48 == 4004):
                sendToLabel(1)
    sprite('null', 1)
    GFX_0('ntef_451slash_kyushuSub', -1)
    Unknown21012('ntef_451_BG', 32)
    label(0)
    sprite('null', 4)
    ScreenShake(10000, 10000)
    SFX_3('ntse_09')
    sprite('null', 4)
    Unknown1097(50)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown3004(-51)

@State
def ntef_451slash_kyushuSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef451_kyushu', '')
        Unknown1096(1200)
        Unknown1075(20)
    sprite('null', 19)

@State
def ntef_451_BG():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('tef_451_bg')
        Unknown4010(2)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ntef_611():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4061(1)
        teleportRelativeX(150000)
        Unknown1007(300000)
    sprite('vr_nt611_00', 4)
    Unknown1099(5)
    physicsXImpulse(1400)
    physicsYImpulse(1000)
    sprite('vr_nt611_01', 3)
    sprite('vr_nt611_02', 3)
    sprite('vr_nt611_03', 4)
    sprite('vr_nt611_04', 4)
    sprite('vr_nt611_05', 4)
    GFX_1('ntef_611_end', 0)
    GFX_1('ntef_611_end', 1)
    GFX_1('ntef_611_end', 2)
    GFX_1('ntef_611_end', 3)
    GFX_1('ntef_611_end', 4)
    GFX_1('ntef_611_end', 5)
    GFX_1('ntef_611_end', 6)
    GFX_1('ntef_611_end', 7)
    GFX_1('ntef_611_end', 8)
    GFX_1('ntef_611_end', 9)
    GFX_1('ntef_611_end', 10)
    GFX_1('ntef_611_end', 11)
    sprite('vr_nt611_06', 3)
    sprite('vr_nt611_07', 3)
    Unknown3004(-26)
    sprite('vr_nt611_08', 3)

@State
def ntef_OverDrive():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ntef333_syuyaku00', '')
        Unknown1077(-100000, 100000)
        Unknown4007(3)
        Unknown4010(3)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    Unknown1099(75)
    Unknown3004(-13)
    sprite('null', 10)

@State
def ntef_D_bodyaura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_2('ntef_D_bodyaura')

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(0)
    sprite('null', 8)
    Unknown3001(0)
    Unknown3004(32)
    sprite('null', 32767)
    label(0)
    sprite('null', 25)
    Unknown3004(-10)

@State
def ntef_D_handaura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(3)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 1002):
                sendToLabel(0)
    label(1)
    sprite('null', 9)
    GFX_0('ntef_D_handaura_1', -1)
    SFX_3('ntse_01')
    gotoLabel(1)
    label(0)
    sprite('null', 0)
    Unknown13(25)

@State
def ntef_D_handaura_1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4011(3)
        Unknown2054(1)
        Unknown4025(2)
        GFX_2('ntef_D_handaura')
    sprite('null', 30)

@State
def ntef_D_handaura_3D():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(3)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 1001):
                sendToLabel(0)
    label(1)
    sprite('null', 6)
    GFX_0('ntef_D_handaura_3D_1', -1)
    gotoLabel(1)
    label(0)
    sprite('null', 10)
    Unknown3004(-25)
    Unknown4009(0)

@State
def ntef_D_handaura_3D_1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('ntef_D_charge.DIG', '')
        Unknown4009(3)
        Unknown4025(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1079()
        Unknown23015(11)
        Unknown1096(1250)
    sprite('null', 15)

@Subroutine
def BloodEdge():
    Unknown3055(208, 255)
    Unknown3055(209, 15)
    Unknown3055(210, 23)
    Unknown3055(211, 31)
    Unknown3055(212, 39)
    Unknown3055(213, 47)
    Unknown3055(214, 55)
    Unknown3055(215, 63)
    Unknown3055(216, 71)
    Unknown3055(217, 79)
    Unknown3055(218, 87)
    Unknown3055(219, 95)
    Unknown3055(220, 103)
    Unknown3055(221, 111)
    Unknown3055(222, 119)
    Unknown3055(223, 127)
    Unknown3055(224, 135)
    Unknown3055(225, 143)
    Unknown3055(226, 151)
    Unknown3055(227, 159)
    Unknown3055(228, 167)
    Unknown3055(229, 175)
    Unknown3055(230, 183)
    Unknown3055(231, 191)
    Unknown3055(232, 199)
    Unknown3055(233, 207)
    Unknown3055(234, 215)
    Unknown3055(235, 223)
    Unknown3055(236, 231)
    Unknown3055(237, 239)
    Unknown3055(238, 247)
    Unknown3055(239, 255)
    Unknown3055(240, 255)
    Unknown3055(241, 255)
    Unknown3055(242, 255)
    Unknown3055(243, 255)
    Unknown3055(244, 255)
    Unknown3055(254, 127)

@State
def MaskTexture():

    def upon_IMMEDIATE():
        Unknown13040('76726e7465663030305f30300000000000000000000000000000000000000000100000000000000000f4010000000000d0070000ffffff7fe8030000f4010000')
        Unknown4061(1)
        Unknown3033()
        Unknown1007(192000)
    sprite('vr_nt203_20', 300)

@Subroutine
def BloodEdge_Particle():
    GFX_1('ntef_test', 0)
    GFX_1('ntef_test', 1)
    GFX_1('ntef_test', 2)
    GFX_1('ntef_test', 3)
    GFX_1('ntef_test', 4)
    GFX_1('ntef_test', 5)

@State
def ntef_looptest():

    def upon_IMMEDIATE():
        Unknown4015()
        Unknown3032()
        Unknown1007(256000)
        teleportRelativeX(256000)
    sprite('null', 1)
    Unknown2007()
    Unknown4003('ntef_looptest.DIG', '')
    sprite('null', 31)
    Unknown4003('ntef_looptest.DIG', '')
    sprite('null', 1)
    Unknown4003('ntef_looptest.DIG', '')
    sprite('null', 32)
    Unknown4003('ntef_looptest.DIG', '')

@State
def ntef_253_a():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4061(1)
        Unknown3032()
        Unknown13044(1)
    sprite('vr_nt253_20', 3)
    sprite('vr_nt253_21', 3)

@State
def ntef_253_b():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4061(1)
        Unknown3032()
        Unknown13044(1)
    sprite('vr_nt253_40', 3)
    sprite('vr_nt253_41', 3)

@State
def ntef_610():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1086(22)
        teleportRelativeY(150000)
    sprite('null', 1)
    if Unknown42('rg'):
        pass
    if Unknown42('jn'):
        pass
    if Unknown42('no'):
        pass
    if Unknown42('rc'):
        pass
    if Unknown42('tk'):
        pass
    if Unknown42('tg'):
        Unknown1007(50000)
    if Unknown42('lc'):
        pass
    if Unknown42('ar'):
        pass
    if Unknown42('bn'):
        pass
    if Unknown42('ca'):
        pass
    if Unknown42('ha'):
        pass
    if Unknown42('ny'):
        pass
    if Unknown42('tb'):
        pass
    if Unknown42('hz'):
        pass
    if Unknown42('mu'):
        pass
    if Unknown42('mk'):
        pass
    if Unknown42('vh'):
        pass
    if Unknown42('pt'):
        pass
    if Unknown42('rl'):
        pass
    if Unknown42('iz'):
        pass
    if Unknown42('am'):
        pass
    if Unknown42('bl'):
        pass
    if Unknown42('az'):
        pass
    if Unknown42('kg'):
        pass
    if Unknown42('kk'):
        pass
    if Unknown42('tm'):
        pass
    if Unknown42('ce'):
        pass
    if Unknown42('rm'):
        pass
    if Unknown42('hb'):
        pass
    if Unknown42('ph'):
        pass
    if Unknown42('nt'):
        pass
    if Unknown42('mi'):
        pass
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(1)
    sprite('null', 1)
    GFX_0('ntef_610_a', -1)
    loopRest()
    label(1)
    sprite('null', 32767)
    GFX_0('ntef_610_b', -1)
    loopRest()

@State
def ntef_610_a():
    sprite('null', 1)
    GFX_1('ntef_610_smoke', -1)
    teleportRelativeX(40000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-80000)
    Unknown35()
    Unknown21007(1, 35)

@State
def ntef_610_b():
    sprite('null', 1)
    GFX_1('ntef_610_smoke', -1)
    teleportRelativeX(40000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-80000)
    Unknown35()
    Unknown21007(1, 36)

@State
def ntef_601():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1086(22)
        teleportRelativeY(475000)
    sprite('null', 1)
    GFX_0('ntef_601_bg', -1)
    if Unknown42('rg'):
        GFX_0('ntef_601_rg', -1)
    if Unknown42('jn'):
        GFX_0('ntef_601_jn', -1)
    if Unknown42('no'):
        GFX_0('ntef_601_no', -1)
    if Unknown42('rc'):
        GFX_0('ntef_601_rc', -1)
    if Unknown42('tk'):
        GFX_0('ntef_601_tk', -1)
    if Unknown42('tg'):
        Unknown1007(60000)
        GFX_0('ntef_601_tg', -1)
    if Unknown42('lc'):
        GFX_0('ntef_601_lc', -1)
    if Unknown42('ar'):
        GFX_0('ntef_601_ar', -1)
    if Unknown42('bn'):
        GFX_0('ntef_601_bn', -1)
    if Unknown42('ca'):
        GFX_0('ntef_601_ca', -1)
    if Unknown42('ha'):
        GFX_0('ntef_601_ha', -1)
    if Unknown42('ny'):
        GFX_0('ntef_601_ny', -1)
    if Unknown42('tb'):
        GFX_0('ntef_601_tb', -1)
    if Unknown42('hz'):
        GFX_0('ntef_601_hz', -1)
    if Unknown42('mu'):
        GFX_0('ntef_601_mu', -1)
    if Unknown42('mk'):
        GFX_0('ntef_601_mk', -1)
    if Unknown42('vh'):
        GFX_0('ntef_601_vh', -1)
    if Unknown42('pt'):
        GFX_0('ntef_601_pt', -1)
    if Unknown42('rl'):
        GFX_0('ntef_601_rl', -1)
    if Unknown42('iz'):
        GFX_0('ntef_601_iz', -1)
    if Unknown42('am'):
        GFX_0('ntef_601_am', -1)
    if Unknown42('bl'):
        GFX_0('ntef_601_bl', -1)
    if Unknown42('az'):
        GFX_0('ntef_601_az', -1)
    if Unknown42('kg'):
        GFX_0('ntef_601_kg', -1)
    if Unknown42('kk'):
        GFX_0('ntef_601_kk', -1)
    if Unknown42('tm'):
        GFX_0('ntef_601_tm', -1)
    if Unknown42('ce'):
        GFX_0('ntef_601_ce', -1)
    if Unknown42('rm'):
        GFX_0('ntef_601_rm', -1)
    if Unknown42('hb'):
        GFX_0('ntef_601_hb', -1)
    if Unknown42('ph'):
        GFX_0('ntef_601_ph', -1)
    if Unknown42('nt'):
        GFX_0('ntef_601_nt', -1)
    if Unknown42('mi'):
        GFX_0('ntef_601_mi', -1)
    if Unknown42('su'):
        Unknown1007(30000)
        GFX_0('ntef_601_su', -1)
    if Unknown42('es'):
        Unknown1007(-70000)
        GFX_0('ntef_601_es', -1)
    if Unknown42('ma'):
        Unknown1007(-10000)
        GFX_0('ntef_601_ma', -1)
    if Unknown42('jb'):
        Unknown1007(-75000)
        GFX_0('ntef_601_jb', -1)
    label(99)

@State
def ntef_601_bg():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown23033(50)
        Unknown23067('ntef_601_black')
    sprite('null', 40)
    Unknown3001(0)
    Unknown3004(3)
    Unknown36(22)
    Unknown3025(-32897, 30)
    Unknown35()
    sprite('null', 5)
    Unknown3004(0)
    sprite('null', 25)
    Unknown36(22)
    Unknown3025(-1, 30)
    Unknown35()
    sprite('null', 30)
    sprite('null', 40)
    Unknown3004(-3)

@State
def ntef_601dist():

    def upon_3():
        Unknown23015(9)
        Unknown4007(2)
        Unknown3057(1)
        Unknown3058(10000)
        Unknown3059(-1000)
    sprite('vr_nt601_dist', 64)
    Unknown1079()
    Unknown1064(500)
    Unknown1056(500)
    Unknown1067(5)
    Unknown1059(5)
    Unknown3001(0)
    Unknown3004(4)
    sprite('vr_nt601_dist', 64)
    Unknown3004(-4)

@State
def ntef_Number_bloom():
    sprite('null', 32)
    Unknown23067('ntef_601_bloom')
    Unknown1096(500)
    Unknown1099(5)
    Unknown3001(0)
    Unknown3004(4)
    sprite('null', 64)
    Unknown3004(-2)

@State
def ntef_Number():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown4061(3)
        Unknown3033()
        Unknown23015(10)
        Unknown3001(0)
        Unknown1057(-100)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        sendToLabelUpon(36, 4)
        sendToLabelUpon(37, 5)
        sendToLabelUpon(38, 6)
        sendToLabelUpon(39, 7)
        sendToLabelUpon(40, 8)
        sendToLabelUpon(41, 9)
    label(0)
    sprite('vr_nt601_number0', 0)
    gotoLabel(100)
    label(1)
    sprite('vr_nt601_number1', 0)
    gotoLabel(100)
    label(2)
    sprite('vr_nt601_number2', 0)
    gotoLabel(100)
    label(3)
    sprite('vr_nt601_number3', 0)
    gotoLabel(100)
    label(4)
    sprite('vr_nt601_number4', 0)
    gotoLabel(100)
    label(5)
    sprite('vr_nt601_number5', 0)
    gotoLabel(100)
    label(6)
    sprite('vr_nt601_number6', 0)
    gotoLabel(100)
    label(7)
    sprite('vr_nt601_number7', 0)
    gotoLabel(100)
    label(8)
    sprite('vr_nt601_number8', 0)
    gotoLabel(100)
    label(9)
    sprite('vr_nt601_number9', 0)
    gotoLabel(100)
    label(100)
    sprite('keep', 32)
    Unknown3004(8)
    Unknown1102(-500, -400)
    Unknown1099(5)
    Unknown1077(-6000, 6000)
    Unknown4049(800)
    Unknown4045('ntef_number_smoke01', -1)
    sprite('keep', 30)
    Unknown1099(2)
    GFX_0('ntef_601dist', -1)
    Unknown36(1)
    Unknown1079()
    Unknown35()
    sprite('keep', 64)
    Unknown3022(-8)
    Unknown3016(-8)
    Unknown3004(-4)

@State
def ntef_601_rg():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-80000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-160000)
    Unknown35()
    Unknown21007(1, 35)

@State
def ntef_601_jn():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown35()
    Unknown21007(1, 40)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-80000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    Unknown21007(1, 39)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-160000)
    Unknown35()
    Unknown21007(1, 41)

@State
def ntef_601_no():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-80000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-160000)
    Unknown35()
    Unknown21007(1, 37)

@State
def ntef_601_rc():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-80000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    Unknown21007(1, 40)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-160000)
    Unknown35()
    Unknown21007(1, 38)

@State
def ntef_601_tk():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-80000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-160000)
    Unknown35()
    Unknown21007(1, 39)

@State
def ntef_601_tg():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-80000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-160000)
    Unknown35()
    Unknown21007(1, 32)

@State
def ntef_601_lc():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 40)

@State
def ntef_601_ar():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 39)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 32)

@State
def ntef_601_bn():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 39)

@State
def ntef_601_ca():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 41)

@State
def ntef_601_ha():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 38)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 35)

@State
def ntef_601_ny():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 32)

@State
def ntef_601_tb():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 39)

@State
def ntef_601_hz():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 36)

@State
def ntef_601_mu():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 39)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 37)

@State
def ntef_601_mk():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 38)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 34)

@State
def ntef_601_vh():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 41)

@State
def ntef_601_pt():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 40)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 41)

@State
def ntef_601_rl():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 40)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 40)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 33)

@State
def ntef_601_iz():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 39)

@State
def ntef_601_am():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 40)

@State
def ntef_601_bl():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 40)

@State
def ntef_601_az():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 38)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 35)

@State
def ntef_601_kg():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 32)

@State
def ntef_601_kk():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 40)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 39)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 39)

@State
def ntef_601_tm():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 39)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 36)

@State
def ntef_601_ce():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 33)

@State
def ntef_601_rm():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 32)

@State
def ntef_601_hb():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 40)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 41)

@State
def ntef_601_nt():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 37)

@State
def ntef_601_ph():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 36)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 39)

@State
def ntef_601_mi():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 32)

@State
def ntef_601_su():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 40)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 41)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 36)

@State
def ntef_601_es():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 34)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 40)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 35)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 39)

@State
def ntef_601_ma():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(-80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(80000)
    Unknown35()
    Unknown21007(1, 38)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(120000)
    Unknown35()
    Unknown21007(1, 37)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    Unknown21007(1, 35)

@State
def ntef_601_jb():
    sprite('null', 1)
    GFX_0('ntef_Number_bloom', -1)
    teleportRelativeX(80000)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-40000)
    Unknown35()
    Unknown21007(1, 33)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-80000)
    Unknown35()
    Unknown21007(1, 32)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    Unknown21007(1, 39)
    GFX_0('ntef_Number', -1)
    Unknown36(1)
    teleportRelativeX(-160000)
    Unknown35()
    Unknown21007(1, 40)

@State
def Fade1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4061(0)
        Unknown3001(160)
        teleportRelativeY(3000)
        Unknown2019(-500)
        Unknown3032()
    sprite('nt000_00', 15)
    Unknown3004(-9)
    Unknown1099(50)
    physicsYImpulse(-12000)
    ScreenShake(5000, 1000)
    SFX_3('ntse_13')
    SFX_3('ntse_13')
    SFX_3('ntse_13')
    GFX_0('LifeLinkEff', 0)
    sprite('nt000_00', 20)
    Unknown1099(-130)
    physicsYImpulse(12000)
    sprite('nt000_00', 2)
    Unknown1096(0)
    physicsYImpulse(0)

@State
def Fade2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown3001(0)
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 60)
    Unknown1096(20000)
    Unknown3026(-16777216)
    Unknown3004(4)
    Unknown23024(2)
    sprite('null', 32767)
    Unknown3004(0)
    Unknown3001(255)

@State
def LifeLinkEff():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 1)
    Unknown4045('ntef_story_lifelinkeff', -1)

@State
def Act3Event_Black():

    def upon_IMMEDIATE():
        Unknown3026(-16777216)
        Unknown23015(3)
        Unknown3031()
        Unknown6001(1)
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown1096(20000)
        Unknown3001(0)
        sendToLabelUpon(32, 0)
    sprite('vr_white', 20)
    Unknown3004(12)
    sprite('vr_white', 32767)
    Unknown3004(0)
    Unknown3001(255)
    GFX_0('Act3Event_mivsnt_eff_sl', -1)
    label(0)
    sprite('vr_white', 30)
    Unknown3004(-8)
    sprite('vr_white', 10)
    Unknown3001(0)
    Unknown3004(0)

@State
def Act3Event_mivsnt_eff_sl():

    def upon_IMMEDIATE():
        teleportRelativeY(185000)
    sprite('null', 1)
    Unknown4052()
    Unknown4054(1)
    Unknown4049(1500)
    Unknown4045('ef_hitlz', 103)
    SFX_0('101_hit_slash_3')

@State
def Act3Event_mivsnt_01():

    def upon_IMMEDIATE():
        Unknown1000(-260000)
        teleportRelativeX(100000)
        Unknown30012(0)
        Unknown2019(-500)
    sprite('rl860_10', 32767)
    loopRest()

@State
def Act3Event_mivsnt_02_rl():

    def upon_IMMEDIATE():
        Unknown1000(-260000)
        Unknown30012(0)
        Unknown2019(-501)
    sprite('rl000_00', 8)
    sprite('rl000_01', 8)
    sprite('rl000_02', 8)
    sprite('rl000_03', 8)
    sprite('rl000_04', 8)
    sprite('rl000_05', 8)
    sprite('rl000_06', 8)
    sprite('rl000_07', 8)
    label(0)
    sprite('rl000_00', 8)
    sprite('rl000_01', 8)
    sprite('rl000_02', 8)
    sprite('rl000_03', 8)
    sprite('rl000_04', 8)
    sprite('rl000_05', 8)
    sprite('rl000_06', 8)
    sprite('rl000_07', 8)
    loopRest()
    gotoLabel(0)

@State
def Act3Event_mivsnt_02_camera():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown1086(22)
        Unknown2005()
        teleportRelativeX(-260000)
    sprite('null', 15)
    sprite('null', 32767)
    Unknown20000(1)
    Unknown21012('Act3Event_mivsnt_02_rl', 32)

@State
def Act3Event_rcef_252Wind():
    sprite('null', 100)
    Unknown23000(80, -350, 0)
    GFX_1('rcef_252up_mc02', -1)