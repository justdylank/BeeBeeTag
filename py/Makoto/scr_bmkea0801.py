@State
def EMB_MK():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ef_emb_MK.DIG', 'ef_emb_MK_motion_000.mmot')
        Unknown23015(5)
        Unknown1096(850)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-1, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 20)

@State
def EMB_MK_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ef_emb_MK.DIG', 'ef_emb_MK_motion_000.mmot')
        Unknown23015(5)
        Unknown1096(850)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-16744193, 10)
    sprite('null', 10)
    Unknown3025(-16744193, 10)
    sprite('null', 20)

@State
def EMB_MK_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('ef_emb_MK.DIG', 'ef_emb_MK_motion_000.mmot')
        Unknown23015(5)
        Unknown1096(850)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-65536, 10)
    sprite('null', 10)
    Unknown3025(-55256, 10)
    sprite('null', 10)
    Unknown3025(-19276, 10)
    sprite('null', 10)
    Unknown3025(-65536, 10)
    sprite('null', 20)

@State
def DriveRing():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(3)

        def upon_43():
            if (SLOT_48 == 1001):
                sendToLabel(22)
            if (SLOT_48 == 1031):
                teleportRelativeX(-65000)
                Unknown1007(200000)
                Unknown4007(3)
            if (SLOT_48 == 1032):
                teleportRelativeX(-30000)
                Unknown1007(240000)
                Unknown4007(3)
            if (SLOT_48 == 1065):
                teleportRelativeX(20000)
                Unknown1007(308000)
                Unknown4007(3)
            if (SLOT_48 == 1042):
                teleportRelativeX(-158000)
                Unknown1007(240000)
                Unknown4007(3)
            if (SLOT_48 == 1043):
                teleportRelativeX(-72000)
                Unknown1007(350000)
                Unknown4007(3)
            if (SLOT_48 == 1044):
                teleportRelativeX(-78000)
                Unknown1007(230000)
                Unknown4007(3)
            if (SLOT_48 == 1050):
                teleportRelativeX(-115000)
                Unknown1007(285000)
                Unknown4007(3)
            if (SLOT_48 == 1061):
                teleportRelativeX(0)
                Unknown1007(208000)
                Unknown4007(3)
            if (SLOT_48 == 1062):
                teleportRelativeX(-135000)
                Unknown1007(270000)
                Unknown4007(3)
            if (SLOT_48 == 1063):
                teleportRelativeX(0)
                Unknown1007(440000)
                Unknown4007(3)
            if (SLOT_48 == 1071):
                teleportRelativeX(-195000)
                Unknown1007(235000)
                Unknown4007(3)

        def upon_58():
            if Unknown23156('mk407_pos'):
                teleportRelativeX(-158000)
                Unknown1007(240000)
                Unknown4007(3)
            if Unknown23156('Blockingpos'):
                teleportRelativeX(-64000)
                Unknown1007(245000)
                Unknown4007(3)
            if Unknown23156('PowerDunkpos'):
                teleportRelativeX(-72000)
                Unknown1007(350000)
                Unknown4007(3)
            if Unknown23156('PowerDunkStepBpos'):
                teleportRelativeX(-68000)
                Unknown1007(350000)
                Unknown4007(3)
            if Unknown23156('PowerDunkStepCpos'):
                teleportRelativeX(-70000)
                Unknown1007(350000)
                Unknown4007(3)
            if Unknown23156('UpperBodyBlowpos'):
                teleportRelativeX(-115000)
                Unknown1007(285000)
                Unknown4007(3)
            if Unknown23156('DashStraightpos'):
                teleportRelativeX(-78000)
                Unknown1007(230000)
                Unknown4007(3)

            def upon_43():
                if (SLOT_48 == 1065):
                    teleportRelativeX(20000)
                    Unknown1007(308000)
                    Unknown4007(3)
            if Unknown23156('ShinSyouryu1Pos'):
                teleportRelativeX(0)
                Unknown1007(208000)
                Unknown4007(3)
            if Unknown23156('ShinSyouryu2Pos'):
                teleportRelativeX(-135000)
                Unknown1007(270000)
                Unknown4007(3)
            if Unknown23156('ShinSyouryu3Pos'):
                teleportRelativeX(0)
                Unknown1007(440000)
                Unknown4007(3)
            if Unknown23156('AstralPos'):
                teleportRelativeX(-195000)
                Unknown1007(235000)
                Unknown4007(3)
        SLOT_51 = SLOT_102
        SLOT_51 = (SLOT_51 + 1)
        SLOT_103 = SLOT_51
        SLOT_103 = (SLOT_103 * 80)
        SLOT_104 = (-80)
        Unknown3000(1)

        def upon_3():
            if (SLOT_18 > SLOT_51):
                Unknown13(25)
    sprite('null', 4)
    sprite('null', 117)
    GFX_0('DriveChargemc', -1)
    loopRest()
    label(22)
    sprite('null', 30)
    clearUponHandler(32)
    Unknown1099(20)
    Unknown21015('DriveChargemc', 1001, 0)
    Unknown4007(0)

@State
def FakeBunshinStepA():

    def upon_IMMEDIATE():
        Unknown23022(1)
        sendToLabelUpon(56, 99)
        Unknown2053(1)
    sprite('mk404_00', 3)
    Unknown3029(1)
    Unknown3069(0)
    sprite('mk404_01', 2)
    physicsXImpulse(10000)
    sprite('mk404_02', 2)
    sprite('mk404_03', 4)
    Unknown1019(200)
    sprite('mk404_04', 4)
    Unknown1019(150)
    sprite('mk404_05', 4)
    sprite('mk404_06', 4)
    Unknown3004(-20)
    Unknown3032()
    sprite('mk404_07', 4)
    sprite('mk404_08', 4)
    sprite('mk404_09', 4)
    label(99)
    sprite('keep', 4)
    Unknown1019(20)
    GFX_1('mkef_fakebunshin', 0)
    Unknown3004(-20)
    Unknown3032()

@State
def FakeBunshinStepB():

    def upon_IMMEDIATE():
        Unknown23022(1)
        sendToLabelUpon(56, 99)
        Unknown2053(1)
    sprite('mk023_00', 2)
    Unknown3029(1)
    Unknown3069(0)
    sprite('mk023_01', 2)
    sprite('mk411_00', 4)
    physicsXImpulse(24000)
    physicsYImpulse(30000)
    setGravity(2000)
    sprite('mk411_01', 4)
    sprite('mk411_02', 3)
    sprite('mk411_03', 3)
    sprite('mk411_04', 1)
    sprite('mk411_04', 2)
    Unknown3004(-20)
    Unknown3032()
    sprite('mk411_05', 3)
    sprite('mk411_12', 2)
    sprite('mk411_13', 2)
    sprite('mk411_14', 3)
    sprite('mk411_15', 2)
    sprite('mk411_16', 2)
    label(99)
    sprite('keep', 4)
    Unknown1019(20)
    GFX_1('mkef_fakebunshin', 0)
    Unknown3004(-20)
    Unknown3032()

@State
def FakeBunshinStepC():

    def upon_IMMEDIATE():
        Unknown23022(1)
        sendToLabelUpon(56, 99)
        Unknown2053(1)
    sprite('mk023_00', 2)
    Unknown3029(1)
    Unknown3069(0)
    sprite('mk023_01', 2)
    sprite('mk411_00', 4)
    physicsXImpulse(9000)
    physicsYImpulse(42000)
    setGravity(2200)
    sprite('mk411_01', 4)
    sprite('mk411_02', 3)
    sprite('mk411_03', 3)
    sprite('mk411_04', 1)
    sprite('mk411_04', 2)
    Unknown3004(-20)
    Unknown3032()
    sprite('mk411_05', 3)
    sprite('mk411_12', 2)
    Unknown1019(80)
    sprite('mk411_13', 2)
    sprite('mk411_14', 3)
    sprite('mk411_15', 2)
    sprite('mk411_16', 2)
    label(99)
    sprite('keep', 4)
    Unknown1019(20)
    GFX_1('mkef_fakebunshin', 0)
    Unknown3004(-20)
    Unknown3032()

