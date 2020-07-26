@State
def EffNmlAtk5ABlade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_201_00', 2)
    sprite('Action_201_01', 2)
    sprite('Action_201_02', 2)
    sprite('Action_201_03', 1)

@State
def EffNmlAtk5BBlade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_202_00', 2)
    sprite('Action_202_01', 2)
    sprite('Action_202_02', 2)
    sprite('Action_202_03', 1)

@State
def EffNmlAtk3BBlade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_205_00', 2)
    sprite('Action_205_01', 2)
    sprite('Action_205_02', 2)
    sprite('Action_205_03', 1)

@State
def EffNmlAtk5CZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(1)
    sprite('Action_222_00', 3)
    sprite('Action_222_01', 3)
    sprite('Action_222_02', 3)
    sprite('Action_222_03', 1)

@State
def EffNmlAtk2BBlade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_204_00', 2)
    sprite('Action_204_01', 2)
    sprite('Action_204_02', 1)

@State
def EffNmlAtk6BZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(1)
    sprite('Action_223_00', 3)
    sprite('Action_223_01', 3)
    sprite('Action_223_02', 1)

@State
def EffNmlAtk4CZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_221_00', 3)
    sprite('Action_221_01', 3)
    sprite('Action_221_02', 3)

@State
def EffNmlAtk3CZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_224_00', 3)
    sprite('Action_224_01', 3)
    sprite('Action_224_02', 1)

@State
def Eff66BZanzo1():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_422_00', 3)
    sprite('Action_422_01', 3)
    sprite('Action_422_02', 1)

@State
def Eff66CBlade1():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_422_00', 3)
    sprite('Action_422_01', 3)
    sprite('Action_422_02', 1)

@State
def Eff66CBlade2():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_423_00', 3)
    sprite('Action_423_01', 3)
    sprite('Action_423_02', 1)

@State
def Eff66CBlade3():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_424_00', 3)
    sprite('Action_424_01', 3)
    sprite('Action_424_02', 1)

@State
def Eff66CBlade4():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_425_00', 3)
    sprite('Action_425_01', 3)
    sprite('Action_425_02', 1)

@State
def Eff66CBlade5():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_426_00', 3)
    sprite('Action_426_01', 3)
    sprite('Action_426_02', 1)

@State
def EffNmlAtkAIR5ABlade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_207_00', 2)
    sprite('Action_207_01', 2)
    sprite('Action_207_02', 1)

@State
def EffNmlAtkAIR5BZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_221_00', 3)
    sprite('Action_221_01', 3)
    sprite('Action_221_02', 3)

@State
def EffNmlAtkAIR5CBlade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown1007(-10000)
    sprite('Action_209_00', 2)
    sprite('Action_209_01', 2)
    sprite('Action_209_02', 2)
    sprite('Action_209_03', 1)

@State
def EffNmlAtkAIR2CZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_226_00', 3)
    sprite('Action_226_01', 3)
    sprite('Action_226_02', 3)

@State
def EffFF():
    sprite('Action_165_00', 7)
    sprite('Action_165_01', 7)
    sprite('Action_165_02', 1)

@State
def InvincibleAttackBlade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_211_00', 6)
    sprite('Action_211_01', 6)
    sprite('Action_211_02', 6)
    sprite('Action_211_03', 8)
    sprite('Action_211_04', 1)

@State
def Assault_Zanzo():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3026(-3618616)
        Unknown2019(1)
    sprite('Action_189_00', 14)
    Unknown3004(-18)
    sprite('Action_189_01', 2)

@State
def Assault_Blade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_210_00', 2)
    sprite('Action_210_01', 2)
    sprite('Action_210_02', 2)
    sprite('Action_210_03', 2)
    sprite('Action_210_04', 2)
    sprite('Action_210_05', 1)

@State
def Assault_AddAtkIC():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(200)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11084(1)
        AttackP2(100)
        PushbackX(0)
        AirPushbackX(8000)
        AirPushbackY(35000)
        AirUntechableTime(60)
        blockstun(25)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11057(700)
        Hitstop(3)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108(3)
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    Unknown9215()
    Hitstop(8)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    
@State
def Assault_AddAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(220)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11084(1)
        AttackP2(100)
        PushbackX(0)
        AirPushbackX(8000)
        AirPushbackY(35000)
        AirUntechableTime(60)
        blockstun(18)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11057(700)
        Hitstop(3)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108(3)
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    sprite('Action_100_atkcol', 4)
    Unknown23151(22, 105)
    RefreshMultihit()
    Unknown9215()
    Hitstop(8)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)

@State
def UltimateAssault_Blade():

    def upon_IMMEDIATE():
        Unknown4010(3)
    sprite('Action_219_00', 3)
    sprite('Action_219_01', 3)
    sprite('Action_219_02', 3)
    sprite('Action_219_03', 3)
    sprite('Action_219_04', 1)

@State
def UltimateShot_ODBlade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown1072(90000)
        Unknown1007(430000)
        teleportRelativeX(-150000)
        Unknown1056(4200)
        Unknown1064(1500)
    sprite('Action_219_00', 18)
    sprite('Action_219_01', 6)
    sprite('Action_219_02', 6)
    sprite('Action_219_03', 3)
    sprite('Action_219_04', 1)

@Subroutine
def Tan_Init():
    Unknown23028(1, 1)
    Unknown2010()
    Unknown4009(3)
    Unknown23013(1)
    Unknown9266(13)
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(0)
    Unknown30041('')
    EnableCollision(0)
    Unknown2053(1)
    teleportRelativeX(1000)
    AttackAttributes(0, 1, 0, 0, 0)
    SLOT_4 = 1

    def upon_44():
        enterState('Tan_Damage')

    def upon_43():
        if (SLOT_48 == 0):
            Unknown4009(0)
            enterState('Tan_Delete')

    def upon_STATE_END():
        Unknown21012('Sealing_Tan_AtkCol', 32)
        Unknown21012('Sealing_Tan_AtkEff', 32)
        Unknown21012('Sealing_Tan_UzuEff', 32)
        Unknown21012('Sealing_Tan_AtkColEX', 32)
        Unknown21012('Sealing_Tan_AtkEffEX', 32)
        Unknown21012('Sealing_Tan_UzuEffEX', 32)
        Unknown21012('Sealing_Tan_AtkColTAG', 32)
        Unknown21012('Sealing_Tan_AtkEffTAG', 32)
        Unknown21012('Sealing_Tan_UzuEffTAG', 32)

@Subroutine
def Tan_Hasei_Init():
    Unknown23028(1, 1)
    Unknown2010()
    Unknown4009(3)
    Unknown23013(1)
    Unknown2053(1)
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown9266(13)
    Unknown23023()
    AttackAttributes(0, 1, 0, 0, 0)
    SLOT_4 = 1

    def upon_44():
        enterState('Tan_Damage')

    def upon_43():
        if (SLOT_48 == 0):
            Unknown4009(0)
            enterState('Tan_Delete')

@Subroutine
def Tan_ForceWarp():
    Unknown23029(11, 0, 0)
    Unknown38(11, 25)

@State
def Tan_Delete():

    def upon_IMMEDIATE():
        Unknown4009(0)
        Unknown2054(1)
        Unknown2019(500)

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('keep', 10)
    Unknown1084(1)
    GFX_0('Tan_SummonOut', 100)
    Unknown23119(16763080, 2, 2)
    SFX_3('SE_HolyVoiceShort')
    sprite('keep', 10)
    Unknown1059(-100)
    Unknown1067(25)
    Unknown3004(-25)
    sprite('keep', 2)
    Unknown3001(0)
    Unknown3038(1)

@State
def Tan_Damage():

    def upon_IMMEDIATE():
        Unknown4009(0)
        Unknown2054(1)
        Unknown38(10, 25)
        Unknown2019(500)

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('Action_158_00', 1)
    Unknown1084(1)
    GFX_0('Tan_SummonOut', 100)
    SFX_3('SE_HolyVoiceShort')
    sprite('Action_158_01', 1)
    teleportRelativeX(-2000)
    sprite('Action_158_02', 1)
    sprite('Action_158_01', 1)
    teleportRelativeX(-2000)
    sprite('Action_158_02', 1)
    teleportRelativeX(2000)
    sprite('Action_158_01', 1)
    sprite('Action_158_02', 1)
    teleportRelativeX(-2000)
    sprite('Action_158_01', 1)
    sprite('Action_158_02', 1)
    teleportRelativeX(2000)
    sprite('Action_158_01', 1)
    sprite('Action_158_02', 1)
    teleportRelativeX(-2000)
    sprite('Action_158_01', 1)
    sprite('Action_158_02', 1)
    teleportRelativeX(2000)
    sprite('Action_158_03', 5)
    physicsXImpulse(-5120)
    Unknown1028(250)
    Unknown3004(-17)
    sprite('Action_158_04', 5)
    sprite('Action_158_05', 5)
    sprite('Action_158_06', 1)

