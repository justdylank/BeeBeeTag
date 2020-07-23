@State
def PAK_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)
    Unknown3038(1)
    Unknown24('50414b5f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PAK_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PAK_ReceptionSignal')
    sprite('null', 32767)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PAK_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 2050):
            Unknown23185('PAK_Persona5A6th', 50)
        if (SLOT_48 == 2040):
            Unknown23185('PAK_Persona5C', 50)
        if (SLOT_48 == 2045):
            Unknown23185('PAK_Persona5D', 50)
        if (SLOT_48 == 2540):
            Unknown23185('PAK_PersonaJC', 50)
        if (SLOT_48 == 4320):
            Unknown23185('PAK_PersonaMahajiodain', 200)
        if (SLOT_48 == 4321):
            Unknown23185('PAK_PersonaMahajiodainSP', 200)
        if (SLOT_48 == 4322):
            Unknown23185('PAK_PersonaMahajiodainDSD', 200)
        if (SLOT_48 == 4323):
            Unknown23185('PAK_PersonaMahajiodainDSDSP', 200)
        if (SLOT_48 == 4500):
            Unknown23185('PAK_PersonaIchigeki', 300)
        if (SLOT_48 == 9999):
            Unknown23185('PersonaDeleteAndIdling', 300)
        if (SLOT_48 == 6100):
            Unknown23185('PAK_PersonaMatchWin', 300)

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
def PAK_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PAK_AttackInit():
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
    callSubroutine('PAK_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PAK_SPAttackInit():
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
    callSubroutine('PAK_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PAK_DDAttackInit():
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
    callSubroutine('PAK_ReceptionSignal')
    Unknown23023()

@Subroutine
def PAK_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PAK_ForceWarp():
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
    enterState('PAK_PersonaWait')

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
        callSubroutine('PAK_ReceptionSignal')
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
def PAK_Persona5A6th():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 80000, 0, 0, 1200000, 0, 0)
        callSubroutine('PAK_AttackInit')
        AttackLevel_(3)
        Damage(500)
        AttackP1(90)
        Unknown23078(1)
        AttackAttributes(0, 1, 0, 0, 0)
        Unknown11044(1)
        Unknown2053(1)
        EnableCollision(0)
        callSubroutine('PAK_CheckWarp')
        Unknown23059(1)

        def upon_78():
            Unknown23029(3, 2051, 0)
            Hitstop(0)
            enterState('PAK_Persona5A6th_Plus')
    sprite('cs208_00', 6)
    Unknown2015(140)
    sprite('cs208_01', 6)
    sprite('cs208_02', 2)
    SFX_3('hit_m_middle')
    sprite('cs208_03', 1)
    RefreshMultihit()
    sprite('cs208_03', 3)
    Unknown23022(0)
    GFX_1('ef_thunder_damage_g', 1)
    sprite('cs208_03', 4)
    StartMultihit()
    sprite('cs208_04', 6)
    sprite('cs208_05', 6)
    sprite('cs208_06', 6)
    StartMultihit()
    sprite('cs208_07', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAK_Persona5A6th_Plus():

    def upon_IMMEDIATE():
        callSubroutine('PAK_AttackInit')
        Unknown17011('PAK_Persona5A6th_Exe', 1, 0, 0)
        Unknown11002(-1)
        AttackLevel_(3)
        Damage(0)
        AttackP1(90)
        AttackP2(100)
        Hitstop(20)
        Unknown11045(0)
        Unknown30061(1)
        setInvincible(1)
        Unknown11032(-1, -1, -1, -1)
        Unknown11054(-1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown2053(1)
        EnableCollision(0)
        callSubroutine('PAK_CheckWarp')

        def upon_78():
            Hitstop(0)
    sprite('keep', 1)
    sprite('cs208_04', 6)
    setInvincible(0)
    sprite('cs208_05', 6)
    sprite('cs208_06', 6)
    StartMultihit()
    sprite('cs208_07', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAK_Persona5A6th_Exe():

    def upon_IMMEDIATE():
        callSubroutine('PAK_AttackInit')
        Unknown17012(1, 0, 0)
        AttackLevel_(5)
        Damage(300)
        AttackP1(90)
        Unknown11092(1)
        MinimumDamagePct(0)
        AirPushbackY(-120000)
        AirPushbackX(10000)
        Unknown9190(1)
        Unknown9118(30)
        AirUntechableTime(60)
        Unknown11068(1)
        Hitstop(0)
        Unknown30079(1)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11064(1)
        Unknown23022(1)
        EnableCollision(1)
        Unknown2053(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        AttackAttributes(0, 1, 0, 0, 0)
        callSubroutine('PAK_CheckWarp')
    sprite('cs209_00', 5)
    Unknown5000(2, 0)
    Unknown5001(0, 1, 1, 0, 0)
    sprite('cs209_01', 5)
    sprite('cs209_00', 5)
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001(0, 1, 1, 0, 0)
    Unknown23119(-10420288, 3, 10)
    Unknown4054(12)
    Unknown4045('csef_209', 1)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 0)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 1)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 2)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 3)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 4)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 5)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 6)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 7)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 8)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 9)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 10)
    sprite('cs209_01', 5)
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001(0, 1, 1, 0, 0)
    sprite('cs209_00', 5)
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001(0, 1, 1, 0, 0)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 0)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 1)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 2)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 3)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 4)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 5)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 6)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 7)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 8)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 9)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 10)
    sprite('cs209_01', 5)
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001(0, 1, 1, 0, 0)
    sprite('cs209_00', 5)
    Unknown5000(2, 0)
    Unknown5001(0, 1, 1, 0, 0)
    RefreshMultihit()
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 0)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 1)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 2)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 3)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 4)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 5)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 6)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 7)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 8)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 9)
    Unknown4054(12)
    Unknown4045('ef_thunder_damage_g', 10)
    sprite('cs209_01', 5)
    RefreshMultihit()
    Unknown5000(2, 0)
    Unknown5001(0, 1, 1, 0, 0)
    sprite('cs209_02', 10)
    Unknown5000(2, 0)
    Unknown5001(0, 1, 1, 0, 0)
    sprite('cs209_03', 1)
    Unknown5000(27, 0)
    Unknown5001(0, 1, 1, 0, 0)
    sprite('cs209_04', 3)
    Unknown5000(26, 0)
    Unknown5001(0, 1, 1, 0, 0)
    RefreshMultihit()
    Damage(1500)
    Unknown1084(1)
    Unknown30079(0)
    Unknown11064(0)
    ScreenShake(1000, 15000)
    SFX_3('down_steal_m')
    SFX_3('counter_hit_l45')
    Unknown23029(3, 2052, 0)
    Unknown30088(1)
    sprite('cs209_05', 3)
    sprite('cs209_06', 5)
    sprite('cs209_07', 13)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAK_Persona5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 0, 0, 1700000, 0, 0)
        callSubroutine('PAK_AttackInit')
        EnableCollision(0)
        Unknown2053(0)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('PAK_CheckWarp')
        Unknown2003(1)
        Unknown23022(1)
        Unknown23059(1)
    sprite('cs204_00', 3)
    sprite('cs204_01', 4)
    sprite('cs204_02', 4)
    sprite('cs204_03', 3)
    sprite('cs204_04', 3)
    sprite('cs204_05', 2)
    sprite('cs204_06', 2)
    SFX_3('slash_sword_middle')
    GFX_0('Zanzoh5C', 100)
    sprite('cs204_07', 1)
    ScreenShake(20000, 20000)
    SFX_3('bomb_m')
    SFX_3('attack_offset')
    sprite('cs204_07', 2)
    sprite('cs204_07', 2)
    Unknown23022(0)
    sprite('cs204_08', 4)
    Unknown4007(0)
    sprite('cs204_09', 4)
    sprite('cs204_10', 4)
    sprite('cs204_08', 4)
    sprite('cs204_09', 4)
    sprite('cs204_10', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    
@State
def PAK_Persona5D():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 104, -150000, 0, 0, 100000, 0, 0)
        EnableCollision(0)
        Unknown2053(0)
        callSubroutine('PAK_CheckWarp')
        SLOT_47 = 10
    sprite('cs205_00', 4)
    sprite('cs205_01', 4)
    sprite('cs205_02', 4)
    label(0)
    sprite('cs205_00', 4)
    SFX_0('cloth_m')
    
    def upon_3():
        if (not CheckInput(0x09)):
            clearUponHandler(3)
            sendToLabel(819)
    sprite('cs205_01', 4)
    sprite('cs205_02', 4)
    SLOT_47 = (SLOT_47 + (-1))
    if (SLOT_47 == 2):
        sendToLabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('cs205_00', 2)
    SFX_0('cloth_m')
    sprite('cs205_01', 4)
    sprite('cs205_02', 4)
    sprite('cs205_00', 2)
    SFX_0('cloth_m')
    sprite('cs205_01', 4)
    sprite('cs205_02', 4)
    sprite('cs205_00', 2)
    SFX_0('cloth_m')
    sprite('cs205_01', 4)
    sprite('cs205_02', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    label(819)
    sprite('cs206_00', 6)
    sprite('cs206_01', 6)
    GFX_0('caef_5D_globe', 0)
    GFX_0('caef_5D_yugami_loop', 0)
    Unknown21003(2500, 2500)
    sprite('cs206_02', 6)
    SLOT_47 = 5
    label(3)
    sprite('cs206_03', 5)
    SFX_0('cloth_m')
    sprite('cs206_04', 5)
    sprite('cs206_05', 5)
    sprite('cs206_03', 5)
    sprite('cs206_04', 5)
    sprite('cs206_05', 4)
    sprite('cs206_05', 1)
    SLOT_47 = (SLOT_47 + (-1))
    if (not SLOT_47):
        sendToLabel(4)
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('cs206_03', 5)
    SFX_0('cloth_m')
    sprite('cs206_04', 5)
    sprite('cs206_05', 5)
    sprite('cs206_03', 5)
    Unknown21003(0, 0)
    sprite('cs206_04', 5)
    sprite('cs206_05', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaJC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -150000, 70000, 0, 0, 0, 0)
        callSubroutine('PAK_AttackInit')
        AttackLevel_(5)
        AirUntechableTime(50)
        AirPushbackX(5000)
        AirPushbackY(-50000)
        GroundedHitstunAnimation(1)
        Unknown9016(1)
        AttackAttributes(1, 0, 0, 0, 0)
        HitOverhead(2)
        Unknown9310(1)
        Unknown23078(1)
        Unknown2053(1)
        EnableCollision(0)
        Unknown4007(3)
        callSubroutine('PAK_CheckWarp')
        Unknown23059(1)

        def upon_12():
            Unknown23029(3, 2061, 0)
    sprite('cs254_00', 1)
    sprite('cs254_01', 1)
    sprite('cs254_02', 1)
    sprite('cs254_03', 2)
    Unknown4007(0)
    physicsXImpulse(15000)
    sprite('cs254_04', 2)
    sprite('cs254_05', 2)
    Unknown1019(150)
    physicsYImpulse(-10000)
    sprite('cs254_06', 2)
    sprite('cs254_07', 2)
    Unknown1019(150)
    YAccel(150)
    sprite('cs254_08', 2)
    Unknown1019(50)
    GFX_0('ZanzohAir5C', 100)
    sprite('cs254_09', 2)
    Unknown1019(50)
    YAccel(150)
    SFX_3('slash_sword_middle')
    sprite('cs254_10', 1)
    RefreshMultihit()
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('cs254_10', 3)
    sprite('cs254_11', 3)
    sprite('cs254_12', 3)
    sprite('cs254_13', 3)
    sprite('cs254_11', 3)
    sprite('cs254_12', 3)
    sprite('cs254_13', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaMahajiodain():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 104, -120000, 60000, 0, 0, 0, 0)
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('cs432_00', 4)
    sprite('cs432_01', 4)
    sprite('cs432_02', 4)
    sprite('cs432_00', 4)
    sprite('cs432_01', 4)
    sprite('cs432_02', 4)
    sprite('cs432_00', 4)
    sprite('cs432_01', 3)
    sprite('cs432_02', 3)
    sprite('cs432_03', 3)
    sprite('cs432_04', 3)
    sprite('cs432_05', 5)
    GFX_0('LightningPlasma_col', 100)
    GFX_0('UltimateLightningPlasma', 1)
    Unknown2054(0)
    loopRest()
    sprite('cs432_06', 5)
    GFX_0('caef_ultimate_globe2', 0)
    SFX_3('thunder_l')
    Unknown23029(3, 4401, 0)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaMahajiodainSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 104, -120000, 60000, 0, 0, 0, 0)
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('cs432_00', 4)
    sprite('cs432_01', 4)
    sprite('cs432_02', 4)
    sprite('cs432_00', 4)
    sprite('cs432_01', 4)
    sprite('cs432_02', 4)
    sprite('cs432_00', 4)
    sprite('cs432_01', 3)
    sprite('cs432_02', 3)
    sprite('cs432_03', 3)
    sprite('cs432_04', 3)
    sprite('cs432_05', 5)
    GFX_0('LightningPlasmaCD_col', 100)
    GFX_0('UltimateLightningPlasma', 1)
    Unknown2054(0)
    loopRest()
    sprite('cs432_06', 5)
    GFX_0('caef_ultimate_globe2', 0)
    SFX_3('thunder_l')
    Unknown23029(3, 4401, 0)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaMahajiodainDSD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 104, -120000, 60000, 0, 0, 0, 0)
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('cs432_00', 4)
    sprite('cs432_01', 4)
    sprite('cs432_02', 4)
    sprite('cs432_00', 4)
    sprite('cs432_01', 4)
    sprite('cs432_02', 4)
    sprite('cs432_00', 4)
    sprite('cs432_01', 3)
    sprite('cs432_02', 3)
    sprite('cs432_03', 3)
    sprite('cs432_04', 3)
    sprite('cs432_05', 5)
    GFX_0('LightningPlasmaDSD_col', 100)
    GFX_0('UltimateLightningPlasma', 1)
    Unknown2054(0)
    loopRest()
    sprite('cs432_06', 5)
    GFX_0('caef_ultimate_globe2', 0)
    SFX_3('thunder_l')
    Unknown23029(3, 4401, 0)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PAK_PersonaMahajiodainDSDSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 104, -120000, 60000, 0, 0, 0, 0)
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('cs432_00', 4)
    sprite('cs432_01', 4)
    sprite('cs432_02', 4)
    sprite('cs432_00', 4)
    sprite('cs432_01', 4)
    sprite('cs432_02', 4)
    sprite('cs432_00', 4)
    sprite('cs432_01', 3)
    sprite('cs432_02', 3)
    sprite('cs432_03', 3)
    sprite('cs432_04', 3)
    sprite('cs432_05', 5)
    GFX_0('LightningPlasmaCDDSD_col', 100)
    GFX_0('UltimateLightningPlasma', 1)
    Unknown2054(0)
    loopRest()
    sprite('cs432_06', 5)
    GFX_0('caef_ultimate_globe2', 0)
    SFX_3('thunder_l')
    Unknown23029(3, 4401, 0)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('cs432_06', 5)
    sprite('cs432_07', 5)
    sprite('cs432_08', 5)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def CorkScrewB_DmyObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3038(1)
        Unknown23091(1)

        def upon_54():
            if (not SLOT_30):
                Unknown23029(3, 3001, 0)
    sprite('ak407_00', 3)
    sprite('ak407_04', 3)
    sprite('ak407_05', 1)
    sprite('ak407_05', 2)
    sprite('ak407_06', 3)
    sprite('ak407_08', 3)
    sprite('ak407_09', 4)
    sprite('ak407_10', 4)
    sprite('ak407_11', 4)
    sprite('ak407_12', 4)
    sprite('ak407_01ex01', 32767)