@State
def DonguriShot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(1000)
        AttackP2(80)
        hitstun(17)
        blockstun(16)
        AirUntechableTime(45)
        AirPushbackY(30000)
        Unknown2053(1)
        sendToLabelUpon(2, 1)
        sendToLabelUpon(54, 1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('vr_donguri', 32767)
    Unknown1074(30000)
    Unknown1007(450000)
    teleportRelativeX(50000)
    setGravity(800)
    physicsYImpulse(20000)
    physicsXImpulse(4000)
    label(1)
    sprite('vr_donguri', 20)
    clearUponHandler(2)
    Unknown2001()
    Unknown1074(-48000)
    YAccel(-40)
    Unknown1019(5)
    Unknown3032()
    sprite('vr_donguri', 40)
    Unknown3004(-30)

@State
def DonguriShotB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(1000)
        AttackP2(80)
        hitstun(17)
        blockstun(16)
        AirUntechableTime(45)
        AirPushbackY(30000)
        Unknown2053(1)
        sendToLabelUpon(2, 1)
        sendToLabelUpon(54, 1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('vr_donguri', 32767)
    Unknown1074(30000)
    Unknown1007(450000)
    teleportRelativeX(50000)
    setGravity(800)
    physicsYImpulse(20000)
    physicsXImpulse(8000)
    label(1)
    sprite('vr_donguri', 20)
    clearUponHandler(2)
    Unknown2001()
    Unknown1074(-48000)
    YAccel(-40)
    Unknown1019(5)
    Unknown3032()
    sprite('vr_donguri', 40)
    Unknown3004(-30)
    
@State
def DonguriShotC():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(1000)
        AttackP2(80)
        hitstun(17)
        blockstun(16)
        AirUntechableTime(45)
        AirPushbackY(30000)
        Unknown2053(1)
        sendToLabelUpon(2, 1)
        sendToLabelUpon(54, 1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('vr_donguri', 32767)
    Unknown1074(30000)
    Unknown1007(450000)
    teleportRelativeX(50000)
    setGravity(800)
    physicsYImpulse(20000)
    physicsXImpulse(12000)
    label(1)
    sprite('vr_donguri', 20)
    clearUponHandler(2)
    Unknown2001()
    Unknown1074(-48000)
    YAccel(-40)
    Unknown1019(5)
    Unknown3032()
    sprite('vr_donguri', 40)
    Unknown3004(-30)

@State
def DonguriAssist():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(1000)
        AttackP1(70)
        hitstun(17)
        blockstun(16)
        Unknown11042(1)
        Unknown30040(1)
        AirUntechableTime(45)
        AirPushbackY(30000)
        Unknown2053(1)
        sendToLabelUpon(2, 1)
        sendToLabelUpon(54, 1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('vr_donguri', 32767)
    Unknown1074(30000)
    Unknown1007(450000)
    teleportRelativeX(50000)
    setGravity(800)
    physicsYImpulse(20000)
    physicsXImpulse(8000)
    label(1)
    sprite('vr_donguri', 20)
    clearUponHandler(2)
    Unknown2001()
    Unknown1074(-48000)
    YAccel(-40)
    Unknown1019(5)
    Unknown3032()
    sprite('vr_donguri', 40)
    Unknown3004(-30)

@State
def DonguriAssistB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(1000)
        AttackP1(70)
        hitstun(17)
        blockstun(16)
        Unknown11042(1)
        Unknown30040(1)
        AirUntechableTime(45)
        AirPushbackY(30000)
        Unknown2053(1)
        sendToLabelUpon(2, 1)
        sendToLabelUpon(54, 1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('vr_donguri', 32767)
    Unknown1074(30000)
    Unknown1007(450000)
    teleportRelativeX(50000)
    setGravity(800)
    physicsYImpulse(20000)
    physicsXImpulse(12000)
    label(1)
    sprite('vr_donguri', 20)
    clearUponHandler(2)
    Unknown2001()
    Unknown1074(-48000)
    YAccel(-40)
    Unknown1019(5)
    Unknown3032()
    sprite('vr_donguri', 40)
    Unknown3004(-30)
    
@State
def DonguriAssistC():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(1000)
        AttackP1(70)
        hitstun(17)
        blockstun(16)
        Unknown11042(1)
        Unknown30040(1)
        AirUntechableTime(45)
        AirPushbackY(30000)
        Unknown2053(1)
        sendToLabelUpon(2, 1)
        sendToLabelUpon(54, 1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('vr_donguri', 32767)
    Unknown1074(30000)
    Unknown1007(450000)
    teleportRelativeX(50000)
    setGravity(800)
    physicsYImpulse(20000)
    physicsXImpulse(16000)
    label(1)
    sprite('vr_donguri', 20)
    clearUponHandler(2)
    Unknown2001()
    Unknown1074(-48000)
    YAccel(-40)
    Unknown1019(5)
    Unknown3032()
    sprite('vr_donguri', 40)
    Unknown3004(-30)

@State
def EnergyBall():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(400)
        Unknown11092(1)
        Hitstop(0)
        blockstun(2)
        Unknown11001(5, 5, 6)
        AirPushbackX(2000)
        AirPushbackY(8000)
        PushbackX(2000)
        Unknown9016(1)
        Unknown11057(400)
        teleportRelativeX(160000)
        Unknown3033()
        Unknown4011(3)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
            if (SLOT_2 == 6):
                clearUponHandler(10)
                Unknown11057(1000)
                Unknown2003(1)
                sendToLabel(100)

        def upon_12():
            Unknown11056(4)

        def upon_43():
            if (SLOT_48 == 1045):
                sendToLabel(0)
            if (SLOT_48 == 1046):
                sendToLabel(1)
            if (SLOT_48 == 1047):
                sendToLabel(2)
            if (SLOT_48 == 1048):
                Unknown2003(1)
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1096(350)
    Unknown1099(10)
    Unknown3038(1)
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(20)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(30)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test00', 3)
    label(100)
    Unknown2003(1)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test00', 28)
    GFX_0('mkef_EnergyBall_Koware', -1)
    loopRest()
    ExitState()
    label(0)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(3)
    Damage(1500)
    AttackP1(80)
    AttackP2(75)
    Unknown11092(0)
    Hitstop(1)
    blockstun(16)
    Unknown11001(0, 12, 18)
    AirUntechableTime(40)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(20000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown11056(0)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    SLOT_51 = 1
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(85000)
    sprite('vr_shot_test01', 10)
    Unknown1019(80)
    Unknown1028(0)
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(1)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(4)
    Damage(1700)
    AttackP1(80)
    AttackP2(75)
    Unknown11092(0)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    Hitstop(1)
    blockstun(18)
    Unknown11001(0, 12, 18)
    AirUntechableTime(60)
    AirPushbackX(90000)
    AirPushbackY(35000)
    Unknown9215()
    Unknown11056(0)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    SLOT_51 = 1
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(95000)
    sprite('vr_shot_test01', 10)
    Unknown1019(80)
    Unknown1028(0)
    sprite('vr_shot_test01', 10)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(2)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(5)
    Damage(900)
    AttackP1(90)
    Unknown11092(0)
    Hitstop(1)
    Unknown11001(0, 12, 18)
    AirUntechableTime(35)
    AirHitstunAnimation(18)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown11056(0)
    FatalCounter(1)
    Unknown9324(12)
    Unknown9336(12)
    AirHitstunAfterWallbounce(50)
    Unknown9108(5)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(110000)
    Unknown1028(-4500)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    Unknown1019(50)
    Unknown1034(50)
    sprite('vr_shot_test01', 10)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(3)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(5)
    Damage(900)
    AttackP1(90)
    Unknown11092(0)
    Hitstop(1)
    AirUntechableTime(35)
    Unknown11001(0, 12, 18)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown11056(0)
    FatalCounter(1)
    AirHitstunAfterWallbounce(50)
    Unknown9108(5)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(110000)
    Unknown1028(-4500)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    Unknown1019(50)
    Unknown1034(50)
    sprite('vr_shot_test01', 10)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(100)
    if SLOT_51:
        _gotolabel(101)
    sprite('vr_shot_test01', 16)
    Unknown2003(1)
    Unknown1019(80)
    Unknown1028(0)
    ExitState()
    label(101)
    sprite('vr_shot_test01', 10)
    Unknown2003(1)
    Unknown1084(1)
    Unknown1028(0)
    Unknown1099(-50)
    Unknown21015('mkef_EnergyBall_Punch', 1049, 0)

@State
def EnergyBallEX():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(400)
        Unknown11092(1)
        Hitstop(0)
        blockstun(2)
        Unknown11001(5, 5, 6)
        AirPushbackX(2000)
        AirPushbackY(8000)
        PushbackX(2000)
        Unknown9016(1)
        Unknown11057(400)
        teleportRelativeX(160000)
        Unknown3033()
        Unknown4011(3)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
            if (SLOT_2 == 9):
                clearUponHandler(10)
                Unknown11057(1000)
                Unknown2003(1)
                sendToLabel(100)

        def upon_12():
            Unknown11056(4)

        def upon_43():
            if (SLOT_48 == 1045):
                sendToLabel(0)
            if (SLOT_48 == 1046):
                sendToLabel(1)
            if (SLOT_48 == 1047):
                sendToLabel(2)
            if (SLOT_48 == 1048):
                Unknown2003(1)
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1096(1000)
    Unknown1099(10)
    Unknown3038(1)
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(20)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(30)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test00', 3)
    label(100)
    Unknown2003(1)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test00', 28)
    GFX_0('mkef_EnergyBall_Koware', -1)
    loopRest()
    ExitState()
    label(0)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(3)
    Damage(1500)
    AttackP1(80)
    AttackP2(75)
    Unknown11092(0)
    Hitstop(1)
    blockstun(16)
    Unknown11001(0, 12, 18)
    AirUntechableTime(40)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(20000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown11056(0)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    SLOT_51 = 1
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(85000)
    sprite('vr_shot_test01', 10)
    Unknown1019(80)
    Unknown1028(0)
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(1)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(4)
    Damage(1700)
    AttackP1(80)
    AttackP2(75)
    Unknown11092(0)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    Hitstop(1)
    blockstun(18)
    Unknown11001(0, 12, 18)
    AirUntechableTime(60)
    AirPushbackX(90000)
    AirPushbackY(35000)
    Unknown9215()
    Unknown11056(0)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    SLOT_51 = 1
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(95000)
    sprite('vr_shot_test01', 10)
    Unknown1019(80)
    Unknown1028(0)
    sprite('vr_shot_test01', 10)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(2)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(5)
    Damage(900)
    AttackP1(90)
    Unknown11092(0)
    Hitstop(1)
    Unknown11001(0, 12, 18)
    AirUntechableTime(35)
    AirHitstunAnimation(18)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown11056(0)
    FatalCounter(1)
    Unknown9324(12)
    Unknown9336(12)
    AirHitstunAfterWallbounce(50)
    Unknown9108(5)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(110000)
    Unknown1028(-4500)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    Unknown1019(50)
    Unknown1034(50)
    sprite('vr_shot_test01', 10)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(3)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(5)
    Damage(900)
    AttackP1(90)
    Unknown11092(0)
    Hitstop(1)
    AirUntechableTime(35)
    Unknown11001(0, 12, 18)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown11056(0)
    FatalCounter(1)
    AirHitstunAfterWallbounce(50)
    Unknown9108(5)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(110000)
    Unknown1028(-4500)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    Unknown1019(50)
    Unknown1034(50)
    sprite('vr_shot_test01', 10)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(100)
    if SLOT_51:
        _gotolabel(101)
    sprite('vr_shot_test01', 16)
    Unknown2003(1)
    Unknown1019(80)
    Unknown1028(0)
    ExitState()
    label(101)
    sprite('vr_shot_test01', 10)
    Unknown2003(1)
    Unknown1084(1)
    Unknown1028(0)
    Unknown1099(-50)
    Unknown21015('mkef_EnergyBall_Punch', 1049, 0)

@State
def EnergyBallAssist():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(400)
        Unknown11092(1)
        Hitstop(0)
        blockstun(2)
        Unknown11001(5, 5, 6)
        AirPushbackX(2000)
        AirPushbackY(8000)
        PushbackX(2000)
        Unknown9016(1)
        Unknown11057(400)
        teleportRelativeX(160000)
        Unknown3033()
        Unknown4011(3)
        Unknown11042(1)
        Unknown30040(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
            if (SLOT_2 == 6):
                clearUponHandler(10)
                Unknown11057(1000)
                Unknown2003(1)
                sendToLabel(100)

        def upon_12():
            Unknown11056(4)

        def upon_43():
            if (SLOT_48 == 1045):
                sendToLabel(0)
            if (SLOT_48 == 1046):
                sendToLabel(1)
            if (SLOT_48 == 1047):
                sendToLabel(2)
            if (SLOT_48 == 1048):
                Unknown2003(1)
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1096(350)
    Unknown1099(10)
    Unknown3038(1)
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(20)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(30)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test00', 3)
    label(100)
    Unknown2003(1)
    GFX_0('mkef_EnergyBall', -1)
    sprite('vr_shot_test00', 28)
    GFX_0('mkef_EnergyBall_Koware', -1)
    loopRest()
    ExitState()
    label(0)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(3)
    Damage(2000)
    AttackP1(70)
    Unknown11092(0)
    Hitstop(1)
    blockstun(16)
    Unknown11001(0, 12, 18)
    AirUntechableTime(40)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(20000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown11056(0)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    SLOT_51 = 1
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(85000)
    sprite('vr_shot_test01', 10)
    Unknown1019(80)
    Unknown1028(0)
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(1)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(4)
    Damage(2000)
    AttackP1(70)
    Unknown11092(0)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    Hitstop(1)
    blockstun(18)
    Unknown11001(0, 12, 18)
    AirUntechableTime(60)
    AirPushbackX(90000)
    AirPushbackY(35000)
    Unknown9215()
    Unknown11056(0)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    SLOT_51 = 1
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(95000)
    sprite('vr_shot_test01', 10)
    Unknown1019(80)
    Unknown1028(0)
    sprite('vr_shot_test01', 10)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(2)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(5)
    Damage(900)
    AttackP1(90)
    Unknown11092(0)
    Hitstop(1)
    Unknown11001(0, 12, 18)
    AirUntechableTime(35)
    AirHitstunAnimation(18)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown11056(0)
    FatalCounter(1)
    Unknown9324(12)
    Unknown9336(12)
    AirHitstunAfterWallbounce(50)
    Unknown9108(5)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(110000)
    Unknown1028(-4500)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    Unknown1019(50)
    Unknown1034(50)
    sprite('vr_shot_test01', 10)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(3)
    sprite('vr_shot_test01', 1)
    Unknown23042()
    AttackLevel_(5)
    Damage(900)
    AttackP1(90)
    Unknown11092(0)
    Hitstop(1)
    AirUntechableTime(35)
    Unknown11001(0, 12, 18)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown11056(0)
    FatalCounter(1)
    AirHitstunAfterWallbounce(50)
    Unknown9108(5)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    Unknown3033()
    Unknown3038(1)
    GFX_0('mkef_EnergyBall', -1)
    Unknown1099(0)
    sprite('vr_shot_test01', 10)
    GFX_0('mkef_EnergyBall_Punch', -1)
    Unknown2003(0)
    RefreshMultihit()
    physicsXImpulse(110000)
    Unknown1028(-4500)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    Unknown1019(50)
    Unknown1034(50)
    sprite('vr_shot_test01', 10)
    Unknown1084(1)
    loopRest()
    gotoLabel(101)
    label(100)
    if SLOT_51:
        _gotolabel(101)
    sprite('vr_shot_test01', 16)
    Unknown2003(1)
    Unknown1019(80)
    Unknown1028(0)
    ExitState()
    label(101)
    sprite('vr_shot_test01', 10)
    Unknown2003(1)
    Unknown1084(1)
    Unknown1028(0)
    Unknown1099(-50)
    Unknown21015('mkef_EnergyBall_Punch', 1049, 0)

@State
def ChargeRing():

    def upon_IMMEDIATE():
        GFX_2('mkef_DriveChage_test')
        Unknown4007(2)
        Unknown4013(2)
        Unknown4010(2)
        Unknown23015(4)
        Unknown1096(1800)
        sendToLabelUpon(32, 22)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 10)
    Unknown3004(20)
    sprite('null', 32767)
    Unknown3004(0)
    Unknown3001(200)
    loopRest()
    label(22)
    sprite('null', 10)
    Unknown3004(-25)

@State
def DriveChargemc():

    def upon_IMMEDIATE():
        GFX_2('mkef_Drivemc')
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4013(2)
        Unknown23015(4)
        Unknown2054(1)
        sendToLabelUpon(44, 22)

        def upon_43():
            if (SLOT_48 == 1001):
                sendToLabel(22)
    sprite('null', 200)
    Unknown3001(255)
    loopRest()
    label(22)
    clearUponHandler(33)
    sprite('null', 8)
    Unknown3001(255)
    Unknown3004(-40)
    sprite('null', 1)
    Unknown3001(0)

@State
def DriveChargeAura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        Unknown1096(0)
        Unknown3026(-939507457)
        Unknown4010(3)

        def upon_43():
            if (SLOT_48 == 1021):
                clearUponHandler(43)
                sendToLabel(99)
        sendToLabelUpon(44, 99)
        Unknown2055(160)
    sprite('vref_env', 15)
    Unknown1099(200)
    sprite('vref_env', 200)
    Unknown1099(0)
    label(99)
    sprite('vref_env', 10)
    clearUponHandler(43)
    clearUponHandler(44)
    Unknown4010(0)
    Unknown4007(0)
    Unknown1099(-100)
    Unknown3004(-40)

@State
def DriveChargeAuraAir():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        Unknown3033()
        Unknown1096(0)
        Unknown3026(-939507457)

        def upon_43():
            if (SLOT_48 == 1022):
                clearUponHandler(43)
                sendToLabel(99)
        Unknown2055(120)
    sprite('vref_env', 15)
    Unknown1099(200)
    sprite('vref_env', 40)
    Unknown1099(0)
    loopRest()
    label(99)
    sprite('vref_env', 14)
    Unknown4007(0)
    Unknown1099(-100)
    Unknown3004(-20)

@State
def DriveChargeWind():

    def upon_IMMEDIATE():
        Unknown4003('mkef_wind.DIG', 'mkef_wind_motion_000.mmot')
        Unknown4015()
        Unknown4007(3)
        Unknown4010(3)
        Unknown3026(13172735)
        Unknown3033()
        Unknown1096(250)
        teleportRelativeX(16000)
        Unknown3001(255)
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 1024):
                sendToLabel(2)
            if (SLOT_48 == 1023):
                sendToLabel(1)
    sprite('null', 5)
    Unknown3004(20)
    Unknown1099(20)
    sprite('null', 32767)
    Unknown1099(0)
    loopRest()
    label(1)
    sprite('null', 5)
    Unknown4007(0)
    Unknown4010(0)
    Unknown3001(200)
    Unknown3004(-60)
    Unknown1059(10)
    label(2)
    sprite('null', 15)
    Unknown4007(0)
    Unknown4010(0)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1059(10)

@State
def DriveChargelightning():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('mkef_lightorange')
        Unknown4010(3)
        Unknown2054(1)
        Unknown1096(800)
    sprite('null', 30)

@State
def Lightblue():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        GFX_2('mkef_lightblue')
    sprite('null', 24)

@State
def ShinigPunch_D():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(1)
    sprite('vrmkef203_00', 2)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    Unknown3033()
    sprite('vrmkef203_01', 5)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3001(200)
    sprite('vrmkef203_02', 2)
    Unknown3004(-50)
    sprite('vrmkef203_02', 3)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)

@State
def ShinigPunchLvG_D():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(2)
    sprite('vrmkef203_00', 2)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    Unknown3033()
    sprite('vrmkef203_01', 5)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3001(200)
    sprite('vrmkef203_02', 2)
    Unknown3004(-50)
    sprite('vrmkef203_02', 3)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)

@State
def ShinigPunch_2D():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(1)
    sprite('vrmkef233_00', 5)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3001(200)
    Unknown3033()
    sprite('vrmkef233_01', 2)
    Unknown3004(-50)
    sprite('vrmkef233_01', 1)
    sprite('vrmkef233_01', 2)

@State
def ShinigPunchLvG_2D():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(2)
    sprite('vrmkef233_00', 5)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3001(200)
    Unknown3033()
    sprite('vrmkef233_01', 2)
    Unknown3004(-50)
    sprite('vrmkef233_01', 1)
    sprite('vrmkef233_01', 2)

@State
def ShinigPunch_5D():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(1)
    sprite('vrmkef254_00', 2)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    Unknown3033()
    sprite('vrmkef254_01', 5)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3001(200)
    sprite('vrmkef254_02', 3)
    Unknown3004(-50)
    sprite('vrmkef254_02', 3)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)

@State
def ShinigPunchLvG_5D():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(2)
    sprite('vrmkef254_00', 2)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    Unknown3033()
    sprite('vrmkef254_01', 5)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3001(200)
    sprite('vrmkef254_02', 3)
    Unknown3004(-50)
    sprite('vrmkef254_02', 3)
    GFX_0('Lightblue', 0)
    GFX_0('Lightblue', 1)

@State
def DriveLv1PunchefD():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv1Punchmc')
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 19)
    Unknown3004(-10)

@State
def DriveLv2PunchefD():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv2Punchmc')
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
        teleportRelativeX(-15000)
    sprite('null', 5)
    teleportRelativeX(20000)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 19)
    Unknown3004(-10)

@State
def DriveLv3PunchefD():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv3Punchmc')
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 19)
    Unknown3004(-8)
    ExitState()
    label(1)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 12)
    Unknown3004(-12)

@State
def DriveLvG_PunchefD():

    def upon_IMMEDIATE():
        GFX_2('mkef_LvGPunchmc')
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 19)
    Unknown3004(-8)

