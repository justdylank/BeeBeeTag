@State
def PMI_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)
    Unknown3038(1)
    Unknown24('504d495f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PMI_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PMI_ReceptionSignal')
    sprite('null', 32767)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PMI_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 9990):
            Unknown23185('PMI_Persona4A6th', 50)    
        if (SLOT_48 == 9991):
            Unknown23185('PMI_Persona5C', 50)
        if (SLOT_48 == 9992):
            Unknown23185('PMI_Persona5A4th', 50)
        if (SLOT_48 == 9980):
            Unknown23185('PMI_Persona4PS', 50)
        if (SLOT_48 == 4320):
            Unknown23185('PMI_Persona6PS', 50)
        if (SLOT_48 == 2330):
            Unknown23185('PMI_Persona2B2nd', 50)
        if (SLOT_48 == 2540):
            Unknown23185('PMI_PersonaAir5A2nd', 50)
        if (SLOT_48 == 2550):
            Unknown23185('PMI_PersonaAir5C', 50)
        if (SLOT_48 == 2320):
            Unknown23185('PMI_PersonaMarinKarin', 100)
        if (SLOT_48 == 4030):
            Unknown23185('PMI_PersonaTentarafoo', 100)
        if (SLOT_48 == 4031):
            Unknown23185('PMI_PersonaEXTentarafoo', 100)    
        if (SLOT_48 == 4020):
            Unknown23185('PMI_PersonaABufula', 100)
        if (SLOT_48 == 4021):
            Unknown23185('PMI_PersonaBBufula', 100)
        if (SLOT_48 == 4022):
            Unknown23185('PMI_PersonaEXBufula', 100)
        if (SLOT_48 == 4310):
            Unknown23185('PMI_PersonaBufudyne', 200)
        if (SLOT_48 == 4311):
            Unknown23185('PMI_PersonaBufudyneSP', 200)
        if (SLOT_48 == 4312):
            Unknown23185('PMI_PersonaBufudyne_DSD', 200)
        if (SLOT_48 == 4313):
            Unknown23185('PMI_PersonaBufudyneSP_DSD', 200)
        if (SLOT_48 == 4500):
            Unknown23185('PMI_PersonaIchigeki1', 300)
        if (SLOT_48 == 4501):
            Unknown23185('PMI_PersonaIchigeki2', 300)
        if (SLOT_48 == 9999):
            Unknown23185('PersonaDeleteAndIdling', 300)
        if (SLOT_48 == 6100):
            Unknown23185('PMI_PersonaMatchWin', 300)

@Subroutine
def PersonaReset():
    Unknown4061(1)
    Unknown23022(0)
    Unknown2053(0)
    Unknown23015(11)
    Unknown2019(-1)
    Unknown1084(1)
    Unknown4009(0)
    Unknown4008(0)
    Unknown4007(0)
    EnableCollision(0)
    Unknown30041('')
    Unknown3031()