@State
def Tan_214A():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Init')
        AttackP1(80)
        AirPushbackY(18000)
        AirUntechableTime(30)
        AttackLevel_(4)
        Unknown9016(1)
        HitLow(2)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown3001(0)
        teleportRelativeX(150000)
        Unknown23078(1)
        AttackAttributes(0, 0, 1, 0, 0)

        def upon_32():
            enterState('Tan_214Add_A')

        def upon_33():
            enterState('Tan_214Add_B')
    sprite('Action_089_00', 1)
    Unknown3004(64)
    sprite('Action_089_01', 1)
    sprite('Action_089_02', 1)
    sprite('Action_089_03', 1)
    sprite('Action_089_04', 2)
    sprite('Action_089_05', 2)
    GFX_0('214A_Tan_Blade', 100)
    SFX_3('SE043')
    sprite('Action_089_06', 5)
    RefreshMultihit()
    sprite('Action_089_07', 6)
    sprite('Action_089_08', 6)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_214B():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Init')
        AttackLevel_(4)
        Damage(2000)
        hitstun(23)
        AirUntechableTime(40)
        Unknown11001(0, -3, -3)
        AirPushbackX(6000)
        AirPushbackY(-70000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(20)
        Unknown9016(1)
        Unknown9312(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown3001(0)
        teleportRelativeX(50000)
        Unknown23078(1)
        Unknown2019(1)

        def upon_32():
            clearUponHandler(32)
            enterState('Tan_214Add_A')

        def upon_33():
            clearUponHandler(33)
            enterState('Tan_214Add_B')
    sprite('Action_090_00', 1)
    Unknown3004(64)
    sprite('Action_090_01', 3)
    sprite('Action_090_02', 5)
    sprite('Action_090_03', 2)
    sprite('Action_090_04', 2)
    teleportRelativeX(100000)
    sprite('Action_090_05', 3)
    GFX_0('214B_Tan_Blade', 100)
    SFX_3('SE043')
    ScreenShake(2000, 8000)
    sprite('Action_090_06', 4)
    sprite('Action_090_07', 4)
    sprite('Action_090_06', 4)
    sprite('Action_090_07', 4)
    sprite('Action_090_08', 3)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_214Add_A():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Hasei_Init')
        Unknown4009(0)
        AttackLevel_(4)
        Damage(1200)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(3)
        AirUntechableTime(45)
        AirPushbackX(4200)
        AirPushbackY(10000)
        PushbackX(19800)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown23078(1)
    sprite('Action_092_00', 2)
    sprite('Action_092_01', 3)
    sprite('Action_092_02', 4)
    sprite('Action_092_03', 3)
    sprite('Action_092_04', 3)
    RefreshMultihit()
    GFX_0('214AddA_Tan_Blade1', 100)
    SFX_3('SE043')
    sprite('Action_092_05', 4)
    sprite('Action_092_06', 3)
    physicsXImpulse(20000)
    Unknown1028(-2000)
    sprite('Action_092_07', 2)
    RefreshMultihit()
    GFX_0('214AddA_Tan_Blade2', 100)
    SFX_3('SE043')
    AirPushbackX(24000)
    AirPushbackY(22000)
    Unknown1084(1)
    sprite('Action_092_08', 2)
    sprite('Action_092_09', 15)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_214Add_B():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Hasei_Init')
        AttackLevel_(4)
        Damage(2500)
        AttackP1(80)
        AirPushbackX(6000)
        AirPushbackY(32500)
        YImpluseBeforeWallbounce(2200)
        AirUntechableTime(60)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown23078(1)
    sprite('Action_093_00', 3)
    sprite('Action_093_01', 3)
    physicsXImpulse(8000)
    Unknown1028(-450)
    sprite('Action_093_02', 2)
    sprite('Action_093_03', 1)
    teleportRelativeX(60000)
    sprite('Action_093_03', 2)
    teleportRelativeX(50000)
    sprite('Action_093_04', 3)
    sprite('Action_093_05', 2)
    RefreshMultihit()
    GFX_0('214AddB_Tan_Blade', 100)
    SFX_3('SE043')
    Unknown1084(1)
    sprite('Action_093_06', 2)
    teleportRelativeX(20000)
    sprite('Action_093_07', 3)
    sprite('Action_093_08', 6)
    teleportRelativeX(5000)
    sprite('Action_093_09', 7)
    sprite('keep', 2)
    enterState('Tan_Delete')
    
@State
def Tan_214Add_BTAG():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Hasei_Init')
        AttackLevel_(5)
        Damage(2000)
        AttackP1(70)
        AirPushbackX(6000)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(2200)
        AirUntechableTime(60)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown23078(1)
        Unknown11042(1)
    sprite('Action_093_00', 5)
    sprite('Action_093_01', 4)
    physicsXImpulse(8000)
    Unknown1028(-450)
    sprite('Action_093_02', 2)
    sprite('Action_093_03', 1)
    teleportRelativeX(60000)
    sprite('Action_093_03', 2)
    teleportRelativeX(50000)
    sprite('Action_093_04', 3)
    sprite('Action_093_05', 2)
    RefreshMultihit()
    GFX_0('214AddB_Tan_Blade', 100)
    SFX_3('SE043')
    Unknown1084(1)
    sprite('Action_093_06', 2)
    teleportRelativeX(20000)
    sprite('Action_093_07', 3)
    sprite('Action_093_08', 6)
    teleportRelativeX(5000)
    sprite('Action_093_09', 7)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_Air214A_Air5B():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Init')
        Unknown4007(3)
        AttackLevel_(3)
        AirUntechableTime(35)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown3001(128)
        teleportRelativeX(150000)
    sprite('Action_083_00', 1)
    Unknown3004(128)
    sprite('Action_083_01', 1)
    sprite('Action_083_02', 1)
    sprite('Action_083_03', 1)
    sprite('Action_083_04', 1)
    sprite('Action_083_05', 1)
    sprite('Action_083_06', 4)
    RefreshMultihit()
    GFX_0('214A_Tan_Blade', 100)
    SFX_3('SE043')
    sprite('Action_083_07', 8)
    Unknown4007(0)
    sprite('Action_083_08', 9)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_Air214A():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Init')
        AttackLevel_(4)
        AttackP1(80)
        AirUntechableTime(30)
        AirPushbackX(12000)
        AirPushbackY(25000)
        Unknown9016(1)
        Unknown9312(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown3001(128)
        teleportRelativeX(150000)
        AttackAttributes(1, 0, 0, 0, 0)
    sprite('Action_083_00', 1)
    Unknown3004(128)
    sprite('Action_083_01', 1)
    sprite('Action_083_02', 1)
    sprite('Action_083_03', 1)
    sprite('Action_083_04', 2)
    sprite('Action_083_05', 2)
    sprite('Action_083_06', 4)
    RefreshMultihit()
    GFX_0('214A_Tan_Blade', 100)
    SFX_3('SE043')
    sprite('Action_083_07', 8)
    sprite('Action_083_08', 9)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_Air214B():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4009(0)
        callSubroutine('Tan_Init')
        AttackLevel_(4)
        Damage(2000)
        AirPushbackX(5500)
        AirPushbackY(-55000)
        AttackP1(80)
        AirUntechableTime(75)
        Unknown9016(1)
        Unknown9190(1)
        Unknown9118(70)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown3001(128)
        teleportRelativeX(150000)
        AttackAttributes(1, 0, 0, 0, 0)
    sprite('Action_084_00', 3)
    Unknown3004(128)
    physicsXImpulse(25000)
    physicsYImpulse(30000)
    setGravity(3750)
    sprite('Action_084_01', 4)
    sprite('Action_084_02', 4)
    sprite('Action_084_03', 3)
    sprite('Action_084_04', 2)
    GFX_0('Air214B_Tan_Blade', 100)
    sprite('Action_084_05', 5)
    Unknown1084(1)
    RefreshMultihit()
    SFX_3('SE043')
    sprite('Action_084_06', 8)
    sprite('Action_084_07', 9)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_214EX():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Init')
        Unknown4009(0)
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackX(26000)
        AirPushbackY(27000)
        AirUntechableTime(60)
        MinimumDamagePct(10)
        blockstun(26)
        Unknown30065(0)
        Hitstop(3)
        Unknown11001(-2, -2, -2)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown3001(0)
        teleportRelativeX(5000)
        teleportRelativeY(0)
        Unknown30040(1)
        Unknown30040(2)
        Unknown2015(55)
        Unknown2016(250)
    sprite('Action_085_01', 4)
    Unknown3004(60)
    sprite('Action_085_01', 3)
    Unknown3001(255)
    sprite('Action_085_02', 4)
    sprite('Action_085_03', 2)
    RefreshMultihit()
    physicsXImpulse(30000)
    Unknown1028(-1500)
    sprite('Action_085_03', 1)
    EnableCollision(1)
    sprite('Action_085_04', 3)
    teleportRelativeX(100000)
    sprite('Action_085_05', 3)
    RefreshMultihit()
    physicsXImpulse(5120)
    Unknown1028(-640)
    physicsYImpulse(40000)
    setGravity(4000)
    sprite('Action_085_06', 2)
    sprite('Action_085_07', 3)
    RefreshMultihit()
    AirPushbackX(6500)
    Damage(2000)
    GFX_0('214EX_Tan_Blade', 100)
    SFX_3('SE043')
    sprite('Action_085_08', 6)
    Unknown1084(1)
    physicsYImpulse(1280)
    sprite('Action_085_09', 6)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_214AirEX():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Init')
        Unknown4009(0)
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackX(4500)
        AirPushbackY(32000)
        AirUntechableTime(60)
        blockstun(26)
        MinimumDamagePct(10)
        Unknown30065(0)
        Hitstop(3)
        Unknown11001(-1, -1, -1)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown3001(0)
        Unknown1007(-600000)
        teleportRelativeX(5000)
        Unknown2015(55)
        Unknown2016(250)
    sprite('Action_085_01', 4)
    Unknown3004(50)
    sprite('Action_085_01', 3)
    Unknown3001(255)
    sprite('Action_085_02', 4)
    sprite('Action_085_03', 2)
    RefreshMultihit()
    physicsXImpulse(30000)
    Unknown1028(-1500)
    sprite('Action_085_03', 1)
    sprite('Action_085_04', 3)
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)
    teleportRelativeX(100000)
    sprite('Action_085_05', 3)
    RefreshMultihit()
    physicsXImpulse(5120)
    Unknown1028(-640)
    physicsYImpulse(40000)
    setGravity(4000)
    sprite('Action_085_06', 2)
    sprite('Action_085_07', 3)
    RefreshMultihit()
    Damage(2000)
    GFX_0('214EX_Tan_Blade', 100)
    SFX_3('SE043')
    sprite('Action_085_08', 6)
    Unknown1084(1)
    physicsYImpulse(1280)
    sprite('Action_085_09', 6)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_Sealing():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Init')
        Unknown4009(0)
        AttackLevel_(3)
        Unknown9016(1)
        Unknown11057(600)
        EnableCollision(0)
        teleportRelativeY(0)
        Unknown1008()
        Unknown1086(22)
        Unknown1009()
        Unknown3001(0)
        Unknown2019(3999)
        SLOT_31 = 1
    sprite('Action_850_00', 8)
    Unknown3004(60)
    label(0)
    sprite('Action_850_01', 6)
    if CheckInput(0x0A):
        sendToLabel(0)
    sprite('Action_850_02', 6)
    sprite('Action_850_03', 4)
    Unknown3001(255)
    GFX_0('Sealing_Tan_AtkCol', 100)
    GFX_0('Sealing_Tan_AtkEff', 100)
    GFX_0('Sealing_Tan_UzuEff', 100)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    Unknown21012('Sealing_Tan_AtkCol', 32)
    Unknown21012('Sealing_Tan_AtkEff', 32)
    Unknown21012('Sealing_Tan_UzuEff', 32)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_SealingEX():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Init')
        Unknown4009(0)
        EnableCollision(0)
        Unknown1086(3)
        teleportRelativeY(0)
        Unknown1008()
        Unknown1086(22)
        Unknown1009()
        Unknown3001(0)
        Unknown2019(3999)
    sprite('Action_850_00', 3)
    Unknown3004(30)
    label(0)
    sprite('Action_850_01', 3)
    if CheckInput(0x013):
        sendToLabel(0)
    sprite('Action_850_02', 10)
    sprite('Action_850_03', 3)
    Unknown1084(1)
    Unknown3001(255)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    GFX_0('Sealing_Tan_AtkColEX', 100)
    GFX_0('Sealing_Tan_AtkEffEX', 100)
    GFX_0('Sealing_Tan_UzuEffEX', 100)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    Unknown21012('Sealing_Tan_AtkColEX', 32)
    Unknown21012('Sealing_Tan_AtkEffEX', 32)
    Unknown21012('Sealing_Tan_UzuEffEX', 32)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Tan_SealingTAG():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Tan_Init')
        Unknown4009(0)
        EnableCollision(0)
        Unknown1086(3)
        teleportRelativeY(0)
        Unknown3001(0)
        Unknown2019(3999)
    sprite('Action_850_00', 3)
    physicsXImpulse(7680)
    Unknown1028(-100)
    Unknown3004(30)
    sprite('Action_850_01', 3)
    sprite('Action_850_02', 10)
    sprite('Action_850_03', 3)
    Unknown1084(1)
    Unknown3001(255)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    GFX_0('Sealing_Tan_AtkColTAG', 100)
    GFX_0('Sealing_Tan_AtkEffTAG', 100)
    GFX_0('Sealing_Tan_UzuEffTAG', 100)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    label(0)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    Unknown21012('Sealing_Tan_AtkColTAG', 32)
    Unknown21012('Sealing_Tan_AtkEffTAG', 32)
    Unknown21012('Sealing_Tan_UzuEffTAG', 32)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def IW_Tan():

    def upon_IMMEDIATE():
        callSubroutine('Tan_ForceWarp')
        callSubroutine('Tan_Init')
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(1700)
        GroundedHitstunAnimation(1)
        AirPushbackX(10000)
        AirPushbackY(-25000)
        YImpluseBeforeWallbounce(0)
        Unknown9310(1)
        Unknown9190(1)
        Unknown9118(20)
        AirUntechableTime(30)
        Unknown9266(13)
        Hitstop(3)
        MinimumDamagePct(15)
        AttackP2(60)
        Unknown11092(1)
        Unknown23182(3)
        Unknown23013(1)
        Unknown9016(1)
        teleportRelativeY(0)
        teleportRelativeX(132500)
        Unknown3001(0)
        Unknown2019(3999)
    sprite('Action_121_00', 7)
    Unknown3004(30)
    physicsYImpulse(15000)
    setGravity(750)
    sprite('Action_121_01', 3)
    Unknown1007(25000)
    sprite('Action_121_02', 2)
    Unknown1007(20000)
    Unknown3001(255)
    sprite('Action_121_03', 1)
    teleportRelativeX(-40000)
    Unknown1007(25000)
    physicsYImpulse(2560)
    setGravity(0)
    sprite('Action_121_03', 5)
    sprite('Action_121_04', 10)
    sprite('Action_121_05', 17)
    sprite('Action_121_06', 30)
    physicsYImpulse(-150000)
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_121_07', 6)
    Unknown1084(1)
    GFX_0('IW_Wave_AtkCol', 100)
    SystemGFX('effect_418', 100)
    ScreenShake(6000, 12000)
    sprite('Action_121_08', 3)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def IW_Tan_OD():

    def upon_IMMEDIATE():
        callSubroutine('Tan_ForceWarp')
        callSubroutine('Tan_Init')
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(1700)
        GroundedHitstunAnimation(1)
        AirPushbackX(10000)
        AirPushbackY(-25000)
        YImpluseBeforeWallbounce(0)
        Unknown9310(1)
        Unknown9190(1)
        Unknown9118(20)
        AirUntechableTime(30)
        MinimumDamagePct(15)
        Unknown9266(13)
        Hitstop(3)
        AttackP2(60)
        Unknown11092(1)
        Unknown23182(3)
        Unknown4009(3)
        Unknown23013(1)
        Unknown9016(1)
        teleportRelativeY(0)
        teleportRelativeX(132500)
        Unknown3001(0)
        Unknown2019(3999)
    sprite('Action_121_00', 7)
    Unknown3004(30)
    physicsYImpulse(15000)
    setGravity(750)
    sprite('Action_121_01', 3)
    Unknown1007(25000)
    sprite('Action_121_02', 2)
    Unknown1007(20000)
    Unknown3001(255)
    sprite('Action_121_03', 1)
    teleportRelativeX(-40000)
    Unknown1007(25000)
    physicsYImpulse(2560)
    setGravity(0)
    sprite('Action_121_03', 5)
    sprite('Action_121_04', 10)
    sprite('Action_121_05', 17)
    sprite('Action_121_06', 30)
    physicsYImpulse(-150000)
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_121_07', 6)
    Unknown1084(1)
    GFX_0('IW_Wave_AtkColOD', 100)
    SystemGFX('effect_418', 100)
    ScreenShake(6000, 12000)
    sprite('Action_121_08', 3)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def IW_Tan_DUO():

    def upon_IMMEDIATE():
        callSubroutine('Tan_ForceWarp')
        callSubroutine('Tan_Init')
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(500)
        Unknown23182(3)
        GroundedHitstunAnimation(1)
        AirPushbackX(10000)
        AirPushbackY(-25000)
        YImpluseBeforeWallbounce(0)
        Unknown9310(1)
        Unknown9190(1)
        Unknown9118(20)
        AirUntechableTime(30)
        Unknown9266(13)
        Hitstop(3)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        Unknown23182(3)
        Unknown23013(1)
        Unknown9016(1)
        teleportRelativeY(0)
        teleportRelativeX(132500)
        Unknown3001(0)
        Unknown2019(3999)
    sprite('Action_121_00', 7)
    Unknown3004(30)
    physicsYImpulse(15000)
    setGravity(750)
    sprite('Action_121_01', 3)
    Unknown1007(25000)
    sprite('Action_121_02', 2)
    Unknown1007(20000)
    Unknown3001(255)
    sprite('Action_121_03', 1)
    teleportRelativeX(-40000)
    Unknown1007(25000)
    physicsYImpulse(2560)
    setGravity(0)
    sprite('Action_121_03', 5)
    sprite('Action_121_04', 10)
    sprite('Action_121_05', 17)
    sprite('Action_121_06', 30)
    physicsYImpulse(-150000)
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_121_07', 6)
    Unknown1084(1)
    GFX_0('IW_Wave_AtkColDUO', 100)
    SystemGFX('effect_418', 100)
    ScreenShake(6000, 12000)
    sprite('Action_121_08', 3)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def IW_Tan_ODDUO():

    def upon_IMMEDIATE():
        callSubroutine('Tan_ForceWarp')
        callSubroutine('Tan_Init')
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(500)
        Unknown23182(3)
        GroundedHitstunAnimation(1)
        AirPushbackX(10000)
        AirPushbackY(-25000)
        YImpluseBeforeWallbounce(0)
        Unknown9310(1)
        Unknown9190(1)
        Unknown9118(20)
        AirUntechableTime(30)
        Unknown9266(13)
        Hitstop(3)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        Unknown23182(3)
        Unknown23013(1)
        Unknown9016(1)
        teleportRelativeY(0)
        teleportRelativeX(132500)
        Unknown3001(0)
        Unknown2019(3999)
    sprite('Action_121_00', 7)
    Unknown3004(30)
    physicsYImpulse(15000)
    setGravity(750)
    sprite('Action_121_01', 3)
    Unknown1007(25000)
    sprite('Action_121_02', 2)
    Unknown1007(20000)
    Unknown3001(255)
    sprite('Action_121_03', 1)
    teleportRelativeX(-40000)
    Unknown1007(25000)
    physicsYImpulse(2560)
    setGravity(0)
    sprite('Action_121_03', 5)
    sprite('Action_121_04', 10)
    sprite('Action_121_05', 17)
    sprite('Action_121_06', 30)
    physicsYImpulse(-150000)
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_121_07', 6)
    Unknown1084(1)
    GFX_0('IW_Wave_AtkColODDUO', 100)
    SystemGFX('effect_418', 100)
    ScreenShake(6000, 12000)
    sprite('Action_121_08', 3)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def UltimateAssault_Tan():

    def upon_IMMEDIATE():
        Unknown2011()
        callSubroutine('Tan_Init')
        Unknown23056()
        AttackLevel_(3)
        Unknown9016(1)
        Unknown11057(600)
        EnableCollision(0)
        Unknown1086(22)
        teleportRelativeY(0)
        teleportRelativeX(-50000)
        Unknown3001(0)
        Unknown2019(3999)
    sprite('Action_850_00', 2)
    physicsXImpulse(7680)
    Unknown1028(-100)
    Unknown3004(30)
    sprite('Action_850_01', 2)
    sprite('Action_850_02', 5)
    sprite('Action_850_03', 2)
    Unknown1084(1)
    Unknown3001(255)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    GFX_0('UltimateAssault_Tan_AtkCol', 100)
    GFX_0('UltimateAssault_Tan_AtkEff', 100)
    GFX_0('UltimateAssault_Tan_UzuEff', 100)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_06', 4)
    label(0)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    sprite('Action_850_04', 4)
    sprite('Action_850_05', 4)
    Unknown21012('UltimateAssault_Tan_AtkCol', 32)
    Unknown21012('UltimateAssault_Tan_AtkEff', 32)
    Unknown21012('UltimateAssault_Tan_UzuEff', 32)
    sprite('Action_850_06', 4)
    sprite('keep', 2)
    enterState('Tan_Delete')

@State
def Astral_Tan():

    def upon_IMMEDIATE():
        Unknown2011()
        callSubroutine('Tan_Init')
        Unknown2054(1)
        AttackLevel_(3)
        Unknown9016(1)
        Unknown11057(600)
        EnableCollision(0)
        Unknown1086(3)
        teleportRelativeY(0)
        teleportRelativeX(-150000)
        Unknown3001(0)
        Unknown2019(3999)

        def upon_32():
            Unknown1000(-350000)
            teleportRelativeX(-150000)

        def upon_33():
            sendToLabel(10)
    sprite('Action_174_04', 3)
    Unknown3004(20)
    physicsYImpulse(2500)
    setGravity(50)
    sprite('Action_174_04', 3)
    sprite('Action_174_04', 8)
    sprite('Action_174_05', 10)
    sprite('Action_174_06', 4)
    Unknown1084(1)
    sprite('Action_174_07', 2)
    sprite('Action_174_08', 2)
    sprite('Action_174_09', 3)
    GFX_0('Astral_Atk', 100)
    label(0)
    sprite('Action_174_10', 4)
    sprite('Action_174_11', 4)
    sprite('Action_174_12', 4)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('Action_176_04', 5)
    sprite('Action_176_05', 4)
    sprite('Action_176_06', 4)
    sprite('Action_176_07', 8)
    GFX_0('AstralBlade', 100)
    sprite('Action_176_08', 8)
    sprite('Action_176_09', 10)
    sprite('Action_176_10', 18)
    sprite('Action_176_11', 2)
    sprite('Action_176_12', 2)
    sprite('Action_176_13', 2)
    label(11)
    sprite('Action_176_14', 3)
    sprite('Action_176_15', 3)
    sprite('Action_176_16', 3)
    loopRest()
    gotoLabel(11)

@State
def Tan_SummonOut():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown1007(250000)
        Unknown2019(499)
    sprite('Action_216_00', 5)
    GFX_0('Tan_Kirakira_Matome', 100)
    sprite('Action_216_01', 5)
    sprite('Action_216_02', 5)
    sprite('Action_216_03', 1)

@State
def Tan_kirakira():
    sprite('null', 5)
    SystemGFX('effect_701', 100)

@State
def Tan_Kirakira_R():

    def upon_IMMEDIATE():
        Unknown1012(0, 180000)
        Unknown1011(-220000, 80000)
        physicsYImpulse(8000)
        setGravity(300)
    sprite('null', 5)
    SystemGFX('effect_701', 100)
    Unknown36(1)
    physicsYImpulse(8000)
    setGravity(150)
    Unknown35()

@State
def Tan_Kirakira_L():

    def upon_IMMEDIATE():
        Unknown1012(-180000, 0)
        Unknown1011(-220000, 80000)
    sprite('null', 5)
    SystemGFX('effect_701', 100)
    Unknown36(1)
    physicsYImpulse(8000)
    setGravity(150)
    Unknown35()

@State
def Tan_Kirakira_Matome():
    sprite('null', 5)
    GFX_0('Tan_Kirakira_R', 100)
    GFX_0('Tan_Kirakira_R', 100)
    GFX_0('Tan_Kirakira_R', 100)
    GFX_0('Tan_Kirakira_R', 100)
    GFX_0('Tan_Kirakira_L', 100)
    GFX_0('Tan_Kirakira_L', 100)
    GFX_0('Tan_Kirakira_L', 100)
    GFX_0('Tan_Kirakira_L', 100)

@State
def __214EX_Tan_Blade():
    sprite('Action_233_00', 3)
    sprite('Action_233_01', 3)
    sprite('Action_233_02', 3)
    sprite('Action_233_03', 1)

@State
def __214A_Tan_Blade():
    Unknown2019(-10)
    sprite('Action_230_00', 3)
    sprite('Action_230_01', 3)
    sprite('Action_230_02', 1)

@State
def __214B_Tan_Blade():
    sprite('Action_750_00', 2)
    sprite('Action_750_01', 2)
    sprite('Action_750_02', 2)

@State
def __214AddA_Tan_Blade1():
    sprite('Action_751_00', 2)
    sprite('Action_751_01', 2)
    sprite('Action_751_02', 2)

@State
def __214AddA_Tan_Blade2():
    sprite('Action_749_00', 2)
    sprite('Action_749_01', 2)
    sprite('Action_749_02', 2)
    sprite('Action_749_03', 2)
    sprite('Action_749_04', 2)

@State
def __214AddB_Tan_Blade():
    sprite('Action_232_00', 3)
    sprite('Action_232_01', 3)
    sprite('Action_232_02', 3)
    sprite('Action_232_03', 1)

@State
def Air214B_Tan_Blade():
    sprite('Action_231_00', 3)
    sprite('Action_231_01', 3)
    sprite('Action_231_02', 3)
    sprite('Action_231_03', 1)

@State
def Sealing_Tan_AtkCol():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        AttackP1(80)
        Unknown9266(13)
        AirUntechableTime(60)
        AirPushbackX(20000)
        AirPushbackY(25000)
        Hitstop(5)
        Unknown2019(-999)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown11044(1)
        Unknown1007(250000)
        Unknown3038(1)

        def upon_32():
            sendToLabel(1)
    sprite('null', 6)
    label(0)
    sprite('Action_851_03', 10)
    RefreshMultihit()
    sprite('Action_851_03', 32767)
    DisableAttackRestOfMove()
    label(1)
    sprite('Action_852_00', 7)
    sprite('Action_852_01', 7)
    sprite('Action_852_02', 1)

@State
def Sealing_Tan_AtkEff():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown1007(250000)
        Unknown2019(-1000)
        Unknown2005()

        def upon_32():
            sendToLabel(1)
    sprite('Action_853_00', 7)
    sprite('Action_853_01', 7)
    sprite('Action_853_02', 7)
    label(0)
    sprite('Action_853_03', 10)
    sprite('Action_853_04', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_852_00', 7)
    Unknown2005()
    sprite('Action_852_01', 7)
    sprite('Action_852_02', 1)

@State
def Sealing_Tan_UzuEff():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown1007(250000)
        Unknown2019(4000)
        Unknown3038(1)

        def upon_32():
            sendToLabel(1)
    sprite('Action_855_00', 7)
    sprite('Action_855_01', 7)
    sprite('Action_855_02', 7)
    sprite('Action_855_03', 20)
    sprite('Action_855_04', 20)
    sprite('Action_855_05', 20)
    sprite('Action_855_06', 20)
    sprite('Action_855_07', 20)
    sprite('Action_855_08', 20)
    label(1)
    sprite('Action_856_00', 7)
    sprite('Action_856_01', 7)
    sprite('Action_856_02', 1)

@State
def Sealing_Tan_AtkColEX():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(450)
        Unknown9266(13)
        AttackP1(80)
        Unknown11092(1)
        AirUntechableTime(45)
        AirPushbackY(25000)
        Hitstop(2)
        Unknown11001(0, 2, 4)
        PushbackX(1500)
        GroundedHitstunAnimation(9)
        Unknown11092(1)
        Unknown2019(-999)
        Unknown1007(250000)
        Unknown3038(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown13044(0)

        def upon_32():
            sendToLabel(1)
    sprite('Action_851_00', 7)
    sprite('Action_851_01', 7)
    sprite('Action_851_02', 7)
    label(0)
    sprite('Action_851_03', 3)
    RefreshMultihit()
    sprite('Action_851_03', 3)
    RefreshMultihit()
    gotoLabel(0)
    label(1)
    
@State
def Sealing_Tan_AtkEffEX():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown1007(250000)
        Unknown2019(-1000)
        Unknown2005()

        def upon_32():
            sendToLabel(1)
    sprite('Action_853_00', 7)
    sprite('Action_853_01', 7)
    sprite('Action_853_02', 7)
    label(0)
    sprite('Action_853_03', 10)
    sprite('Action_853_04', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_852_00', 7)
    Unknown2005()
    sprite('Action_852_01', 7)
    sprite('Action_852_02', 1)

@State
def Sealing_Tan_UzuEffEX():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown1007(250000)
        Unknown2019(4000)
        Unknown3038(1)

        def upon_32():
            sendToLabel(1)
    sprite('Action_855_00', 7)
    sprite('Action_855_01', 7)
    sprite('Action_855_02', 7)
    sprite('Action_855_03', 20)
    sprite('Action_855_04', 20)
    sprite('Action_855_05', 20)
    sprite('Action_855_06', 20)
    sprite('Action_855_07', 20)
    sprite('Action_855_08', 20)
    label(1)
    sprite('Action_856_00', 7)
    sprite('Action_856_01', 7)
    sprite('Action_856_02', 1)
    
@State
def Sealing_Tan_AtkColTAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(450)
        Unknown9266(13)
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        AirUntechableTime(45)
        AirPushbackY(25000)
        Hitstop(2)
        Unknown11001(0, 2, 4)
        PushbackX(1500)
        GroundedHitstunAnimation(9)
        Unknown11092(1)
        Unknown2019(-999)
        Unknown11042(1)
        Unknown1007(250000)
        Unknown3038(1)
        Unknown13044(0)

        def upon_32():
            sendToLabel(1)
    sprite('Action_851_00', 7)
    sprite('Action_851_01', 7)
    sprite('Action_851_02', 7)
    label(0)
    sprite('Action_851_03', 3)
    RefreshMultihit()
    sprite('Action_851_03', 3)
    RefreshMultihit()
    gotoLabel(0)
    label(1)

@State
def Sealing_Tan_AtkEffTAG():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown1007(250000)
        Unknown2019(-1000)
        Unknown2005()

        def upon_32():
            sendToLabel(1)
    sprite('Action_853_00', 7)
    sprite('Action_853_01', 7)
    sprite('Action_853_02', 7)
    label(0)
    sprite('Action_853_03', 10)
    sprite('Action_853_04', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_852_00', 7)
    Unknown2005()
    sprite('Action_852_01', 7)
    sprite('Action_852_02', 1)

@State
def Sealing_Tan_UzuEffTAG():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown1007(250000)
        Unknown2019(4000)
        Unknown3038(1)

        def upon_32():
            sendToLabel(1)
    sprite('Action_855_00', 7)
    sprite('Action_855_01', 7)
    sprite('Action_855_02', 7)
    sprite('Action_855_03', 20)
    sprite('Action_855_04', 20)
    sprite('Action_855_05', 20)
    sprite('Action_855_06', 20)
    sprite('Action_855_07', 20)
    sprite('Action_855_08', 20)
    label(1)
    sprite('Action_856_00', 7)
    sprite('Action_856_01', 7)
    sprite('Action_856_02', 1)

@State
def IW_Wave_AtkCol():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown53(1)
        AttackLevel_(5)
        Damage(1280)
        Unknown9266(13)
        Hitstop(3)
        Unknown11001(-1, -1, -1)
        AttackP2(60)
        Unknown11092(1)
        AirUntechableTime(90)
        Unknown23182(3)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        AirPushbackX(75000)
        AirPushbackY(9000)
        Unknown30055(50000, 70, 0)
        Unknown30056(150000, 70, 0)
        YImpluseBeforeWallbounce(1500)
        PushbackX(30400)
        MinimumDamagePct(15)
        Unknown2053(1)
        Unknown2034(1)

        def upon_3():
            if (SLOT_2 >= 6):
                clearUponHandler(3)
                Unknown2053(0)
                Unknown2034(0)
                SLOT_51 = 1
                sendToLabel(1)

        def upon_44():
            clearUponHandler(3)
            Unknown2053(0)
            Unknown2034(0)
            SLOT_51 = 1
            sendToLabel(1)
    sprite('null', 1)
    physicsXImpulse(67000)
    GFX_0('IW_Wave', 100)
    GFX_0('IW_Wave_eff1', 100)
    label(0)
    sprite('Action_122_atkcol', 2)
    GFX_0('IW_Wave_Zanzo1', 100)
    RefreshMultihit()
    Unknown2038(1)
    sprite('Action_122_atkcol', 2)
    GFX_0('IW_Wave_Zanzo2', 100)
    if (not SLOT_51):
        SystemGFX('effect_419', 100)
        SFX_3('SE015_BoundWall')
        ScreenShake(8000, 8000)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown2003(1)

@State
def IW_Wave_AtkColOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown53(1)
        AttackLevel_(5)
        Damage(700)
        Unknown9266(13)
        Hitstop(3)
        Unknown11001(-1, -1, -1)
        AttackP2(60)
        Unknown11092(1)
        AirUntechableTime(90)
        Unknown23182(3)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        AirPushbackX(75000)
        AirPushbackY(9000)
        Unknown30055(50000, 70, 0)
        Unknown30056(150000, 70, 0)
        YImpluseBeforeWallbounce(1500)
        PushbackX(30400)
        MinimumDamagePct(15)
        Unknown2053(1)
        Unknown2034(1)

        def upon_3():
            if (SLOT_2 >= 7):
                clearUponHandler(3)
                Unknown2053(0)
                Unknown2034(0)
                SLOT_51 = 1
                sendToLabel(1)

        def upon_78():
            if (SLOT_2 == 6):
                clearUponHandler(78)
                GroundedHitstunAnimation(13)
                AirHitstunAnimation(13)
                AirUntechableTime(120)
                AirPushbackX(6500)
                AirPushbackY(11000)
                YImpluseBeforeWallbounce(500)
                Unknown11072(1, 0, 185000)
                Unknown23029(3, 5001, 1)

        def upon_44():
            clearUponHandler(3)
            Unknown2053(0)
            Unknown2034(0)
            SLOT_51 = 1
            sendToLabel(1)
    sprite('null', 1)
    physicsXImpulse(67000)
    GFX_0('IW_Wave', 100)
    GFX_0('IW_Wave_eff1', 100)
    label(0)
    sprite('Action_122_atkcol', 2)
    GFX_0('IW_Wave_Zanzo1', 100)
    RefreshMultihit()
    Unknown2038(1)
    sprite('Action_122_atkcol', 2)
    GFX_0('IW_Wave_Zanzo2', 100)
    if (SLOT_2 < 6):
        RefreshMultihit()
    if (not SLOT_51):
        SystemGFX('effect_419', 100)
        SFX_3('SE015_BoundWall')
        ScreenShake(8000, 8000)
    gotoLabel(0)
    label(1)
    sprite('null', 10)

@State
def IW_Wave_AtkColDUO():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown53(1)
        AttackLevel_(5)
        Damage(250)
        Unknown9266(13)
        Hitstop(3)
        AirUntechableTime(90)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        Unknown23182(3)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        AirPushbackX(75000)
        AirPushbackY(9000)
        Unknown30055(50000, 70, 0)
        Unknown30056(150000, 70, 0)
        YImpluseBeforeWallbounce(1500)
        PushbackX(30400)
        Unknown2053(1)
        Unknown2034(1)

        def upon_3():
            if (SLOT_2 >= 6):
                clearUponHandler(3)
                Unknown2053(0)
                Unknown2034(0)
                SLOT_51 = 1
                sendToLabel(1)

        def upon_44():
            clearUponHandler(3)
            Unknown2053(0)
            Unknown2034(0)
            SLOT_51 = 1
            sendToLabel(1)
    sprite('null', 1)
    physicsXImpulse(67000)
    GFX_0('IW_Wave', 100)
    GFX_0('IW_Wave_eff1', 100)
    label(0)
    sprite('Action_122_atkcol', 2)
    GFX_0('IW_Wave_Zanzo1', 100)
    RefreshMultihit()
    Unknown2038(1)
    sprite('Action_122_atkcol', 2)
    GFX_0('IW_Wave_Zanzo2', 100)
    if (not SLOT_51):
        SystemGFX('effect_419', 100)
        SFX_3('SE015_BoundWall')
        ScreenShake(8000, 8000)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown2003(1)

@State
def IW_Wave_AtkColODDUO():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown53(1)
        AttackLevel_(5)
        Damage(125)
        Unknown9266(13)
        Hitstop(3)
        Unknown11001(-1, -1, -1)
        AirUntechableTime(90)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        Unknown23182(3)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        AirPushbackX(75000)
        AirPushbackY(9000)
        Unknown30055(50000, 70, 0)
        Unknown30056(150000, 70, 0)
        YImpluseBeforeWallbounce(1500)
        PushbackX(30400)
        Unknown2053(1)
        Unknown2034(1)

        def upon_3():
            if (SLOT_2 >= 7):
                clearUponHandler(3)
                Unknown2053(0)
                Unknown2034(0)
                SLOT_51 = 1
                sendToLabel(1)

        def upon_78():
            if (SLOT_2 == 6):
                clearUponHandler(78)
                GroundedHitstunAnimation(13)
                AirHitstunAnimation(13)
                AirUntechableTime(120)
                AirPushbackX(6500)
                AirPushbackY(11000)
                YImpluseBeforeWallbounce(500)
                Unknown11072(1, 0, 185000)
                Unknown23029(3, 5001, 1)

        def upon_44():
            clearUponHandler(3)
            Unknown2053(0)
            Unknown2034(0)
            SLOT_51 = 1
            sendToLabel(1)
    sprite('null', 1)
    physicsXImpulse(67000)
    GFX_0('IW_Wave', 100)
    GFX_0('IW_Wave_eff1', 100)
    label(0)
    sprite('Action_122_atkcol', 2)
    GFX_0('IW_Wave_Zanzo1', 100)
    RefreshMultihit()
    Unknown2038(1)
    sprite('Action_122_atkcol', 2)
    GFX_0('IW_Wave_Zanzo2', 100)
    if (SLOT_2 < 6):
        RefreshMultihit()
    if (not SLOT_51):
        SystemGFX('effect_419', 100)
        SFX_3('SE015_BoundWall')
        ScreenShake(8000, 8000)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown2003(1)

@State
def IW_Wave():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2019(-4000)
    sprite('Action_123_00', 3)
    sprite('Action_123_01', 3)
    label(0)
    sprite('Action_123_02', 3)
    sprite('Action_123_03', 3)
    sprite('Action_123_04', 3)
    sprite('Action_123_05', 3)
    sprite('Action_123_06', 3)
    sprite('Action_123_07', 3)
    gotoLabel(0)
    sprite('Action_123_08', 3)
    sprite('Action_123_09', 3)
    sprite('Action_123_10', 3)

@State
def IW_Wave_eff1():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2019(-3999)
        teleportRelativeX(90000)
    sprite('Action_128_00', 35)
    sprite('Action_128_01', 1)

@State
def IW_Wave_Zanzo1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2019(-3998)
    sprite('Action_125_00', 4)
    sprite('Action_125_01', 4)
    sprite('Action_125_02', 4)

@State
def IW_Wave_Zanzo2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2019(-3999)
    sprite('Action_126_00', 4)
    sprite('Action_126_01', 4)
    sprite('Action_126_02', 4)

@State
def UltimateAssault_Tan_AtkCol():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4010(3)
        AttackLevel_(5)
        Damage(500)
        Unknown23182(3)
        Unknown9266(13)
        Unknown11001(0, 60, 60)
        Unknown11064(1)
        Unknown1007(250000)
        Hitstop(2)
        AirUntechableTime(60)
        PushbackX(1500)
        Unknown30055(30000, 70, 0)
        Unknown30056(30000, 70, 0)
        Unknown11092(1)
        Unknown2019(-999)
        MinimumDamagePct(10)
        Unknown3038(1)

        def upon_32():
            sendToLabel(1)
        Unknown11069('UltimateAssaultOD')
    sprite('null', 5)
    label(0)
    sprite('Action_851_03', 5)
    RefreshMultihit()
    sprite('Action_851_03', 32767)
    StartMultihit()
    label(1)
    sprite('null', 1)
    Unknown2003(1)

@State
def UltimateAssault_Tan_AtkEff():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown1007(250000)
        Unknown2019(-1000)
        Unknown2005()

        def upon_32():
            sendToLabel(1)
    sprite('Action_853_00', 7)
    sprite('Action_853_01', 7)
    sprite('Action_853_02', 7)
    label(0)
    sprite('Action_853_03', 10)
    sprite('Action_853_04', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_852_00', 7)
    Unknown2005()
    sprite('Action_852_01', 7)
    sprite('Action_852_02', 1)

@State
def UltimateAssault_Tan_UzuEff():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown1007(250000)
        Unknown2019(4000)
        Unknown3038(1)

        def upon_32():
            sendToLabel(1)
    sprite('Action_855_00', 7)
    sprite('Action_855_01', 7)
    sprite('Action_855_02', 7)
    sprite('Action_855_03', 20)
    sprite('Action_855_04', 20)
    sprite('Action_855_05', 20)
    sprite('Action_855_06', 20)
    sprite('Action_855_07', 20)
    sprite('Action_855_08', 20)
    label(1)
    sprite('Action_856_00', 7)
    sprite('Action_856_01', 7)
    sprite('Action_856_02', 1)

@State
def UltimateAssault_Camera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown20000(1)

        def upon_3():
            Unknown1086(3)

        def upon_32():
            clearUponHandler(3)

        def upon_33():
            Unknown48(25, 2, 23, 22, 2, 23)
            Unknown1007(180000)

        def upon_34():
            physicsYImpulse(-25000)

            def upon_LANDING():
                clearUponHandler(2)
                Unknown1084(1)

        def upon_STATE_END():
            Unknown20000(0)
    sprite('null', 32767)

@State
def UltimateAssaultOD_Camera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown20000(1)

        def upon_3():
            Unknown1086(3)

        def upon_32():
            clearUponHandler(3)

        def upon_33():
            physicsYImpulse(125000)
            setGravity(1900)
            Unknown1007(350000)
            Unknown4009(3)

        def upon_34():
            physicsYImpulse(0)
            setGravity(1900)
            Unknown4009(0)

        def upon_35():
            physicsYImpulse(-50000)

            def upon_LANDING():
                clearUponHandler(2)
                Unknown1084(1)

        def upon_43():
            pass

        def upon_STATE_END():
            Unknown20000(0)
    sprite('null', 32767)

@State
def UltimateAssault_Blade1():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_219_00', 8)
    sprite('Action_219_01', 8)
    sprite('Action_219_02', 3)
    sprite('Action_219_03', 3)
    sprite('Action_219_04', 1)

@State
def Ultimate_kirakira_matome():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        loopRelated(17, 120)

        def upon_17():
            sendToLabel(580)

        def upon_32():
            Unknown4007(0)
            Unknown1084(1)
            Unknown1086(3)
            sendToLabel(1)
    label(0)
    sprite('null', 1)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 1)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    gotoLabel(0)
    label(1)
    sprite('null', 17)
    Unknown1007(-100000)
    sprite('null', 2)
    physicsYImpulse(35000)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 2)
    GFX_0('Ultimate_kirakira', 100)
    GFX_0('Ultimate_kirakira', 100)
    sprite('null', 32767)
    label(580)
    sprite('null', 2)

@State
def Ultimate_kirakira():

    def upon_IMMEDIATE():
        Unknown1026(-3000, 3000)
        Unknown1011(-150000, 150000)
        Unknown1012(-50000, 50000)
    sprite('Action_165_00', 7)
    sprite('Action_165_01', 7)
    sprite('Action_165_02', 1)

@State
def Ultimate_kirakira_matomeX():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown1007(220000)
        loopRelated(17, 15)

        def upon_17():
            sendToLabel(580)
    label(0)
    sprite('null', 1)
    GFX_0('Ultimate_kirakiraX', 100)
    GFX_0('Ultimate_kirakiraX', 100)
    GFX_0('Ultimate_kirakiraX', 100)
    sprite('null', 1)
    GFX_0('Ultimate_kirakiraX', 100)
    GFX_0('Ultimate_kirakiraX', 100)
    GFX_0('Ultimate_kirakiraX', 100)
    gotoLabel(0)
    label(580)
    sprite('null', 2)

@State
def Ultimate_kirakiraX():

    def upon_IMMEDIATE():
        Unknown1025(1000, 2000)
        Unknown1011(-80000, 80000)
        Unknown1012(-50000, 50000)
    sprite('Action_165_00', 7)
    sprite('Action_165_01', 7)
    sprite('Action_165_02', 1)

@State
def CommandOrderAddC_kirakiraX():

    def upon_IMMEDIATE():
        Unknown1025(5000, 3000)
        Unknown1011(300000, 250000)
        Unknown1012(-300000, 300000)
    sprite('Action_165_00', 7)
    sprite('Action_165_01', 7)
    sprite('Action_165_02', 1)

@Subroutine
def DeleteAstralObj():
    Unknown26('Astral_Cross')
    Unknown26('Astral_Cross_Parts1')
    Unknown26('Astral_Cross_Parts2')
    Unknown26('Astral_Cross_Parts3')
    Unknown26('Astral_Cross_Parts4')
    Unknown26('Astral_Cross_Parts5')
    Unknown26('AstralBG')
    Unknown26('AstralBG_Blaze')

@State
def Astral_Atk():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown2054(1)
        AttackLevel_(5)
        Damage(1550)
        MinimumDamagePct(100)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11072(1, 0, 0)
        GroundedHitstunAnimation(0)
        AirHitstunAnimation(0)
        Unknown30048(1)
        Unknown11064(1)
        PushbackX(0)
        Hitstop(0)
        Unknown11001(3, 3, 3)
        hitstun(9999)
        Unknown9016(1)
        Unknown1086(22)
        teleportRelativeY(250000)
        Unknown2019(-4000)

        def upon_78():
            Unknown21007(3, 37)
            Unknown2038(1)
            GFX_0('AstralBG', 100)
        Unknown11086(1)
    sprite('Action_175_00', 4)
    blockstun(30)
    sprite('Action_175_01', 4)
    sprite('Action_175_02', 4)
    sprite('Action_175_03', 4)
    sprite('Action_175_04', 4)
    sprite('Action_175_05', 4)
    sprite('Action_175_06', 4)
    sprite('Action_175_07', 4)
    RefreshMultihit()
    blockstun(20)
    sprite('Action_175_08', 4)
    RefreshMultihit()
    sprite('Action_175_09', 4)
    RefreshMultihit()
    sprite('Action_175_10', 4)
    RefreshMultihit()
    sprite('Action_175_11', 4)
    loopRest()
    if (not SLOT_2):
        sendToLabel(999)
    sprite('Action_175_12', 10)
    sprite('Action_175_13', 20)
    GFX_0('AstralCamera', 100)
    sprite('Action_175_14', 4)
    GFX_0('Astral_Cross', 100)
    sprite('Action_175_15', 4)
    sprite('Action_175_16', 4)
    label(999)
    sprite('null', 1)

@State
def BGWhite_Dummy():
    sprite('Action_175_14', 15)
    Unknown1096(2500)
    sprite('Action_175_15', 4)
    Unknown1096(1000)
    sprite('Action_175_16', 4)
    loopRest()

@State
def AstralBG():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown23032(50)
        Unknown23033(50)
        Unknown23084(1)
        Unknown23024(3)
        Unknown20006(1)

        def upon_32():
            Unknown1086(22)
    sprite('Action_186_01', 4)
    sprite('Action_186_02', 4)
    sprite('Action_186_03', 4)
    sprite('Action_186_04', 4)
    label(0)
    sprite('Action_186_05', 4)
    sprite('Action_186_06', 4)
    sprite('Action_186_07', 4)
    sprite('Action_186_08', 4)
    sprite('Action_186_09', 4)
    sprite('Action_186_10', 4)
    gotoLabel(0)
    sprite('Action_186_11', 4)

@State
def AstralCamera():

    def upon_IMMEDIATE():
        Unknown20009(1000)
        Unknown23013(0)
        Unknown20008(1)
        Unknown20003(1)

        def upon_STATE_END():
            Unknown20000(0)
    label(0)
    sprite('null', 10)
    sprite('null', 1)
    Unknown20000(1)
    Unknown36(3)
    Unknown1000(-350000)
    Unknown35()
    Unknown21007(3, 32)
    Unknown36(22)
    Unknown1000(-350000)
    Unknown1007(300000)
    setGravity(0)
    Unknown23178(24)
    Unknown35()
    if Unknown42('btg'):
        Unknown36(22)
        Unknown1007(-100000)
        Unknown35()
    if Unknown42('uwa'):
        Unknown36(22)
        Unknown1007(-120000)
        Unknown35()
    if Unknown42('ume'):
        Unknown36(22)
        Unknown1007(-100000)
        Unknown35()
    Unknown1086(22)
    Unknown1007(-250000)
    physicsYImpulse(10000)
    setGravity(100)
    Unknown20009(980)
    SFX_1('uor291')
    Unknown21012('AstralBG', 32)
    GFX_0('BGWhite_Dummy', 100)
    sprite('null', 1)
    Unknown20009(960)
    sprite('null', 1)
    Unknown20009(940)
    sprite('null', 1)
    Unknown20009(920)
    sprite('null', 1)
    Unknown20009(900)
    sprite('null', 1)
    Unknown20009(880)
    sprite('null', 1)
    Unknown20009(860)
    sprite('null', 1)
    Unknown20009(840)
    sprite('null', 1)
    Unknown20009(820)
    sprite('null', 60)
    Unknown20009(800)
    sprite('null', 60)
    Unknown1084(1)
    sprite('null', 1)
    Unknown23013(1)
    Unknown20008(0)
    Unknown20003(0)
    SLOT_12 = SLOT_22
    SLOT_12 = (SLOT_12 * (-1))
    SLOT_13 = SLOT_23
    SLOT_13 = (SLOT_13 * (-1))
    Unknown1019(4)
    YAccel(2)
    Unknown20009(804)
    GFX_0('AstralBG_Blaze', 100)
    sprite('null', 50)
    Unknown20000(0)
    sprite('null', 1)
    Unknown21007(3, 33)

@State
def Astral_Cross():

    def upon_IMMEDIATE():
        Unknown2019(4000)
        Unknown1000(350000)
        teleportRelativeY(0)
        teleportRelativeX(30000)
        GFX_0('Astral_Cross_Parts1', 100)
        GFX_0('Astral_Cross_Parts2', 100)
        GFX_0('Astral_Cross_Parts3', 100)
        GFX_0('Astral_Cross_Parts4', 100)
        GFX_0('Astral_Cross_Parts5', 100)
    sprite('Action_185_00', 10)
    sprite('Action_185_01', 10)
    label(0)
    sprite('Action_185_02', 10)
    sprite('Action_185_03', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_185_04', 10)

@State
def Astral_Cross_Parts1():

    def upon_IMMEDIATE():
        Unknown2019(-4000)
        Unknown4007(2)
        teleportRelativeX(-10000)
    sprite('Action_180_00', 10)
    sprite('Action_180_01', 10)
    sprite('Action_180_02', 10)
    label(0)
    sprite('Action_180_03', 10)
    sprite('Action_180_04', 10)
    sprite('Action_180_05', 10)
    sprite('Action_180_06', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_180_07', 10)

@State
def Astral_Cross_Parts2():

    def upon_IMMEDIATE():
        Unknown2019(3995)
        Unknown4007(2)
    sprite('Action_181_00', 10)
    sprite('Action_181_01', 10)
    sprite('Action_181_02', 10)
    label(0)
    sprite('Action_181_03', 10)
    sprite('Action_181_04', 10)
    sprite('Action_181_05', 10)
    sprite('Action_181_06', 10)
    sprite('Action_181_07', 10)
    sprite('Action_181_08', 10)
    sprite('Action_181_09', 10)
    sprite('Action_181_10', 10)
    sprite('Action_181_11', 10)
    sprite('Action_181_12', 10)
    sprite('Action_181_13', 10)
    sprite('Action_181_14', 10)
    sprite('Action_181_15', 10)
    sprite('Action_181_16', 10)
    sprite('Action_181_17', 10)
    sprite('Action_181_18', 10)
    sprite('Action_181_19', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_181_20', 10)

@State
def Astral_Cross_Parts3():

    def upon_IMMEDIATE():
        Unknown2019(3995)
        Unknown4007(2)
    sprite('Action_182_00', 10)
    sprite('Action_182_01', 10)
    sprite('Action_182_02', 10)
    label(0)
    sprite('Action_182_03', 10)
    sprite('Action_182_04', 10)
    sprite('Action_182_05', 10)
    sprite('Action_182_06', 10)
    sprite('Action_182_07', 10)
    sprite('Action_182_08', 10)
    sprite('Action_182_09', 10)
    sprite('Action_182_10', 10)
    sprite('Action_182_11', 10)
    sprite('Action_182_12', 10)
    sprite('Action_182_13', 10)
    sprite('Action_182_14', 10)
    sprite('Action_182_15', 10)
    sprite('Action_182_16', 10)
    sprite('Action_182_17', 10)
    sprite('Action_182_18', 10)
    sprite('Action_182_20', 10)
    sprite('Action_182_21', 10)
    sprite('Action_182_22', 10)
    sprite('Action_182_23', 10)
    sprite('Action_182_24', 10)
    sprite('Action_182_25', 10)
    sprite('Action_182_26', 10)
    sprite('Action_182_27', 10)
    sprite('Action_182_28', 10)
    sprite('Action_182_29', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_182_30', 10)

@State
def Astral_Cross_Parts4():

    def upon_IMMEDIATE():
        Unknown2019(3995)
        Unknown4007(2)
    sprite('Action_183_00', 10)
    sprite('Action_183_01', 10)
    sprite('Action_183_02', 10)
    label(0)
    sprite('Action_183_03', 10)
    sprite('Action_183_04', 10)
    sprite('Action_183_05', 10)
    sprite('Action_183_06', 10)
    sprite('Action_183_07', 10)
    sprite('Action_183_08', 10)
    sprite('Action_183_09', 10)
    sprite('Action_183_10', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_183_11', 10)

@State
def Astral_Cross_Parts5():

    def upon_IMMEDIATE():
        Unknown2019(3995)
        Unknown4007(2)
    sprite('Action_184_00', 10)
    sprite('Action_184_01', 10)
    sprite('Action_184_02', 10)
    label(0)
    sprite('Action_184_03', 10)
    sprite('Action_184_04', 10)
    sprite('Action_184_05', 10)
    sprite('Action_184_06', 10)
    sprite('Action_184_07', 10)
    gotoLabel(0)
    label(1)
    sprite('Action_184_08', 10)

@State
def AstralBG_Blaze():

    def upon_IMMEDIATE():
        Unknown2019(-4000)
        Unknown23032(50)
        Unknown1007(-150000)

        def upon_32():
            Unknown1086(22)
    sprite('Action_187_00', 3)
    sprite('Action_187_01', 3)
    sprite('Action_187_02', 3)
    label(0)
    sprite('Action_187_03', 3)
    sprite('Action_187_04', 3)
    sprite('Action_187_05', 3)
    sprite('Action_187_06', 3)
    sprite('Action_187_07', 3)
    sprite('Action_187_08', 3)
    gotoLabel(0)
    label(1)
    sprite('Action_187_09', 3)
    sprite('Action_187_10', 3)

@State
def AstralBlade():

    def upon_IMMEDIATE():
        Unknown1086(2)
        Unknown1072(104000)
        teleportRelativeX(0)
        Unknown1007(250000)
        Unknown2019(4000)

        def upon_32():
            Unknown1084(1)
            sendToLabel(1)
    sprite('Action_178_00', 25)
    Unknown1074(-40000)
    physicsYImpulse(90000)
    setGravity(6500)
    physicsXImpulse(40000)
    Unknown1028(-4000)
    SFX_3('SE045')

    def upon_3():
        Unknown2038(1)
        if (SLOT_2 >= 5):
            SFX_3('SE045')
            SLOT_2 = 0
        Unknown1075(90)
    sprite('Action_178_01', 2)
    Unknown1084(1)
    Unknown1074(-5000)
    physicsXImpulse(100000)
    clearUponHandler(3)

    def upon_3():
        Unknown1019(90)
    sprite('Action_178_01', 2)
    Unknown1074(0)
    Unknown1072(0)
    sprite('Action_178_02', 45)
    SFX_3('SE_HolyVoice')
    Unknown1084(1)
    GFX_0('AstralBladeAura', 100)
    GFX_0('AstralBladeAlpha', 100)
    sprite('Action_178_03', 4)
    SFX_3('SE_ShotSpecialHoly')
    Unknown3001(64)
    Unknown2019(-4000)
    physicsXImpulse(5000)
    Unknown1028(15000)
    sprite('Action_178_03', 255)
    SFX_1('uor292')
    label(1)
    sprite('keep', 5)

@State
def AstralBladeAlpha():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown4007(2)
        Unknown2019(-4000)
        Unknown1096(1100)
        Unknown3001(128)
    sprite('Action_178_02', 58)

@State
def AstralBladeAura():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2012()
        AttackLevel_(5)
        Damage(15000)
        MinimumDamagePct(100)
        hitstun(9999)
        AirUntechableTime(9999)
        Hitstop(0)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        Unknown9016(1)
        YImpluseBeforeWallbounce(0)
        AirPushbackX(0)
        AirPushbackY(0)
        PushbackX(0)
        Unknown11086(1)
        Unknown4007(2)
        Unknown2019(-3995)

        def upon_78():
            clearUponHandler(78)
            SFX_3('SE071_KO')
            Unknown21007(2, 32)
            SLOT_54 = 1
            sendToLabel(1)

        def upon_45():
            Unknown36(22)
            Unknown1000(-350000)
            teleportRelativeY(300000)
            setGravity(0)
            Unknown23178(24)
            Unknown35()
            if Unknown42('btg'):
                Unknown36(22)
                Unknown1007(-100000)
                Unknown35()
            if Unknown42('uwa'):
                Unknown36(22)
                Unknown1007(-120000)
                Unknown35()
            if Unknown42('ume'):
                Unknown36(22)
                Unknown1007(-100000)
                Unknown35()
    sprite('Action_179_01', 4)
    sprite('Action_179_02', 4)
    sprite('Action_179_03', 4)
    sprite('Action_179_04', 4)
    sprite('Action_179_05', 4)
    label(0)
    sprite('Action_179_06', 4)
    sprite('Action_179_07', 4)
    sprite('Action_179_08', 4)
    sprite('Action_179_09', 4)
    sprite('Action_179_10', 4)
    sprite('Action_179_11', 4)
    gotoLabel(0)
    label(1)
    sprite('keep', 3)
    Unknown36(22)
    Unknown23178(24)
    Unknown35()
    GFX_0('AstralFinish', 100)

@State
def AstralFinish():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2012()
        Unknown11023(1)
        AttackLevel_(5)
        Damage(18500)
        MinimumDamagePct(100)
        hitstun(9999)
        AirUntechableTime(9999)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Hitstop(0)
        YImpluseBeforeWallbounce(0)
        AirPushbackX(0)
        AirPushbackY(0)
        PushbackX(0)
        Unknown11064(3)
        Unknown23015(1)
        Unknown11086(1)
    sprite('Action_179_13', 4)
    sprite('Action_179_14', 4)
    sprite('Action_179_15', 4)
    sprite('Action_179_16', 4)
    sprite('Action_179_17', 4)
    sprite('Action_179_18', 3)
    sprite('Action_179_19', 3)
    sprite('Action_179_18', 3)
    sprite('Action_179_19', 3)
    sprite('Action_179_18', 3)
    sprite('Action_179_19', 3)
    sprite('Action_179_18', 3)
    sprite('Action_179_19', 3)
    sprite('Action_179_18', 3)
    sprite('Action_179_19', 3)
    sprite('Action_179_18', 3)
    sprite('Action_179_19', 3)
    sprite('Action_179_18', 3)
    sprite('Action_179_19', 3)
    sprite('Action_179_18', 3)
    sprite('Action_179_19', 3)
    sprite('Action_179_20', 3)
    sprite('Action_179_21', 3)
    sprite('Action_179_22', 3)
    Unknown1084(1)
    Unknown1007(500000)
    sprite('Action_179_23', 4)
    RefreshMultihit()
    SFX_3('SE_BigBomb')
    Unknown1007(-400000)
    Unknown1099(50)
    sprite('Action_179_24', 4)
    sprite('Action_179_25', 4)
    sprite('Action_179_26', 4)
    sprite('Action_179_27', 80)
    callSubroutine('DeleteAstralObj')
    Unknown21007(3, 40)
    Unknown36(22)
    setGravity(1200)
    Unknown35()
    Unknown23024(0)
    sprite('keep', 1)
    Unknown21007(3, 41)

@State
def Ori_CutIn():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        Unknown23015(5)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_999_01', 2)
    sprite('Action_999_02', 2)
    sprite('Action_999_03', 3)
    sprite('Action_999_04', 2)
    sprite('Action_999_05', 2)
    sprite('Action_999_06', 3)
    sprite('Action_999_07', 4)
    sprite('Action_999_08', 5)
    sprite('Action_999_09', 5)
    sprite('Action_999_10', 2)
    sprite('Action_999_11', 2)
    sprite('Action_999_12', 4)
    sprite('Action_999_13', 8)
    sprite('Action_999_14', 3)
    sprite('Action_999_15', 3)
    sprite('Action_999_16', 3)
    sprite('Action_999_17', 3)
    sprite('Action_999_18', 2)
    Unknown1019(0)
    sprite('Action_999_19', 3)
    sprite('Action_999_20', 10)
    physicsXImpulse(12000)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(20)
    sprite('Action_999_21', 3)