@State
def SpecialAtemiSuccess():

    def upon_IMMEDIATE():
        Unknown23067('akef_403_fistflash')
        Unknown4009(2)
        Unknown4010(2)
    sprite('null', 60)

@State
def SpecialAtemiGood():

    def upon_IMMEDIATE():
        Unknown23067('akef_403_gooddaze')
        Unknown4009(2)
        Unknown4010(2)
        Unknown1096(800)
    sprite('null', 60)

@State
def SpecialRash00():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(40000)
        Unknown1007(180000)
        Unknown1096(1500)
        Unknown2019(100)
    sprite('vrakef_sp_rash00', 2)
    sprite('vrakef_sp_rash00', 4)
    physicsXImpulse(36000)
    physicsYImpulse(20000)
    Unknown3004(-64)

@State
def SpecialRash01():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(130000)
        Unknown1007(270000)
    sprite('vrakef_sp_rash03', 2)
    sprite('vrakef_sp_rash03', 2)
    Unknown3004(-128)

@State
def SpecialRash02():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(-20000)
        Unknown1007(255000)
        Unknown1096(1500)
    sprite('vrakef_sp_rash02', 2)
    sprite('vrakef_sp_rash02', 4)
    physicsXImpulse(60000)
    Unknown3004(-64)

@State
def SpecialRash03():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(122000)
        Unknown1007(250000)
    sprite('vrakef_sp_rash03', 2)
    sprite('vrakef_sp_rash03', 2)
    Unknown3004(-128)