@Subroutine
def PMI_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PMI_AttackInit():
    Unknown23028(1, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    SLOT_11 = 100
    callSubroutine('PMI_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PMI_SPAttackInit():
    Unknown23028(2, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    SLOT_11 = 110
    callSubroutine('PMI_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PMI_DDAttackInit():
    Unknown23028(3, 1)
    Unknown30037('')
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    SLOT_11 = 120
    callSubroutine('PMI_ReceptionSignal')
    Unknown23023()

@Subroutine
def PMI_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PMI_ForceWarp():
    SLOT_58 = 1
    Unknown3001(0)
    Unknown3004(85)
    loopRelated(17, 4)

    def upon_17():
        Unknown3001(255)
        Unknown3004(0)

@State
def PersonaDeleteAndIdling():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
    sprite('keep', 32767)
    if SLOT_143:
        GFX_0('PersonaDeleteEffect', 100)
        SFX_0('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PMI_PersonaWait')

@State
def PersonaSummonEffect():
    sprite('null', 30)
    Unknown23015(13)
    Unknown4054(11)
    Unknown4045('persona_summon', 100)

@State
def PersonaSummonEffect_PLAYER():
    sprite('null', 30)
    Unknown1007(288000)
    teleportRelativeX(112000)
    GFX_1('persona_summon_ply', 100)

@State
def PersonaDeleteEffect():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        callSubroutine('PMI_ReceptionSignal')
    sprite('null', 30)
    Unknown2019(1)
    Unknown23053('190000000b000000')
    Unknown4061(1)
    Unknown3032()
    Unknown1059(-100)
    Unknown1067(150)
    Unknown3004(-20)
    Unknown23022(1)
    Unknown4054(11)
    Unknown4045('persona_delete', 100)
    Unknown2054(1)
    EnableCollision(0)
    Unknown1084(1)

@State
def PMI_Persona4A6th():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 0, 0, -200000, 200000, 0, 0)
        callSubroutine('PMI_AttackInit')
        AttackLevel_(3)
        Damage(1000)
        AttackP1(90)
        Unknown11092(1)
        Hitstop(1)
        Unknown9310(10)
        Unknown9266(9)
        Unknown23078(0)
        Unknown4007(3)
        EnableCollision(1)
        Unknown2053(1)
        callSubroutine('PMI_CheckWarp')
        Unknown11044(1)

        def upon_56():

            def upon_44():
                sendToLabel(2)
            sendToLabel(1)
        Unknown23059(1)
    sprite('ar204_00', 3)
    sprite('ar204_01', 1)
    physicsXImpulse(80000)
    Unknown4007(0)
    sprite('ar204_01', 1)
    Unknown1019(60)
    sprite('ar204_01', 1)
    Unknown1019(60)
    label(0)
    sprite('ar204_02', 2)
    Unknown1019(0)
    SLOT_51 = (SLOT_51 + 1)
    sprite('ar204_03', 1)
    GFX_0('aref_204', 100)
    RefreshMultihit()
    AirPushbackY(-5000)
    AirPushbackX(0)
    PushbackX(4000)
    SFX_3('hit_h_middle')
    sprite('ar204_03', 1)
    Unknown23022(0)
    sprite('ar204_04', 2)
    sprite('ar204_05', 2)
    sprite('ar204_06', 2)
    RefreshMultihit()
    AirPushbackY(-5000)
    AirPushbackX(-2000)
    PushbackX(8000)
    SFX_3('hit_l_slow')
    sprite('ar204_07', 2)
    sprite('ar204_08', 2)
    sprite('ar204_09', 3)
    RefreshMultihit()
    AirPushbackY(-15000)
    AirPushbackX(2000)
    PushbackX(2000)
    SFX_3('hit_m_middle')
    if (SLOT_51 == 1):
        AirUntechableTime(40)
        Unknown9310(0)
        AirPushbackY(-100000)
        AirPushbackX(10000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9190(1)
        Unknown9118(30)
        Unknown30088(1)
    sprite('ar204_10', 4)
    Unknown23029(3, 7000, 0)
    if (SLOT_51 == 1):
        sendToLabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ar204_11', 3)
    physicsXImpulse(0)
    clearUponHandler(56)
    sprite('ar204_12', 4)
    sprite('ar204_13', 4)
    sprite('ar204_14', 4)
    sprite('ar204_12', 5)
    sprite('ar204_13', 5)
    sprite('ar204_14', 5)
    sprite('ar204_12', 5)
    sprite('ar204_13', 5)
    sprite('ar204_14', 5)
    label(2)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_Persona5A4th():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 0, 0, -200000, 200000, 0, 0)
        callSubroutine('PMI_AttackInit')
        AttackLevel_(3)
        Damage(1000)
        AttackP1(90)
        Unknown11092(1)
        Hitstop(1)
        Unknown9310(10)
        Unknown9266(9)
        Unknown23078(0)
        Unknown4007(3)
        EnableCollision(1)
        Unknown2053(1)
        callSubroutine('PMI_CheckWarp')
        Unknown11044(1)

        def upon_56():

            def upon_44():
                sendToLabel(2)
            sendToLabel(1)
        Unknown23059(1)
    sprite('ar204_00', 3)
    sprite('ar204_01', 1)
    physicsXImpulse(150000)
    Unknown4007(0)
    sprite('ar204_01', 1)
    Unknown1019(60)
    sprite('ar204_01', 1)
    Unknown1019(60)
    label(0)
    sprite('ar204_02', 2)
    Unknown1019(0)
    SLOT_51 = (SLOT_51 + 1)
    sprite('ar204_03', 1)
    GFX_0('aref_204', 100)
    RefreshMultihit()
    AirPushbackY(-5000)
    AirPushbackX(0)
    PushbackX(4000)
    SFX_3('hit_h_middle')
    sprite('ar204_03', 1)
    Unknown23022(0)
    sprite('ar204_04', 2)
    sprite('ar204_05', 2)
    sprite('ar204_06', 2)
    RefreshMultihit()
    AirPushbackY(-5000)
    AirPushbackX(-2000)
    PushbackX(8000)
    SFX_3('hit_l_slow')
    sprite('ar204_07', 2)
    sprite('ar204_08', 2)
    sprite('ar204_09', 3)
    RefreshMultihit()
    AirPushbackY(-15000)
    AirPushbackX(2000)
    PushbackX(2000)
    SFX_3('hit_m_middle')
    if (SLOT_51 == 1):
        AirUntechableTime(40)
        Unknown9310(0)
        AirPushbackY(-100000)
        AirPushbackX(10000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9190(1)
        Unknown9118(30)
        Unknown30088(1)
    sprite('ar204_10', 4)
    Unknown23029(3, 7000, 0)
    if (SLOT_51 == 1):
        sendToLabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ar204_11', 3)
    physicsXImpulse(0)
    clearUponHandler(56)
    sprite('ar204_12', 4)
    sprite('ar204_13', 4)
    sprite('ar204_14', 4)
    sprite('ar204_12', 5)
    sprite('ar204_13', 5)
    sprite('ar204_14', 5)
    sprite('ar204_12', 5)
    sprite('ar204_13', 5)
    sprite('ar204_14', 5)
    label(2)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_Persona5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 0, 0, -200000, 200000, 0, 0)
        callSubroutine('PMI_AttackInit')
        AttackLevel_(3)
        Damage(250)
        AttackP1(60)
        Unknown11092(1)
        Hitstop(1)
        Unknown9310(10)
        Unknown9266(9)
        Unknown23078(0)
        Unknown4007(3)
        EnableCollision(1)
        Unknown2053(1)
        callSubroutine('PMI_CheckWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
        Unknown23059(1)
    sprite('ar204_00', 4)
    sprite('ar204_01', 3)
    Unknown4007(0)
    sprite('ar204_01', 3)
    physicsXImpulse(80000)
    Unknown1019(60)
    sprite('ar204_01', 2)
    Unknown1019(60)
    label(0)
    sprite('ar204_02', 2)
    Unknown1019(0)
    sprite('ar204_03', 1)
    GFX_0('aref_204', 100)
    RefreshMultihit()
    AirPushbackY(-5000)
    AirPushbackX(0)
    PushbackX(4000)
    SFX_3('hit_h_middle')
    sprite('ar204_03', 1)
    Unknown23022(0)
    sprite('ar204_04', 2)
    sprite('ar204_05', 2)
    sprite('ar204_06', 2)
    RefreshMultihit()
    AirPushbackY(-5000)
    AirPushbackX(-2000)
    PushbackX(8000)
    SFX_3('hit_l_slow')
    sprite('ar204_07', 2)
    sprite('ar204_08', 2)
    sprite('ar204_09', 3)
    
    def upon_3():
        if CheckInput(0x0E):
            AirUntechableTime(40)
            Unknown9310(0)
            AirPushbackY(-100000)
            AirPushbackX(10000)
            AirHitstunAnimation(9)
            GroundedHitstunAnimation(9)
            Unknown9190(1)
            Unknown9118(30)
            SLOT_51 = 12
        else:
            if (not CheckInput(0x0E)):
                SLOT_51 = (SLOT_51 + 1)
            if (SLOT_51 >= 10):
                AirUntechableTime(40)
                Unknown9310(0)
                AirPushbackY(-100000)
                AirPushbackX(10000)
                AirHitstunAnimation(9)
                GroundedHitstunAnimation(9)
                Unknown9190(1)
                Unknown9118(30)       
                
    RefreshMultihit()
    AirPushbackY(-15000)
    AirPushbackX(2000)
    PushbackX(2000)
    SFX_3('hit_m_middle')   
    sprite('ar204_10', 4)

    if (not CheckInput(0xa)):
                sendToLabel(1)
    
    Unknown23029(3, 7000, 0)
    def upon_3():
        if CheckInput(0x0E):
            SLOT_51 = 12
            
    if (SLOT_51 >= 12):
        sendToLabel(1)
    loopRest()
    gotoLabel(0) 
    label(1)
    sprite('ar204_11', 3)
    physicsXImpulse(0)
    clearUponHandler(3)
    sprite('ar204_12', 4)
    sprite('ar204_13', 4)
    sprite('ar204_14', 4)
    SLOT_10 = 0
    sprite('ar204_12', 5)
    sprite('ar204_13', 5)
    sprite('ar204_14', 5)
    sprite('ar204_12', 5)
    sprite('ar204_13', 5)
    sprite('ar204_14', 5)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_Persona6PS():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -150000, 0, -500000, 300000, 0, 0)
        callSubroutine('PMI_AttackInit')
        AttackLevel_(3)
        Hitstop(6)
        Unknown9266(9)
        Unknown11042(1)
        EnableCollision(0)
        Unknown2053(1)
        Unknown2034(1)
        Unknown2019(501)
        callSubroutine('PMI_CheckWarp')
    sprite('ar432_00', 6)
    sprite('ar432_01', 3)
    sprite('ar432_02', 3)
    sprite('ar432_03', 3)
    sprite('ar432_04', 3)
    SFX_3('ice_fast')
    GFX_0('Tsurara_Shot', 0)
    Unknown23029(1, 4321, 0)
    GFX_0('Tsurara_Shot', 1)
    Unknown23029(1, 4324, 0)
    sprite('ar432_05', 3)
    SFX_3('ice_fast')
    GFX_0('Tsurara_Shot', 0)
    Unknown23029(1, 4322, 0)
    GFX_0('Tsurara_Shot', 1)
    Unknown23029(1, 4323, 0)
    sprite('ar432_06', 3)
    SFX_3('ice_fast')
    GFX_0('Tsurara_Shot', 0)
    Unknown23029(1, 4323, 0)
    GFX_0('Tsurara_Shot', 1)
    Unknown23029(1, 4322, 0)
    sprite('ar432_07', 3)
    SFX_3('ice_fast')
    GFX_0('Tsurara_Shot', 0)
    Unknown23029(1, 4324, 0)
    GFX_0('Tsurara_Shot', 1)
    Unknown23029(1, 4321, 0)
    sprite('ar432_08', 3)
    sprite('ar432_09', 3)
    sprite('ar432_10', 3)
    sprite('ar432_19', 3)
    Unknown21015('Tsurara_Shot', 4325, 0)
    sprite('ar432_20', 6)
    sprite('ar432_21', 6)
    sprite('ar432_22', 6)
    sprite('ar432_20', 6)
    sprite('ar432_21', 6)
    sprite('ar432_22', 6)
    sprite('ar432_20', 6)
    sprite('ar432_21', 6)
    sprite('ar432_22', 6)
    sprite('ar432_20', 6)
    sprite('ar432_21', 6)
    sprite('ar432_22', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_Persona4PS():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -50000, 50000, 0, 0, 0, 0)
        callSubroutine('PMI_SPAttackInit')
        AttackLevel_(4)
        AttackP1(70)
        Hitstop(7)
        AirUntechableTime(60)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-4000)
        AirPushbackY(28000)
        YImpluseBeforeWallbounce(1500)
        AttackAttributes(1, 0, 0, 0, 0)
        Unknown9266(9)
        Unknown23078(1)
        Unknown11056(2)
        Unknown11042(1)
        AttackAttributes(0, 1, 0, 0, 0)
        callSubroutine('PMI_CheckWarp')
        Unknown23059(1)
    sprite('ar254_00', 4)
    sprite('ar254_01', 3)
    GFX_0('aref_254', 100)
    sprite('ar254_02', 1)
    SFX_3('slash_pole_middle')
    RefreshMultihit()
    sprite('ar254_02', 3)
    sprite('ar254_03', 4)
    sprite('ar254_04', 4)
    Unknown23029(3, 7000, 0)
    sprite('ar254_05', 4)
    sprite('ar254_06', 4)
    sprite('ar254_07', 5)
    sprite('ar254_08', 5)
    sprite('ar254_09', 5)
    sprite('ar254_10', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_Persona2B2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 0, -200000, 200000, 0, 0)
        callSubroutine('PMI_AttackInit')
        AttackLevel_(5)
        Damage(1300)
        Hitstop(7)
        AirPushbackX(20000)
        AirPushbackY(24000)
        YImpluseBeforeWallbounce(1500)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        PushbackX(3000)
        Unknown9266(9)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        callSubroutine('PMI_CheckWarp')

        def upon_77():
            SLOT_51 = 1
    sprite('ar233_00', 4)
    Unknown2006()
    sprite('ar233_01', 4)
    sprite('ar233_02', 4)
    GFX_1('mief_muchispeeds_04', 0)
    SFX_3('slash_sword_middle')
    sprite('ar233_03', 2)
    GFX_1('mief_muchispeeds_04', 0)
    GFX_0('MuchiAura2D', 1)
    RefreshMultihit()
    SFX_3('ice_fast')
    sprite('ar233_03a', 1)
    if (not SLOT_51):
        Unknown23029(3, 7000, 0)
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar233_03a', 1)
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar233_04', 1)
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar233_04', 1)
    GFX_1('mief_muchispeeds_04', 1)
    sprite('ar233_04a', 1)
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar233_04a', 1)
    GFX_1('mief_muchispeeds_04', 1)
    sprite('ar233_03b', 1)
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar234_00', 1)
    StartMultihit()
    sprite('ar234_01', 1)
    sprite('ar234_02', 1)
    StartMultihit()
    if SLOT_51:
        GFX_0('2BBhikiyose', -1)
    SFX_3('slash_rapier_fast')
    sprite('ar234_03', 4)
    sprite('ar234_04', 4)
    sprite('ar234_05', 3)
    sprite('ar234_06', 3)
    sprite('ar234_07', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def __2BBhikiyose():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(1300)
        Hitstop(0)
        AirUntechableTime(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(-5000)
        AirPushbackY(-30000)
        PushbackX(-60000)
        Unknown9190(1)
        Unknown9118(20)
        Unknown9266(9)
        Unknown23151(22, 103)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 2331, 0)
        Unknown23059(1)
    sprite('dmy_atk01', 1)
    RefreshMultihit()
    sprite('null', 1)
    Unknown23029(3, 7000, 0)

@State
def PMI_PersonaAir5A2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -50000, 50000, -200000, 200000, 0, 0)
        callSubroutine('PMI_AttackInit')
        AttackLevel_(4)
        AirUntechableTime(28)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AttackAttributes(1, 0, 0, 0, 0)
        Unknown9266(9)
        Unknown23078(1)
        callSubroutine('PMI_CheckWarp')
        Unknown4007(3)
    sprite('ar254_00', 4)
    Unknown1007(-80000)
    sprite('ar254_01', 3)
    GFX_0('aref_254', 100)
    sprite('ar254_02', 1)
    SFX_3('slash_pole_middle')
    RefreshMultihit()
    sprite('ar254_02', 3)
    sprite('ar254_03', 4)
    sprite('ar254_04', 4)
    sprite('ar254_05', 4)
    sprite('ar254_06', 4)
    sprite('ar254_07', 5)
    sprite('ar254_08', 5)
    sprite('ar254_09', 5)
    sprite('ar254_10', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaAir5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -50000, 50000, -200000, 200000, 0, 0)
        callSubroutine('PMI_AttackInit')
        AttackLevel_(5)
        Damage(1300)
        Hitstop(7)
        AirPushbackX(15000)
        AirPushbackY(14000)
        YImpluseBeforeWallbounce(2500)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        PushbackX(3000)
        AttackAttributes(1, 0, 0, 0, 0)
        Unknown9266(9)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        callSubroutine('PMI_CheckWarp')

        def upon_77():
            SLOT_51 = 1
        Unknown23059(1)
    sprite('ar255_00', 12)
    sprite('ar255_01', 4)
    sprite('ar255_02', 2)
    GFX_1('mief_muchispeeda_04', 0)
    SFX_3('slash_sword_middle')
    sprite('ar255_02', 2)
    GFX_1('mief_muchispeeda_04', 1)
    GFX_0('MuchAuraAir5D', 2)
    sprite('ar255_03', 2)
    GFX_1('mief_muchispeeda_04', 0)
    SFX_3('ice_fast')
    RefreshMultihit()
    sprite('ar255_03a', 2)
    GFX_1('mief_muchispeeda_04', 0)
    sprite('ar255_04', 2)
    sprite('ar255_04a', 2)
    sprite('ar255_05', 1)
    sprite('ar256_00', 1)
    if (not SLOT_51):
        Unknown23029(3, 7000, 0)
    sprite('ar256_01', 1)
    sprite('ar256_02', 1)
    sprite('ar256_03', 1)
    sprite('ar256_04', 4)
    StartMultihit()
    if SLOT_51:
        GFX_0('Air5Chikiyose', -1)
    SFX_3('slash_rapier_fast')
    sprite('ar256_05', 5)
    sprite('ar256_06', 5)
    sprite('ar256_07', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def Air5Chikiyose():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(1300)
        Hitstop(0)
        AirUntechableTime(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(-10000)
        AirPushbackY(40000)
        PushbackX(-60000)
        YImpluseBeforeWallbounce(2200)
        Unknown9266(9)
        Unknown23151(22, 103)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 2551, 0)
    sprite('dmy_atk01', 1)
    RefreshMultihit()
    sprite('null', 1)
    Unknown23029(3, 7000, 0)

@State
def PMI_PersonaMarinKarin():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 0, -200000, 200000, 0, 0)
        callSubroutine('PMI_SPAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
    sprite('ar232_00', 4)
    Unknown2006()
    sprite('ar232_01', 4)
    sprite('ar232_02', 4)
    sprite('ar232_03', 3)
    sprite('ar232_04', 3)
    sprite('ar232_05', 3)
    sprite('ar232_06', 1)
    GFX_0('MarinKarin_shot', 0)
    sprite('ar232_06', 4)
    Unknown23022(0)
    sprite('ar232_07', 5)
    sprite('ar232_08', 5)
    sprite('ar232_06', 5)
    sprite('ar232_07', 5)
    sprite('ar232_08', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaTentarafoo():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 0, 0, 0, 0, 0)
        callSubroutine('PMI_SPAttackInit')
        callSubroutine('PMI_CheckWarp')

        def upon_3():
            if SLOT_51:
                clearUponHandler(3)
                sendToLabel(1)

        def upon_56():
            clearUponHandler(3)
        Unknown2006()
        Unknown23022(1)
    sprite('ar403_00', 4)
    GFX_0('aref_403_hand', 0)
    sprite('ar403_01', 4)
    sprite('ar403_02', 4)
    sprite('ar403_03', 4)
    sprite('ar403_04', 6)
    SFX_3('hit_m_fast')
    Unknown26('aref_403_hand')
    sprite('ar403_05', 6)
    GFX_0('Tentarafu_dmy', 0)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('ar403_07', 4)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('ar403_07', 4)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('ar403_07', 4)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('ar403_07', 4)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    Unknown21015('Tentarafu_dmy', 4032, 0)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaEXTentarafoo():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 0, 0, 0, 0, 0)
        callSubroutine('PMI_SPAttackInit')
        callSubroutine('PMI_CheckWarp')

        def upon_3():
            if SLOT_51:
                clearUponHandler(3)
                sendToLabel(1)

        def upon_56():
            clearUponHandler(3)
        Unknown2006()
        Unknown23022(1)
    sprite('ar403_00', 3)
    GFX_0('aref_403_hand', 0)
    sprite('ar403_01', 3)
    sprite('ar403_02', 3)
    sprite('ar403_03', 2)
    sprite('ar403_04', 3)
    SFX_3('hit_m_fast')
    Unknown26('aref_403_hand')
    sprite('ar403_05', 3)
    GFX_0('EXTentarafu_dmy', 0)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('ar403_07', 4)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('ar403_07', 4)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('ar403_07', 4)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('ar403_07', 4)
    sprite('ar403_05', 4)
    sprite('ar403_06', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    Unknown21015('EXTentarafu_dmy', 4032, 0)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 3)
    sprite('ar403_07', 3)
    sprite('ar403_05', 3)
    sprite('ar403_06', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaABufula():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 0, -300000, 1000000, -1000000, 1000000)
        callSubroutine('PMI_SPAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23059(1)
    sprite('ar402_00', 4)
    GFX_0('AIceMiller_Shot', 0)
    sprite('ar402_01', 4)
    sprite('ar402_02', 4)
    sprite('ar402_03', 4)
    sprite('ar402_04', 4)
    sprite('ar402_05', 6)
    sprite('ar402_06', 6)
    sprite('ar402_07', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBBufula():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 0, -300000, 1000000, -1000000, 1000000)
        callSubroutine('PMI_SPAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23059(1)
    sprite('ar402_00', 4)
    GFX_0('BIceMiller_Shot', 0)
    sprite('ar402_01', 4)
    sprite('ar402_02', 4)
    sprite('ar402_03', 4)
    sprite('ar402_04', 4)
    sprite('ar402_05', 6)
    sprite('ar402_06', 6)
    sprite('ar402_07', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaEXBufula():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 0, -300000, 1000000, -1000000, 1000000)
        callSubroutine('PMI_SPAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23059(1)
    sprite('ar402_00', 4)
    GFX_0('EXIceMiller_Shot', 0)
    sprite('ar402_01', 4)
    sprite('ar402_02', 4)
    sprite('ar402_03', 4)
    sprite('ar402_04', 4)
    sprite('ar402_05', 6)
    sprite('ar402_06', 6)
    sprite('ar402_07', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBufudyne():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -50000, 100000, 0, 0, 0, 0)
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
        Unknown2054(1)
    sprite('ar431_00', 6)
    sprite('ar431_01', 6)
    sprite('ar431_02', 6)
    sprite('ar431_03', 6)
    GFX_0('aref_431C', 100)
    GFX_0('aref_431_colC', 100)
    sprite('ar431_04', 4)
    sprite('ar431_05', 4)
    sprite('ar431_06', 6)
    sprite('ar431_07', 6)
    sprite('ar431_08', 6)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBufudyneSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -50000, 100000, 0, 0, 0, 0)
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
        Unknown2054(1)
    sprite('ar431_00', 6)
    sprite('ar431_01', 6)
    sprite('ar431_02', 6)
    sprite('ar431_03', 6)
    GFX_0('aref_431CD', 100)
    GFX_0('aref_431_colCD', 100)
    sprite('ar431_04', 4)
    sprite('ar431_05', 4)
    sprite('ar431_06', 6)
    sprite('ar431_07', 6)
    sprite('ar431_08', 6)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBufudyne_DSD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -50000, 100000, 0, 0, 0, 0)
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
        Unknown2054(1)
    sprite('ar431_00', 6)
    sprite('ar431_01', 6)
    sprite('ar431_02', 6)
    sprite('ar431_03', 6)
    GFX_0('aref_431C', 100)
    GFX_0('aref_431_colC_DSD', 100)
    sprite('ar431_04', 4)
    sprite('ar431_05', 4)
    sprite('ar431_06', 6)
    sprite('ar431_07', 6)
    sprite('ar431_08', 6)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBufudyneSP_DSD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -50000, 100000, 0, 0, 0, 0)
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
        Unknown2054(1)
    sprite('ar431_00', 6)
    sprite('ar431_01', 6)
    sprite('ar431_02', 6)
    sprite('ar431_03', 6)
    GFX_0('aref_431CD', 100)
    GFX_0('aref_431_colCD_DSD', 100)
    sprite('ar431_04', 4)
    sprite('ar431_05', 4)
    sprite('ar431_06', 6)
    sprite('ar431_07', 6)
    sprite('ar431_08', 6)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('ar431_06', 8)
    sprite('ar431_07', 8)
    sprite('ar431_08', 8)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def mief203_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi203_00', 2)
    sprite('vr_mi203_01', 2)
    sprite('vr_mi203_02', 30)

@State
def mief207_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(-100000)
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi207_00', 30)

@State
def mief201_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi201_00', 2)
    sprite('vr_mi201_01', 2)
    teleportRelativeX(-182000)
    sprite('vr_mi201_02', 30)
    teleportRelativeX(-30000)

@State
def mief202_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi202_00', 1)
    sprite('vr_mi202_01', 3)
    sprite('vr_mi202_02', 30)

@State
def mief210_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi210_00', 2)
    sprite('vr_mi210_01', 2)
    sprite('vr_mi210_02', 3)

@State
def mief211_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi211_00', 2)
    sprite('vr_mi211_01', 30)

@State
def mief211_Zanzoh_CA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi211_00', 2)
    sprite('vr_mi211_01', 28)

@State
def aref_204():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref204_muchi00.DIG', '')
        Unknown4015()
    sprite('null', 30)
    GFX_1('mief_slashkira_01', 100)

@State
def MuchiAura2D():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        GFX_2('mief_muchisentan_02')
        Unknown1072(-30000)
    sprite('null', 8)
    physicsXImpulse(30000)
    physicsYImpulse(15000)
    sprite('null', 5)
    Unknown3004(-51)

@State
def aref_254():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref254_muchi00.DIG', '')
        Unknown3032()
        Unknown4015()
    sprite('null', 15)
    GFX_1('mief_slashkira_01', 100)

@State
def MuchAuraAir5D():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        GFX_2('mief_muchisentan_02')
        Unknown1072(30000)
    sprite('null', 6)
    physicsXImpulse(40000)
    physicsYImpulse(-21000)
    sprite('null', 5)
    Unknown3004(-51)

@State
def mief_311():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
    sprite('vr_mi311_00', 2)
    sprite('vr_mi311_01', 2)
    sprite('vr_mi311_02', 2)
    sprite('vr_mi311_03', 2)
    sprite('vr_mi311_04', 2)

@State
def mief_311_HitEff():

    def upon_IMMEDIATE():
        Unknown23151(22, 105)
        Unknown23067('ef_hit_slashm')
        Unknown4049(500)
        Unknown4053(30000, 150000)
        Unknown4045('ef_hitlz00', 100)
        SFX_3('damage_slash_h')
    sprite('null', 10)

@State
def mief_311_finish():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi311_10', 4)
    sprite('vr_mi311_11', 16)

@State
def Tsurara_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(600)
        AttackP1(70)
        AttackP2(97)
        Unknown11042(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(50)
        Unknown9016(1)
        Unknown9266(9)
        Unknown11057(500)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(2, 9)
        sendToLabelUpon(54, 9)

        def upon_43():
            if (SLOT_48 == 4321):
                SLOT_51 = 1
                physicsYImpulse(400)
                Unknown1007(400)
            if (SLOT_48 == 4322):
                SLOT_51 = 2
                physicsYImpulse(-400)
                Unknown1007(-400)
            if (SLOT_48 == 4323):
                SLOT_51 = 3
                physicsYImpulse(-400)
                Unknown1007(-400)
            if (SLOT_48 == 4324):
                SLOT_51 = 4
                physicsYImpulse(400)
                Unknown1007(400)
                SLOT_52 = 1
            if (SLOT_48 == 4325):
                if (SLOT_51 > 0):
                    sendToLabel(1)
            if (SLOT_48 == 4326):
                sendToLabel(9)
        Unknown4061(3)
        Unknown3033()
        GFX_0('aref_432_pa', 100)
        Unknown38(4, 1)
        DisableAttackRestOfMove()
    sprite('vr_ar432_00', 15)
    label(5)
    sprite('vr_ar432_00', 30)
    YAccel(-100)
    loopRest()
    gotoLabel(5)
    label(1)
    sprite('vr_ar432_00', 5)
    Unknown4010(0)
    Unknown1074(30000)
    if SLOT_52:
        SFX_3('slash_rapier_fast')
    sprite('vr_ar432_00', 5)
    if SLOT_52:
        SFX_3('slash_rapier_fast')
    sprite('vr_ar432_00', 5)
    if SLOT_52:
        SFX_3('slash_rapier_fast')
    sprite('vr_ar432_00', 5)
    RefreshMultihit()
    Unknown1074(0)
    Unknown1072(0)
    SLOT_12 = SLOT_19
    Unknown1019(5)
    if (SLOT_12 < 20000):
        SLOT_12 = 20000
    Unknown1028(300)
    Unknown47('0100000000000000400d03000200000017000000020000000d000000')
    YAccel(5)
    Unknown1108(0)
    GFX_1('aref_turarashot_fire', 100)
    GFX_0('aref_432_move', 100)
    Unknown38(5, 1)
    if SLOT_52:
        SFX_3('slash_rapier_fast')
    sprite('vr_ar432_00', 180)
    Unknown53(1)
    label(9)
    sprite('null', 30)
    physicsXImpulse(0)
    physicsYImpulse(0)
    DisableAttackRestOfMove()
    Unknown13(4)
    Unknown13(5)
    GFX_1('aref_turarashot_delete', 100)

@State
def aref_432_pa():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 1)
    GFX_1('aref_turarashot', 100)
    loopRest()
    gotoLabel(0)

@State
def aref_432_move():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 1)
    GFX_1('aref_turarashot_move', 100)
    loopRest()
    gotoLabel(0)

@State
def mief_400():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('mief400_slash.DIG', '')
        Unknown4015()
        Unknown23015(1)
        Unknown4061(0)
        Unknown23122(55)
    sprite('null', 5)
    Unknown1096(750)
    Unknown1099(20)
    teleportRelativeX(-16000)
    Unknown1007(64000)
    Unknown1097(20)
    sprite('null', 6)
    teleportRelativeX(-16000)
    Unknown1007(-64000)
    Unknown1097(80)
    sprite('null', 6)
    Unknown1099(0)
    Unknown3004(-48)
    teleportRelativeX(16000)
    Unknown1007(-4000)

@State
def mief_400_2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('mief400_slash2.DIG', '')
        Unknown4015()
        Unknown23015(1)
        Unknown4061(0)
        Unknown23122(55)
    sprite('null', 5)
    Unknown1096(750)
    Unknown1099(20)
    Unknown3001(0)
    Unknown3004(32)
    teleportRelativeX(-16000)
    Unknown1007(64000)
    Unknown1097(20)
    sprite('null', 6)
    Unknown3001(255)
    Unknown3004(0)
    teleportRelativeX(-16000)
    Unknown1007(-64000)
    Unknown1097(80)
    sprite('null', 6)
    Unknown1099(0)
    Unknown3004(-48)
    teleportRelativeX(16000)
    Unknown1007(-8000)

@State
def mief_401():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(0)
        Unknown23122(55)
        Unknown4010(2)
        Unknown4003('aref401_tsuki00.DIG', '')
        Unknown4015()

        def upon_43():
            if (SLOT_48 == 4011):
                clearUponHandler(43)
                sendToLabel(10)
            if (SLOT_48 == 4012):
                clearUponHandler(43)
                sendToLabel(100)
    sprite('null', 6)
    Unknown3001(150)
    GFX_0('mief401_shock', 100)
    sprite('null', 5)
    Unknown1067(-200)
    Unknown1059(100)
    Unknown3004(51)
    ExitState()
    label(10)
    sprite('null', 13)
    sprite('null', 5)
    Unknown1067(-200)
    Unknown1059(100)
    Unknown3004(51)
    ExitState()
    label(100)
    sprite('null', 5)
    sprite('null', 5)
    Unknown1067(-200)
    Unknown1059(100)
    Unknown3004(51)

@State
def mief401_shock():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref401_tsuki01.DIG', '')
        Unknown4015()
        Unknown4061(0)
        Unknown23122(55)
        Unknown3001(150)
        Unknown3033()
    sprite('null', 12)
    GFX_0('mief401_shockAdd', 100)

@State
def mief401_shockAdd():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3001(120)
        Unknown3033()
    sprite('vr_mi401_add', 5)
    Unknown1067(-55)
    sprite('vr_mi401_add', 5)
    Unknown3004(-51)

@State
def MarinKarin_shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Unknown11001(0, 10, 10)
        Unknown11050(8, 'status_charm_damage')
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 1)
        Unknown11106(0)
        Unknown2053(1)
        DisableAttackRestOfMove()
        Unknown4061(3)
        Unknown3032()
        Unknown3029(1)
        Unknown3070(2)
        AfterimageCount(10)
        AfterimageMask_1(0, 255, 255, 255)
        AfterimageMask_2(0, 255, 255, 255)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 2321):
                clearUponHandler(43)
                Unknown23090(25)

        def upon_78():
            SFX_3('mi004')
            ConsumeSuperMeter(1800)
            Unknown36(22)
            ConsumeSuperMeter(-2500)
            Unknown35()
    sprite('vr_ar232_00', 2)
    GFX_0('MarinKarin_Jizoku', 0)
    GFX_1('mief_marincarin_02', 0)
    Unknown1072(12000)
    Unknown1096(500)
    sprite('vr_ar232_01', 2)
    GFX_1('mief_marincarin_02', 0)
    Unknown1096(600)
    sprite('vr_ar232_02', 2)
    Unknown1096(700)
    sprite('vr_ar232_03', 2)
    GFX_1('mief_marincarin_02', 0)
    Unknown1096(900)
    sprite('vr_ar232_04', 2)
    Unknown1096(1000)
    sprite('vr_ar232_05', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_06', 2)
    sprite('vr_ar232_07', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_08', 2)
    RefreshMultihit()
    sprite('vr_ar232_09', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_10', 2)
    SFX_3('slash_knife_slow')
    sprite('vr_ar232_11', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_12', 2)
    sprite('vr_ar232_13', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_14', 2)
    sprite('vr_ar232_15', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_16', 2)
    sprite('vr_ar232_17', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_18', 2)
    sprite('vr_ar232_19', 2)
    GFX_1('mief_marincarin_02', 0)
    SFX_3('badst_charm_damage')
    physicsXImpulse(1000)
    physicsYImpulse(1000)
    setGravity(0)

    def upon_3():
        Unknown1019(98)
        YAccel(98)
        SLOT_58 = SLOT_40
        if (SLOT_40 > 100):
            SLOT_58 = (SLOT_58 / 5120)
            if SLOT_38:
                SLOT_58 = (SLOT_58 / (-1))
            SLOT_12 = (SLOT_12 + SLOT_58)
        if (SLOT_40 < (-100)):
            SLOT_58 = (SLOT_58 / 5120)
            if SLOT_38:
                SLOT_58 = (SLOT_58 / (-1))
            SLOT_12 = (SLOT_12 + SLOT_58)
        if (SLOT_12 < 5000):
            SLOT_12 = 5000
        SLOT_58 = SLOT_41
        if (SLOT_41 > 100):
            SLOT_58 = (SLOT_58 + 50000)
            SLOT_58 = (SLOT_58 / 5120)
            SLOT_13 = (SLOT_13 + SLOT_58)
        if (SLOT_41 < (-100)):
            SLOT_58 = (SLOT_58 + 50000)
            SLOT_58 = (SLOT_58 / 5120)
            SLOT_13 = (SLOT_13 + SLOT_58)
    SLOT_51 = 4
    label(0)
    sprite('vr_ar232_00', 2)
    SFX_3('slash_knife_slow')
    sprite('vr_ar232_01', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_02', 2)
    sprite('vr_ar232_03', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_04', 2)
    sprite('vr_ar232_05', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_06', 2)
    sprite('vr_ar232_07', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_08', 2)
    sprite('vr_ar232_09', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_10', 2)
    SFX_3('slash_knife_slow')
    sprite('vr_ar232_11', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_12', 2)
    sprite('vr_ar232_13', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_14', 2)
    sprite('vr_ar232_15', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_16', 2)
    sprite('vr_ar232_17', 2)
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_18', 2)
    sprite('vr_ar232_19', 2)
    GFX_1('mief_marincarin_02', 0)
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(1, 2, 51)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_ar232_00', 30)
    GFX_1('mief_maricarifin_04', 0)
    clearUponHandler(3)
    DisableAttackRestOfMove()
    Unknown1084(1)
    Unknown3001(10)

@State
def MarinKarin_Jizoku():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown23067('mief_marinjizoku_00')
        Unknown3032()
    sprite('null', 1200)
    sprite('null', 10)
    Unknown3004(-26)

@State
def Tentarafu_dmy():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        ProjectileDurabilityLvl(2)
        Damage(300)
        AttackP1(70)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(0)
        AirHitstunAnimation(4)
        HitLow(2)
        AttackAttributes(0, 0, 1, 0, 0)
        Unknown9021(1)
        Unknown9266(9)
        Unknown11068(1)
        Unknown11066(1)
        Unknown11044(1)
        Unknown11069('Tentarafu_dmy')
        Unknown3032()
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(1)
        Unknown4061(3)
        Unknown3001(150)
        Unknown3038(1)
        Unknown2073(1)

        def upon_43():
            if (SLOT_48 == 4032):
                clearUponHandler(43)
                sendToLabel(9)

        def upon_77():
            DisableAttackRestOfMove()

        def upon_78():
            clearUponHandler(78)
            PushbackX(0)
            Unknown11064(1)
            FreezeCount(100)
            FreezeDuration(120)
            hitstun(80)
            SLOT_0 = 1
            Unknown48(2, 2, 51, 25, 2, 0)
            Unknown21015('Tentarafoo', 4031, 0)
            Hitstop(0)
            sendToLabel(1)

        def upon_82():
            clearUponHandler(82)
            Unknown9215()
            Unknown11064(0)
            FreezeCount(0)
            FreezeDuration(0)
            Unknown9155()
            Unknown11069('')
    sprite('vr_ar402Freeze00_dmy', 1)
    SFX_3('ice_fast')
    GFX_0('aref_403_ground', 100)
    RefreshMultihit()
    sprite('vr_ar402Freeze00_dmy', 2)
    GFX_0('aref_403_ground_C', 0)
    physicsXImpulse(68000)
    sprite('vr_ar402Freeze00_dmy', 3)
    SFX_3('ice_fast')
    sprite('vr_ar402Freeze00_dmy', 3)
    SFX_3('ice_fast')
    sprite('vr_ar402Freeze00_dmy', 2)
    SFX_3('ice_fast')
    Unknown26('aref_403_ground_C')
    sprite('vr_ar402Freeze00_dmy', 1)
    Unknown1084(1)
    sprite('vr_ar402Freeze00_dmy', 2)
    SFX_3('ice_fast')
    DisableAttackRestOfMove()
    ExitState()
    label(1)
    sprite('null', 1)
    SFX_3('ice_slow')
    physicsXImpulse(0)
    Unknown26('aref_403_ground_C')
    sprite('null', 59)
    GFX_0('aref_403_bind', -1)
    Unknown36(1)
    Unknown23151(22, 104)
    Unknown35()
    Unknown48(25, 2, 51, 22, 2, 83)
    ExitState()
    label(9)
    sprite('vr_ar402Freeze01_dmy', 6)
    Unknown26('aref_403_bind')
    GFX_0('aref_403_damege', -1)
    Unknown36(1)
    Unknown23151(22, 104)
    Unknown35()
    AttackLevel_(4)
    Damage(3000)
    AttackP2(80)
    AirUntechableTime(45)
    AirPushbackY(38000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    FreezeCount(0)
    FreezeDuration(0)
    Unknown9021(1)
    Unknown9266(9)
    Unknown11064(0)
    Unknown11068(0)
    Unknown11066(0)
    Unknown11044(0)
    Unknown30048(1)
    Unknown11069('')
    SLOT_83 = SLOT_51
    Unknown3038(1)
    RefreshMultihit()
    Unknown21015('Tentarafoo', 4033, 0)

@State
def EXTentarafu_dmy():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        ProjectileDurabilityLvl(2)
        Damage(300)
        AttackP1(70)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(0)
        AirHitstunAnimation(4)
        HitLow(2)
        AttackAttributes(0, 0, 1, 0, 0)
        Unknown9021(1)
        Unknown9266(9)
        Unknown11068(1)
        Unknown11066(1)
        Unknown11044(1)
        Unknown11069('EXTentarafu_dmy')
        Unknown3032()
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(1)
        Unknown4061(3)
        Unknown3001(150)
        Unknown3038(1)
        Unknown2073(1)

        def upon_43():
            if (SLOT_48 == 4032):
                clearUponHandler(43)
                sendToLabel(9)

        def upon_77():
            DisableAttackRestOfMove()

        def upon_78():
            clearUponHandler(78)
            PushbackX(0)
            Unknown11064(1)
            FreezeCount(100)
            FreezeDuration(120)
            hitstun(80)
            SLOT_0 = 1
            Unknown48(2, 2, 51, 25, 2, 0)
            Unknown21015('Tentarafoo', 4031, 0)
            Hitstop(0)
            sendToLabel(1)

        def upon_82():
            clearUponHandler(82)
            Unknown9215()
            Unknown11064(0)
            FreezeCount(0)
            FreezeDuration(0)
            Unknown9155()
            Unknown11069('')
    sprite('vr_ar402Freeze00_dmy', 1)
    SFX_3('ice_fast')
    GFX_0('aref_403_ground', 100)
    RefreshMultihit()
    sprite('vr_ar402Freeze00_dmy', 2)
    GFX_0('aref_403_ground_C', 0)
    physicsXImpulse(68000)
    sprite('vr_ar402Freeze00_dmy', 3)
    SFX_3('ice_fast')
    sprite('vr_ar402Freeze00_dmy', 3)
    SFX_3('ice_fast')
    sprite('vr_ar402Freeze00_dmy', 2)
    SFX_3('ice_fast')
    Unknown26('aref_403_ground_C')
    sprite('vr_ar402Freeze00_dmy', 1)
    Unknown1084(1)
    sprite('vr_ar402Freeze00_dmy', 2)
    SFX_3('ice_fast')
    DisableAttackRestOfMove()
    ExitState()
    label(1)
    sprite('null', 1)
    SFX_3('ice_slow')
    physicsXImpulse(0)
    Unknown26('aref_403_ground_C')
    sprite('null', 59)
    GFX_0('aref_403_bind', -1)
    Unknown36(1)
    Unknown23151(22, 104)
    Unknown35()
    Unknown48(25, 2, 51, 22, 2, 83)
    ExitState()
    label(9)
    sprite('vr_ar402Freeze01_dmy', 6)
    Unknown26('aref_403_bind')
    GFX_0('aref_403_damege', -1)
    Unknown36(1)
    Unknown23151(22, 104)
    Unknown35()
    AttackLevel_(4)
    Damage(3000)
    AttackP2(80)
    AirUntechableTime(45)
    AirPushbackY(30000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    FreezeCount(1)
    FreezeDuration(0)
    Unknown9021(1)
    Unknown9266(9)
    Unknown11064(0)
    Unknown11068(0)
    Unknown11066(0)
    Unknown11044(0)
    Unknown30048(1)
    Unknown11069('')
    SLOT_83 = SLOT_51
    Unknown3038(1)
    RefreshMultihit()
    Unknown21015('Tentarafoo', 4033, 0)
    FreezeCount(2)
    FreezeDuration(40)

@State
def aref_403_hand():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('null', 32767)
    Unknown1096(1300)
    Unknown1007(35000)
    teleportRelativeX(-20000)
    GFX_2('aref_403_hand')

@State
def aref_403_ground():

    def upon_IMMEDIATE():
        teleportRelativeX(110000)
        Unknown4010(2)
    sprite('null', 32767)
    GFX_1('aref_403_ground', 100)

@State
def aref_403_ground_C():

    def upon_IMMEDIATE():
        teleportRelativeX(200000)
        physicsXImpulse(75000)
        Unknown4010(2)
    label(0)
    sprite('null', 2)
    GFX_1('aref_403_ground', 100)
    gotoLabel(0)

@State
def aref_403_bind():

    def upon_IMMEDIATE():
        pass
    sprite('null', 60)
    GFX_1('aref_403_ground', 100)
    GFX_2('aref_403_bind')

@State
def aref_403_damege():

    def upon_IMMEDIATE():
        pass
    sprite('null', 60)
    GFX_1('aref_403_damege', 100)

@State
def AIceMiller_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        AttackP2(85)
        AirUntechableTime(60)
        Hitstop(6)
        AirPushbackX(3500)
        AirPushbackY(15000)
        PushbackX(1000)
        YImpluseBeforeWallbounce(1500)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        FreezeCount(1)
        FreezeDuration(30)
        Unknown2053(1)
        Unknown11092(1)
        Unknown9021(1)
        Unknown9266(9)               
      
        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown53(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown11032(150000, -150000, 1000000, -1000000)
        Unknown2053(1)
        Unknown3038(1)
        Unknown23020(2000)
        Unknown23021(2000)
        
        def upon_19():
            Unknown23022(1)
            Unknown23090(25)

        def upon_14():
            Unknown1017()
            sendToLabel(2)
        loopRelated(17, 1000)

        def upon_17():
            sendToLabel(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 1)
        Unknown3032()
        teleportRelativeX(250000)
        teleportRelativeY(230000)
        SFX_3('ice_fast')
        SFX_3('distortion_b')

        def upon_43():
            if (SLOT_31 == 2):
                clearUponHandler(43)
                Unknown23090(25)   
                SLOT_31 = (SLOT_31 - 1)     
        GFX_0('Icemirrorstart_Yugami', 100)
        GFX_0('450icemirrorstart', 100)
        SLOT_31 = (SLOT_31 + 1)   
    sprite('vr_ar402_00', 12)
    StartMultihit()
    Unknown23022(1)
    sprite('vr_ar402_00', 4)
    StartMultihit()
    Unknown23022(0)
    SFX_3('ice_fast')
    Unknown4003('aref402_icemirror.DIG', '')
    Unknown23067('mief_402icemirror')
    Unknown4015()
    sprite('vr_ar402_00', 1)
    StartMultihit()
    physicsXImpulse(5000)
    label(0)
    sprite('vr_ar402_00', 10)
    RefreshMultihit()
    Unknown1019(95)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 12)
    if SLOT_0:
        _gotolabel(1)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('vr_ar402_00', 10)
    physicsXImpulse(-10000)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 12)
    if SLOT_0:
        _gotolabel(1)

    def upon_3():
        Unknown1019(80)
    sprite('vr_ar402_00', 10)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 12)
    if SLOT_0:
        _gotolabel(1)
    loopRest()
    clearUponHandler(3)
    Unknown1018()
    Unknown1019(50)
    if (SLOT_12 < 300):
        SLOT_12 = 300
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(14)
    clearUponHandler(19)
    clearUponHandler(43)
    clearUponHandler(3)
    sprite('vr_ar402_00', 1)
    Unknown1084(1)
    Unknown23119(-16730881, 5, 1)
    Unknown3004(-70)
    GFX_0('450icemirrorbreak', 100)
    SLOT_31 = 0
    ExitState()
    label(3)
    clearUponHandler(17)
    clearUponHandler(14)
    clearUponHandler(19)
    clearUponHandler(43)
    clearUponHandler(3)
    sprite('vr_ar402_00', 1)
    Unknown1084(1)
    Unknown23119(-16730881, 5, 1)
    Unknown3004(-70)
    GFX_0('450icemirrorbreak', 100)
    SLOT_31 = 0

@State
def BIceMiller_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        AttackP2(85)
        Hitstop(6)
        AirPushbackX(-3500)
        AirPushbackY(15000)
        PushbackX(1000)
        YImpluseBeforeWallbounce(1500)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        FreezeCount(1)
        FreezeDuration(30)
        Unknown2053(1)
        Unknown9021(1)
        Unknown9266(9)
        
        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown53(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown11032(150000, -150000, 1000000, -1000000)
        Unknown2053(1)
        Unknown3038(1)
        Unknown23020(2000)
        Unknown23021(2000)
        
        def upon_19():
            Unknown23022(1)
            Unknown23090(25)

        def upon_14():
            Unknown1017()
            sendToLabel(2)
        loopRelated(17, 1000)

        def upon_17():
            sendToLabel(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 1)
        Unknown3032()
        teleportRelativeX(600000)
        SFX_3('ice_fast')
        SFX_3('distortion_b')

        def upon_43():
            if (SLOT_31 == 2):
                clearUponHandler(43)
                Unknown23090(25)
                SLOT_31 = (SLOT_31 - 1)
        GFX_0('Icemirrorstart_Yugami', 100)
        GFX_0('450icemirrorstart', 100)
        SLOT_31 = (SLOT_31 + 1)
    sprite('vr_ar402_00', 12)
    StartMultihit()
    Unknown23022(1)
    sprite('vr_ar402_00', 4)
    StartMultihit()
    Unknown23022(0)
    SFX_3('ice_fast')
    Unknown4003('aref402_icemirror.DIG', '')
    Unknown23067('mief_402icemirror')
    Unknown4015()
    sprite('vr_ar402_00', 1)
    StartMultihit()
    physicsXImpulse(-3000)
    label(0)
    sprite('vr_ar402_00', 10)
    RefreshMultihit()
    Unknown1019(95)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 16)
    if SLOT_0:
        _gotolabel(1)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('vr_ar402_00', 10)
    physicsXImpulse(-10000)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 16)
    if SLOT_0:
        _gotolabel(1)

    def upon_3():
        Unknown1019(80)
    sprite('vr_ar402_00', 10)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 16)
    if SLOT_0:
        _gotolabel(1)
    loopRest()
    clearUponHandler(3)
    Unknown1018()
    Unknown1019(50)
    if (SLOT_12 < 300):
        SLOT_12 = 300
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(14)
    clearUponHandler(19)
    clearUponHandler(43)
    clearUponHandler(3)
    sprite('vr_ar402_00', 1)
    Unknown1084(1)
    Unknown23119(-16730881, 5, 1)
    Unknown3004(-70)
    GFX_0('450icemirrorbreak', 100)
    SLOT_31 = 0
    ExitState()
    label(3)
    clearUponHandler(17)
    clearUponHandler(14)
    clearUponHandler(19)
    clearUponHandler(43)
    clearUponHandler(3)
    sprite('vr_ar402_00', 1)
    Unknown1084(1)
    Unknown23119(-16730881, 5, 1)
    Unknown3004(-70)
    GFX_0('450icemirrorbreak', 100)
    SLOT_31 = 0

@State
def EXIceMiller_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        AttackP2(85)
        AirUntechableTime(60)
        Hitstop(6)
        AirPushbackX(1500)
        AirPushbackY(15000)
        PushbackX(1000)
        YImpluseBeforeWallbounce(1500)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        FreezeCount(3)
        FreezeDuration(30)
        Unknown2053(1)
        Unknown9021(1)
        Unknown9266(9)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown11032(150000, -150000, 1000000, -1000000)
        Unknown2053(1)
        Unknown3038(1)
        Unknown23020(2000)
        Unknown23021(2000)

        def upon_19():
            Unknown23022(1)
            Unknown23090(25)

        def upon_14():
            Unknown1017()
            sendToLabel(2)
        loopRelated(17, 1000)

        def upon_17():
            sendToLabel(1)
        Unknown23089(3, 1, 1, 1, 1, 0, 3, 0)
        sendToLabelUpon(54, 1)
        Unknown3032()
        teleportRelativeX(250000)
        SFX_3('ice_fast')
        SFX_3('distortion_b')

        def upon_43():
            if (SLOT_31 == 2):
                clearUponHandler(43)
                Unknown23090(25)
                SLOT_31 = (SLOT_31 - 1)    
        GFX_0('Icemirrorstart_Yugami', 100)
        GFX_0('450icemirrorstart', 100)
        SLOT_31 = (SLOT_31 + 1)
    sprite('vr_ar402_00', 12)
    StartMultihit()
    Unknown23022(1)
    sprite('vr_ar402_00', 4)
    StartMultihit()
    Unknown23022(0)
    SFX_3('ice_fast')
    Unknown4003('aref402_icemirror.DIG', '')
    Unknown23067('mief_402icemirror')
    Unknown4015()
    sprite('vr_ar402_00', 1)
    StartMultihit()
    physicsXImpulse(3000)
    label(0)
    sprite('vr_ar402_00', 10)
    RefreshMultihit()
    Unknown1019(95)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 36)
    if SLOT_0:
        _gotolabel(1)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('vr_ar402_00', 10)
    physicsXImpulse(-10000)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 36)
    if SLOT_0:
        _gotolabel(1)

    def upon_3():
        Unknown1019(80)
    sprite('vr_ar402_00', 10)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 36)
    if SLOT_0:
        _gotolabel(1)
    loopRest()
    clearUponHandler(3)
    Unknown1018()
    Unknown1019(50)
    if (SLOT_12 < 300):
        SLOT_12 = 300
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(14)
    clearUponHandler(19)
    clearUponHandler(43)
    clearUponHandler(3)
    sprite('vr_ar402_00', 1)
    Unknown1084(1)
    Unknown23119(-16730881, 5, 1)
    Unknown3004(-70)
    GFX_0('450icemirrorbreak', 100)
    SLOT_31 = 0
    ExitState()
    label(3)
    clearUponHandler(17)
    clearUponHandler(14)
    clearUponHandler(19)
    clearUponHandler(43)
    clearUponHandler(3)
    sprite('vr_ar402_00', 1)
    Unknown1084(1)
    Unknown23119(-16730881, 5, 1)
    Unknown3004(-70)
    GFX_0('450icemirrorbreak', 100)
    SLOT_31 = 0

@State
def __450icemirrorstart():

    def upon_IMMEDIATE():
        Unknown4003('aref402_icemirrorstart.DIG', '')
        Unknown3032()
        Unknown4015()
        Unknown4010(2)
        Unknown3001(0)
    sprite('null', 13)
    Unknown3004(20)
    sprite('null', 5)
    Unknown23119(-16730881, 5, 1)
    Unknown3004(-60)

@State
def Icemirrorstart_Yugami():

    def upon_IMMEDIATE():
        Unknown1096(600)
        Unknown1007(270000)
    sprite('vr_mi402_yugami', 1)
    GFX_1('mief_402start', 100)
    Unknown4007(2)
    Unknown4010(2)
    Unknown3032()
    Unknown3057(1)
    Unknown3058(35000)
    sprite('keep', 25)
    Unknown1059(140)
    Unknown1067(140)
    Unknown3004(-13)
    loopRest()

@State
def __450icemirrorbreak():

    def upon_IMMEDIATE():
        Unknown4003('aref402_icemirrorbreak.DIG', '')
        Unknown23015(4)
        Unknown3032()
        Unknown1096(800)
    sprite('null', 10)
    SFX_3('ice_fast')
    SFX_3('ice_fast')
    sprite('null', 8)
    Unknown3004(-35)

@State
def RenzokuSlash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref430_slash_00.DIG', '')
        Unknown23067('mief_430slash_03')
    sprite('null', 25)
    GFX_0('RenzokuSlashThunder', 100)
    GFX_0('RenzokuSlashAdd', 100)
    sprite('null', 10)
    Unknown3004(-26)

@State
def RenzokuSlashAdd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref430_slash_03.DIG', '')
        Unknown3001(150)
    sprite('null', 25)
    sprite('null', 10)
    Unknown3004(-26)

@State
def RenzokuSlashThunder():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref430_slash_02.DIG', '')
    sprite('null', 10)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(150)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(150)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(150)

@State
def RenzokuTsukiA():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref430_slash_01.DIG', '')
        Unknown1056(400)
    sprite('null', 10)
    Unknown1059(10)
    sprite('null', 5)
    Unknown1067(-180)
    Unknown3004(-26)

@State
def RenzokuTsukiB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref430_slash_01.DIG', '')
        Unknown1073(-15000)
        Unknown1056(300)
    sprite('null', 10)
    Unknown1059(20)
    sprite('null', 5)
    Unknown1067(-180)
    Unknown3004(-26)

@State
def RenzokuTsukiC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref430_slash_01.DIG', '')
        Unknown1073(28000)
        Unknown1056(400)
    sprite('null', 10)
    Unknown1059(20)
    sprite('null', 5)
    Unknown1067(-180)
    Unknown3004(-26)

@State
def RenzokuTsukiD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref430_slash_01.DIG', '')
        Unknown1073(28000)
        Unknown1056(300)
    sprite('null', 10)
    Unknown1059(20)
    sprite('null', 5)
    Unknown1067(-180)
    Unknown3004(-26)

@State
def RenzokuTsukiE():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('aref430_slash_01.DIG', '')
        Unknown1073(-15000)
        Unknown1056(500)
    sprite('null', 10)
    Unknown1059(20)
    sprite('null', 5)
    Unknown1067(-180)
    Unknown3004(-26)

@State
def aref_431C():

    def upon_IMMEDIATE():
        Unknown4003('aref431_bigice3.DIG', '')
        Unknown4015()
        Unknown23015(13)
        Unknown3032()
        Unknown3001(0)
        Unknown1072(5000)
        teleportRelativeX(8000)
        Unknown2054(1)
        Unknown1096(1200)
    sprite('null', 6)
    ScreenShake(6000, 6000)
    GFX_1('aref_431ice', 100)
    GFX_0('431ice1', 100)
    Unknown36(1)
    Unknown1072(5000)
    Unknown35()
    SFX_3('quake_l')
    sprite('null', 6)
    GFX_0('431ice2', 100)
    Unknown36(1)
    Unknown1072(5000)
    Unknown35()
    SFX_3('ice_fast')
    SFX_3('mi000')
    sprite('null', 20)
    GFX_0('431ice_subeffC', 100)
    ScreenShake(28000, 28000)
    Unknown3004(120)
    SFX_3('mi001')
    sprite('null', 15)
    Unknown23119(-6915876, 15, 1)
    sprite('null', 6)
    GFX_0('431icebreakC', 100)
    ScreenShake(15000, 15000)
    Unknown1099(15)
    Unknown3004(-50)

@State
def aref_431_colC():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(5500)
        AttackP2(60)
        MinimumDamagePct(33)
        AirPushbackX(18000)
        AirPushbackY(60000)
        AirUntechableTime(90)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9021(1)
        Unknown9266(9)
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown2019(1000)
        Unknown2054(1)
        teleportRelativeX(200000)
        Unknown1007(-128000)
        Unknown3001(0)
        Unknown1096(1100)
    sprite('null', 14)
    sprite('vr_ar431_02', 10)
    RefreshMultihit()

@State
def aref_431_colC_DSD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(2000)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirPushbackX(18000)
        AirPushbackY(60000)
        AirUntechableTime(90)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9021(1)
        Unknown9266(9)
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown2019(1000)
        Unknown2054(1)
        teleportRelativeX(200000)
        Unknown1007(-128000)
        Unknown3001(0)
        Unknown1096(1100)
    sprite('null', 14)
    sprite('vr_ar431_02', 10)
    RefreshMultihit()

@State
def aref_431CD():

    def upon_IMMEDIATE():
        Unknown4003('aref431_bigice3.DIG', '')
        Unknown4015()
        Unknown23015(13)
        Unknown3032()
        Unknown3001(0)
        Unknown1072(10000)
        teleportRelativeX(8000)
        Unknown2054(1)
        Unknown1096(1800)
    sprite('null', 6)
    ScreenShake(6000, 6000)
    GFX_1('aref_431ice', 100)
    GFX_0('431ice1', 100)
    Unknown36(1)
    Unknown1072(10000)
    Unknown35()
    SFX_3('quake_l')
    sprite('null', 6)
    GFX_0('431ice2', 100)
    Unknown36(1)
    Unknown1072(10000)
    Unknown35()
    SFX_3('ice_fast')
    SFX_3('mi000')
    sprite('null', 20)
    GFX_0('431ice_subeffCD', 100)
    ScreenShake(28000, 28000)
    Unknown3004(120)
    SFX_3('mi001')
    sprite('null', 15)
    Unknown23119(-6915876, 15, 1)
    sprite('null', 6)
    GFX_0('431icebreakCD', 100)
    ScreenShake(15000, 15000)
    Unknown1099(15)
    Unknown3004(-50)

@State
def aref_431_colCD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(6500)
        AttackP2(60)
        MinimumDamagePct(31)
        AirPushbackX(18000)
        AirPushbackY(60000)
        AirUntechableTime(90)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9021(1)
        Unknown9266(9)
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown2019(1000)
        Unknown2054(1)
        teleportRelativeX(200000)
        Unknown1007(-128000)
        Unknown3001(0)
        Unknown1096(1700)
    sprite('null', 14)
    sprite('vr_ar431_02ex', 10)
    RefreshMultihit()

@State
def aref_431_colCD_DSD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(2500)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirPushbackX(18000)
        AirPushbackY(60000)
        AirUntechableTime(90)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9021(1)
        Unknown9266(9)
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown2019(1000)
        Unknown2054(1)
        teleportRelativeX(200000)
        Unknown1007(-128000)
        Unknown3001(0)
        Unknown1096(1700)
    sprite('null', 14)
    sprite('vr_ar431_02ex', 10)
    RefreshMultihit()

@State
def __431ice1():

    def upon_IMMEDIATE():
        Unknown4003('aref431_bigice1.DIG', '')
        Unknown4015()
        Unknown23015(13)
        Unknown3032()
        teleportRelativeX(128000)
        Unknown2054(1)
    sprite('null', 7)
    sprite('null', 2)
    Unknown3004(-130)

@State
def __431ice2():

    def upon_IMMEDIATE():
        Unknown4003('aref431_bigice2.DIG', '')
        Unknown4015()
        Unknown23015(13)
        Unknown3032()
        teleportRelativeX(128000)
        Unknown2054(1)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3004(-80)

@State
def __431ice_subeffC():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('aref_431icefin')
        Unknown1072(45000)
        teleportRelativeX(-150000)
        Unknown2054(1)
    sprite('null', 35)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431icebreakC():

    def upon_IMMEDIATE():
        Unknown4003('aref431_icebreak.DIG', '')
        Unknown23015(13)
        Unknown3032()
        teleportRelativeX(60000)
        Unknown1007(30000)
        Unknown1072(5000)
        Unknown23119(-8231736, 3, 1)
        Unknown1096(1200)
    sprite('null', 2)
    GFX_0('431icebreakeffC', 100)
    SFX_3('ice_fast')
    sprite('null', 3)
    SFX_3('ice_fast')
    sprite('null', 10)
    SFX_3('down_water_m')
    sprite('null', 8)
    Unknown3004(-40)

@State
def __431icebreakeffC():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('mief_431icebreak')
        teleportRelativeX(180000)
        Unknown1007(280000)
        Unknown1096(1200)
    sprite('null', 55)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431ice_subeffCD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('aref_431icefin')
        Unknown1072(50000)
        teleportRelativeX(-150000)
        Unknown2054(1)
    sprite('null', 35)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431icebreakCD():

    def upon_IMMEDIATE():
        Unknown4003('aref431_icebreak.DIG', '')
        Unknown23015(13)
        Unknown3032()
        teleportRelativeX(75000)
        Unknown1007(30000)
        Unknown1072(15000)
        Unknown23119(-8231736, 3, 1)
        Unknown1096(1800)
    sprite('null', 2)
    GFX_0('431icebreakeffCD', 100)
    SFX_3('ice_fast')
    sprite('null', 3)
    SFX_3('ice_fast')
    sprite('null', 10)
    SFX_3('down_water_m')
    sprite('null', 8)
    Unknown3004(-40)

@State
def __431icebreakeffCD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('mief_431icebreak')
        teleportRelativeX(430000)
        Unknown1007(280000)
        Unknown1096(1400)
    sprite('null', 55)
    sprite('null', 5)
    Unknown3004(-51)

@State
def PMI_PersonaIchigeki1():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -130000, 0, 0, 0, 0, 0)
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown4007(3)
        Unknown2054(1)
        Unknown3032()
        Unknown23022(1)
    sprite('ar432_20', 3)
    GFX_0('450Personaineff', 100)
    sprite('ar432_21', 3)
    sprite('ar432_22', 3)
    sprite('ar432_21', 3)
    sprite('ar432_20', 3)
    sprite('ar432_21', 3)
    sprite('ar432_22', 3)
    sprite('ar432_21', 3)
    sprite('ar432_20', 3)
    sprite('ar432_21', 3)
    sprite('ar432_22', 3)
    sprite('ar432_21', 3)
    sprite('ar432_20', 3)
    sprite('ar432_21', 3)
    sprite('ar432_22', 3)
    Unknown23119(-1002241, 10, 1)
    sprite('ar432_21', 8)
    enterState('PersonaDeleteAndIdling')
    physicsYImpulse(12000)
    Unknown3004(-35)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def __450Personaineff():

    def upon_IMMEDIATE():
        GFX_2('aref_450personain')
        Unknown2054(1)
        Unknown3001(0)
        Unknown3004(40)
    sprite('null', 55)
    sprite('null', 7)
    Unknown1099(300)
    Unknown3004(-40)

@State
def Ichigeki_Whip():

    def upon_IMMEDIATE():
        Unknown2012()
        Damage(0)
        AttackLevel_(5)
        Hitstop(7)
        Unknown11001(0, 30, 0)
        GroundedHitstunAnimation(1)
        AirPushbackX(-10000)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(999)
        ProjectileDurabilityLvl(3)
        ChipDamagePct(0)
        Unknown11042(1)
        Unknown48(25, 2, 83, 22, 2, 83)
        teleportRelativeX(-150000)
        Unknown48(25, 2, 23, 22, 2, 23)
        Unknown1007(1350000)
        Unknown1072(80000)
        Unknown1110(100000, 0)
        SLOT_12 = SLOT_19
        Unknown1019(5)
        SLOT_13 = SLOT_20
        SLOT_13 = (SLOT_13 * (-1))
        YAccel(5)
        Unknown1108(0)
        Unknown2035(1)
        sendToLabelUpon(12, 1)

        def upon_11():
            clearUponHandler(11)
            physicsXImpulse(0)
            physicsYImpulse(0)
    sprite('vr_ar450_00', 1)
    SFX_3('slash_pole_middle')
    sprite('vr_mi450_dummy', 3)
    Unknown1110(120000, 0)
    GFX_0('450muchi', 0)
    RefreshMultihit()
    sprite('vr_ar450_00', 3)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown21015('AstralHeat', 5002, 0)
    Unknown26('450muchi')
    DisableAttackRestOfMove()
    sprite('vr_ar450_03', 1)
    Unknown1110(-94000, 0)
    SFX_3('highjump_l')
    sprite('vr_ar450_02', 11)
    Unknown3004(-30)
    loopRest()
    ExitState()
    label(1)
    clearUponHandler(11)
    clearUponHandler(12)
    sprite('vr_mi450_dummy', 30)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown3029(1)
    Unknown3070(1)
    AfterimageCount(3)
    AfterimageMask_1(0, 0, 127, 255)
    AfterimageMask_2(0, 0, 0, 0)
    GFX_0('450upline', -1)
    sprite('vr_ar450_00', 3)
    Unknown21015('AstralHeat', 5001, 0)
    sprite('vr_ar450_03', 1)
    Unknown1110(-94000, 0)
    SFX_3('highjump_l')
    sprite('vr_ar450_02', 11)
    Unknown3004(-30)
    Unknown1084(1)

@State
def PMI_PersonaIchigeki2():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 0, 0, 0, 0, 0, 0)
        callSubroutine('PMI_DDAttackInit')
        Unknown2012()
        AirPushbackX(0)
        AirPushbackY(1)
        YImpluseBeforeWallbounce(0)
        Hitstop(0)
        AirUntechableTime(999)
        Unknown11064(1)
        Unknown9266(9)
        Unknown11023(1)
        Unknown23022(1)
        Unknown3032()
        Unknown1000(0)
        teleportRelativeY(2000000)
        callSubroutine('PMI_CheckWarp')
    label(0)
    sprite('ar450_00', 20)
    sprite('ar450_00', 3)
    sprite('ar450_01', 3)
    sprite('ar450_02', 3)
    sprite('ar450_01', 3)
    sprite('ar450_00', 3)
    sprite('ar450_01', 3)
    sprite('ar450_02', 3)
    sprite('ar450_01', 3)
    sprite('ar450_00', 3)
    sprite('ar450_01', 3)
    SFX_3('slash_knife_fast')
    sprite('ar450_02', 3)
    SFX_3('slash_pole_middle')
    label(1)
    sprite('ar450_03', 2)
    sprite('ar450_04', 2)
    Unknown4045('aref_450zanC', -1)
    GFX_0('450icebase_lv1', -1)
    Unknown36(1)
    Unknown1096(800)
    Unknown35()
    ScreenShake(12000, 12000)
    RefreshMultihit()
    SFX_3('ice_break_fast')
    sprite('ar450_05', 2)
    sprite('ar450_06', 3)
    sprite('ar450_07', 3)
    sprite('ar450_08', 4)
    Unknown3004(-8)
    sprite('ar450_09', 4)
    sprite('ar450_10', 4)
    GFX_0('Ichigeki_Ranbu', -1)
    Unknown21015('IchigekiCamera', 5014, 0)
    label(2)
    sprite('ar450_08', 6)
    SLOT_52 = (SLOT_52 + 1)
    sprite('ar450_09', 6)
    sprite('ar450_10', 6)
    Unknown3038(1)
    (SLOT_52 == 20)
    Unknown19(2, 2, 0)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def Ichigeki_Ranbu():

    def upon_IMMEDIATE():
        Unknown2012()
        Damage(0)
        AttackLevel_(5)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(999)
        Unknown11023(1)
        Unknown11050(5, '')
        Unknown23022(1)
        Unknown11083(1)
    sprite('dmy_atk00', 20)
    Unknown4045('aref_450zanD', 100)
    ScreenShake(12000, 12000)
    GFX_0('450icebase', 100)
    GFX_0('Ichigeki_RanbuSE', 100)
    Unknown21015('Ichigeki_RanbuSE', 5021, 0)
    SLOT_51 = 15
    label(0)
    sprite('dmy_atk00', 6)
    Unknown4045('aref_450zanC', 100)
    RefreshMultihit()
    Unknown23151(22, 105)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(10, 2, 51)
    gotoLabel(0)
    label(10)
    SLOT_51 = 15
    label(11)
    sprite('dmy_atk00', 4)
    Unknown4045('aref_450zanD', 100)
    RefreshMultihit()
    Unknown23151(22, 105)
    SLOT_51 = (SLOT_51 + (-1))
    Unknown21015('Ichigeki_RanbuSE', 5022, 0)
    loopRest()
    Unknown19(20, 2, 51)
    gotoLabel(11)
    label(20)
    SLOT_51 = 30
    label(21)
    sprite('dmy_atk00', 2)
    Unknown4045('aref_450zanD', 100)
    RefreshMultihit()
    Unknown23151(22, 105)
    SLOT_51 = (SLOT_51 + (-1))
    Unknown21015('Ichigeki_RanbuSE', 5023, 0)
    loopRest()
    Unknown19(1, 2, 51)
    gotoLabel(21)
    label(1)
    sprite('dmy_atk00', 1)
    Unknown4045('aref_450zanE', 100)
    RefreshMultihit()
    sprite('null', 5)
    Unknown21015('AstralHeat', 5004, 0)

@State
def Ichigeki_RanbuSE():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5021):
                if (not SLOT_52):
                    sendToLabel(1)
            if (SLOT_48 == 5022):
                if (not SLOT_53):
                    sendToLabel(2)
            if (SLOT_48 == 5023):
                if (not SLOT_IsInOverdrive2):
                    sendToLabel(3)
            if (SLOT_48 == 5024):
                sendToLabel(9)
    label(1)
    sprite('keep', 3)
    SLOT_52 = 1
    SFX_3('slash_pole_middle')
    sprite('keep', 15)
    SFX_3('damage_magic_m')
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('keep', 3)
    SLOT_53 = 1
    SFX_3('slash_pole_middle')
    sprite('keep', 10)
    SFX_3('damage_magic_m')
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('keep', 3)
    SLOT_54 = 1
    SFX_3('slash_pole_middle')
    sprite('keep', 5)
    SFX_3('damage_magic_m')
    loopRest()
    gotoLabel(3)
    label(9)
    sprite('keep', 10)

@State
def IchigekiCamera():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5011):
                sendToLabel(1)
            if (SLOT_48 == 5012):
                sendToLabel(2)
            if (SLOT_48 == 5013):
                sendToLabel(3)
            if (SLOT_48 == 5014):
                sendToLabel(4)
            if (SLOT_48 == 5015):
                sendToLabel(5)
    label(1)
    sprite('keep', 32767)
    Unknown1086(22)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    label(2)
    sprite('keep', 20)
    SystemGFX('SCEF_FadeBlack12In', 100)
    sprite('keep', 30)
    Unknown26('SCEF_FadeBlack12In')
    SystemGFX('SCEF_FadeBlack12Out', 100)
    SystemGFX('SCEF_LiveRyuhaiNaname', 100)
    Unknown1086(22)
    Unknown20001(1)
    Unknown1007(300000)
    physicsXImpulse(0)
    physicsYImpulse(10000)
    sprite('keep', 20)
    SystemGFX('SCEF_FadeBlack12In', 100)
    Unknown21015('AstralHeat', 5003, 0)
    label(3)
    sprite('keep', 20)
    sprite('keep', 20)
    Unknown26('SCEF_FadeBlack12In')
    SystemGFX('SCEF_FadeBlack12Out', 100)
    SystemGFX('SCEF_LiveRyuhaiNaname', 100)
    Unknown1086(28)
    Unknown1084(1)
    teleportRelativeY(2120000)
    teleportRelativeX(198000)
    sprite('keep', 32767)
    GFX_0('450Circlebg', -1)
    Unknown26('SCEF_LiveRyuhaiNaname')
    Unknown26('subSCEF_LiveRyuhaiUpper2naname')
    label(4)
    sprite('keep', 32767)
    Unknown1086(22)
    Unknown20000(1)
    teleportRelativeY(2120000)
    label(5)
    sprite('keep', 20)
    Unknown26('SCEF_LiveRyuhaiNaname')
    SystemGFX('SCEF_FadeBlack12In', 100)
    sprite('keep', 32767)
    Unknown26('SCEF_FadeBlack12In')
    SystemGFX('SCEF_FadeBlack12Out', 100)
    Unknown1086(0)
    Unknown20000(1)
    Unknown1000(0)
    teleportRelativeY(0)

@State
def __450muchi():

    def upon_IMMEDIATE():
        Unknown23067('aref_450muchi')
        Unknown4007(2)
        Unknown1072(-9000)
    sprite('null', 30)
    sprite('null', 10)
    Unknown1059(200)
    Unknown1067(400)
    Unknown3004(-26)

@State
def __450upline():

    def upon_IMMEDIATE():
        Unknown1072(-10000)
    sprite('null', 30)
    Unknown23067('mief_450upline00')

@State
def __450icebase():

    def upon_IMMEDIATE():
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 20)
    GFX_0('450icemove1', 100)
    sprite('null', 30)
    GFX_0('450icebase_lv1', 100)
    ScreenShake(6000, 6000)
    sprite('null', 20)
    GFX_0('450icemove1', 100)
    sprite('null', 25)
    GFX_0('450icebase_lv2', 100)
    ScreenShake(8000, 8000)
    sprite('null', 20)
    GFX_0('450icemove1', 100)
    sprite('null', 20)
    GFX_0('450icebase_lv3', 100)
    ScreenShake(12000, 12000)
    sprite('null', 15)
    GFX_0('450icemove2', 100)
    sprite('null', 15)
    GFX_0('450icebase_lv4', 100)
    ScreenShake(16000, 16000)
    sprite('null', 15)
    GFX_0('450icemove2', 100)
    sprite('null', 20)
    GFX_0('450icebase_lv5', 100)
    ScreenShake(24000, 24000)
    sprite('null', 20)
    ScreenShake(24000, 24000)
    sprite('null', 20)
    ScreenShake(24000, 24000)
    sprite('null', 20)
    ScreenShake(24000, 24000)
    sprite('null', 32767)

@State
def __450icebase_lv1():

    def upon_IMMEDIATE():
        Unknown4003('aref450_icebase_lv1.DIG', '')
        Unknown4054(1)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 58)
    GFX_1('aref_450icestay', 100)
    sprite('null', 2)
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-130)

@State
def __450icebase_lv2():

    def upon_IMMEDIATE():
        Unknown4003('aref450_icebase_lv2.DIG', '')
        Unknown4054(1)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 58)
    GFX_1('aref_450icestay', 100)
    sprite('null', 2)
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-130)

@State
def __450icebase_lv3():

    def upon_IMMEDIATE():
        Unknown4003('aref450_icebase_lv3.DIG', '')
        Unknown4054(1)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 58)
    GFX_1('aref_450icestay', 100)
    sprite('null', 2)
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-130)

