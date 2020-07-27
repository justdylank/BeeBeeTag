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
def Hyd_500():

    def upon_IMMEDIATE():
        Unknown1079()
    sprite('Action_500_00', 3)
    sprite('Action_500_01', 3)
    sprite('Action_500_02', 3)
    sprite('Action_500_03', 1)

@State
def Hyd_501():

    def upon_IMMEDIATE():
        Unknown1079()
    sprite('Action_501_00', 2)
    sprite('Action_501_01', 2)
    sprite('Action_501_02', 2)
    sprite('Action_501_03', 4)
    sprite('Action_501_04', 4)
    sprite('Action_501_05', 1)

@State
def Hyd_503():

    def upon_IMMEDIATE():
        Unknown1079()
    sprite('Action_503_00', 2)
    sprite('Action_503_01', 2)
    sprite('Action_503_02', 2)
    sprite('Action_503_03', 3)
    sprite('Action_503_04', 3)
    sprite('Action_503_05', 1)

@State
def Hyd_504():

    def upon_IMMEDIATE():
        Unknown1079()
    sprite('Action_504_00', 2)
    sprite('Action_504_01', 2)
    sprite('Action_504_02', 1)
    sprite('Action_504_03', 1)
    sprite('Action_504_04', 1)
    sprite('Action_504_05', 1)

@Subroutine
def InsulatorInit():
    Unknown9016(1)
    Unknown11057(0)
    Unknown11050(2, 'Hyd_501')
    ChipDamagePct(20)

@Subroutine
def InsulatorSpecialInit():
    Unknown9016(1)
    Unknown11057(0)
    Unknown11050(2, 'Hyd_501')
    Unknown9266(11)
    ChipDamagePct(30)

@State
def EffNmlAtk5ABlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_088_00', 2)
    sprite('Action_088_01', 3)
    sprite('Action_088_02', 8)
    sprite('Action_088_03', 1)

@State
def EffNmlAtk5AA():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_098_00', 1)
    sprite('Action_098_01', 2)
    sprite('Action_098_02', 2)
    sprite('Action_098_03', 4)
    sprite('Action_098_04', 6)
    sprite('Action_098_05', 1)

@State
def EffNmlAtk5BBlade00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_081_00', 1)
    sprite('Action_081_01', 2)
    sprite('Action_081_02', 2)
    sprite('Action_081_03', 4)
    sprite('Action_081_04', 6)
    sprite('Action_081_05', 1)

@State
def EffNmlAtk5BBlade01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_082_00', 1)
    sprite('Action_082_01', 2)
    sprite('Action_082_02', 2)
    sprite('Action_082_03', 4)
    sprite('Action_082_04', 6)
    sprite('Action_082_05', 1)

@State
def EffNmlAtk5CBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_089_00', 1)
    sprite('Action_089_01', 2)
    sprite('Action_089_02', 2)
    sprite('Action_089_03', 4)
    sprite('Action_089_04', 10)
    sprite('Action_089_05', 1)

@State
def EffNmlAtk66CBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_119_01', 4)
    sprite('Action_093_00', 2)
    sprite('Action_093_01', 2)
    sprite('Action_093_02', 2)
    sprite('Action_093_03', 4)
    sprite('Action_093_04', 3)
    sprite('Action_093_05', 3)

@State
def EffNmlAtk6CBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_225_00', 3)
    physicsXImpulse(15000)
    Unknown1030(-1500)
    sprite('Action_225_01', 5)
    Unknown1084(1)
    sprite('Action_225_02', 5)
    sprite('Action_225_03', 5)
    sprite('Action_225_04', 4)
    sprite('Action_225_05', 4)
    sprite('Action_225_06', 1)

@State
def EffNmlAtk6CHoldBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(240000)
        Unknown1007(-100000)
    sprite('Action_225_00', 3)
    sprite('Action_225_01', 5)
    sprite('Action_225_02', 5)
    sprite('Action_225_03', 5)
    sprite('Action_225_04', 4)
    sprite('Action_225_05', 4)
    sprite('Action_225_06', 1)

@State
def EffNmlAtk66CBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_093_00', 3)
    sprite('Action_093_01', 3)
    sprite('Action_093_02', 3)
    sprite('Action_093_03', 4)
    sprite('Action_093_04', 3)
    sprite('Action_093_05', 3)

@State
def EffNmlAtk2BBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_104_00', 2)
    sprite('Action_104_01', 3)
    sprite('Action_104_02', 8)
    sprite('Action_104_03', 1)

@State
def EffNmlAtk2CBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_091_00', 1)
    sprite('Action_091_01', 2)
    sprite('Action_091_02', 2)
    sprite('Action_091_03', 4)
    sprite('Action_091_04', 6)
    sprite('Action_091_05', 1)

@State
def EffNmlAtkAir5ABlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_085_00', 2)
    sprite('Action_085_01', 3)
    sprite('Action_085_02', 8)
    sprite('Action_085_03', 1)

@State
def EffNmlAtkAir5BBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_090_00', 3)
    sprite('Action_090_01', 3)
    sprite('Action_090_02', 3)
    sprite('Action_090_03', 3)
    sprite('Action_090_04', 1)

@State
def EffNmlAtkAir5CBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(-35000)
        Unknown1007(-90000)
    sprite('Action_087_00', 1)
    sprite('Action_087_01', 2)
    sprite('Action_087_02', 2)
    sprite('Action_087_03', 4)
    sprite('Action_087_04', 6)
    sprite('Action_087_05', 1)

@State
def Hyd_244():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_244_00', 1)
    sprite('Action_244_01', 2)
    sprite('Action_244_02', 3)
    sprite('Action_244_03', 3)
    sprite('Action_244_04', 4)
    sprite('Action_244_05', 3)
    sprite('Action_244_06', 1)