@State
def DriveLvG_PunchefD():

    def upon_IMMEDIATE():
        GFX_2('mkef_LvGPunchmc')
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 19)
    Unknown3004(-8)

@State
def DriveLv1Punchef2D():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv1Punchmc')
        Unknown3033()
        Unknown2054(1)
        Unknown4010(3)
        Unknown1072(270000)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-10)

@State
def DriveLv2Punchef2D():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv2Punchmc')
        Unknown3033()
        Unknown2054(1)
        Unknown4010(3)
        Unknown1072(270000)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-10)

@State
def DriveLv3Punchef2D():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv3Punchmc')
        Unknown3033()
        Unknown2054(1)
        Unknown4010(3)
        Unknown1072(270000)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-8)

@State
def DriveLvG_Punchef2D():

    def upon_IMMEDIATE():
        GFX_2('mkef_LvGPunchmc')
        Unknown3033()
        Unknown2054(1)
        Unknown4010(3)
        Unknown1072(270000)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-8)

@State
def DriveLv1PunchefPowerDunk():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv1Punchmc')
        Unknown3033()
        Unknown4010(3)
        Unknown2054(1)
        Unknown1072(80000)
    sprite('null', 5)
    Unknown4007(3)
    sprite('null', 3)
    Unknown4007(0)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-10)
    label(70)
    sprite('null', 8)
    Unknown4007(0)
    Unknown3004(-30)