@State
def __450icebase_lv4():

    def upon_IMMEDIATE():
        Unknown4003('aref450_icebase_lv4.DIG', '')
        Unknown4054(1)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 58)
    GFX_1('aref_450icestay', 100)
    sprite('null', 2)
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-130)

@State
def __450icebase_lv5():

    def upon_IMMEDIATE():
        Unknown4003('aref450_icebase_lv5.DIG', '')
        Unknown4054(1)
        Unknown1096(1300)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 55)
    GFX_1('aref_450icestay', 100)
    sprite('null', 100)
    sprite('null', 5)
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-90)

@State
def __450icemove1():

    def upon_IMMEDIATE():
        Unknown4003('aref450_icemove1.DIG', 'aref450_icemove1_000.mmot')
        Unknown4054(1)
        Unknown3032()
    sprite('null', 17)
    GFX_1('aref_450icesmoke', 100)
    sprite('null', 3)
    Unknown23119(-16744193, 8, 1)
    SFX_3('mi000')
    Unknown3004(-90)

@State
def __450icemove2():

    def upon_IMMEDIATE():
        Unknown4003('aref450_icemove2.DIG', 'aref450_icemove2_000.mmot')
        Unknown4054(1)
        Unknown3032()
    sprite('null', 12)
    GFX_1('aref_450icesmoke', 100)
    sprite('null', 3)
    Unknown23119(-16744193, 8, 1)
    SFX_3('mi000')
    Unknown3004(-90)