@State
def SpecialRash04():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(130000)
        Unknown1007(240000)
    sprite('vrakef_sp_rash04', 2)

@State
def SpecialRash05():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(80000)
        Unknown1007(320000)
        Unknown1099(50)
        physicsXImpulse(-5000)
        physicsYImpulse(1000)
    sprite('null', 2)
    sprite('vrakef_sp_rash05', 8)
    Unknown3004(-32)

@State
def SpecialQuakeSmoke():

    def upon_IMMEDIATE():
        Unknown23067('akef_quake_smoke')
        Unknown4009(2)
    sprite('null', 70)

@State
def SpecialBodyBlowFirst():

    def upon_IMMEDIATE():
        Unknown4003('akef_sp_blow_wind00', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown3026(-14336)
        teleportRelativeX(-80000)
        Unknown1007(150000)
        Unknown1096(1200)
    sprite('null', 4)
    Unknown3004(-62)

@State
def SpecialBodyBlowMain():

    def upon_IMMEDIATE():
        Unknown4003('akef_sp_blow_wind01', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(80000)
        Unknown1007(100000)
        Unknown1096(1200)
        Unknown1067(-50)
        Unknown1072(-500)
        Unknown1074(-400)
    sprite('null', 2)
    sprite('null', 5)
    Unknown3004(-51)

@State
def akef_dashupper():

    def upon_IMMEDIATE():
        Unknown4003('akef_409upper', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown3026(-14336)
        Unknown1096(1500)
    sprite('null', 2)
    Unknown3001(64)
    Unknown3004(128)
    GFX_1('akef_dashupper_splash', 100)
    sprite('null', 2)
    sprite('null', 4)
    Unknown3004(-32)

@State
def SpecialScrewWind():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_0('SpecialScrewWind00', 100)
        GFX_0('SpecialScrewWind01', 100)
        GFX_0('SpecialScrewWind02', 100)
        Unknown1007(-16000)
    sprite('null', 30)

@State
def SpecialScrewWind00():

    def upon_IMMEDIATE():
        Unknown4003('akef_sp_screw_wind', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown1072(20000)
        Unknown4010(2)
        Unknown3032()
        Unknown23118(-14336)
        Unknown1096(500)
        Unknown1066(60)
        Unknown1099(6)
    sprite('null', 10)
    Unknown3004(-25)

@State
def SpecialScrewWind01():

    def upon_IMMEDIATE():
        Unknown4003('akef_sp_screw_wind2', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown1072(20000)
        Unknown4010(2)
        Unknown3032()
        Unknown23118(-14336)
        teleportRelativeX(60000)
        Unknown1096(350)
        Unknown1066(60)
        Unknown1099(4)
        Unknown1007(-12000)
    sprite('null', 15)
    Unknown3004(-20)

@State
def SpecialScrewWind02():

    def upon_IMMEDIATE():
        Unknown4003('akef_sp_screw_wind', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown1072(20000)
        Unknown4010(2)
        Unknown3032()
        Unknown23118(-14336)
        teleportRelativeX(100000)
        Unknown1096(250)
        Unknown1058(120)
        Unknown1066(60)
        Unknown1099(2)
        Unknown1007(12000)
    sprite('null', 20)
    Unknown3004(-15)

@State
def SpecialScrewFistAura():

    def upon_IMMEDIATE():
        Unknown23067('akef_404_fistaura')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1056(500)
        Unknown1064(1000)
        teleportRelativeX(80000)
        GFX_0('SpecialScrewShockWave', 100)
        GFX_0('SpecialScrewShockWave', 100)
        Unknown36(1)
        Unknown1098(70)
        teleportRelativeX(110000)
        Unknown35()
    sprite('null', 2)
    sprite('null', 10)
    Unknown4007(0)
    Unknown1064(1500)
    teleportRelativeX(60000)
    Unknown3004(-25)

@State
def SpecialScrewShockWave():

    def upon_IMMEDIATE():
        Unknown23067('akef_404_shockwave')
        Unknown4011(3)
    sprite('null', 20)

@State
def UltimateUpperSmoke():

    def upon_IMMEDIATE():
        Unknown23067('akef_dash_smoke')
        Unknown4009(2)
    sprite('null', 70)

@State
def SpecialAirBodyAura():

    def upon_IMMEDIATE():
        Unknown23067('akef_408_bodyaura')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(1500)
        Unknown1072(130000)
        teleportRelativeX(150000)
        Unknown1007(80000)

        def upon_STATE_END():
            GFX_0('SpecialAirAuraEnd', 100)
    sprite('null', 120)

@State
def SpecialAirAuraEnd():

    def upon_IMMEDIATE():
        Unknown23067('akef_408_aura_end')
        Unknown4013(2)
        Unknown4006(2)
        Unknown4011(3)
        teleportRelativeX(-140000)
        Unknown1007(80000)
    sprite('null', 20)

@State
def SpecialAirFistAura():

    def upon_IMMEDIATE():
        Unknown23067('akef_408_fistaura')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(1300)
    sprite('null', 120)

@State
def SpecialDoubleUpperFirst():

    def upon_IMMEDIATE():
        Unknown23067('akef_400_1st_punch')
        Unknown4009(2)
        Unknown4010(2)
    sprite('null', 10)

@State
def SpecialDoubleUpperSecond():

    def upon_IMMEDIATE():
        Unknown23067('akef_400_uppersmoke')
        Unknown4010(2)
        teleportRelativeX(40000)
    sprite('null', 60)

@State
def SpecialDashSmoke():

    def upon_IMMEDIATE():
        Unknown23067('akef_dash_smoke')
        Unknown4009(2)
    sprite('null', 70)

@State
def UltimateFirstStep():

    def upon_IMMEDIATE():
        Unknown23067('akef_430_1st_step')
        Unknown4009(2)
    sprite('null', 60)

@State
def UltimatePunchSuccess():

    def upon_IMMEDIATE():
        Unknown23067('akef_430_punch_ok')
        Unknown4009(2)
    sprite('null', 60)
    SFX_3('grip_hugs')
    ScreenShake(5000, 10000)

@State
def UltimateFirstPunch():

    def upon_IMMEDIATE():
        Unknown23067('akef_430_1st_punch')
        Unknown4009(2)
    sprite('null', 60)

@State
def UltimateUpperFistAura():

    def upon_IMMEDIATE():
        Unknown23067('akef_431_fistaura')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)

@State
def UltimateUpperSmoke():

    def upon_IMMEDIATE():
        Unknown23067('akef_dash_smoke')
        Unknown4009(2)
    sprite('null', 70)

@State
def UltimateUpperWind():

    def upon_IMMEDIATE():
        Unknown4003('akef_ultm_upper_wind', '')
        Unknown4009(2)
        Unknown3033()
        Unknown3026(-328976)
        teleportRelativeX(-120000)
        Unknown1007(120000)
        physicsXImpulse(8000)
        GFX_0('UltimateUpperWindPlus', 100)
    sprite('null', 20)
    sprite('null', 10)
    Unknown3004(-25)

@State
def UltimateUpperWindPlus():

    def upon_IMMEDIATE():
        Unknown4003('akef_ultm_upper_wind', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown3033()
        Unknown3026(-328976)
        Unknown3001(0)
        teleportRelativeX(120000)
        Unknown1007(200000)
        Unknown1096(600)
    sprite('null', 2)
    Unknown3004(125)
    sprite('null', 20)
    sprite('null', 25)
    Unknown3004(-10)

@State
def UltimateTodomeUpper():

    def upon_IMMEDIATE():
        Unknown4003('akef_ultm_upper_light', '')
        Unknown4009(2)
        Unknown4010(3)
        Unknown3032()
        Unknown23015(2)
        Unknown2019(500)
        teleportRelativeX(-50000)
        Unknown1056(200)
        Unknown1065(-500)
        Unknown1072(10000)
        GFX_0('UltimateTodomeUpperPlus', 100)

        def upon_43():
            if (SLOT_48 == 4301):
                sendToLabel(0)
            if (SLOT_48 == 4302):
                Unknown4007(3)
                sendToLabel(1)
    sprite('null', 2)
    Unknown1057(100)
    physicsXImpulse(5000)
    loopRest()
    sprite('null', 10)
    sprite('null', 15)
    Unknown3004(-50)
    Unknown1059(10)
    ExitState()
    label(1)
    sprite('null', 1)
    GFX_0('UltimateTodomeUpper', 100)
    physicsXImpulse(0)
    loopRest()
    sprite('null', 32767)
    ExitState()
    label(0)
    sprite('null', 15)
    Unknown3004(-15)

@State
def UltimateTodomeUpperB():

    def upon_IMMEDIATE():
        Unknown4003('akef_ultm_upper_light', '')
        Unknown4009(2)
        Unknown4010(3)
        Unknown23015(2)
        Unknown2019(500)
        Unknown3032()
        teleportRelativeX(-50000)
        Unknown1056(300)
        Unknown1065(-250)
        Unknown1072(10000)
        GFX_0('UltimateTodomeUpperPlus', 100)

        def upon_43():
            if (SLOT_48 == 4301):
                sendToLabel(0)
            if (SLOT_48 == 4302):
                Unknown4007(3)
                sendToLabel(1)
    sprite('null', 2)
    Unknown1057(100)
    physicsXImpulse(5000)
    loopRest()
    sprite('null', 10)
    sprite('null', 15)
    Unknown3004(-50)
    Unknown1059(10)
    ExitState()
    label(1)
    sprite('null', 1)
    GFX_0('UltimateTodomeUpperB', 100)
    physicsXImpulse(0)
    loopRest()
    sprite('null', 32767)
    ExitState()
    label(0)
    sprite('null', 15)
    Unknown3004(-15)

@State
def UltimateTodomeUpperPlus():

    def upon_IMMEDIATE():
        Unknown23067('akef_430_2nd_todome')
    sprite('null', 70)

@State
def Zanzoh5C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
        Unknown3001(255)
    sprite('vr_cs204_00', 2)
    sprite('vr_cs204_01', 16)
    Unknown3004(-20)

@State
def ZanzohAir5C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
        Unknown3001(255)
    sprite('vr_cs254_00', 2)
    sprite('vr_cs254_01', 2)
    sprite('vr_cs254_02', 16)
    Unknown3004(-50)

@State
def LightningPlasma_col():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(480)
        AttackP1(80)
        AttackP2(97)
        MinimumDamagePct(15)
        AirUntechableTime(100)
        AirPushbackY(5000)
        PushbackX(2000)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11023(1)
        Unknown11056(3)
        Unknown11068(1)
        ChipDamagePct(5)
        SLOT_51 = 16
        if (SLOT_6 == 0):
            pass
        if (SLOT_6 == 1):
            Unknown10000(110)
            ChipDamagePct(6)
        if (SLOT_6 == 2):
            Unknown10000(120)
            ChipDamagePct(7)
        if (SLOT_6 == 3):
            Unknown10000(130)
            ChipDamagePct(8)
        if (SLOT_6 == 4):
            Unknown10000(140)
            ChipDamagePct(9)
        if (SLOT_6 == 5):
            Unknown10000(150)
            ChipDamagePct(10)

        def upon_3():
            op(4, 2, 51, 0, 2)
            if (SLOT_0 == 0):
                Unknown11050(0, '')
            else:
                Unknown11050(5, '')
    label(0)
    sprite('dmy_atk00', 1)
    Unknown23151(22, 105)
    RefreshMultihit()
    if (SLOT_51 == 1):
        Unknown9083()
    sprite('dmy_atk00', 1)
    DisableAttackRestOfMove()
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(9, 2, 51)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 10)
    SLOT_6 = 0
    Unknown21015('UltimateLightningPlasma', 4301, 0)

@State
def LightningPlasmaCD_col():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(410)
        AttackP1(80)
        AttackP2(98)
        MinimumDamagePct(14)
        AirUntechableTime(100)
        AirPushbackY(5000)
        PushbackX(2000)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11023(1)
        Unknown11056(3)
        Unknown11068(1)
        ChipDamagePct(5)
        SLOT_51 = 24
        if (SLOT_6 == 0):
            pass
        if (SLOT_6 == 1):
            Unknown10000(110)
            ChipDamagePct(6)
        if (SLOT_6 == 2):
            Unknown10000(120)
            ChipDamagePct(7)
        if (SLOT_6 == 3):
            Unknown10000(130)
            ChipDamagePct(8)
            Unknown11110(99)
        if (SLOT_6 == 4):
            Unknown10000(140)
            ChipDamagePct(9)
            Unknown11110(96)
        if (SLOT_6 == 5):
            Unknown10000(150)
            ChipDamagePct(10)
            Unknown11110(94)

        def upon_3():
            op(4, 2, 51, 0, 2)
            if (SLOT_0 == 0):
                Unknown11050(0, '')
            else:
                Unknown11050(5, '')
    label(0)
    sprite('dmy_atk00', 1)
    Unknown23151(22, 105)
    RefreshMultihit()
    if (SLOT_51 == 1):
        Unknown9083()
    sprite('dmy_atk00', 1)
    DisableAttackRestOfMove()
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(9, 2, 51)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 10)
    SLOT_6 = 0
    Unknown21015('UltimateLightningPlasma', 4301, 0)

@State
def LightningPlasmaDSD_col():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(125)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirUntechableTime(100)
        AirPushbackY(5000)
        PushbackX(2000)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11023(1)
        Unknown11056(3)
        Unknown11068(1)
        SLOT_51 = 16

        def upon_3():
            op(4, 2, 51, 0, 2)
            if (SLOT_0 == 0):
                Unknown11050(0, '')
            else:
                Unknown11050(5, '')
    label(0)
    sprite('dmy_atk00', 1)
    Unknown23151(22, 105)
    RefreshMultihit()
    if (SLOT_51 == 1):
        Unknown9083()
    sprite('dmy_atk00', 1)
    DisableAttackRestOfMove()
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(9, 2, 51)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 10)
    SLOT_6 = 0
    Unknown21015('UltimateLightningPlasma', 4301, 0)

@State
def LightningPlasmaCDDSD_col():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirUntechableTime(100)
        AirPushbackY(5000)
        PushbackX(2000)
        Hitstop(0)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9266(6)
        Unknown9021(1)
        Unknown11023(1)
        Unknown11056(3)
        Unknown11068(1)
        SLOT_51 = 24

        def upon_3():
            op(4, 2, 51, 0, 2)
            if (SLOT_0 == 0):
                Unknown11050(0, '')
            else:
                Unknown11050(5, '')
    label(0)
    sprite('dmy_atk00', 1)
    Unknown23151(22, 105)
    RefreshMultihit()
    if (SLOT_51 == 1):
        Damage(200)
        Unknown9083()
    sprite('dmy_atk00', 1)
    DisableAttackRestOfMove()
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(9, 2, 51)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 10)
    SLOT_6 = 0
    Unknown21015('UltimateLightningPlasma', 4301, 0)

@State
def UltimateLightningPlasma():

    def upon_IMMEDIATE():
        GFX_2('akef_432_lightning')
        Unknown4009(2)
        GFX_0('UltimateLightningPlasma00', 100)
        GFX_0('UltimateLightningPlasma01', 100)
        GFX_0('UltimateLightningPlasma02', 100)
        GFX_0('UltimateLightningPlasma03', 100)

        def upon_43():
            if (SLOT_48 == 4301):
                sendToLabel(0)
    sprite('null', 140)
    label(0)
    sprite('null', 1)

@State
def UltimateLightningPlasma00():

    def upon_IMMEDIATE():
        Unknown4003('akef_ultm_thunder00', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
    label(5)
    sprite('null', 2)
    Unknown3001(255)
    Unknown1056(1000)
    Unknown1064(1000)
    Unknown1079()
    sprite('null', 2)
    Unknown3001(20)
    Unknown1056(1000)
    Unknown1064(-1000)
    Unknown1079()
    sprite('null', 2)
    Unknown3001(255)
    Unknown1056(-1000)
    Unknown1064(1000)
    Unknown1079()
    sprite('null', 2)
    Unknown3001(20)
    Unknown1056(-1000)
    Unknown1064(-1000)
    Unknown1079()
    loopRest()
    gotoLabel(5)

@State
def UltimateLightningPlasma01():

    def upon_IMMEDIATE():
        Unknown4003('akef_ultm_thunder01', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
    label(5)
    sprite('null', 2)
    Unknown3001(50)
    Unknown1056(1000)
    Unknown1064(1000)
    Unknown1079()
    sprite('null', 2)
    Unknown3001(255)
    Unknown1056(1000)
    Unknown1064(-1000)
    Unknown1079()
    sprite('null', 2)
    Unknown1056(-1000)
    Unknown1064(1000)
    Unknown1079()
    sprite('null', 2)
    Unknown3001(255)
    Unknown1056(-1000)
    Unknown1064(-1000)
    Unknown1079()
    loopRest()
    gotoLabel(5)

@State
def UltimateLightningPlasma02():

    def upon_IMMEDIATE():
        Unknown4003('akef_ultm_thunder02', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
    label(5)
    sprite('null', 2)
    Unknown3001(100)
    Unknown1056(1000)
    Unknown1064(1000)
    sprite('null', 2)
    Unknown3001(50)
    Unknown1056(1000)
    Unknown1064(-1000)
    sprite('null', 2)
    Unknown3001(100)
    Unknown1056(-1000)
    Unknown1064(1000)
    sprite('null', 2)
    Unknown3001(50)
    Unknown1056(-1000)
    Unknown1064(-1000)
    loopRest()
    gotoLabel(5)

@State
def UltimateLightningPlasma03():

    def upon_IMMEDIATE():
        Unknown4003('akef_ultm_thunder03', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
    label(5)
    sprite('null', 2)
    Unknown3001(150)
    Unknown1056(1000)
    Unknown1064(1000)
    sprite('null', 2)
    Unknown3001(255)
    Unknown1056(1000)
    Unknown1064(-1000)
    sprite('null', 2)
    Unknown3001(150)
    Unknown1056(-1000)
    Unknown1064(1000)
    sprite('null', 2)
    Unknown3001(255)
    Unknown1056(-1000)
    Unknown1064(-1000)
    loopRest()
    gotoLabel(5)

@State
def caef_ultimate_globe2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown1096(1000)
        Unknown2019(-100)
        GFX_0('caef_ultimate_globe_add2', 100)
        Unknown38(4, 1)

        def upon_STATE_END():
            Unknown13(4)

        def upon_43():
            if (SLOT_48 == 4301):
                sendToLabel(10)
    label(0)
    sprite('vr_csef_globe00', 4)
    sprite('vr_csef_globe01', 4)
    sprite('vr_csef_globe02', 4)
    sprite('vr_csef_globe03', 4)
    sprite('vr_csef_globe04', 4)
    sprite('vr_csef_globe05', 4)
    sprite('vr_csef_globe06', 4)
    sprite('vr_csef_globe07', 4)
    sprite('vr_csef_globe08', 4)
    sprite('vr_csef_globe09', 4)
    sprite('vr_csef_globe10', 4)
    sprite('vr_csef_globe11', 4)
    gotoLabel(0)
    label(10)
    sprite('vr_csef_globe00', 2)
    Unknown1099(-100)
    sprite('vr_csef_globe01', 2)
    sprite('vr_csef_globe02', 2)
    sprite('vr_csef_globe03', 2)
    sprite('vr_csef_globe04', 2)

@State
def caef_ultimate_globe_add2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4010(2)
        Unknown2019(-100)
    sprite('vr_csef_globe_add', 32767)

@State
def PAK_PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, 50000, 0, 0, 0, 0, 0)
        callSubroutine('PAK_DDAttackInit')
        callSubroutine('PAK_CheckWarp')
        Unknown23022(1)
        Unknown23066(1)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 4511):
                sendToLabel(0)
            if (SLOT_48 == 4512):
                sendToLabel(1)
            if (SLOT_48 == 4513):
                sendToLabel(2)
    sprite('cs450_00', 6)
    sprite('cs450_01', 6)
    sprite('cs450_02', 6)
    sprite('cs450_03', 6)
    sprite('cs450_04', 6)
    sprite('cs450_05', 6)
    sprite('cs450_06', 6)
    GFX_0('caef_Ichigeki_globe', 0)
    GFX_0('caef_Ichigeki_globe_col', 0)
    sprite('cs450_07', 6)
    sprite('cs450_08', 6)
    sprite('cs450_06', 6)
    GFX_0('450Vacuum', 0)
    sprite('cs450_07', 6)
    sprite('cs450_08', 6)
    sprite('cs450_06', 6)
    sprite('cs450_07', 6)
    sprite('cs450_08', 6)
    sprite('cs450_06', 6)
    sprite('cs450_07', 6)
    sprite('cs450_08', 6)
    sprite('cs450_07', 6)
    sprite('cs450_08', 6)
    Unknown26('caef_Ichigeki_globe_col')
    sprite('cs450_06', 6)
    sprite('cs450_07', 6)
    sprite('cs450_08', 6)
    sprite('cs450_06', 6)
    sprite('cs450_07', 6)
    sprite('cs450_08', 6)
    sprite('cs450_06', 6)
    sprite('cs450_07', 6)
    sprite('cs450_08', 6)
    gotoLabel(9)
    label(0)
    sprite('cs450_06', 6)
    Unknown23022(1)
    sprite('cs450_07', 6)
    sprite('cs450_08', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 32767)
    Unknown23022(1)
    Unknown21015('450Vacuum', 4532, 0)
    Unknown26('caef_Ichigeki_globe')
    Unknown26('caef_Ichigeki_globe_col')
    Unknown1000(2500000)
    label(2)
    sprite('cs450_09', 8)
    Unknown23022(1)
    GFX_0('caef_Ichigeki_globe', 0)
    Unknown1000(0)
    teleportRelativeY(5930000)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('cs450_10', 8)
    GFX_0('450globeyoin', 0)
    SFX_3('bomb_m')
    sprite('cs450_11', 8)
    sprite('cs450_11', 8)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_11', 8)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_11', 8)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_11', 8)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_11', 8)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_11', 8)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_11', 8)
    label(3)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_11', 8)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_11', 8)
    sprite('cs450_09', 8)
    sprite('cs450_10', 8)
    sprite('cs450_11', 8)
    gotoLabel(3)
    label(9)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def IchigekiCamera():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20002(0)
            Unknown20003(0)

        def upon_43():
            if (SLOT_48 == 4521):
                sendToLabel(1)
            if (SLOT_48 == 4522):
                sendToLabel(2)
            if (SLOT_48 == 4523):
                sendToLabel(3)
            if (SLOT_48 == 4524):
                sendToLabel(4)
            if (SLOT_48 == 4525):
                sendToLabel(5)
    label(1)
    sprite('null', 10)
    Unknown1086(3)
    teleportRelativeX(260000)
    Unknown1007(275000)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown23013(0)
    Unknown2008()

    def upon_3():
        SLOT_105 = (SLOT_105 + (-10))
    sprite('null', 5)
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-20))
    sprite('null', 5)
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-30))
    sprite('null', 5)
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-40))
    sprite('keep', 10)
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-50))
    sprite('keep', 20)
    clearUponHandler(3)
    SystemGFX('SCEF_FadeBlack12In', 100)
    Unknown23024(3)
    sprite('keep', 32767)
    Unknown20009(1000)
    Unknown21015('AstralHeat', 4502, 0)
    label(2)
    sprite('keep', 20)
    Unknown1000(0)
    teleportRelativeY(1200000)
    physicsXImpulse(0)
    physicsYImpulse(-60000)
    Unknown20000(1)
    Unknown20001(1)
    Unknown26('SCEF_FadeBlack12In')
    sprite('keep', 30)
    sprite('keep', 30)
    Unknown21015('AstralHeat', 4503, 0)
    label(3)
    sprite('keep', 20)
    SystemGFX('SCEF_FadeBlack12In', 100)
    sprite('keep', 2)
    teleportRelativeY(1950000)
    physicsYImpulse(62500)
    sprite('keep', 18)
    Unknown26('SCEF_FadeBlack12In')
    SystemGFX('SCEF_FadeBlack12Out', 100)
    Unknown36(1)
    Unknown1096(8000)
    Unknown35()
    Unknown20009(3800)
    Unknown20000(1)
    Unknown20001(1)
    sprite('keep', 10)
    physicsYImpulse(-10000)
    sprite('keep', 60)
    physicsYImpulse(-8000)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-30))
    SFX_3('ak000')
    sprite('keep', 5)
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + (-150))
    physicsYImpulse(70000)
    sprite('keep', 10)
    GFX_0('IchigekiWhite', 100)
    GFX_1('csef_450flash', 100)
    sprite('keep', 32767)
    clearUponHandler(3)
    Unknown21015('AstralHeat', 4504, 0)
    label(4)
    sprite('keep', 80)
    teleportRelativeY(0)
    physicsYImpulse(0)
    Unknown20009(1000)
    Unknown20007(1)
    Unknown20001(1)
    sprite('keep', 32767)
    GFX_1('csef_450flash', 100)
    label(5)
    sprite('keep', 20)
    sprite('keep', 195)
    Unknown1000(0)
    teleportRelativeY(6300000)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown20000(1)
    Unknown20001(1)
    sprite('keep', 60)
    Unknown1000(-134000)
    teleportRelativeY(6550000)
    physicsYImpulse(-900)
    Unknown20000(1)
    Unknown20001(1)
    Unknown20009(100)

    def upon_3():
        SLOT_105 = (SLOT_105 + 9)
    sprite('keep', 80)
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + 7)
    physicsYImpulse(-700)
    sprite('keep', 80)
    clearUponHandler(3)

    def upon_3():
        SLOT_105 = (SLOT_105 + 3)
    physicsYImpulse(-300)
    sprite('keep', 30)
    SystemGFX('SCEF_FadeBlack12In', 100)
    Unknown21015('AstralHeat', 4505, 0)
    label(6)
    sprite('keep', 20)
    clearUponHandler(3)
    Unknown20009(1000)
    Unknown1000(0)
    teleportRelativeY(0)
    GFX_0('450finishsmoke', 103)
    Unknown23024(0)
    sprite('keep', 32767)
    Unknown26('SCEF_FadeBlack12In')
    SystemGFX('SCEF_FadeBlack12Out', 100)