@State
def DriveLv2PunchefPowerDunk():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv2Punchmc')
        Unknown3033()
        Unknown4010(3)
        Unknown2054(1)
        Unknown1072(80000)
    sprite('null', 5)
    Unknown4007(3)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown4007(0)
    Unknown3004(-10)

@State
def DriveLv3PunchefPowerDunk():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv3Punchmc')
        Unknown3033()
        Unknown4010(3)
        Unknown2054(1)
        Unknown1072(80000)
    sprite('null', 8)
    Unknown4007(3)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown4007(0)
    Unknown3004(-8)

@State
def DriveLvG_PunchefPowerDunk():

    def upon_IMMEDIATE():
        GFX_2('mkef_LvGPunchmc')
        Unknown3033()
        Unknown4010(3)
        Unknown2054(1)
        Unknown1072(80000)
    sprite('null', 8)
    Unknown4007(3)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown4007(0)
    Unknown3004(-8)

@State
def DriveLv1PunchefSyouryu2():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv1Punchmc')
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
        Unknown1072(290000)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-10)

@State
def DriveLv2PunchefSyouryu2():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv2Punchmc')
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
        Unknown1072(290000)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-10)

@State
def DriveLv3PunchefSyouryu2():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv3Punchmc')
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
        Unknown1072(290000)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-8)

@State
def DriveLv3PunchefSyouryu():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv3Punchmc')
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
        Unknown1072(270000)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-8)

@State
def DriveLv3PunchefSyouryu_Air():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv3Punchmc')
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown2054(1)
        Unknown1072(270000)
    sprite('null', 4)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-8)

@State
def mkef_hit_low():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_1('mkef_hit_low', -1)

@State
def mkef_hit_middle():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_1('mkef_hit_middle', -1)

@State
def mkef_hit_high():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_1('mkef_hit_high', -1)

@State
def mkef_hit_tailsp():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_1('mkef_hit_tailsp', -1)
    SFX_3('mkse_06')
    SFX_3('mkse_06')

@State
def mkef_hit_tailsp_nage():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_1('mkef_hit_tailsp_nage', -1)
    SFX_3('mkse_06')

@State
def mkef_hibana():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4007(2)
        GFX_2('mkef_hibana')
    sprite('null', 6)

@State
def mkef_EnergyBall():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4007(2)
        GFX_2('mkef_EnergyBall')
        Unknown1096(750)
    sprite('null', 6)

@State
def mkef_EnergyBall_Punch():

    def upon_IMMEDIATE():
        Unknown4013(2)
        Unknown4007(2)
        GFX_2('mkef_400energyball')
        Unknown3001(255)
        sendToLabelUpon(54, 11)

        def upon_43():
            if (SLOT_48 == 1049):
                sendToLabel(11)
    sprite('null', 30)
    sprite('null', 1)
    Unknown23090(25)
    loopRest()
    ExitState()
    label(11)
    sprite('null', 4)
    sprite('null', 5)
    Unknown3004(-50)
    sprite('null', 1)
    Unknown3001(0)
    loopRest()
    ExitState()

@State
def mkef_EnergyBall_Koware():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('mkef_400energyball')
        Unknown1096(600)
        Unknown3033()
    sprite('null', 8)
    Unknown7015()
    Unknown3004(-30)
    Unknown1099(10)
    sprite('null', 1)
    Unknown3001(0)

@State
def SyouryuUpper():

    def upon_IMMEDIATE():
        GFX_2('mkef_401upperpunch')
        Unknown4007(3)
    sprite('null', 8)
    Unknown1072(15000)
    sprite('null', 32)

@State
def PowerDunkAirwallLv2():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv2Puncheairwall')
        Unknown4010(3)
        Unknown4007(3)
    sprite('null', 75)
    Unknown1072(80000)

@State
def PowerDunkAirwallLv3():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv3Puncheairwall')
        Unknown4010(3)
        Unknown4007(3)
    sprite('null', 75)
    Unknown1072(80000)

@State
def PowerDunkAirwallLvG():

    def upon_IMMEDIATE():
        GFX_2('mkef_PuncheairwallLvG')
        Unknown4010(3)
        Unknown4007(3)
    sprite('null', 75)
    Unknown1072(80000)

@State
def BlockingPunchLv1():

    def upon_IMMEDIATE():
        GFX_2('mkef_403Lv1punch')
        Unknown4010(3)
        Unknown4009(3)
        Unknown4007(3)
    sprite('null', 5)
    Unknown1007(6000)
    sprite('null', 65)
    teleportRelativeX(75000)

@State
def BlockingPunchLv2():

    def upon_IMMEDIATE():
        GFX_2('mkef_403Lv2punch')
        Unknown4010(3)
        Unknown4009(3)
        Unknown4007(3)
    sprite('null', 5)
    Unknown1007(6000)
    sprite('null', 65)
    teleportRelativeX(75000)

@State
def BlockingPunchLv3():

    def upon_IMMEDIATE():
        GFX_2('mkef_403Lv3punch')
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 70)
    Unknown4007(3)
    Unknown1007(6000)
    teleportRelativeX(40000)

@State
def BlockingPunchLv3_G():

    def upon_IMMEDIATE():
        GFX_2('mkef_403Lv3punch_G')
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 70)
    Unknown4007(3)
    Unknown1007(6000)
    teleportRelativeX(40000)

@State
def BlockingSpeedLine():

    def upon_IMMEDIATE():
        GFX_2('mkef_403speedline00')
        Unknown4010(3)
        Unknown4007(3)
    sprite('null', 12)
    teleportRelativeY(200000)
    teleportRelativeX(-80000)

@State
def BlockingWind():

    def upon_IMMEDIATE():
        Unknown4003('mkef_screw.DIG', 'mkef_screw_motion_000.mmot')
        Unknown4015()
        Unknown4010(3)
        Unknown3033()
        Unknown1064(500)
        Unknown1056(750)
        Unknown3001(200)
    sprite('null', 3)
    Unknown3004(-15)
    teleportRelativeX(-300000)
    Unknown1007(-30000)
    physicsXImpulse(-10000)
    sprite('null', 21)
    physicsXImpulse(-10000)

@State
def EntryMant():

    def upon_IMMEDIATE():
        Unknown3032()
    sprite('vrmkef600m_00', 6)
    Unknown1007(10000)
    sprite('vrmkef600m_01', 3)
    Unknown1007(180000)
    sprite('vrmkef600m_01', 3)
    Unknown1007(100000)

@State
def GuardCrash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(1)
        Unknown3033()
    sprite('vrmkef414_00', 4)
    GFX_0('mkef_414Lv3airwall', 0)
    sprite('vrmkef414_01', 4)
    sprite('vrmkef414_02', 4)
    sprite('vrmkef414_03', 4)

@State
def mkef_414Lv3airwall():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('mkef_414')
    sprite('null', 30)
    Unknown1072(90000)

@State
def mkef413_lv1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(1)
        Unknown3033()
    sprite('vrmkef413_00', 1)
    GFX_0('DriveLv1PunchefD413', 0)
    Unknown3038(1)

@State
def DriveLv1PunchefD413():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        GFX_2('mkef_Lv1Punchmc')
        Unknown2054(1)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 19)
    Unknown3004(-10)

@State
def mkef413_lv2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(1)
        Unknown3033()
    sprite('vrmkef413_00', 1)
    GFX_0('DriveLv2PunchefD413', 0)
    Unknown3038(1)

@State
def DriveLv2PunchefD413():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        GFX_2('mkef_Lv2Punchmc')
        Unknown2054(1)
    sprite('null', 5)
    teleportRelativeX(20000)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 19)
    Unknown3004(-10)

@State
def mkef413_lv3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(1)
        Unknown3033()
    sprite('vrmkef413_00', 2)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    GFX_0('DriveLv3PunchefD413', 0)
    sprite('vrmkef413_01', 2)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3001(200)
    sprite('vrmkef413_02', 2)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3004(-50)

@State
def DriveLv3PunchefD413():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('mkef_Lv3Punchmc')
        Unknown4010(3)
        Unknown2054(1)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 19)
    Unknown3004(-8)