@State
def __450icebreak():

    def upon_IMMEDIATE():
        Unknown4003('aref450_icebase_lv5.DIG', '')
        Unknown4054(1)
        Unknown1096(1100)
        teleportRelativeX(500000)
        Unknown1007(500000)
        Unknown3033()

        def upon_43():
            if (SLOT_48 == 5031):
                sendToLabel(0)
    sprite('null', 32767)
    GFX_1('aref_450icestay2', 100)
    label(0)
    sprite('null', 2)
    GFX_1('mief_450icebreak', 100)
    Unknown23119(-1, 20, 1)
    Unknown3004(-13)
    SFX_3('damage_hit_mh')
    sprite('null', 2)
    SFX_3('ice_break_fast')
    sprite('null', 16)
    SFX_3('ice_break_fast')

@State
def __450Circlebg():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('aref450_circlebg.DIG', '')
        Unknown3001(0)
        Unknown1007(-200000)
    sprite('null', 32767)
    Unknown3004(30)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3032()
        Unknown6001(1)
        Unknown1001(640000)
        teleportRelativeX(180000)
        teleportRelativeY(100000)
        Unknown3001(0)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('ichigeki', 12)
    physicsXImpulse(80000)
    Unknown3004(10)
    sprite('ichigeki', 80)
    physicsXImpulse(200)
    sprite('ichigeki', 20)
    Unknown23119(10198015, 20, 1)
    sprite('ichigeki', 30)
    Unknown3004(-9)