@State
def caef_Ichigeki_globe():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    sprite('vr_csef_globe00', 4)
    sprite('vr_csef_globe01', 4)
    sprite('vr_csef_globe02', 4)
    sprite('vr_csef_globe03', 4)
    sprite('vr_csef_globe04', 4)
    sprite('vr_csef_globe05', 4)
    sprite('vr_csef_globe06', 4)
    sprite('vr_csef_globe07', 4)
    sprite('vr_csef_globe08', 4)
    sprite('vr_csef_globe09', 4)
    sprite('vr_csef_globe10', 4)
    sprite('vr_csef_globe11', 4)
    label(0)
    sprite('vr_csef_globe00', 4)
    sprite('vr_csef_globe01', 4)
    sprite('vr_csef_globe02', 4)
    sprite('vr_csef_globe03', 4)
    sprite('vr_csef_globe04', 4)
    sprite('vr_csef_globe05', 4)
    sprite('vr_csef_globe06', 4)
    sprite('vr_csef_globe07', 4)
    sprite('vr_csef_globe08', 4)
    sprite('vr_csef_globe09', 4)
    sprite('vr_csef_globe10', 4)
    sprite('vr_csef_globe11', 4)
    gotoLabel(0)

@State
def caef_Ichigeki_globe_col():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(10000)
        Unknown11064(1)
        AirUntechableTime(10000)
        Unknown9310(10000)
        AirPushbackX(0)
        AirPushbackY(150)
        YImpluseBeforeWallbounce(3)
        Unknown11072(1, 5000, -220000)
        GroundedHitstunAnimation(1)
        Unknown30055(0, 2, 2)
        Unknown30056(0, 2, 2)
        ProjectileDurabilityLvl(3)
        Unknown4007(2)
        Unknown4009(3)
        Unknown4010(3)
        DisableAttackRestOfMove()

        def upon_12():
            Unknown21015('AstralHeat', 4501, 0)
    sprite('dmy_atk00', 15)
    Unknown21003(1000, 250)
    sprite('dmy_atk00', 15)
    Unknown21003(4000, 1000)
    sprite('dmy_atk00', 15)
    Unknown21003(7000, 1750)
    SFX_3('ak003')
    sprite('dmy_atk00', 15)
    Unknown21003(10000, 2500)
    RefreshMultihit()
    SFX_3('ak003')
    sprite('dmy_atk00', 15)
    Unknown21003(11000, 2750)
    SFX_3('ak003')
    sprite('dmy_atk00', 15)
    Unknown21003(12000, 3000)
    SFX_3('ak003')
    sprite('dmy_atk00', 15)
    SFX_3('ak003')
    sprite('dmy_atk00', 15)
    SFX_3('ak003')
    sprite('dmy_atk00', 32767)