@State
def mkef413_lvG():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4061(2)
        Unknown3033()
    sprite('vrmkef413_00', 2)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    GFX_0('DriveLvG_PunchefD413', 0)
    sprite('vrmkef413_01', 2)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3001(200)
    sprite('vrmkef413_02', 2)
    GFX_0('Lightblue', 1)
    GFX_0('Lightblue', 2)
    Unknown3004(-50)

@State
def DriveLvG_PunchefD413():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('mkef_LvGPunchmc')
        Unknown4010(3)
        Unknown2054(1)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    Unknown4007(0)
    sprite('null', 19)
    Unknown3004(-8)

@State
def Drive412Lv1():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv1Punchmc')
        Unknown4010(3)
        Unknown2054(1)
        Unknown1072(-60000)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-10)

@State
def Drive412Lv2():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv2Punchmc')
        Unknown4010(3)
        Unknown2054(1)
        Unknown1072(-60000)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-10)

@State
def Drive412Lv3():

    def upon_IMMEDIATE():
        GFX_2('mkef_Lv3Punchmc')
        Unknown4010(3)
        Unknown2054(1)
        Unknown1072(-60000)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-8)

@State
def Drive412LvG():

    def upon_IMMEDIATE():
        GFX_2('mkef_LvGPunchmc')
        Unknown4010(3)
        Unknown2054(1)
        Unknown1072(-60000)
    sprite('null', 8)
    sprite('null', 3)
    Unknown3004(-25)
    sprite('null', 19)
    Unknown3004(-8)

@State
def Drive412Lv1_hit():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('mkef_412Lv1')
        Unknown2054(1)
        Unknown21010(1)
    sprite('null', 60)
    Unknown1072(32000)

@State
def Drive412Lv2_hit():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('mkef_412Lv2')
        Unknown2054(1)
        Unknown21010(1)
    sprite('null', 60)
    Unknown1072(32000)

@State
def Drive412Lv3_hit():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('mkef_412Lv3')
        Unknown2054(1)
        Unknown21010(1)
    sprite('null', 60)
    Unknown1072(32000)

@State
def Drive412LvG_hit():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('mkef_412LvG')
        Unknown2054(1)
        Unknown21010(1)
    sprite('null', 60)
    Unknown1072(32000)

@State
def mkef_415_punch():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown3033()
        Unknown4003('mkef_415', '')
        Unknown4015()
        Unknown1096(1250)
    sprite('null', 16)
    GFX_1('mkef_415', -1)
    Unknown3004(-16)

@State
def mkef_415_atk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Damage(1500)
        Hitstop(12)
        hitstun(20)
        AirUntechableTime(22)
        AttackP1(80)
        AttackP2(80)
        GroundedHitstunAnimation(0)
        AirHitstunAnimation(1)
        AirPushbackX(30000)
        AirPushbackY(11666)
        PushbackX(50000)
        Unknown11109('01000000')
        Unknown23078(1)
        MinimumDamagePct(10)
        Unknown30065(0)

        def upon_43():
            if (SLOT_48 == 1041):
                Unknown2003(1)

        def upon_3():
            Unknown48(25, 2, 51, 22, 2, 23)
            if (SLOT_51 == 0):
                Unknown11025(1)
            else:
                Unknown11025(0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21015('SiriusJolt', 1041, 0)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('mk415_10_dmyAtk', 3)

@State
def BigPunch_SE():

    def upon_IMMEDIATE():
        Unknown2054(0)
        Unknown4009(3)
        Unknown2055(50)
    label(0)
    sprite('null', 4)
    SFX_0('019_quake_0')
    ScreenShake(1000, 0)
    loopRest()
    gotoLabel(0)

@State
def mk430cutin_up():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown4009(3)
        Unknown4061(0)
        Unknown3032()
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(-580000)
        Unknown1001(640000)
    sprite('mk430cutin_00', 5)
    Unknown3001(0)
    Unknown3004(25)
    sprite('mk430cutin_01', 5)
    sprite('mk430cutin_00', 7)
    Unknown3004(0)
    Unknown3001(255)
    sprite('mk430cutin_01', 7)
    sprite('mk430cutin_00', 7)
    sprite('mk430cutin_01', 7)
    sprite('mk430cutin_00', 7)
    sprite('mk430cutin_01', 7)
    sprite('mk430cutin_00', 5)
    Unknown3004(-25)
    sprite('mk430cutin_01', 5)

@State
def mkef_430circlering_lv1():

    def upon_IMMEDIATE():
        GFX_2('mkef_430circlering')
        Unknown3033()
        Unknown4010(3)
        Unknown2054(1)
        Unknown1096(1000)
        Unknown1007(20000)
    sprite('null', 45)
    sprite('null', 30)
    Unknown3004(-20)

@State
def mkef_430circlering_lv2():

    def upon_IMMEDIATE():
        GFX_2('mkef_430circlering')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1110)
        Unknown1007(20000)
    sprite('null', 45)
    sprite('null', 30)
    Unknown3004(-20)

@State
def mkef_430circlering_lv3():

    def upon_IMMEDIATE():
        GFX_2('mkef_430circlering')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1220)
        Unknown1007(20000)
    sprite('null', 50)
    sprite('null', 35)
    Unknown3004(-20)

@State
def mkef_430bigpunch_lv2():

    def upon_IMMEDIATE():
        GFX_2('mkef_430bigpunch04')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1000)
        teleportRelativeX(800000)
    sprite('null', 30)
    sprite('null', 40)
    Unknown3004(-20)

@State
def mkef_430bigpunch_lv3():

    def upon_IMMEDIATE():
        GFX_2('mkef_430bigpunch')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1220)
        teleportRelativeX(800000)
    sprite('null', 30)
    sprite('null', 40)
    Unknown3004(-20)

@State
def mkef_430bigpunch_lvG():

    def upon_IMMEDIATE():
        GFX_2('mkef_430bigpunch')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(2020)
        teleportRelativeX(800000)
    sprite('null', 30)
    sprite('null', 40)
    Unknown3004(-20)