@State
def __450cutinbg():

    def upon_IMMEDIATE():
        Unknown4003('mief450_cutinbg.DIG', '')
        Unknown23015(1)
        Unknown3032()
        Unknown3001(0)
    sprite('null', 110)
    Unknown3004(30)
    sprite('null', 50)
    Unknown3004(-6)

@State
def Issen():

    def upon_IMMEDIATE():
        Unknown4003('aref450_issen.DIG', '')
        Unknown3032()
        Unknown23015(1)
        Unknown4015()
        Unknown1096(1500)
    sprite('null', 7)
    sprite('null', 5)
    Unknown3004(-60)

@State
def __450KObg():

    def upon_IMMEDIATE():
        Unknown23067('mief_450bg')
        Unknown4003('aref450_bg.DIG', '')
        Unknown23015(2)
        Unknown3032()
        Unknown3001(0)
    sprite('null', 32767)
    Unknown3004(30)

@State
def LifeLinkEff():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 1)
    Unknown4045('ntef_story_lifelinkeff_line2', -1)

@State
def PMI_PersonaMatchWin():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 100000, 20000, 100000, 20000, 100000, 20000)
        callSubroutine('PersonaReset')
        Unknown23022(1)
        Unknown4007(3)
        callSubroutine('PMI_CheckWarp')
    sprite('ar610_00', 6)
    sprite('ar610_01', 6)
    sprite('ar610_02', 6)
    sprite('ar610_00', 6)
    sprite('ar610_01', 6)
    sprite('ar610_02', 6)
    sprite('ar610_03', 6)
    sprite('ar610_04', 6)
    sprite('ar610_05', 6)
    sprite('ar610_06', 6)
    sprite('ar610_07', 6)
    label(0)
    sprite('ar610_08', 6)
    SFX_3('cloth_l')
    sprite('ar610_09', 6)
    sprite('ar610_10', 6)
    gotoLabel(0)