@State
def __450Vacuum():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        GFX_2('csef_450vacuum')
        Unknown4010(2)
        Unknown3032()
        Unknown3057(1)
        Unknown3058(1000)
        Unknown1096(2500)
        Unknown1099(-20)

        def upon_43():
            if (SLOT_48 == 4532):
                sendToLabel(0)
    sprite('vr_ak_yugami', 5)
    Unknown1074(5000)
    Unknown3058(4000)
    sprite('vr_ak_yugami', 10)
    Unknown1074(10000)
    Unknown3058(8000)
    sprite('vr_ak_yugami', 15)
    Unknown1074(25000)
    Unknown3058(14000)
    sprite('vr_ak_yugami', 20)
    Unknown1074(50000)
    Unknown3058(19000)
    sprite('vr_ak_yugami', 32767)
    Unknown1074(90000)
    Unknown3058(24000)
    label(0)
    sprite('vr_ak_yugami', 5)
    Unknown1074(90000)
    Unknown3058(24000)
    Unknown3004(-51)

@State
def Groundglobe():

    def upon_IMMEDIATE():
        Unknown4003('akef_450globe.DIG', '')
        Unknown3032()
        teleportRelativeY(0)
        Unknown1000(0)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 4531):
                sendToLabel(0)
    sprite('null', 32767)
    Unknown3004(50)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def Ichigekibeam():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('akef_450beam.DIG', '')
        Unknown23067('akef_450punch')
        Unknown2054(1)
        Unknown3032()
    sprite('null', 600)
    sprite('null', 20)
    Unknown3004(-13)