@State
def mk430cutin_lv1():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(80)
        AttackP2(79)
        MinimumDamagePct(25)
        AirUntechableTime(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        Unknown11001(0, 20, 20)
        Unknown9015(1)
        StarterRating(2)
        Unknown23015(15)
        Unknown4061(1)
        Unknown3032()
        Unknown1096(820)
        teleportRelativeX(-15000)
        Unknown1007(-5000)
        if Unknown42('ta'):
            Unknown23015(1)
    sprite('null', 1)
    GFX_0('mk430effLv1', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(30000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(35000)
    sprite('mk430_punchlv01', 4)
    physicsXImpulse(0)
    teleportRelativeX(25000)
    sprite('mk430_punchlv01', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv01', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv01', 15)
    StartMultihit()
    Unknown3004(-25)
    Unknown3033()

@State
def mk430effLv1():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1056(1400)
        Unknown1064(1600)
        teleportRelativeX(200000)
        Unknown3001(0)
        Unknown3033()
        Unknown23015(15)
        if Unknown42('ta'):
            Unknown23015(1)
    sprite('vrmkef430add_00ex00', 4)
    Unknown4007(2)
    Unknown3004(30)
    sprite('vrmkef430add_00', 23)
    Unknown3001(160)
    Unknown3004(0)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    Unknown4007(0)
    Unknown3004(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk430cutin_lv2():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(4)
        Damage(4500)
        AttackP2(60)
        MinimumDamagePct(30)
        AirUntechableTime(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        Unknown11001(0, 20, 20)
        Unknown9015(1)
        Unknown23015(15)
        Unknown4061(1)
        Unknown3032()
        Unknown1096(980)
        teleportRelativeX(-160000)
        Unknown1007(400000)
    sprite('null', 1)
    GFX_0('mkef_430bigpunch_lv2', -1)
    GFX_0('mk430effLv2', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(30000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(35000)
    sprite('mk430_punchlv02', 4)
    physicsXImpulse(0)
    teleportRelativeX(35000)
    sprite('mk430_punchlv02', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv02', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv02', 15)
    StartMultihit()
    Unknown3004(-25)
    Unknown3033()

@State
def mk430effLv2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1056(1700)
        Unknown1064(2000)
        teleportRelativeX(220000)
        Unknown3001(0)
        Unknown3033()
        Unknown23015(15)
    sprite('vrmkef430add_00ex00', 5)
    Unknown4007(2)
    Unknown3004(30)
    sprite('vrmkef430add_00', 22)
    Unknown3001(180)
    Unknown3004(0)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    Unknown4007(0)
    Unknown3004(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk430cutin_lv3():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(4800)
        AttackP2(60)
        MinimumDamagePct(32)
        AirUntechableTime(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        Unknown11001(0, 20, 20)
        Unknown9015(1)
        Unknown23015(15)
        Unknown4061(1)
        Unknown3032()
        Unknown1096(1000)
        teleportRelativeX(45000)
        Unknown1007(405000)
    sprite('null', 1)
    GFX_0('mkef_430bigpunch_lv3', -1)
    GFX_0('mk430effLv3', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(30000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(35000)
    sprite('mk430_punchlv03', 1)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03', 4)
    physicsXImpulse(0)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv03', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv03', 15)
    StartMultihit()
    Unknown3004(-15)
    Unknown3033()

@State
def mk430cutin_lv3Duo():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(2000)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirUntechableTime(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        Unknown11001(0, 20, 20)
        Unknown9015(1)
        Unknown23015(15)
        Unknown4061(1)
        Unknown3032()
        Unknown1096(1000)
        teleportRelativeX(45000)
        Unknown1007(405000)
        Unknown2054(1)
    sprite('null', 1)
    GFX_0('mkef_430bigpunch_lv3', -1)
    GFX_0('mk430effLv3', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(30000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(35000)
    sprite('mk430_punchlv03duo', 1)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03duo', 4)
    physicsXImpulse(0)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03duo', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv03duo', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv03duo', 15)
    StartMultihit()
    Unknown3004(-15)
    Unknown3033()

@State
def mk430effLv3():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1096(2020)
        teleportRelativeX(100000)
        Unknown3001(0)
        Unknown3033()
        Unknown23015(15)
        if Unknown42('ta'):
            Unknown23015(1)
    sprite('vrmkef430add_00ex00', 5)
    Unknown4007(2)
    Unknown3004(30)
    sprite('vrmkef430add_00', 22)
    Unknown3001(200)
    Unknown3004(0)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    Unknown4007(0)
    Unknown3004(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk430cutin_lvG():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(5800)
        AttackP2(60)
        MinimumDamagePct(33)
        AirUntechableTime(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        Unknown11001(0, 20, 20)
        Unknown9015(1)
        Unknown23015(15)
        Unknown4061(2)
        Unknown3032()
        Unknown1096(1000)
        teleportRelativeX(45000)
        Unknown1007(405000)
        Unknown3033()
    sprite('null', 1)
    GFX_0('mkef_430bigpunch_lvG', -1)
    GFX_0('mk430effLvG', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(30000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(35000)
    sprite('mk430_punchlv03', 1)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03', 4)
    physicsXImpulse(0)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv03', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv03', 15)
    StartMultihit()
    Unknown3004(-15)

@State
def mk430cutin_lvGDuo():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(5)
        Damage(2500)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirUntechableTime(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        Unknown11001(0, 20, 20)
        Unknown9015(1)
        Unknown23015(15)
        Unknown4061(2)
        Unknown3032()
        Unknown1096(1000)
        teleportRelativeX(45000)
        Unknown1007(405000)
        Unknown3033()
        Unknown2054(1)
    sprite('null', 1)
    GFX_0('mkef_430bigpunch_lvG', -1)
    GFX_0('mk430effLvG', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(30000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(35000)
    sprite('mk430_punchlv03duo', 1)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03duo', 4)
    physicsXImpulse(0)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03duo', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv03duo', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv03duo', 15)
    StartMultihit()
    Unknown3004(-15)

@State
def mk430effLvG():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(2)
        Unknown1096(2020)
        teleportRelativeX(100000)
        Unknown3001(0)
        Unknown3033()
        Unknown23015(15)
        if Unknown42('ta'):
            Unknown23015(1)
    sprite('vrmkef430add_00ex00', 5)
    Unknown4007(2)
    Unknown3004(30)
    sprite('vrmkef430add_00', 22)
    Unknown3004(0)
    Unknown3001(150)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    Unknown4007(0)
    Unknown3004(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mkef_circle_small():

    def upon_IMMEDIATE():
        Unknown4003('mkef_circle.DIG', 'mkef_circle_motion_000.mmot')
        Unknown4015()
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(2)
        Unknown3033()
        Unknown1096(640)
        Unknown3001(0)
    sprite('null', 5)
    Unknown3004(50)
    sprite('null', 25)
    Unknown3001(255)
    sprite('null', 20)
    Unknown3004(-15)

@State
def mkef_circle_middle():

    def upon_IMMEDIATE():
        Unknown4003('mkef_circle.DIG', 'mkef_circle_motion_000.mmot')
        Unknown4015()
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(2)
        Unknown3033()
        Unknown1096(720)
        Unknown3001(0)
    sprite('null', 5)
    Unknown3004(50)
    sprite('null', 25)
    Unknown3001(255)
    sprite('null', 20)
    Unknown3004(-15)

@State
def mkef_circle_large():

    def upon_IMMEDIATE():
        Unknown4003('mkef_circle.DIG', 'mkef_circle_motion_000.mmot')
        Unknown4015()
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(2)
        Unknown3033()
        Unknown1096(820)
        Unknown3001(0)
    sprite('null', 5)
    Unknown3004(50)
    sprite('null', 25)
    Unknown3001(255)
    sprite('null', 20)
    Unknown3004(-15)

@State
def mkef_mahojin_small():

    def upon_IMMEDIATE():
        Unknown4003('mkef_mahojin.DIG', 'mkef_mahojin_motion_000.mmot')
        Unknown4015()
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(2)
        Unknown3033()
        Unknown1096(660)
        Unknown3001(0)
    sprite('null', 5)
    Unknown3004(50)
    sprite('null', 30)
    Unknown3001(255)
    sprite('null', 30)
    Unknown3004(-10)
    sprite('null', 60)

@State
def mkef_mahojin_middle():

    def upon_IMMEDIATE():
        Unknown4003('mkef_mahojin.DIG', 'mkef_mahojin_motion_000.mmot')
        Unknown4015()
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(2)
        Unknown3033()
        Unknown1096(760)
        Unknown3001(0)
    sprite('null', 5)
    Unknown3004(50)
    sprite('null', 35)
    Unknown3001(255)
    sprite('null', 35)
    Unknown3004(-10)
    sprite('null', 60)

@State
def mkef_mahojin_large():

    def upon_IMMEDIATE():
        Unknown4003('mkef_mahojin.DIG', 'mkef_mahojin_motion_000.mmot')
        Unknown4015()
        Unknown4010(3)
        Unknown2054(1)
        Unknown23015(2)
        Unknown3033()
        Unknown1096(840)
        Unknown3001(0)
    sprite('null', 5)
    Unknown3004(50)
    sprite('null', 38)
    Unknown3001(255)
    sprite('null', 38)
    Unknown3004(-10)
    sprite('null', 60)

@State
def mk431cutin_up():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3032()
        Unknown2054(1)
        Unknown23032(50)
        teleportRelativeY(1825000)

        def upon_43():
            if (SLOT_48 == 1064):
                sendToLabel(23)
    sprite('mk431cutin_00', 5)
    Unknown1096(1000)
    Unknown3001(0)
    Unknown3004(25)
    sprite('mk431cutin_01', 5)
    sprite('mk431cutin_00', 7)
    Unknown3004(0)
    Unknown3001(255)
    sprite('mk431cutin_01', 7)
    sprite('mk431cutin_00', 7)
    sprite('mk431cutin_01', 7)
    sprite('mk431cutin_00', 7)
    sprite('mk431cutin_01', 7)
    sprite('mk431cutin_00', 5)
    Unknown3004(-25)
    sprite('mk431cutin_01', 5)
    sprite('mk431cutin_01', 1)
    Unknown3001(0)
    loopRest()
    label(23)
    sprite('mk431cutin_00', 5)
    Unknown3004(-50)
    sprite('mk431cutin_01', 1)
    Unknown3001(0)

@State
def mk431cutin_punchLv1():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(2)
        Unknown4061(1)
        Unknown3032()
        Unknown1007(595000)
        Unknown1072(10000)
        Unknown1096(750)
    sprite('mk431cutin_02', 6)
    GFX_0('mk431effLv1', -1)
    Unknown3001(0)
    Unknown3004(35)
    sprite('mk431cutin_02', 37)
    Unknown3004(0)
    Unknown3001(255)
    sprite('mk431cutin_02', 3)
    physicsYImpulse(-40000)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    Unknown3004(-35)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 21)
    sprite('mk431cutin_02', 1)
    Unknown3001(0)

@State
def mk431effLv1():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1096(1800)
        Unknown1072(90000)
        Unknown3001(128)
        Unknown3033()
    sprite('vrmkef430add_00', 45)
    Unknown1007(-30000)
    Unknown4007(2)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    Unknown4007(0)
    Unknown3004(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk431cutin_punchLv2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(2)
        Unknown4061(1)
        Unknown3032()
        Unknown1007(595000)
        Unknown1096(850)
        Unknown1072(10000)
    sprite('mk431cutin_02', 6)
    GFX_0('mk431effLv2', -1)
    Unknown3001(0)
    Unknown3004(35)
    sprite('mk431cutin_02', 35)
    Unknown3004(0)
    Unknown3001(255)
    sprite('mk431cutin_02', 3)
    physicsYImpulse(-60000)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    Unknown3004(-30)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 21)
    sprite('mk431cutin_02', 1)
    Unknown3001(0)

@State
def mk431effLv2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1096(2000)
        Unknown1072(90000)
        Unknown3001(200)
        Unknown3033()
    sprite('vrmkef430add_00', 45)
    Unknown4007(2)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    Unknown4007(0)
    Unknown3004(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk431cutin_punchLv3():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(2)
        Unknown4061(1)
        Unknown3032()
        Unknown1007(640000)
        Unknown1096(950)
        Unknown1072(10000)
    sprite('mk431cutin_02', 6)
    GFX_0('mk431effLv3', -1)
    Unknown3001(0)
    Unknown3004(35)
    sprite('mk431cutin_02', 35)
    Unknown3004(0)
    Unknown3001(255)
    sprite('mk431cutin_02', 3)
    physicsYImpulse(-60000)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    Unknown3004(-30)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 21)
    sprite('mk431cutin_02', 1)
    Unknown3001(0)

@State
def mk431effLv3():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1096(2200)
        Unknown1072(90000)
        Unknown3001(200)
        Unknown3033()
    sprite('vrmkef430add_00', 45)
    Unknown4007(2)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    Unknown4007(0)
    Unknown3004(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk431cutin_punchLvG():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(2)
        Unknown4061(2)
        Unknown3032()
        Unknown1007(640000)
        Unknown1096(950)
        Unknown1072(10000)
    sprite('mk431cutin_02', 6)
    GFX_0('mk431effLvG', -1)
    Unknown3001(0)
    Unknown3004(35)
    sprite('mk431cutin_02', 35)
    Unknown3004(0)
    Unknown3001(255)
    sprite('mk431cutin_02', 3)
    physicsYImpulse(-60000)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    Unknown3004(-30)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 21)
    sprite('mk431cutin_02', 1)
    Unknown3001(0)

@State
def mk431effLvG():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(2)
        Unknown1096(2200)
        Unknown1072(90000)
        Unknown3001(150)
        Unknown3033()
    sprite('vrmkef430add_00', 45)
    Unknown4007(2)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    Unknown4007(0)
    Unknown3004(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk431dummy():

    def upon_IMMEDIATE():
        Unknown3032()
    sprite('mk431_18', 20)

@State
def mkef_431Lv1first():

    def upon_IMMEDIATE():
        GFX_2('mkef_431Lv1first')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1000)
    sprite('null', 80)
    Unknown1072(27000)

@State
def mkef_431Lv2first():

    def upon_IMMEDIATE():
        GFX_2('mkef_431Lv2first')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1100)
    sprite('null', 80)
    Unknown1072(27000)

@State
def mkef_431Lv3first():

    def upon_IMMEDIATE():
        GFX_2('mkef_431Lv3first')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1400)
    sprite('null', 80)
    Unknown1072(27000)

@State
def mkef_431Lv1secondtame():

    def upon_IMMEDIATE():
        GFX_2('mkef_431Lv1secondtame')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(900)
    sprite('null', 80)

@State
def mkef_431Lv2secondtame():

    def upon_IMMEDIATE():
        GFX_2('mkef_431Lv2secondtame')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1100)
    sprite('null', 80)

@State
def mkef_431Lv3secondtame():

    def upon_IMMEDIATE():
        GFX_2('mkef_431Lv3secondtame')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1400)
    sprite('null', 80)

@State
def mkef_431_2ndsub_back():

    def upon_IMMEDIATE():
        GFX_2('mkef_431_2nd000_back')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1100)
    sprite('null', 80)

@State
def mkef_431Lv1second():

    def upon_IMMEDIATE():
        GFX_2('mkef_431Lv1second')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1200)
    sprite('null', 80)

@State
def mkef_431Lv2second():

    def upon_IMMEDIATE():
        GFX_2('mkef_431Lv2second')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1400)
    sprite('null', 80)

@State
def mkef_431Lv3second():

    def upon_IMMEDIATE():
        GFX_2('mkef_431Lv3second')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(1800)
    sprite('null', 80)

@State
def mkef_jumpsmoke11():

    def upon_IMMEDIATE():
        GFX_2('mkef_jumpsmoke02')
        Unknown2054(1)
        Unknown1096(800)
    sprite('null', 40)

@State
def mkef_jumpsmoke12():

    def upon_IMMEDIATE():
        GFX_2('mkef_jumpsmoke02')
        Unknown2054(1)
        Unknown1096(1100)
    sprite('null', 40)

@State
def mkef_jumpsmoke13():

    def upon_IMMEDIATE():
        GFX_2('mkef_jumpsmoke02')
        Unknown2054(1)
        Unknown1096(1400)
    sprite('null', 40)

@State
def mkef_jumpsmoke21():

    def upon_IMMEDIATE():
        GFX_2('mkef_jumpsmoke')
        Unknown2054(1)
        Unknown1096(800)
    sprite('null', 40)

@State
def mkef_jumpsmoke22():

    def upon_IMMEDIATE():
        GFX_2('mkef_jumpsmoke')
        Unknown2054(1)
        Unknown1096(1100)
    sprite('null', 40)

@State
def mkef_jumpsmoke23():

    def upon_IMMEDIATE():
        GFX_2('mkef_jumpsmoke')
        Unknown2054(1)
        Unknown1096(1400)
    sprite('null', 40)

@State
def mk431_dmyatk():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        AirPushbackX(10)
        AirPushbackY(600)
        YImpluseBeforeWallbounce(4)
        AirUntechableTime(150)
        Hitstop(0)
        Unknown11064(1)
        Unknown11023(1)
        Unknown11072(1, 0, 0)
        Unknown30048(1)
        Unknown11062(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        AttackAttributes(0, 0, 0, 0, 0)
        Unknown11050(5, '')
        Unknown11069('ShinSyouryu3')
        Unknown2053(1)
        Unknown2034(1)
        Unknown1086(3)
        teleportRelativeY(1450000)
        teleportRelativeX(50000)
    sprite('mk431_dmyatk', 20)

@State
def mk431_dmyatkOD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        AirPushbackX(10)
        AirPushbackY(600)
        YImpluseBeforeWallbounce(4)
        AirUntechableTime(150)
        Hitstop(0)
        Unknown11064(1)
        Unknown11023(1)
        Unknown11072(1, 0, 0)
        Unknown30048(1)
        Unknown11062(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        AttackAttributes(0, 0, 0, 0, 0)
        Unknown11050(5, '')
        Unknown11069('ShinSyouryu3_OD')
        Unknown2053(1)
        Unknown2034(1)
        Unknown1086(3)
        teleportRelativeY(1450000)
        teleportRelativeX(50000)
    sprite('mk431_dmyatk', 20)

@State
def mk450_energy():

    def upon_IMMEDIATE():
        GFX_2('mk450_energy')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(700)
    sprite('null', 5)
    Unknown3004(50)
    sprite('null', 30)
    Unknown3001(255)
    sprite('null', 30)
    Unknown3004(-10)
    sprite('null', 60)

@State
def mk450_tame():

    def upon_IMMEDIATE():
        GFX_2('mk450_tame2')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(600)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 1072):
                sendToLabel(80)
    sprite('null', 5)
    Unknown3004(50)
    sprite('null', 115)
    Unknown3001(255)
    label(80)
    sprite('null', 10)
    Unknown3004(-25)
    sprite('null', 1)
    Unknown3001(0)

@State
def mk450_syogeki():

    def upon_IMMEDIATE():
        GFX_2('mk450_syogeki')
        Unknown3033()
        Unknown4007(3)
        Unknown2054(1)
        Unknown1096(1400)
    sprite('null', 12)
    Unknown3001(255)
    sprite('null', 10)
    Unknown3004(-30)
    sprite('null', 1)
    Unknown3001(0)

@State
def mk450_impact():

    def upon_IMMEDIATE():
        GFX_2('mk450_impact')
        Unknown3033()
        Unknown4007(3)
        Unknown2054(1)
        Unknown4010(3)
        Unknown1096(800)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 1073):
                sendToLabel(81)
    sprite('null', 5)
    Unknown3004(50)
    sprite('null', 115)
    Unknown3001(255)
    label(81)
    sprite('null', 10)
    Unknown3004(-35)
    sprite('null', 1)
    Unknown3001(0)

@State
def mk450_bunsan():

    def upon_IMMEDIATE():
        GFX_2('mk450_bunsan')
        Unknown3033()
        Unknown4007(3)
        Unknown2054(1)
        Unknown4010(3)
        Unknown1096(1000)
    sprite('null', 60)

@State
def mk450_footef():

    def upon_IMMEDIATE():
        GFX_2('mk450_footef')
        Unknown3033()
        Unknown1096(1000)
    sprite('null', 27)
    Unknown3001(255)
    sprite('null', 10)
    Unknown3004(-30)
    sprite('null', 1)
    Unknown3001(0)

@State
def mk450_bgef():

    def upon_IMMEDIATE():
        GFX_2('mkef_450bg')
        Unknown3033()
        Unknown3001(0)
        Unknown1007(-50000)
    sprite('null', 9)
    Unknown3004(25)
    sprite('null', 174)
    Unknown3001(255)

@State
def mk450_hibana():

    def upon_IMMEDIATE():
        GFX_2('mkef_450hibana')
        Unknown3033()
    sprite('null', 164)

@State
def mk450cutin_tame():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4061(0)
        Unknown3033()
        Unknown1007(290000)
    sprite('mk450cutin_00', 6)
    Unknown3001(0)
    Unknown3004(50)
    sprite('mk450cutin_01', 6)
    Unknown3001(255)
    sprite('mk450cutin_02', 7)
    sprite('mk450cutin_03', 6)
    sprite('mk450cutin_03', 6)
    Unknown3004(-35)

@State
def mk450cutin_impact():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4061(1)
        Unknown3032()
        Unknown1007(245000)
    sprite('mk450cutin_04', 4)
    GFX_0('mk450_impactline', 0)
    sprite('mk450cutin_05', 4)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    GFX_0('mk450_kirari', 0)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)

@State
def mk450cutin_impact_small():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown4009(3)
        Unknown4007(3)
        Unknown4061(0)
        Unknown3032()
        teleportRelativeX(-390000)
        Unknown1007(-89500)
    sprite('mk450cutin_06', 4)
    sprite('mk450cutin_07', 4)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)

@State
def mk450_impactline():

    def upon_IMMEDIATE():
        GFX_2('mk450_impactline')
        Unknown3033()
        Unknown2054(1)
        Unknown1096(500)
    sprite('null', 80)
    Unknown3001(255)
    sprite('null', 10)
    Unknown3004(-30)
    sprite('null', 1)
    Unknown3001(0)

@State
def mk450_kirari():

    def upon_IMMEDIATE():
        GFX_2('mk450_kirari')
        Unknown3033()
        Unknown1096(750)
    sprite('null', 50)

@State
def AstWhite():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        Unknown4007(3)
        teleportRelativeY(340000)
        Unknown1096(10000)
        Unknown3033()
        Unknown3001(0)
    sprite('vr_white', 8)
    Unknown3004(30)
    sprite('vr_white', 15)
    sprite('vr_white', 8)
    Unknown3001(240)
    Unknown3004(-30)

@State
def mk450_kamifubuki():

    def upon_IMMEDIATE():
        GFX_2('mk450_kamifubuki')
        Unknown3032()
    sprite('null', 600)

@State
def AstralHeatKillObject():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11064(3)
        Damage(11080)
        MinimumDamagePct(100)
        Unknown11056(3)
        Unknown11071(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(10000)
        Unknown11023(1)
        Unknown1086(22)
        Unknown3038(1)
        Unknown1096(3000)
    sprite('vr_donguri', 1)
    Unknown1086(22)
    sprite('vr_donguri', 1)
    Unknown1086(22)
    sprite('vr_donguri', 1)
    Unknown1086(22)
    sprite('vr_donguri', 1)
    Unknown1086(22)

@State
def bmk_AH_ray():

    def upon_IMMEDIATE():
        Unknown23057(50)
        Unknown23058(50)
        Unknown4054(4)
        Unknown23067('ef_speedline_wt')
    sprite('null', 200)

@State
def bmk_AH_ray2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4008(2)
        Unknown23032(50)
        teleportRelativeX(1790000)
        teleportRelativeY(580000)
        Unknown1096(1250)
        Unknown4054(4)
        Unknown23067('ef_speedline_bk')
    sprite('null', 120)

@State
def RLAstLockmc():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4054(5)
        Unknown23067('rlef_ashlock_mc')
        Unknown4010(3)
    sprite('null', 120)
    Unknown3001(0)
    Unknown3004(2)
    sprite('null', 32767)
    Unknown3004(0)

@State
def RLAstLockAura():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown23067('rlef_ashlock_aura')
        Unknown4010(3)
    sprite('null', 120)
    Unknown3001(0)
    Unknown3004(2)
    sprite('null', 32767)
    Unknown3004(0)

@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown20000(1)
        Unknown20003(1)
        Unknown4007(22)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        sendToLabelUpon(36, 4)

        def upon_56():
            Unknown20000(0)
            Unknown20001(0)
            Unknown20003(0)
    sprite('null', 25)
    sprite('null', 300)
    Unknown4007(0)
    ExitState()
    label(0)
    sprite('null', 15)
    Unknown20001(1)
    physicsYImpulse(100000)
    sprite('null', 300)
    Unknown1084(1)
    ExitState()
    label(1)
    sprite('null', 5)
    sprite('null', 15)
    physicsYImpulse(-100000)
    sprite('null', 300)
    Unknown1084(1)
    ExitState()
    label(2)
    sprite('null', 10)
    physicsXImpulse(-70000)
    sprite('null', 300)
    Unknown1084(1)
    ExitState()
    label(3)
    sprite('null', 5)
    physicsXImpulse(100000)
    Unknown20000(0)
    sprite('null', 1)
    Unknown1084(1)
    Unknown20003(0)
    ExitState()
    label(4)
    sprite('null', 5)
    physicsXImpulse(100000)
    Unknown20000(0)
    sprite('null', 1)
    Unknown1084(1)
    Unknown20003(0)

@State
def mk440cutin():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4061(1)
        Unknown4009(3)
        Unknown4007(3)
        teleportRelativeX(-100000)
        Unknown1007(100000)
        Unknown1096(1600)
    sprite('null', 11)
    GFX_0('mk440cutinEffStart', -1)
    sprite('mk440cutin_00', 3)
    GFX_0('mk440cutinEff', -1)
    sprite('mk440cutin_01', 3)
    sprite('mk440cutin_02', 3)
    physicsXImpulse(30000)
    Unknown1028(10000)
    physicsYImpulse(-8000)
    setGravity(-2000)
    Unknown3004(-24)
    sprite('mk440cutin_03', 1)
    Unknown1028(0)
    sprite('mk440cutin_04', 5)
    Unknown1019(3)

@State
def mk440cutinEffStart():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown3029(1)
        AfterimageCount(2)
    sprite('vrmkeff440_00', 2)
    sprite('vrmkeff440_01', 3)
    sprite('vrmkeff440_02', 3)
    sprite('vrmkeff440_03', 3)

@State
def mk440cutinEff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown3029(1)
        AfterimageCount(2)
    sprite('vrmkeff440_04', 3)
    sprite('vrmkeff440_05', 3)
    sprite('vrmkeff440_06', 3)
    sprite('vrmkeff440_07', 1)
    sprite('vrmkeff440_08', 3)
    sprite('null', 3)
    GFX_0('mk440cutinEffEnd', -1)

@State
def mk440cutinEffEnd():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown1096(1600)
    sprite('vrmkeff440_09', 4)
    sprite('vrmkeff440_10', 4)
    sprite('vrmkeff440_11', 4)
    Unknown3004(-23)
    sprite('vrmkeff440_12', 4)
    sprite('vrmkeff440_13', 4)

@State
def mk440cutin_Active():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4061(2)
        Unknown4007(3)
        teleportRelativeX(-100000)
        Unknown1007(100000)
        Unknown1096(1800)
        Unknown3029(1)
        AfterimageCount(2)
    sprite('null', 11)
    GFX_0('mk440cutinEffStarEx', -1)
    sprite('mk440cutin_00', 3)
    GFX_0('mk440cutinEffEx', -1)
    Unknown4009(3)
    sprite('mk440cutin_01', 3)
    sprite('mk440cutin_02', 3)
    Unknown3004(-24)
    physicsXImpulse(30000)
    Unknown1028(10000)
    physicsYImpulse(-8000)
    setGravity(-2000)
    sprite('mk440cutin_03', 1)
    physicsYImpulse(15000)
    Unknown1028(0)
    sprite('mk440cutin_04', 5)
    Unknown1019(3)

@State
def mk440cutinEffStarEx():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown3029(1)
        AfterimageCount(2)
    sprite('vrmkeff440_00', 2)
    sprite('vrmkeff440_01', 3)
    sprite('vrmkeff440_02', 3)
    sprite('vrmkeff440_03', 3)

@State
def mk440cutinEffEx():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown3029(1)
        AfterimageCount(2)
    sprite('vrmkeff440_04', 3)
    sprite('vrmkeff440_05', 3)
    sprite('vrmkeff440_06', 3)
    sprite('vrmkeff440_07', 1)
    sprite('vrmkeff440_08', 3)
    sprite('null', 3)
    GFX_0('mk440cutinEffEndEX', -1)

@State
def mk440cutinEffEndEX():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown1096(1800)
    sprite('vrmkeff440_09', 4)
    sprite('vrmkeff440_10', 4)
    sprite('vrmkeff440_11', 4)
    Unknown3004(-23)
    sprite('vrmkeff440_12', 4)
    sprite('vrmkeff440_13', 4)

@State
def mk440cutin_Active2():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown4061(2)
        Unknown1007(-250000)
        Unknown1096(1400)

        def upon_33():
            sendToLabel(1)
    sprite('null', 8)
    GFX_0('mk440cutinEffStarEx2', -1)
    sprite('mk440cutin_05', 4)
    GFX_0('mk440cutinEffEx2', -1)
    Unknown4009(3)
    physicsXImpulse(2000)
    physicsYImpulse(6000)
    sprite('mk440cutin_06', 2)
    physicsXImpulse(6000)
    physicsYImpulse(2000)
    sprite('mk440cutin_07', 3)
    physicsYImpulse(0)
    physicsXImpulse(10000)
    Unknown1028(5000)
    sprite('mk440cutin_08', 30)
    physicsXImpulse(70000)
    Unknown1028(10000)
    label(1)
    sprite('mk440cutin_09', 4)
    Unknown3004(-31)
    Unknown1084(1)
    Unknown21012('mk440cutinEffEx2', 32)
    sprite('mk440cutin_10', 4)

@State
def mk440cutinEffStarEx2():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown3033()
        Unknown4061(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown3029(1)
        AfterimageCount(2)
    sprite('vrmkeff440_20', 2)
    sprite('vrmkeff440_21', 2)
    sprite('vrmkeff440_22', 2)
    sprite('vrmkeff440_23', 2)

@State
def mk440cutinEffEx2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown3029(1)
        AfterimageCount(2)
        sendToLabelUpon(32, 0)
        Unknown3001(255)
    sprite('vrmkeff440_24', 4)
    Unknown23015(2)
    sprite('vrmkeff440_25', 2)
    sprite('vrmkeff440_26', 3)
    sprite('vrmkeff440_28', 32767)
    label(0)
    sprite('vrmkeff440_29', 4)
    sprite('null', 1)
    GFX_0('mk440cutinEffEndEX2', -1)

@State
def mk440cutinEffEndEX2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown1096(1400)
    sprite('vrmkeff440_29', 2)
    sprite('vrmkeff440_30', 2)
    sprite('vrmkeff440_31', 2)
    sprite('vrmkeff440_32', 5)
    Unknown3004(-51)

@State
def EntryMant2():

    def upon_IMMEDIATE():
        Unknown3032()
    sprite('vrmkef603m_00', 6)
    Unknown1007(10000)
    sprite('vrmkef603m_01', 3)
    Unknown1007(180000)
    sprite('vrmkef603m_01', 3)
    Unknown1007(100000)

@State
def Event_mk430cutin_lv3():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown2003(1)
        Unknown4061(1)
        Unknown3032()
        Unknown1096(1000)
        teleportRelativeX(45000)
        Unknown1007(405000)
        if Unknown42('ta'):
            Unknown23015(1)
    sprite('null', 1)
    GFX_0('mkef_430bigpunch_lv3', -1)
    GFX_0('mk430effLv3', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(30000)
    sprite('mk430_punch01', 1)
    teleportRelativeX(35000)
    sprite('mk430_punchlv03', 1)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03', 4)
    physicsXImpulse(0)
    teleportRelativeX(60000)
    sprite('mk430_punchlv03', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv03', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv03', 15)
    StartMultihit()
    Unknown3004(-15)
    Unknown3033()

@State
def Act3Event_Noel():

    def upon_IMMEDIATE():
        Unknown30012(0)
        Unknown1000(-360000)
        Unknown2019(750)
        EnableCollision(0)
        Unknown2034(0)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(2, 1)
    sprite('no620_08', 32767)
    label(0)
    sprite('no064_02', 4)
    sprite('no064_03', 4)
    sprite('no064_04', 4)
    sprite('no064_05', 4)
    sprite('no064_06', 4)
    sprite('no064_07', 4)
    sprite('no064_08', 4)
    sprite('no033_00', 3)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no033_01', 3)
    physicsXImpulse(-26000)
    physicsYImpulse(12000)
    setGravity(800)
    Unknown8002()
    Unknown8001(3, 100)
    label(9)
    sprite('no033_02', 2)
    sprite('no033_03', 2)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('null', 2)
    Unknown1084(1)
    Unknown3038(1)

@State
def Eventoffset_Sosai():

    def upon_IMMEDIATE():
        Unknown1001(0)
        teleportRelativeY(300000)
        Unknown1010(-30000, 100000)
    sprite('null', 4)
    GFX_1('ef_offset', 0)
    SFX_0('108_attack_offset')
    ScreenShake(30000, 30000)