@State
def P4U_Cutin_Parent():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 1)
    GFX_0('P4U_Cutin_Face', 100)

@State
def P4U_Cutin_Face():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown2054(1)
        Unknown13044(0)
        Unknown6001(1)
        Unknown1000(-650000)
        teleportRelativeY(-292000)
        Unknown1096(1350)
        Unknown2037(0)
        Unknown3001(0)

        def upon_3():
            if (SLOT_2 == 2):
                Unknown1007(15000)
                Unknown3001(150)
            if (SLOT_2 == 3):
                Unknown1007(-30000)
                Unknown3001(180)
            if (SLOT_2 == 4):
                Unknown1007(25000)
                Unknown3001(210)
            if (SLOT_2 == 5):
                Unknown1007(-20000)
                Unknown3001(255)
            if (SLOT_2 == 6):
                Unknown1007(10000)
            Unknown2038(1)
    sprite('vr_99p4u_face00', 45)
    SFX_0('spsys_over_power')
    SFX_0('spsys_over_power')
    if SLOT_168:
        GFX_0('P4U_ka_NotJPN', 100)
    else:
        GFX_0('P4U_ka_JPN', 100)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(180)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(120)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(60)

@State
def P4U_ka_JPN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown6001(1)
        Unknown1000(-950000)
        teleportRelativeY(-232000)
        Unknown1096(1350)
    sprite('vr_p4_ka_mozi', 1)
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi', 38)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(60)
    Unknown1096(100)