@State
def Ichigekiimpact():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('akef_450hitimpact.DIG', '')
        Unknown2054(1)
        Unknown3032()
    sprite('null', 30)
    sprite('null', 80)
    Unknown1099(40)
    sprite('null', 20)
    Unknown3004(-13)

@State
def Ichigekiimpact_bg():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown23015(1)
        GFX_2('csef_450aura')
        Unknown2054(1)
        Unknown3032()
        Unknown3001(0)
    sprite('null', 30)
    sprite('null', 100)
    Unknown3004(6)
    sprite('null', 20)
    Unknown3004(-13)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown23015(2)
        Unknown6001(1)
        Unknown2007()
        Unknown1000(0)
        teleportRelativeY(200000)
        Unknown3001(0)
        Unknown3004(8)
        GFX_0('Cutinbg', 100)
        Unknown23119(16777215, 166, 1)
        GFX_0('450flasheff', 100)
    SLOT_51 = 20
    label(1)
    sprite('ichigeki', 2)
    Unknown1000(0)
    teleportRelativeY(200000)
    Unknown1010(-6000, 6000)
    Unknown1011(-6000, 6000)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(10, 2, 51)
    gotoLabel(1)
    label(10)
    SLOT_51 = 20
    label(11)
    sprite('ichigeki', 2)
    Unknown1000(0)
    teleportRelativeY(200000)
    Unknown1010(-8000, 8000)
    Unknown1011(-8000, 8000)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(20, 2, 51)
    gotoLabel(11)
    label(20)
    SLOT_51 = 30
    label(21)
    sprite('ichigeki', 1)
    Unknown1000(0)
    teleportRelativeY(200000)
    Unknown1010(-14000, 14000)
    Unknown1011(-14000, 14000)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(30, 2, 51)
    gotoLabel(21)
    label(30)
    SLOT_51 = 55
    label(31)
    sprite('ichigeki', 1)
    Unknown1000(0)
    teleportRelativeY(200000)
    Unknown1010(-18000, 18000)
    Unknown1011(-18000, 18000)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(0, 2, 51)
    gotoLabel(31)
    label(0)
    sprite('ichigeki', 1)