@State
def EffNmlReversalAction():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4022(3)
        Unknown4009(3)
        Unknown1007(-20000)
        teleportRelativeX(50000)
    sprite('Action_106_00', 1)
    sprite('Action_106_01', 3)
    sprite('Action_106_02', 2)
    sprite('Action_106_03', 2)
    Unknown4022(0)
    Unknown1084(1)
    sprite('Action_106_04', 3)
    sprite('Action_106_05', 4)
    sprite('Action_106_06', 6)
    sprite('Action_106_07', 1)

@Subroutine
def Hyd_shot_Init():
    Unknown2010()
    AttackLevel_(3)
    AirPushbackY(18000)
    AirUntechableTime(25)
    AirHitstunAnimation(10)
    callSubroutine('InsulatorSpecialInit')
    callSubroutine('Hyd_shot__Delete')

    def upon_44():
        SLOT_4 = 0

    def upon_ON_HIT_OR_BLOCK():
        Unknown2038(1)

    def upon_43():
        if (SLOT_48 == 20):
            enterState('UHY_Request_ShotExplode')

@Subroutine
def Hyd_shot__Delete():
    Unknown4011(3)
    Unknown23089(1, 1, 1, 1, 1, 0, 0, 0)

    def upon_54():
        Unknown1084(1)
        sendToLabel(1)

    def upon_STATE_END():
        pass

    def upon_3():
        if SLOT_38:
            Unknown23045(125)
            if (SLOT_22 < SLOT_0):
                SLOT_4 = 0
                Unknown13(25)
        else:
            Unknown23045(125)
            if (SLOT_22 > SLOT_0):
                SLOT_4 = 0
                Unknown13(25)

@State
def ShotEff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    if random_(2, 0, 33):
        sendToLabel(1)
    elif random_(2, 0, 50):
        sendToLabel(2)
    else:
        sendToLabel(3)
    label(1)
    sprite('Action_072_00', 5)
    physicsXImpulse(-1000)
    Unknown1028(50)
    sprite('Action_072_01', 5)
    ExitState()
    label(2)
    sprite('Action_072_02', 5)
    physicsXImpulse(-700)
    Unknown1028(50)
    sprite('Action_072_03', 5)
    ExitState()
    label(3)
    sprite('Action_072_04', 5)
    physicsXImpulse(-500)
    Unknown1028(50)
    sprite('Action_072_05', 5)
    ExitState()