@State
def P4U_ka_NotJPN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown6001(1)
        Unknown1000(-950000)
        teleportRelativeY(-232000)
        Unknown1096(1350)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi_notjpn', 38)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(60)
    Unknown1096(100)

@State
def rimzineHontaiA():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(6)
        teleportRelativeY(40000)
        teleportRelativeX(-1525000)
        Unknown2019(1000)
        Unknown13044(1)
        Unknown23069(1)
        Unknown2047(1)
        Unknown4010(3)
    sprite('vr_mi601b_00', 110)
    physicsXImpulse(24900)
    GFX_0('rimzineHontaiB', 100)
    GFX_0('rimzineHontaiC', 100)
    GFX_0('rimzineDoor', 100)
    GFX_0('rimzinetaiya', 0)
    SFX_3('mi002')
    sprite('vr_mi601b_00', 10)
    physicsXImpulse(12400)
    sprite('vr_mi601b_00', 10)
    physicsXImpulse(6200)
    SFX_3('mi003')
    sprite('vr_mi601b_00', 10)
    physicsXImpulse(3100)
    sprite('vr_mi601b_00', 130)
    physicsXImpulse(0)
    sprite('vr_mi601b_00', 10)
    physicsXImpulse(3100)
    SFX_3('mi002')
    sprite('vr_mi601b_00', 10)
    physicsXImpulse(6200)
    sprite('vr_mi601b_00', 10)
    physicsXImpulse(12400)
    sprite('vr_mi601b_00', 100)
    physicsXImpulse(24900)