@State
def __450flasheff():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        teleportRelativeX(550000)
        teleportRelativeY(5800000)
        Unknown1096(2500)
    sprite('null', 100)
    GFX_1('akef450_flash', 100)

@State
def Cutinbg():

    def upon_IMMEDIATE():
        Unknown4003('akef_450cutinbg.DIG', '')
        Unknown3032()
        Unknown23015(2)
        Unknown2007()
        Unknown3001(0)
        Unknown1007(850000)
    sprite('null', 40)
    Unknown3004(15)
    sprite('null', 115)
    Unknown23119(16777215, 110, 1)
    sprite('null', 45)
    sprite('null', 30)
    Unknown3004(-9)

@State
def __450burst():

    def upon_IMMEDIATE():
        Unknown1000(0)
        teleportRelativeY(6300000)
        Unknown3032()
    sprite('null', 40)
    sprite('null', 20)
    GFX_1('csef_450burst', 100)
    Unknown23119(-14216, 30, 1)
    Unknown3004(-13)

@State
def __450globeyoin():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4007(2)
        Unknown3032()
    sprite('null', 30)
    sprite('null', 50)
    GFX_1('csef_450globeyoin', 100)
    GFX_1('csef_450globehikari', 100)
    sprite('null', 20)
    Unknown3004(-13)