@State
def ShotA():

    def upon_IMMEDIATE():
        callSubroutine('Hyd_shot_Init')
    sprite('Action_075_00', 3)
    SFX_3('SE_ShotDiscBall')
    SFX_3('SE_ApperLightBlade')
    sprite('Action_075_01', 3)
    sprite('Action_075_02', 2)
    RefreshMultihit()
    physicsXImpulse(32000)
    SLOT_4 = 1
    SFX_0('011_spin_2')
    GFX_0('ShotEff', -1)
    label(0)
    sprite('Action_075_03', 2)
    GFX_0('ShotEff', -1)
    SFX_0('011_spin_2')
    sprite('Action_075_04', 2)
    GFX_0('ShotEff', -1)
    sprite('Action_075_05', 2)
    GFX_0('ShotEff', -1)
    sprite('Action_075_06', 2)
    GFX_0('ShotEff', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    SLOT_4 = 0
    if SLOT_2:
        GFX_0('UHY_Request_ShotHitEffect', 100)
        Unknown38(1, 4)

@State
def ShotAssist():

    def upon_IMMEDIATE():
        callSubroutine('Hyd_shot_Init')
        Unknown11042(1)
    sprite('Action_075_00', 3)
    SFX_3('SE_ShotDiscBall')
    SFX_3('SE_ApperLightBlade')
    sprite('Action_075_01', 3)
    sprite('Action_075_02', 2)
    RefreshMultihit()
    physicsXImpulse(32000)
    SLOT_4 = 1
    SFX_0('011_spin_2')
    GFX_0('ShotEff', -1)
    label(0)
    sprite('Action_075_03', 2)
    GFX_0('ShotEff', -1)
    SFX_0('011_spin_2')
    sprite('Action_075_04', 2)
    GFX_0('ShotEff', -1)
    sprite('Action_075_05', 2)
    GFX_0('ShotEff', -1)
    sprite('Action_075_06', 2)
    GFX_0('ShotEff', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    SLOT_4 = 0
    if SLOT_2:
        GFX_0('UHY_Request_ShotHitEffect', 100)
        Unknown38(1, 4)

@State
def ShotB():

    def upon_IMMEDIATE():
        callSubroutine('Hyd_shot_Init')
    sprite('Action_075_00', 3)
    SFX_3('SE_ShotDiscBall')
    SFX_3('SE_ApperLightBlade')
    sprite('Action_075_01', 3)
    sprite('Action_075_02', 2)
    RefreshMultihit()
    physicsXImpulse(42000)
    SLOT_4 = 1
    SFX_0('011_spin_2')
    GFX_0('ShotEff', -1)
    label(0)
    sprite('Action_075_03', 2)
    GFX_0('ShotExEff', -1)
    SFX_0('011_spin_2')
    sprite('Action_075_04', 2)
    GFX_0('ShotExEff', -1)
    sprite('Action_075_05', 2)
    GFX_0('ShotExEff', -1)
    sprite('Action_075_06', 2)
    GFX_0('ShotExEff', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    SLOT_4 = 0
    if SLOT_2:
        GFX_0('UHY_Request_ShotHitEffect', 100)
        Unknown38(1, 4)

@State
def UHY_Request_ShotExplode():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(800)
        Unknown11092(1)
        AirPushbackX(2500)
        AirPushbackY(27000)
        AirUntechableTime(45)
        Hitstop(2)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown30055(0, 20, 0)
        callSubroutine('InsulatorSpecialInit')
        Unknown11110(74)
        teleportRelativeX(110000)
        SLOT_5 = 1
        Unknown23042()

        def upon_STATE_END():
            SLOT_4 = 0
            SLOT_5 = 0
        Unknown23089(1, 0, 0, 0, 1, 0, 0, 0)

        def upon_54():
            Unknown1084(1)
            sendToLabel(1)
        Unknown1096(1250)
        Unknown2053(1)
    sprite('Action_172_00', 7)
    Unknown1084(1)
    SFX_3('VanishDiscBall')
    sprite('Action_172_01', 6)
    sprite('Action_172_02', 3)
    RefreshMultihit()
    sprite('Action_172_03', 3)
    GFX_0('UHY_Request_ExplodeBlackEffect', 100)
    SFX_3('SE220')
    RefreshMultihit()
    sprite('Action_172_04', 3)
    RefreshMultihit()
    sprite('Action_172_05', 5)
    sprite('Action_172_06', 4)
    sprite('Action_172_07', 5)
    sprite('Action_172_08', 4)
    sprite('Action_172_09', 1)
    label(1)
    sprite('keep', 1)

@State
def UHY_Request_ShotExplodeASS():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(800)
        AttackP1(70)
        Unknown11092(1)
        AirPushbackX(2500)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Hitstop(2)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown30055(0, 20, 0)
        Unknown11042(1)
        callSubroutine('InsulatorSpecialInit')
        teleportRelativeX(110000)
        SLOT_5 = 1
        Unknown23042()

        def upon_STATE_END():
            SLOT_4 = 0
            SLOT_5 = 0
        Unknown23089(3, 1, 1, 1, 1, 0, 3, 3)

        def upon_54():
            Unknown1084(1)
            sendToLabel(1)
        Unknown1096(1250)
        Unknown2053(1)
    sprite('Action_172_00', 7)
    Unknown1084(1)
    SFX_3('VanishDiscBall')
    sprite('Action_172_01', 6)
    sprite('Action_172_02ex01', 3)
    RefreshMultihit()
    sprite('Action_172_03ex01', 3)
    GFX_0('UHY_Request_ExplodeBlackEffect', 100)
    SFX_3('SE220')
    RefreshMultihit()
    sprite('Action_172_04ex01', 3)
    RefreshMultihit()
    sprite('Action_172_05', 5)
    sprite('Action_172_06', 4)
    sprite('Action_172_07', 5)
    sprite('Action_172_08', 4)
    sprite('Action_172_09', 1)
    label(1)
    sprite('keep', 1)

@State
def UHY_Request_ExplodeBladeEffect():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(140000)
        Unknown1007(250000)
    sprite('Action_155_00', 6)
    sprite('Action_155_01', 4)
    sprite('Action_155_02', 3)
    sprite('Action_155_03', 1)

@State
def UHY_Request_ExplodeBlackEffect():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(-80000)
        Unknown1007(30000)
    sprite('Action_157_00', 2)
    sprite('Action_157_01', 2)
    sprite('Action_157_02', 2)
    sprite('Action_157_03', 1)

@State
def UHY_Request_ShotHitEffect():

    def upon_IMMEDIATE():
        teleportRelativeX(110000)

        def upon_43():
            if (SLOT_48 == 20):
                enterState('UHY_Request_ShotExplode')
    sprite('Action_171_00', 4)
    SFX_3('SE_VanishDiscBall')
    sprite('Action_171_01', 5)
    sprite('Action_171_02', 4)
    sprite('Action_171_03', 1)

@State
def EffShotBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(-20000)
    sprite('Action_076_00', 3)
    sprite('Action_076_01', 3)
    sprite('Action_076_02', 3)
    sprite('Action_076_03', 1)

@State
def EffShotSlashBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_083_00', 1)
    sprite('Action_083_01', 2)
    sprite('Action_083_02', 2)
    sprite('Action_083_03', 4)
    sprite('Action_083_04', 6)
    sprite('Action_083_05', 1)

@State
def EffAssult1st():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_110_00', 3)
    GFX_0('Assault1stSubEff', 100)
    sprite('Action_110_01', 3)
    sprite('Action_110_02', 1)

@State
def Assault1stSubEff():

    def upon_IMMEDIATE():
        Unknown23015(11)
    sprite('Action_142_00', 6)
    sprite('Action_142_01', 6)
    sprite('Action_142_02', 6)

@State
def EffAssult2nd():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_111_00', 3)
    GFX_0('Assault2ndSubEff', 100)
    sprite('Action_111_01', 3)
    sprite('Action_111_02', 1)

@State
def Assault2ndSubEff():

    def upon_IMMEDIATE():
        Unknown23015(11)
    sprite('Action_143_00', 6)
    sprite('Action_143_01', 6)
    sprite('Action_143_02', 6)

@State
def EffAssult3rd():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_114_00', 4)
    GFX_0('Assault3rdSubEff', 100)
    sprite('Action_114_01', 4)
    sprite('Action_114_02', 4)
    sprite('Action_114_03', 4)
    sprite('Action_114_04', 1)

@State
def Assault3rdSubEff():

    def upon_IMMEDIATE():
        Unknown23015(11)
    sprite('Action_144_00', 6)
    sprite('Action_144_01', 6)
    sprite('Action_144_02', 6)

@State
def FloatShot_Blade00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_128_00', 3)
    sprite('Action_128_01', 3)
    sprite('Action_128_02', 3)
    sprite('Action_128_03', 1)

@State
def FloatShot_Blade01():

    def upon_IMMEDIATE():
        Unknown1072(87000)
        Unknown1007(150000)
        teleportRelativeX(35000)
        Unknown1096(1250)
    sprite('Action_157_00', 2)
    sprite('Action_157_01', 2)
    sprite('Action_157_02', 2)
    sprite('Action_157_03', 1)

@State
def FloatShot():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        AttackP2(85)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(36000)
        AirUntechableTime(27)
        Hitstop(2)
        Unknown11001(10, 10, 15)
        callSubroutine('InsulatorInit')
        Unknown23182(2)
        Unknown11108(3)
        Unknown1007(-100000)
        if (SLOT_23 <= 50000):
            teleportRelativeY(50000)
        Unknown4011(3)
        Unknown23089(1, 0, 0, 1, 1, 0, 0, 0)

        def upon_54():
            Unknown13(25)
    sprite('Action_236_00', 4)
    sprite('Action_236_01', 4)
    SFX_0('016_explode_0')
    sprite('Action_236_02', 2)
    RefreshMultihit()
    sprite('Action_236_03', 2)
    sprite('Action_236_04', 2)
    sprite('Action_236_05', 4)
    sprite('Action_236_06', 3)
    sprite('Action_236_07', 4)
    sprite('Action_236_08', 3)
    sprite('Action_236_09', 1)

@State
def EffChnageBlade00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_077_00', 2)
    sprite('Action_077_01', 1)

@State
def EffChnageBlade01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_115_00', 3)
    sprite('Action_115_01', 2)
    sprite('Action_115_02', 8)
    sprite('Action_115_03', 1)

@State
def EffChnageBlade02():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        teleportRelativeX(390000)
    sprite('null', 1)
    sprite('Action_119_01', 3)
    sprite('Action_119_02', 3)
    sprite('Action_119_03', 3)
    sprite('Action_119_04', 1)

@State
def EdgeShot():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        AttackP2(70)
        AirUntechableTime(32)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(24000)
        PushbackX(10000)
        Hitstop(4)
        Unknown11001(0, 4, 6)
        callSubroutine('InsulatorInit')
        Unknown2053(1)
        teleportRelativeX(500000)
        ScreenShake(0, 20000)

        def upon_46():
            Unknown2003(1)
        Unknown1096(800)
    sprite('Action_117_00', 4)
    SFX_0('211_down_steal_1')
    sprite('Action_117_01', 5)
    sprite('Action_117_02', 6)
    sprite('Action_117_03', 6)
    sprite('Action_117_04', 9)
    sprite('Action_117_05', 3)
    sprite('Action_117_06', 1)

@State
def EdgeShot_SC_A():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(1000)
        AttackP2(90)
        AirUntechableTime(32)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(20000)
        AirPushbackY(27000)
        PushbackX(10000)
        Hitstop(4)
        Unknown11001(0, 4, 6)
        callSubroutine('InsulatorSpecialInit')
        Unknown2053(1)
        teleportRelativeX(450000)
        ScreenShake(0, 20000)

        def upon_46():
            Unknown2003(1)
        Unknown1096(800)
    sprite('Action_117_00', 4)
    SFX_0('211_down_steal_1')
    sprite('Action_117_01', 5)
    sprite('Action_117_02', 6)
    sprite('Action_117_03', 6)
    sprite('Action_117_04', 9)
    sprite('Action_117_05', 3)
    sprite('Action_117_06', 1)

@State
def EdgeShot_SC_B():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(1300)
        AttackP2(80)
        AirUntechableTime(32)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(20000)
        AirPushbackY(27000)
        PushbackX(10000)
        Hitstop(4)
        Unknown11001(0, 4, 6)
        callSubroutine('InsulatorSpecialInit')
        Unknown2053(1)
        teleportRelativeX(700000)
        ScreenShake(0, 20000)

        def upon_46():
            Unknown2003(1)
        Unknown1096(800)
    sprite('Action_117_00', 4)
    SFX_0('211_down_steal_1')
    sprite('Action_117_01', 5)
    sprite('Action_117_02', 6)
    sprite('Action_117_03', 6)
    sprite('Action_117_04', 9)
    sprite('Action_117_05', 3)
    sprite('Action_117_06', 1)

@State
def EdgeShot_SC_C():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(1000)
        AttackP2(80)
        blockstun(28)
        MinimumDamagePct(10)
        AirUntechableTime(32)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        PushbackX(30000)
        AirPushbackX(9000)
        AirPushbackY(25000)
        Hitstop(4)
        Unknown11001(0, 4, 6)
        callSubroutine('InsulatorSpecialInit')
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown2053(1)
        teleportRelativeX(300000)
        ScreenShake(0, 20000)

        def upon_46():
            Unknown2003(1)
        Unknown1096(800)
    
    
    def upon_7():
        teleportRelativeX(-150000)
    sprite('Action_117_00', 3)
    SFX_0('211_down_steal_1')
    sprite('Action_117_01', 4)
    sprite('Action_117_02', 5)
    sprite('Action_117_03', 5)
    sprite('Action_117_04', 9)
    sprite('Action_117_05', 3)
    sprite('Action_117_06', 1)
    RefreshMultihit()
    teleportRelativeX(150000)
    PushbackX(15000)
    def upon_7():
        teleportRelativeX(-150000)
    sprite('Action_117_00', 3)
    SFX_0('211_down_steal_1')
    sprite('Action_117_01', 4)
    sprite('Action_117_02', 5)
    sprite('Action_117_03', 5)
    sprite('Action_117_04', 9)
    sprite('Action_117_05', 3)
    sprite('Action_117_06', 1)
    RefreshMultihit()
    teleportRelativeX(150000)
    def upon_7():
        teleportRelativeX(-150000)
    sprite('Action_117_00', 3)
    SFX_0('211_down_steal_1')
    sprite('Action_117_01', 4)
    sprite('Action_117_02', 5)
    sprite('Action_117_03', 5)
    sprite('Action_117_04', 9)
    sprite('Action_117_05', 3)
    sprite('Action_117_06', 1)
    
    
@State
def ShotEx():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(750)
        Unknown11092(1)
        Unknown30065(0)
        AirPushbackX(15000)
        AirPushbackY(15000)
        Unknown30055(60000, 50, 0)
        AirUntechableTime(24)
        Hitstop(3)
        Unknown11001(-2, 0, 2)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        callSubroutine('InsulatorSpecialInit')
        MinimumDamagePct(10)
        Unknown11110(78)
        Unknown1096(1200)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
            if (SLOT_2 <= 0):
                Unknown2038(-1)
                GFX_0('UHY_Request_ShotHitEffect', 100)
        Unknown23089(5, 1, 1, 1, 1, 0, 5, 0)

        def upon_54():
            Unknown1084(1)
            sendToLabel(1)
            GFX_0('UHY_Request_ShotHitEffect', 100)

        def upon_3():
            if SLOT_38:
                Unknown23045(140)
                if (SLOT_22 < SLOT_0):
                    SLOT_4 = 0
                    Unknown13(25)
            else:
                Unknown23045(140)
                if (SLOT_22 > SLOT_0):
                    SLOT_4 = 0
                    Unknown13(25)

        def upon_STATE_END():
            SLOT_4 = 0
            SLOT_5 = 0
    sprite('Action_075_00', 3)
    SFX_3('SE_ApperLightBlade')
    sprite('Action_075_01', 3)
    sprite('Action_075_02', 2)
    RefreshMultihit()
    physicsXImpulse(22000)
    GFX_0('ShotExEff', -1)
    label(0)
    sprite('Action_075_03', 2)
    RefreshMultihit()
    GFX_0('ShotExEff', -1)
    SFX_0('011_spin_2')
    sprite('Action_075_04', 2)
    RefreshMultihit()
    GFX_0('ShotExEff', -1)
    sprite('Action_075_05', 2)
    RefreshMultihit()
    GFX_0('ShotExEff', -1)
    sprite('Action_075_06', 2)
    RefreshMultihit()
    GFX_0('ShotExEff', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    sprite('null', 15)

@State
def ShotEx_Assist():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(70)
        Unknown11092(1)
        AirPushbackY(15000)
        Unknown30055(60000, 50, 0)
        AirUntechableTime(40)
        Hitstop(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11042(1)
        callSubroutine('InsulatorSpecialInit')
        Unknown1096(1200)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
            if (SLOT_2 <= 0):
                Unknown2038(-1)
                GFX_0('UHY_Request_ShotHitEffect', 100)
        Unknown23089(3, 1, 1, 1, 1, 0, 3, 0)

        def upon_54():
            Unknown1084(1)
            sendToLabel(1)
            GFX_0('UHY_Request_ShotHitEffect', 100)

        def upon_3():
            if SLOT_38:
                Unknown23045(140)
                if (SLOT_22 < SLOT_0):
                    SLOT_4 = 0
                    Unknown13(25)
            else:
                Unknown23045(140)
                if (SLOT_22 > SLOT_0):
                    SLOT_4 = 0
                    Unknown13(25)

        def upon_STATE_END():
            SLOT_4 = 0
            SLOT_5 = 0
    sprite('Action_075_00', 3)
    SFX_3('SE_ShotDiscBall')
    SFX_3('SE_ApperLightBlade')
    sprite('Action_075_01', 3)
    sprite('Action_075_02', 2)
    RefreshMultihit()
    physicsXImpulse(40000)
    GFX_0('ShotExEff', -1)
    label(0)
    sprite('Action_075_03', 1)
    RefreshMultihit()
    GFX_0('ShotExEff', -1)
    SFX_0('011_spin_2')
    sprite('Action_075_03', 1)
    RefreshMultihit()
    sprite('Action_075_04', 1)
    RefreshMultihit()
    sprite('Action_075_04', 1)
    RefreshMultihit()
    GFX_0('ShotExEff', -1)
    sprite('Action_075_05', 1)
    RefreshMultihit()
    sprite('Action_075_05', 1)
    RefreshMultihit()
    GFX_0('ShotExEff', -1)
    sprite('Action_075_06', 1)
    RefreshMultihit()
    sprite('Action_075_06', 1)
    RefreshMultihit()
    GFX_0('ShotExEff', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    sprite('null', 15)

@State
def ShotExEff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    if random_(2, 0, 33):
        sendToLabel(1)
    elif random_(2, 0, 50):
        sendToLabel(2)
    else:
        sendToLabel(3)
    label(1)
    sprite('Action_073_00', 5)
    physicsXImpulse(-10000)
    Unknown1028(500)
    sprite('Action_073_01', 5)
    ExitState()
    label(2)
    sprite('Action_073_02', 5)
    physicsXImpulse(-7000)
    Unknown1028(500)
    sprite('Action_073_03', 5)
    ExitState()
    label(3)
    sprite('Action_073_04', 5)
    physicsXImpulse(-5000)
    Unknown1028(500)
    sprite('Action_073_05', 5)
    ExitState()

@State
def FloatShotEx():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(400)
        Unknown30065(0)
        Unknown11092(1)
        AttackP1(80)
        AirPushbackX(2000)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(1400)
        AirUntechableTime(24)
        PushbackX(8000)
        Unknown12052(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(4)
        Unknown9016(1)
        Unknown9266(11)
        Unknown1007(-100000)
        if (SLOT_23 <= 50000):
            teleportRelativeY(50000)
        Unknown4011(3)
        Unknown23089(1, 0, 0, 1, 1, 0, 0, 0)

        def upon_54():
            Unknown1084(1)
            Unknown13(25)
    sprite('Action_237_00', 2)
    sprite('Action_237_01', 2)
    sprite('Action_237_02', 2)
    sprite('Action_237_03', 3)
    SFX_0('016_explode_0')
    sprite('Action_237_04', 3)
    sprite('Action_237_05', 4)
    RefreshMultihit()
    sprite('Action_237_06', 4)
    RefreshMultihit()
    sprite('Action_237_07', 4)
    RefreshMultihit()
    sprite('Action_237_05', 4)
    RefreshMultihit()
    sprite('Action_237_06', 4)
    RefreshMultihit()
    sprite('Action_237_08', 4)
    sprite('Action_237_09', 4)
    sprite('Action_237_10', 4)
    sprite('Action_237_11', 4)
    sprite('Action_237_12', 1)

@State
def EffIWBlade00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
    sprite('Action_216_00', 3)
    sprite('Action_216_01', 2)
    sprite('Action_216_02', 1)
    sprite('Action_216_03', 1)

@State
def EffConcentration():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2054(1)
    sprite('Action_201_00', 5)
    sprite('Action_201_01', 2)
    sprite('Action_201_02', 7)
    sprite('Action_201_03', 6)
    sprite('Action_201_04', 5)
    sprite('Action_201_05', 4)
    sprite('Action_201_06', 3)
    sprite('Action_201_07', 3)
    sprite('Action_201_08', 3)
    sprite('Action_201_09', 8)
    sprite('Action_201_10', 1)

@State
def ObjIWMatome():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(790)
        AttackP2(96)
        MinimumDamagePct(17)
        ProjectileDurabilityLvl(3)
        AirUntechableTime(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1500)
        AirPushbackY(37000)
        YImpluseBeforeWallbounce(2500)
        Unknown9310(10)
        PushbackX(4000)
        PushbackX(10000)
        Unknown30055(140000, 100, 0)
        callSubroutine('InsulatorSpecialInit')
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23078(1)

        def upon_43():
            if (SLOT_48 == 5000):
                Damage(140)
                AttackP1(100)
                AttackP2(100)
                MinimumDamagePct(100)
    sprite('Action_208_00', 4)
    SystemGFX('effect_297', 65535)
    SystemGFX('effect_298', 65535)
    GFX_0('ObjIW_Thunder', 100)
    ScreenShake(10000, 20000)
    SFX_3('SE_220')
    sprite('Action_208_01', 3)
    ScreenShake(5000, 5000)
    Hitstop(2)
    Unknown11001(2, 2, 2)
    GFX_0('ObjIW_EffFront', 100)
    GFX_0('ObjIW_EffBack', 100)
    sprite('Action_208_01', 3)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    SFX_3('SE_221')
    sprite('Action_208_01', 3)
    GFX_0('ObjIW_EffStorm', 100)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    SFX_3('SE015_BoundWall')
    GFX_0('IWA', -1)
    GFX_0('IWA', -1)
    GFX_0('IWA', -1)
    GFX_0('IWA', -1)
    sprite('Action_208_01', 3)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    sprite('Action_208_01', 3)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    sprite('Action_208_02', 2)
    sprite('Action_208_03', 3)
    ScreenShake(5000, 5000)
    Hitstop(0)
    Unknown11001(0, 0, 0)
    Unknown30055(0, 0, 0)
    RefreshMultihit()
    sprite('Action_208_03', 2)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(0)
    Unknown26('IWA')
    sprite('Action_208_03', 2)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(2)
    sprite('Action_208_03', 2)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(0)
    sprite('Action_208_03', 2)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(2)
    sprite('Action_208_04', 2)
    sprite('Action_208_05', 2)
    sprite('Action_208_06', 2)
    sprite('Action_208_07', 2)

@State
def ObjIW_Thunder():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_205_00', 2)
    sprite('Action_205_01', 2)
    sprite('Action_205_02', 1)

@State
def ObjIW_EffFront():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_206_00', 3)
    sprite('Action_206_01', 3)
    sprite('Action_206_02', 3)
    sprite('Action_206_03', 3)
    sprite('Action_206_04', 3)
    sprite('Action_206_05', 3)
    sprite('Action_206_06', 3)
    sprite('Action_206_07', 3)
    sprite('Action_206_08', 3)
    sprite('Action_206_09', 3)
    sprite('Action_206_10', 3)
    sprite('Action_206_11', 1)

@State
def ObjIW_EffBack():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_207_00', 3)
    sprite('Action_207_01', 3)
    sprite('Action_207_02', 3)
    sprite('Action_207_03', 4)
    sprite('Action_207_04', 5)
    sprite('Action_207_05', 6)
    sprite('Action_207_06', 3)
    sprite('Action_207_07', 3)
    sprite('Action_207_08', 3)
    sprite('Action_207_09', 1)

@State
def ObjIW_EffStorm():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_204_00', 3)
    sprite('Action_204_01', 4)
    sprite('Action_204_02', 4)
    sprite('Action_204_03', 4)
    sprite('Action_204_04', 4)
    sprite('Action_204_05', 4)
    sprite('Action_204_06', 4)
    sprite('Action_204_07', 4)
    sprite('Action_204_08', 1)

@State
def IWEndEff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(-150000)
        Unknown1007(250000)
    sprite('Action_217_00', 4)
    sprite('Action_217_01', 3)

@State
def IWA():

    def upon_IMMEDIATE():
        Unknown61(0, 1, 0, 3, 0, 9999, 0, 9999, 0, 9999, 0, 9999)
        SLOT_2 = SLOT_0
        Unknown4011(3)
    label(0)
    sprite('null', 1)
    Unknown2038(-1)
    if SLOT_2:
        sendToLabel(0)
    else:
        sendToLabel(1)
    label(1)
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()
    sprite('null', 6)
    SystemGFX('effect_284', 65535)
    Unknown36(1)
    Unknown1025(-10000, 10000)
    Unknown1026(20000, 40000)
    Unknown1041(-1000, -3000)
    Unknown1099(40)
    Unknown1010(-300000, 300000)
    Unknown35()

@State
def ObjIWMatomeOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(510)
        AttackP2(98)
        MinimumDamagePct(15)
        ProjectileDurabilityLvl(3)
        AirUntechableTime(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(37000)
        YImpluseBeforeWallbounce(2500)
        Unknown9310(10)
        PushbackX(4000)
        PushbackX(10000)
        Unknown30055(140000, 100, 0)
        callSubroutine('InsulatorSpecialInit')
        Unknown11110(66)
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23078(1)
        Unknown1096(1250)

        def upon_43():
            if (SLOT_48 == 5000):
                Damage(90)
                AttackP1(100)
                AttackP2(100)
                MinimumDamagePct(100)
    sprite('Action_208_00', 4)
    SystemGFX('effect_297', 65535)
    SystemGFX('effect_298', 65535)
    GFX_0('ObjIW_ThunderOD', 100)
    ScreenShake(10000, 20000)
    SFX_3('SE_220')
    sprite('Action_208_01', 3)
    ScreenShake(5000, 5000)
    Hitstop(2)
    Unknown11001(2, 2, 2)
    GFX_0('ObjIW_EffFrontOD', 100)
    GFX_0('ObjIW_EffBackOD', 100)
    SFX_3('SE_221')
    sprite('Action_208_01', 3)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    SFX_3('SE015_BoundWall')
    GFX_0('IWA', -1)
    GFX_0('IWA', -1)
    GFX_0('IWA', -1)
    GFX_0('IWA', -1)
    sprite('Action_208_01', 3)
    GFX_0('ObjIW_EffStormOD', 100)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    sprite('Action_208_01', 3)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    sprite('Action_208_01', 3)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    sprite('Action_208_02', 2)
    sprite('Action_208_03', 3)
    ScreenShake(5000, 5000)
    Hitstop(0)
    Unknown11001(0, 0, 0)
    Unknown30055(0, 0, 0)
    RefreshMultihit()
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(0)
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(2)
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(0)
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(2)
    sprite('Action_208_03', 3)
    GFX_0('ObjIW_EffStormOD', 100)
    ScreenShake(5000, 5000)
    Hitstop(0)
    Unknown11001(0, 0, 0)
    Unknown30055(0, 0, 0)
    RefreshMultihit()
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(0)
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(2)
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(0)
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(2)
    sprite('Action_208_03', 3)
    ScreenShake(5000, 5000)
    Hitstop(0)
    Unknown11001(0, 0, 0)
    Unknown30055(0, 0, 0)
    RefreshMultihit()
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(0)
    Unknown26('IWA')
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(2)
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(0)
    sprite('Action_208_03', 1)
    ScreenShake(5000, 5000)
    RefreshMultihit()
    Hitstop(2)
    sprite('Action_208_04', 2)
    sprite('Action_208_05', 2)
    sprite('Action_208_06', 2)
    sprite('Action_208_07', 2)

@State
def ObjIW_ThunderOD():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown1096(1250)
    sprite('Action_205_00', 2)
    sprite('Action_205_01', 2)
    sprite('Action_205_02', 1)

@State
def ObjIW_EffFrontOD():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown1096(1250)
    sprite('Action_206_00', 3)
    sprite('Action_206_01', 3)
    sprite('Action_206_02', 3)
    sprite('Action_206_03', 3)
    sprite('Action_206_04', 3)
    sprite('Action_206_05', 3)
    sprite('Action_206_06', 3)
    sprite('Action_206_07', 3)
    sprite('Action_206_02', 3)
    sprite('Action_206_03', 3)
    sprite('Action_206_04', 3)
    sprite('Action_206_05', 3)
    sprite('Action_206_06', 3)
    sprite('Action_206_07', 3)
    sprite('Action_206_08', 3)
    sprite('Action_206_09', 3)
    sprite('Action_206_10', 3)
    sprite('Action_206_11', 1)

@State
def ObjIW_EffBackOD():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1096(1250)
    sprite('Action_207_00', 3)
    sprite('Action_207_01', 3)
    sprite('Action_207_02', 3)
    sprite('Action_207_03', 4)
    sprite('Action_207_04', 5)
    sprite('Action_207_05', 6)
    sprite('Action_207_06', 3)
    sprite('Action_207_07', 3)
    sprite('Action_207_08', 3)
    sprite('Action_207_09', 1)

@State
def ObjIW_EffStormOD():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1096(1250)
    sprite('Action_204_00', 3)
    sprite('Action_204_01', 4)
    sprite('Action_204_02', 4)
    sprite('Action_204_03', 4)
    sprite('Action_204_04', 4)
    sprite('Action_204_05', 4)
    sprite('Action_204_06', 4)
    sprite('Action_204_07', 4)
    sprite('Action_204_08', 1)

@State
def IWEndEffOD():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(-150000)
        Unknown1007(250000)
        Unknown1096(1250)
    sprite('Action_217_00', 4)
    sprite('Action_217_01', 3)

@State
def EffTagAssistBlade00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(246000)
        Unknown1007(132000)
    sprite('Action_120_00', 10)
    sprite('Action_120_01', 4)
    sprite('Action_120_02', 4)
    sprite('Action_120_03', 4)
    sprite('Action_120_04', 1)

@State
def EffTagAssistBlade01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4009(3)
        teleportRelativeX(160000)
        teleportRelativeY(0)
    sprite('Action_125_00', 4)
    sprite('Action_125_01', 5)
    sprite('Action_125_02', 5)
    sprite('Action_125_03', 5)
    sprite('Action_125_04', 6)
    sprite('Action_125_05', 6)
    sprite('Action_125_06', 1)

@State
def EffTagAssistBlade02():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4009(3)
        teleportRelativeY(0)
        Unknown1064(1800)
    sprite('Action_125_00', 4)
    sprite('Action_125_01', 15)
    sprite('Action_125_02', 5)
    sprite('Action_125_03', 5)
    sprite('Action_125_04', 6)
    sprite('Action_125_05', 6)
    sprite('Action_125_06', 1)

@State
def Astral_Camera():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20004(1)
    sprite('null', 32767)
    teleportRelativeX(-70000)
    Unknown1007(70000)
    label(0)
    sprite('null', 32767)

    def upon_3():
        if (SLOT_105 >= 900):
            SLOT_105 = (SLOT_105 + (-2))
        else:
            SLOT_105 = 900
            clearUponHandler(3)
    label(1)
    sprite('null', 30)
    SLOT_12 = (SLOT_12 + SLOT_19)
    SLOT_13 = (SLOT_13 + SLOT_20)
    Unknown1019(2)
    YAccel(10)
    sprite('null', 60)
    Unknown1019(50)
    YAccel(50)
    sprite('null', 32767)
    Unknown1084(1)

@State
def Hyd_360():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(-30000)
        Unknown1007(250000)
    sprite('Action_360_00', 3)
    sprite('Action_360_01', 3)
    sprite('Action_360_02', 3)
    sprite('Action_360_03', 3)
    sprite('Action_360_04', 3)
    sprite('Action_360_05', 1)

@State
def Hyd_361():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(800000)
        Unknown1007(250000)
    sprite('null', 6)
    sprite('Action_361_00', 3)
    sprite('Action_361_01', 3)
    sprite('Action_361_02', 3)
    sprite('Action_361_03', 3)
    sprite('Action_361_04', 3)
    sprite('Action_361_05', 3)
    sprite('Action_361_06', 3)
    sprite('Action_361_07', 1)

@State
def Hyd_362():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
    sprite('Action_362_00', 5)
    sprite('Action_362_01', 30)
    sprite('Action_362_02', 5)
    sprite('Action_362_03', 3)
    GFX_0('Hyd_363', 100)
    sprite('Action_362_04', 3)
    sprite('Action_362_05', 3)
    sprite('Action_362_06', 3)
    sprite('Action_362_07', 3)
    sprite('Action_362_08', 3)
    label(0)
    sprite('Action_362_09', 3)
    sprite('Action_362_10', 3)
    sprite('Action_362_11', 3)
    sprite('Action_362_12', 3)
    sprite('Action_362_13', 3)
    sprite('Action_362_14', 3)
    loopRest()
    gotoLabel(0)

@State
def Hyd_363():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
    sprite('Action_363_00', 3)
    sprite('Action_363_01', 3)
    sprite('Action_363_02', 3)
    sprite('Action_363_03', 3)
    label(0)
    sprite('Action_363_04', 3)
    sprite('Action_363_05', 3)
    sprite('Action_363_06', 3)
    sprite('Action_363_07', 3)
    sprite('Action_363_08', 3)
    sprite('Action_363_09', 3)
    sprite('Action_363_10', 3)
    sprite('Action_363_11', 3)
    sprite('Action_363_12', 3)
    sprite('Action_363_13', 3)
    sprite('Action_363_14', 3)
    loopRest()
    gotoLabel(0)
    sprite('Action_363_15', 3)
    sprite('Action_363_16', 3)
    sprite('Action_363_17', 1)

@State
def Hyd_999():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(5)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('hyd999_01', 3)
    sprite('hyd999_02', 3)
    sprite('hyd999_03', 3)
    sprite('hyd999_04', 3)
    sprite('hyd999_05', 3)
    sprite('hyd999_06', 3)
    sprite('hyd999_07', 3)
    sprite('hyd999_08', 3)
    sprite('hyd999_09', 3)
    sprite('hyd999_10', 4)
    sprite('hyd999_11', 4)
    sprite('hyd999_12', 5)
    sprite('hyd999_13', 5)
    sprite('hyd999_14', 3)
    sprite('hyd999_15', 3)
    sprite('hyd999_16', 3)
    sprite('hyd999_17', 2)
    sprite('hyd999_18', 10)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)

@State
def EffEntryBlade01():
    sprite('Action_101_00', 3)
    sprite('Action_101_01', 3)
    sprite('Action_101_02', 3)
    sprite('Action_101_03', 1)

@State
def EffEntryBlade_Summon1():

    def upon_IMMEDIATE():
        teleportRelativeX(5000)
        Unknown1007(-5000)
        loopRelated(17, 300)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('Action_123_00', 3)
    sprite('Action_123_01', 3)
    sprite('Action_123_02', 3)
    sprite('Action_123_03', 3)
    sprite('Action_123_04', 3)
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def EffEntryBlade_Summon2():

    def upon_IMMEDIATE():
        teleportRelativeX(14000)
        loopRelated(17, 300)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('Action_123_06', 3)
    sprite('Action_123_07', 3)
    sprite('Action_123_08', 3)
    sprite('Action_123_09', 3)
    sprite('Action_123_10', 3)
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def EffEntryBlade_Summon3():

    def upon_IMMEDIATE():
        teleportRelativeX(18000)
        Unknown1007(-5000)
        loopRelated(17, 300)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('Action_123_12', 3)
    sprite('Action_123_13', 3)
    sprite('Action_123_14', 3)
    sprite('Action_123_15', 3)
    sprite('Action_123_16', 3)
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def EffEntryBlade_Summon4():

    def upon_IMMEDIATE():
        teleportRelativeX(18000)
        Unknown1007(-5000)
        loopRelated(17, 300)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('Action_123_18', 3)
    sprite('Action_123_19', 3)
    sprite('Action_123_20', 3)
    sprite('Action_123_21', 3)
    sprite('Action_123_22', 3)
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def EffEntryBlade_Summon5():

    def upon_IMMEDIATE():
        teleportRelativeX(15000)
    sprite('Action_123_32', 3)
    sprite('Action_123_33', 3)
    sprite('Action_123_34', 3)
    sprite('Action_123_37', 3)
    teleportRelativeX(5000)
    Unknown1007(-3000)
    sprite('Action_123_38', 3)
    sprite('Action_123_39', 3)
    sprite('Action_123_40', 1)

@State
def EffWinBlade01():
    sprite('Action_102_00', 3)
    sprite('Action_102_01', 3)
    sprite('Action_102_02', 1)

@State
def DDD_Particle():

    def upon_IMMEDIATE():
        teleportRelativeY(0)
    sprite('null', 5)
    Unknown4047(251, 251, 251)
    Unknown4045('uhyef_DDD_dust', -1)