@State
def rimzineHontaiB():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(1)
        Unknown2019(1000)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601b_01', 32767)

@State
def rimzineHontaiC():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(0)
        Unknown2019(1000)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601b_02', 110)
    GFX_0('rimzinetaiya2', 0)
    sprite('vr_mi601b_02', 32767)

@State
def rimzineDoor():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(1)
        Unknown2019(500)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601a_00', 150)
    sprite('vr_mi601a_01', 4)
    sprite('vr_mi601a_02', 4)
    sprite('vr_mi601a_03', 4)
    sprite('vr_mi601a_04', 45)
    sprite('null', 300)
    Unknown3001(0)
    GFX_0('rimzineDoor2', 100)

@State
def rimzineDoor2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown2019(1000)
        Unknown13044(1)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601a_03', 4)
    sprite('vr_mi601a_02', 4)
    sprite('vr_mi601a_01', 4)
    sprite('vr_mi601a_00', 300)

@State
def rimzinetaiya():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(1)
        Unknown2019(500)
        Unknown23069(1)
        Unknown2047(1)
    label(0)
    sprite('vr_mi601c_02', 2)
    sprite('vr_mi601c_01', 2)
    sprite('vr_mi601c_00', 2)
    gotoLabel(0)

@State
def rimzinetaiya2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(1)
        Unknown2019(500)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 130)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 4)
    sprite('vr_mi601c_01', 4)
    sprite('vr_mi601c_00', 4)
    sprite('vr_mi601c_02', 3)
    sprite('vr_mi601c_01', 3)
    sprite('vr_mi601c_00', 3)
    sprite('vr_mi601c_02', 3)
    sprite('vr_mi601c_01', 3)
    sprite('vr_mi601c_00', 3)
    sprite('vr_mi601c_02', 2)
    sprite('vr_mi601c_01', 2)
    sprite('vr_mi601c_00', 2)
    sprite('vr_mi601c_02', 2)
    sprite('vr_mi601c_01', 2)
    sprite('vr_mi601c_00', 2)
    sprite('vr_mi601c_02', 2)
    sprite('vr_mi601c_01', 2)
    sprite('vr_mi601c_00', 2)
    sprite('vr_mi601c_02', 2)
    sprite('vr_mi601c_01', 2)
    sprite('vr_mi601c_00', 2)
    sprite('vr_mi601c_02', 2)
    sprite('vr_mi601c_01', 2)
    sprite('vr_mi601c_00', 2)
    sprite('vr_mi601c_02', 2)
    sprite('vr_mi601c_01', 2)
    sprite('vr_mi601c_00', 2)
    sprite('vr_mi601c_02', 2)
    sprite('vr_mi601c_01', 2)
    sprite('vr_mi601c_00', 2)

@State
def rimzineShadow():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(6)
        Unknown3035()
        Unknown1007(10000)
        Unknown3001(100)
    sprite('vr_mi601s_00', 260)

@State
def P4U_Cutin_Parent():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 1)
    GFX_0('P4U_Cutin_Face', 100)

@State
def P4U_Cutin_Face():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown2054(1)
        Unknown13044(0)
        Unknown6001(1)
        Unknown1000(-650000)
        teleportRelativeY(-292000)
        Unknown1096(1350)
        Unknown2037(0)
        Unknown3001(0)

        def upon_3():
            if (SLOT_2 == 2):
                Unknown1007(15000)
                Unknown3001(150)
            if (SLOT_2 == 3):
                Unknown1007(-30000)
                Unknown3001(180)
            if (SLOT_2 == 4):
                Unknown1007(25000)
                Unknown3001(210)
            if (SLOT_2 == 5):
                Unknown1007(-20000)
                Unknown3001(255)
            if (SLOT_2 == 6):
                Unknown1007(10000)
            Unknown2038(1)
    sprite('vr_99p4u_face00', 45)
    SFX_0('spsys_over_power')
    SFX_0('spsys_over_power')
    if SLOT_168:
        GFX_0('P4U_ka_NotJPN', 100)
    else:
        GFX_0('P4U_ka_JPN', 100)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(180)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(120)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(60)

@State
def P4U_ka_JPN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown6001(1)
        Unknown1000(-950000)
        teleportRelativeY(-232000)
        Unknown1096(1350)
    sprite('vr_p4_ka_mozi', 1)
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi', 38)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(60)
    Unknown1096(100)

@State
def P4U_ka_NotJPN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(5)
        Unknown2007()
        Unknown4009(2)
        Unknown6001(1)
        Unknown1000(-950000)
        teleportRelativeY(-232000)
        Unknown1096(1350)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi_notjpn', 38)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(60)
    Unknown1096(100)