@State
def IchigekiWhite():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown23015(4)
        Unknown1096(5000)
        Unknown4007(2)
        Unknown3001(0)
    sprite('vr_ak450_white', 30)
    Unknown3004(16)
    sprite('vr_ak450_white', 25)
    Unknown3004(-11)

@State
def __450finishsmoke():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23067('csef_450smoke')
        Unknown1000(0)
        teleportRelativeY(0)
    sprite('null', 90)
    sprite('null', 26)
    Unknown3004(-10)

@State
def LifeLinkEff():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 1)
    Unknown4045('ntef_story_lifelinkeff_line2', -1)

@State
def PAK_PersonaMatchWin():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184(3, 100, -100000, 180000, -100000, 180000, -100000, 180000)
        callSubroutine('PersonaReset')
        callSubroutine('PAK_CheckWarp')
        Unknown23022(1)
        Unknown4007(3)
    sprite('cs610_00', 6)
    physicsYImpulse(-6000)
    sprite('cs610_01', 6)
    sprite('cs610_00', 6)
    sprite('cs610_01', 6)
    sprite('cs610_00', 6)
    sprite('cs610_02', 6)
    Unknown8000(100, 1, 1)
    ScreenShake(5000, 15000)
    sprite('cs610_03', 6)
    label(9)
    sprite('cs610_04', 6)
    SFX_0('cloth_l')
    sprite('cs610_05', 6)
    sprite('cs610_06', 6)
    gotoLabel(9)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def akef_entry_shadows():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown13044(1)
        Unknown23023()
        teleportRelativeY(0)
    sprite('vr_ak600_00', 32767)
    GFX_0('akef_entry_bag', 100)

@State
def akef_entry_shadows_clash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown13044(1)
        Unknown23023()
    sprite('vr_ak600_00', 8)
    Unknown1000(-1230000)
    Unknown3004(-32)
    GFX_1('akef_entry_clash02', 0)
    GFX_1('akef_entry_clash02', 1)
    GFX_1('akef_entry_clash02', 2)
    GFX_1('akef_entry_clash02', 3)
    GFX_1('akef_entry_clash02', 4)
    GFX_1('akef_entry_clash02', 5)
    GFX_1('akef_entry_clash02', 6)
    GFX_1('akef_entry_clash02', 7)
    GFX_0('akef_entry_bag_clash', 100)

@State
def akef_entry_bag():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown13044(1)
        Unknown23023()
        teleportRelativeX(50000)
        Unknown1007(500000)
    sprite('vr_ak600_10', 32767)

@State
def akef_entry_bag_clash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown13044(1)
        Unknown23023()
        teleportRelativeX(50000)
        Unknown1007(500000)
    sprite('vr_ak600_11', 60)
    physicsXImpulse(12000)
    physicsYImpulse(8000)
    Unknown3004(-8)
    Unknown1074(15000)

@State
def pak644_wind():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(30000)
    sprite('null', 1)
    GFX_1('pakef644_landwind', 100)

@State
def pak644_wind_3D():

    def upon_IMMEDIATE():
        pass
    sprite('null', 2)
    GFX_1('pakef644_knackle', 100)
    GFX_0('pak644_wind_3D_1', 100)
    sprite('null', 3)
    GFX_0('pak644_wind_3D_2', 100)
    sprite('null', 3)
    GFX_0('pak644_wind_3D_3', 100)
    sprite('null', 3)
    GFX_0('pak644_wind_3D_4', 100)

@State
def pak644_wind_3D_1():

    def upon_IMMEDIATE():
        Unknown4003('pakef_600wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(80)
        Unknown1096(2500)
        Unknown1072(-45000)
        Unknown1077(-5000, 5000)
    sprite('null', 60)
    Unknown2055(9)
    Unknown1099(500)

@State
def pak644_wind_3D_2():

    def upon_IMMEDIATE():
        Unknown4003('pakef_600wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(80)
        Unknown1096(2500)
        Unknown1072(45000)
        Unknown1077(-5000, 5000)
    sprite('null', 60)
    Unknown2055(9)
    Unknown1099(500)

@State
def pak644_wind_3D_3():

    def upon_IMMEDIATE():
        Unknown4003('pakef_600wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(80)
        Unknown1096(1750)
        Unknown1007(-125000)
        Unknown1072(-15000)
        Unknown1077(-5000, 5000)
    sprite('null', 60)
    Unknown2055(9)
    Unknown1099(500)

@State
def pak644_wind_3D_4():

    def upon_IMMEDIATE():
        Unknown4003('pakef_600wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(80)
        Unknown1096(2500)
        Unknown1007(-175000)
        Unknown1072(15000)
        Unknown1077(-5000, 5000)
    sprite('null', 60)
    Unknown2055(9)
    Unknown1099(500)

@State
def WinCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20002(1)
    sprite('null', 32767)

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